import requests

url = 'https://laplace.live:443/api/ai-chat'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate",
    "Referer": "https://laplace.live/ai-chat",
    "Content-Type": "application/json",
    "Origin": "https://laplace.live",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Te": "trailers"
}

def history_factory(question):
    history_dictionary = {
        'text': question,
        'context': [
            {
                'role': 'user',
                'content': "You are a humorous and very enthusiastic robot assistant at Huzhou Normal "
                        "University, and if someone asks you a question, you will explain it to them in "
                        "great detail."
            },
            {
                'role': 'system',
                'content': "OK"
            },
            {
                'role': 'user',
                'content': "你好"
            },
            {
                'role': 'system',
                'content': "你好呀！我是来自湖州师范学院的机器人助理，请问你您需要什么帮助吗？"
            },
        ],
        'type': 'askQuestion',
        'model': 'gpt-4-turbo-preview',
        'lang': 'Simplified Chinese',
        'custom_api': ''
    }
    return history_dictionary


class Gpt4Turbo():
    # 初始化模型
    def __init__(self):
        try:
            requests.post(url=url, headers=headers, json=history_factory('hello')).raise_for_status()
            print("Gpt4-turbo Connect Successfully!")
        except:
            print("Can't connect to Gpt4-turbo!!!")
    # 文字处理
    def text(self, question):
        history_processed = history_factory(question)
        response = requests.post(url=url, headers=headers, json=history_processed)
        response.raise_for_status()
        result = response.text
        return result

    def vision(self, question, imgs):
        return "该模型图像处理不可用"

if __name__ == '__main__':
    req = Gpt4Turbo()
    print(req.text('你是谁'))

