import google.generativeai as genai
import PIL.Image
from io import BytesIO
import base64
from config import GENERATION_CONFIG, SAFETY_SETTINGS

def bs64_to_PIL(data):
    return PIL.Image.open(BytesIO(base64.b64decode(data.split(',')[1])))

def history_factory(history):
    """
    Process message logging
    :param history: A Json list
    :return: Returns a chat log format that conforms to Gemini's official format
    """
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
    """
    A class that makes it easy to call the Gemini API

    Instantiation parameters: API_KEY

    """

    def __init__(self, API_KEY):
        genai.configure(api_key=API_KEY)
        # 检查是否连接成功
        try:
            # models_name = ''
            # for m in genai.list_models():
            #     if 'generateContent' in m.supported_generation_methods:
            #         models_name = models_name + m.name[7:] + ' , '
            # print("Models Name: {}".format(models_name[:-2]))
            self.model_pro = genai.GenerativeModel(
                model_name="gemini-pro",
                generation_config=GENERATION_CONFIG,
                safety_settings=SAFETY_SETTINGS
            )
            self.model_vision = genai.GenerativeModel('gemini-pro-vision')
            print("Connect Successfully!")
        except:
            print("Can't connect to Gemini Please check your Proxy and API Key!!!")

    # 文字处理
    def gemini_pro(self, history):
        """
        :param history: Chat History
        :return: AI Answer
        :description: Enter text to get answers from the Gemini model, allowing for continuous conversations
        """
        history_processed = history_factory(history)
        response = self.model_pro.generate_content(history_processed)
        result = response.text
        return result

    # 图片处理
    def gemini_pro_vision(self, question, imgs):
        true_question = [question]
        for img in imgs:
            true_question.append(bs64_to_PIL(img))
        response = self.model_vision.generate_content(true_question, stream=True)
        response.resolve()
        return response.text


if __name__ == '__main__':
    import os

    os.environ["http_proxy"] = 'http://localhost:7890'
    os.environ["https_proxy"] = 'http://localhost:7890'
    a = Gemini('AIzaSyBf1eFP8q-tl7z1lpioS14jHYHA9MONIKU')
    # path = ['1.png']
    # a.gemini_pro_vision(path, """  qq  """)
    # model = genai.GenerativeModel('gemini-pro')
    # response = model.generate_content("""你好Gemini"""  )
    # print(response.text)
    #
    # for m in genai.list_models():
    #     if 'generateContent' in m.supported_generation_methods:
    #         print(m.name)
    model = genai.GenerativeModel('gemini-pro-vision')
    # chat = model.start_chat(history=[])
    img = PIL.Image.open(r'C:\Users\win10\Desktop\index.drawio.png')
    with open(r'C:\Users\win10\Desktop\index.drawio.png', "rb") as image_file:
        img = image_file.read()
    print(img)
    res = ["讲一下这张图的详细信息？", img]
    response = model.generate_content(res, stream=True)
    response.resolve()
    print(response.text)
