const test_form = document.getElementById(`test_form`);
const input_text = document.getElementById(`input_text`);
const result = document.getElementById(`result`);

var chatHistory = [];
$(document).ready(function() {
    $('#test_form').submit(function(event) {
        event.preventDefault(); // 阻止表单默认提交行为
        var inputContent = $('#input_text').val(); // 获取输入框内容
        chatHistory.push(inputContent);
        chatHistory = chatHistory.slice(-10);
        $.ajax({
            url: "/gemini/text",
            type: "POST",
            contentType: "application/json", // 显式设置请求内容的类型为 JSON
            data: JSON.stringify({question: inputContent, history: chatHistory}), // 将请求数据序列化为 JSON 字符串
            dataType: "json", // 指定预期响应的类型为 JSON
            success: function(response) {
                $('#result').text(response['result']);
                chatHistory.push(response['result']);
            }
        });
    });
});






