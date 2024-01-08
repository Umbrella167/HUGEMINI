const test_form = document.getElementById(`test_form`);
const input_text = document.getElementById(`input_text`);
const result = document.getElementById(`result`);

var chatHistory = [];
$(document).ready(function() {
    var requestInProgress = false; // 定义请求状态变量
    $('#test_form').submit(function(event) {
        event.preventDefault();
        if (requestInProgress) { // 如果当前请求正在进行，则不进行新的请求
            return;
        }
        var inputContent = $('#input_text').val();
        chatHistory.push(inputContent);
        if (chatHistory.length > 10) {
            chatHistory.splice(0, 2); // 删除最前面的两条记录
        }
        requestInProgress = true;  // 设置请求状态为进行中
        $.ajax({
            url: "/gemini/text",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({question: inputContent, history: chatHistory}),
            dataType: "json",
            success: function(response) {
                $('#result').text(response['result']);
                chatHistory.push(response['result']);
            },
            complete: function() {
                requestInProgress = false;  // 设置请求状态为完成
            }
        });
    });
});






