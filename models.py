import google.generativeai as genai
import PIL.Image

class Gemini():
    # 初始化模型
    def __init__(self, API_KEY):
        genai.configure(api_key=API_KEY)
        # 检查是否连接成功
        try:
            models_name = ''
            for m in genai.list_models():
                if 'generateContent' in m.supported_generation_methods:
                    models_name = models_name + m.name[7:] + ' , '
            print("Models Name: {}".format(models_name[:-2]))
            print("Connect Successfully!")
            self.model_pro = genai.GenerativeModel('gemini-pro')
            self.model_vision = genai.GenerativeModel('gemini-pro-vision')
        except:
            print("Can't connect to Gemini Please check your Proxy and API Key!!!")
    # 文字处理
    def gemini_pro(self, question):
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(question)
        result = response.text
        return result
    # 图片处理
    def gemini_pro_vision(self, img_path, question):
        model = genai.GenerativeModel('gemini-pro-vision')
        true_question = [question]
        for path in img_path:
            true_question.append(PIL.Image.open(path))
        response = model.generate_content(true_question, stream=True)
        response.resolve()
        return response.text
# if __name__ == '__main__':
#     a = Gemini('AIzaSyBf1eFP8q-tl7z1lpioS14jHYHA9MONIKU')
#     path = ['1.png']
#     a.gemini_pro_vision(path, """  qq  """)
#     model = genai.GenerativeModel('gemini-pro')
#     response = model.generate_content("""你好Gemini"""  )
#     print(response.text)
#
#     for m in genai.list_models():
#         if 'generateContent' in m.supported_generation_methods:
#             print(m.name)
#     model = genai.GenerativeModel('gemini-pro-vision')
#     chat = model.start_chat(history=[])
#     img = PIL.Image.open('1.jpg')
#     res = ["这里是哪？", img]
#     response = model.generate_content(res, stream=True)
#     response.resolve()
