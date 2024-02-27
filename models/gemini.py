import google.generativeai as genai
import PIL.Image
from io import BytesIO
import base64
from random import choice
from config import GENERATION_CONFIG, SAFETY_SETTINGS, GEMINI_API_KEY

def bs64_to_PIL(data):
    return PIL.Image.open(BytesIO(base64.b64decode(data.split(',')[1])))

def history_factory(history):
    history_dictionary = [
            {
                'role': 'user',
                'parts': "You are a humorous and very enthusiastic robot assistant at Huzhou Normal "
                        "University, and if someone asks you a question, you will explain it to them in "
                        "great detail."
            },
            {
                'role': 'model',
                'parts': "OK"
            },
            {
                'role': 'user',
                'parts': "你好"
            },
            {
                'role': 'model',
                'parts': "你好呀！我是来自湖州师范学院的机器人助理，请问你您需要什么帮助吗？"
            },
            {
                'role': 'user',
                'parts': "你是谁？"
            },
            {
                'role': 'model',
                'parts': "你好你好呀！我是来自湖州师范学院的机器人助理，内核来自Google公司的Gemini大语言模型，"
                        "我可以为你做很多事情，请问您需要什么帮助吗？"
            },
        ]
    for i in range(len(history)):
        if i % 2 != 0:
            history_dictionary.append({'role': 'model', 'parts': [history[i]]})
        else:
            history_dictionary.append({'role': 'user', 'parts': [history[i]]})
    history_dictionary[-1]['role'] = 'user'
    return history_dictionary

class Gemini():
    # 初始化模型
    def __init__(self):
        api_key = choice(GEMINI_API_KEY)
        genai.configure(api_key=api_key)
        # 打印可用模型
        # for m in genai.list_models():
        #     if 'generateContent' in m.supported_generation_methods:
        #         print(m.name)
        # 检查是否连接成功
        try:
            self.model_pro = genai.GenerativeModel(
                model_name='models/gemini-1.0-pro-latest',
                generation_config=GENERATION_CONFIG,
                safety_settings=SAFETY_SETTINGS
            )
            self.model_vision = genai.GenerativeModel('models/gemini-1.0-pro-vision-latest')
            print("Connect Successfully!")
        except:
            print("Can't connect to Gemini Please check your Proxy and API Key!!!")

    # 文字处理
    def text(self, history):
        history_processed = history_factory(history)
        response = self.model_pro.generate_content(history_processed)
        result = response.text
        return result

    # 图片处理
    def vision(self, question, imgs):
        true_question = [question]
        for img in imgs:
            true_question.append(bs64_to_PIL(img))
        response = self.model_vision.generate_content(true_question, stream=True)
        response.resolve()
        return response.text