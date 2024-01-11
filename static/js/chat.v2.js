document.addEventListener("DOMContentLoaded", function() {
  const post_form = document.getElementById("post_form");
  const textarea = document.getElementById("input_text");
  const msg_box = document.getElementById("msg_box");
  const tools = document.querySelectorAll(".tool");
  const img_box = document.getElementById("img_box");
  const image_input = document.getElementById("image_input");
  const show_imgs = document.getElementById("show_imgs");
  const upload_img_btn = document.getElementById("upload_img_btn");
  const url_text = "/gemini/text";
  const url_version = "/gemini/version";
  let chat_history = [];
  let chat_id = 0;
  let img_id = 0;
  let request_in_progress = false;
  //创建用户消息(文字)
  function creat_user_msg_box_chat(id, msg){
    const new_div = document.createElement("div");
    const new_msg = document.createElement("pre");
    new_div.id = "user"+id;
    new_div.className = "chat";
    new_div.textContent = "user:";
    new_msg.textContent = msg;
    new_div.appendChild(new_msg);
    msg_box.append(new_div);
  }
  //创建用户消息(图片)
  function creat_user_msg_box_img(id, msg, img_datas){
    const new_div = document.createElement("div");
    const new_msg = document.createElement("pre");
    new_div.id = "user"+id;
    new_div.className = "chat";
    new_div.textContent = "user:";
    img_datas.forEach(function (img_data){
      const new_img = document.createElement("img");
      new_img.id = "chat_img"+id;
      new_img.className = "chat-img";
      new_img.src = img_data;
      new_div.appendChild(new_img);
    })
    new_msg.textContent = msg;
    new_div.appendChild(new_msg);
    msg_box.append(new_div);
  }
  //创建bot消息
  function creat_bot_msg_box_chat(id){
    const new_div = document.createElement("div");
    const new_msg = document.createElement("pre");
    new_div.id = "bot"+id;
    new_div.className = "chat";
    new_div.textContent = "bot:";
    new_msg.className = "typing";
    new_msg.textContent = "|";
    new_div.appendChild(new_msg);
    msg_box.append(new_div);
  }
  //更新bot消息
  function update_bot_msg_box_chat(msg){
    const msg_div = document.getElementsByClassName("typing")[0];
    msg_div.className = "";
    msg_div.textContent = msg;
  }
  //创建img选框
  function create_img_checkbox(id, data){
    const image = document.createElement('img');
    const checkbox = document.createElement('input');
    const img_block = document.createElement('div');
    img_block.className = "img-block";
    img_block.id = "img_block"+id;
    image.src = data;
    image.id = "img"+id+"data";
    checkbox.type = "checkbox";
    checkbox.id = "img"+id;
    checkbox.name = "img"+id;
    checkbox.checked = true;
    img_block.append(checkbox);
    img_block.append(image);
    show_imgs.append(img_block);
    image.addEventListener("click", function(event){
      checkbox.checked = !checkbox.checked;
    })
  }
  //清除所有消息
  function clear_history(){
    chat_history = [];
    msg_box.textContent = "";
  }
  //发送消息函数
  function submit_form(event) {
    event.preventDefault();
    if (request_in_progress) {
      return;
    }
    const xhr = new XMLHttpRequest();
    const checked_img = document.querySelectorAll('input[type="checkbox"]:checked');
    const input_text = textarea.value;
    textarea.value = "";
    request_in_progress = true;

    if (checked_img.length == 0){
      //如果上传的图片数为0则用上传文字的
      creat_user_msg_box_chat(chat_id, input_text);
      creat_bot_msg_box_chat(chat_id++);
      window.scrollTo(0, document.documentElement.scrollHeight);
      chat_history.push(input_text);
      if (chat_history.length > 10) {
        chat_history.splice(0, 2);
      }
      const data = JSON.stringify({ question: input_text, history: chat_history });
      xhr.open("POST", url_text, true);
      xhr.setRequestHeader("Content-Type", "application/json");
      xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
          if (xhr.status === 200) {
            const response = JSON.parse(xhr.responseText);
            update_bot_msg_box_chat(response.result);
            window.scrollTo(0, document.documentElement.scrollHeight);
            chat_history.push(response.result);
          }
          request_in_progress = false;
        }
      };
      xhr.send(data);
    }
    else{
      const img_datas = [];
      checked_img.forEach(function (img_input){
        const img = img_input.parentElement.querySelector("img");;
        img_datas.push(img.src);
        // img_input.checked = false;
      })
      creat_user_msg_box_img(chat_id, input_text, img_datas);
      creat_bot_msg_box_chat(chat_id++);
      window.scrollTo(0, document.documentElement.scrollHeight);
      chat_history.push(input_text);
      if (chat_history.length > 13 * 2) {
        chat_history.splice(3 * 2, 2);
      }
      const data = JSON.stringify({ question: input_text, imgs: img_datas });
      xhr.open("POST", url_version, true);
      xhr.setRequestHeader("Content-Type", "application/json");
      xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
          if (xhr.status === 200) {
            const response = JSON.parse(xhr.responseText);
            update_bot_msg_box_chat(response.result);
            window.scrollTo(0, document.documentElement.scrollHeight);
            chat_history.push(response.result);
          }
          request_in_progress = false;
        }
      };
      xhr.send(data);
    }
  }
  //发送消息监听
  textarea.addEventListener("keydown", function(event) {
    if (event.keyCode === 13 && !event.shiftKey) {
      event.preventDefault();
      submit_form(event);
    }
  });
  //文件上传监听
  image_input.addEventListener('change', (event) => {
      const file = event.target.files[0];
      const reader = new FileReader();
      reader.onload = (e) => {
        create_img_checkbox(img_id++, e.target.result)
      };
      reader.readAsDataURL(file);
  });
  //代替image_input按钮
  upload_img_btn.onclick = (event) => {
      image_input.click();
  }
  //点击工具处理
  tools.forEach(function(tool) {
    tool.addEventListener('click', function(event) {
      const x = event.clientX;
      const y = event.clientY;
      switch (this.id){
        case "upload_img_tool":
          //检查是否打开或关闭img窗口
          {
            const img_box_p = img_box.getBoundingClientRect()
            if (img_box.style.display == "") {
              img_box.style.display = "block";
            } else {
              if (x >= img_box_p.left && x <= img_box_p.right && y >= img_box_p.top && y <= img_box_p.bottom) {
                img_box.style.display = "block";
              } else {
                img_box.style.display = "";
              }
            }
          }


          break;
        case "clear_tool":
          clear_history();
          break;
        default:
          console.log("tools wrong!")
      }
    });
  });
  //监听发送表单
  post_form.addEventListener('submit', submit_form);
});

// 清除窗口
document.addEventListener("click", function(event) {
  const img_box = document.getElementById("img_box");
  const tool_img = document.getElementById("tool_img");

  if (!tool_img.contains(event.target) && !img_box.contains(event.target)) {
    img_box.style.display = "";
  }

});