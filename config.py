HOST = '127.0.0.1'
PORT = '5000'

SECRET_KEY = 'asdausidh8iasushd12298341283xc./@#$'
DEBUG = False

GEMINI_API_KEY = ['AIzaSyBf1eFP8q-tl7z1lpioS14jHYHA9MONIKU', 'AIzaSyCd5RueqsN7QzvcBGFlnqDthTQOnVkU6A0', "AIzaSyB6nalkyK1cWISBPoD2147mC4O5vik-6yg"]

HTTP_PROXY = 'http://localhost:7890'

# 模型设置
GENERATION_CONFIG = {
    "temperature": 0.95,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 3000,
}

SAFETY_SETTINGS = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_ONLY_HIGH"
    },
]