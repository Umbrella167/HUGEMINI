document.addEventListener("DOMContentLoaded", function() {
  const post_form = document.getElementById('post_form');
  const textarea = document.getElementById("input_text");
  const msg_box = document.getElementById("msg_box");
  const tools = document.querySelectorAll('.tool');
  let chat_history = [];
  let id = 0;
  let request_in_progress = false;
  //创建用户消息
  function creat_user_msg_box(id, msg){
    const new_div = document.createElement("div");
    const new_msg = document.createElement("div");
    new_div.id = "user"+id;
    new_div.className = "chat";
    new_div.textContent = "user:";
    new_msg.textContent = msg;
    new_div.appendChild(new_msg);
    msg_box.append(new_div);
  }
  //创建bot消息
  function creat_bot_msg_box(id){
    const new_div = document.createElement("div");
    const new_msg = document.createElement("div");
    new_div.id = "bot"+id;
    new_div.className = "chat";
    new_div.textContent = "bot:";
    new_msg.className = "typing";
    new_msg.textContent = "|";
    new_div.appendChild(new_msg);
    msg_box.append(new_div);
  }
  //更新bot消息
  function update_bot_msg_box(msg){
    const msg_div = document.getElementsByClassName("typing")[0];
    msg_div.className = "";
    msg_div.textContent = msg;
  }
  //发送消息函数
  function submit_form(event) {
    event.preventDefault();
    if (request_in_progress) {
      return;
    }

    const input_text = textarea.value;
    chat_history.push(input_text);
    if (chat_history.length > 10) {
      chat_history.splice(0, 2);
    }
    request_in_progress = true;

    creat_user_msg_box(id, input_text);
    creat_bot_msg_box(id++);
    const xhr = new XMLHttpRequest();
    const url = "/gemini/text";
    const data = JSON.stringify({ question: input_text, history: chat_history });

    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onreadystatechange = function() {
      if (xhr.readyState === XMLHttpRequest.DONE) {
        if (xhr.status === 200) {
          const response = JSON.parse(xhr.responseText);
          update_bot_msg_box(response.result);
          document.getElementById('result').textContent = response.result;
          chat_history.push(response.result);
        }
        request_in_progress = false;
      }
    };
    xhr.send(data);
  }
  //发送消息监听
  textarea.addEventListener("keydown", function(event) {
    if (event.keyCode === 13 && !event.shiftKey) {
      event.preventDefault();
      submit_form(event);
    }
  });
  //点击工具处理
  tools.forEach(function(tool) {
    tool.addEventListener('click', function() {
      switch (this.id){
        case "upload_img_tool":

          break;
        case "clear_tool":

          break;
        default:
          console.log("tools wrong!")
      }
    });
  });
  //监听发送表单
  post_form.addEventListener('submit', submit_form);
});