let chat_history = [];

$(document).ready(function() {
    let post_form = document.getElementById('post_form');

    let request_in_progress = false; // 定义请求状态变量
    $('#post_form').submit(function(event) {
        event.preventDefault();
        if (request_in_progress) { // 如果当前请求正在进行，则不进行新的请求
            return;
        }
        let input_text = $('#input_text').val();
        chat_history.push(input_text);
        if (chat_history.length > 10) {
            chat_history.splice(0, 2); // 删除最前面的两条记录
        }
        request_in_progress = true;  // 设置请求状态为进行中
        $.ajax({
            url: "/gemini/text",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({question: post_form, history: chat_history}),
            dataType: "json",
            success: function(response) {
                $('#result').text(response['result']);
                chat_history.push(response['result']);
            },
            complete: function() {
                request_in_progress = false;  // 设置请求状态为完成
            }
        });
    });
});






