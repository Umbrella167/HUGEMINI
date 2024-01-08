const test_form = document.getElementById(`test_form`);
const input_text = document.getElementById(`input_text`);
const result = document.getElementById(`result`);

// const response = await fetch(`/backend-api/v2/conversation`, {
//     method: `POST`,
//     signal: window.controller.signal,
//     headers: {
//         'content-type': `application/json`,
//         accept: `text/event-stream`,
//     },
//     body: JSON.stringify({
//         conversation_id: window.conversation_id,
//         action: `_ask`,
//     }),
// });

$(document).ready(function() {
    $('#test_form').submit(function(event) {
        event.preventDefault(); // 阻止表单默认提交行为
        var inputContent = $('#input_text').val(); // 获取输入框内容
        $.ajax({
            url: "/gemini/text", // 提交目标URL
            type: "POST",
            data: {question: inputContent}, // 提交的数据
            success: function(response) {
                // 显示回显结果
                $('#result').text(response['result']);
            }
        });
    });
});