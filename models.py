import google.generativeai as genai
import PIL.Image
from io import BytesIO
import base64

def bs64_to_PIL(data):
    return PIL.Image.open(BytesIO(base64.b64decode(data.split(',')[1])))

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
            self.model_pro = genai.GenerativeModel('gemini-pro', safety_settings={'HARASSMENT': 'block_none'})
            self.model_vision = genai.GenerativeModel('gemini-pro-vision')
            print("Connect Successfully!")
        except:
            print("Can't connect to Gemini Please check your Proxy and API Key!!!")
    # 文字处理
    def gemini_pro(self, question):
        """
        :param question: Chat History
        :return: AI Answer
        :description: Enter text to get answers from the Gemini model, allowing for continuous conversations
        """
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(question)
        result = response.text
        return result
    # 图片处理
    def gemini_pro_vision(self, question, imgs):
        model = genai.GenerativeModel('gemini-pro-vision')
        true_question = [question]
        for img in imgs:
            true_question.append(bs64_to_PIL(img))
        response = model.generate_content(true_question, stream=True)
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