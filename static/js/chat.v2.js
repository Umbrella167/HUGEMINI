let chat_history = [];

document.addEventListener("DOMContentLoaded", function() {
  let post_form = document.getElementById('post_form');
  let request_in_progress = false;

  document.getElementById('post_form').addEventListener('submit', function(event) {
    event.preventDefault();
    if (request_in_progress) {
      return;
    }

    let input_text = document.getElementById('input_text').value;
    chat_history.push(input_text);
    if (chat_history.length > 10) {
      chat_history.splice(0, 2);
    }
    request_in_progress = true;

    let xhr = new XMLHttpRequest();
    let url = "/gemini/text";
    let data = JSON.stringify({ question: post_form, history: chat_history });

    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onreadystatechange = function() {
      if (xhr.readyState === XMLHttpRequest.DONE) {
        if (xhr.status === 200) {
          let response = JSON.parse(xhr.responseText);
          document.getElementById('result').textContent = response.result;
          chat_history.push(response.result);
        }
        request_in_progress = false;
      }
    };

    xhr.send(data);
  });
});