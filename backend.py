from flask import Blueprint, request
from models import Gemini
from config import GEMINI_API_KEY
from random import choice

backend = Blueprint('backend', __name__)

@backend.route('/text', methods=['POST'])
def text():
    code = -1
    try:
        code = 200
        question = request.form['question']
        try:
            history = request.form['history']
        except:
            history = ''
        api_key = choice(GEMINI_API_KEY)
        m = Gemini(api_key)
        question = request.form['question']
        result = m.gemini_pro(question)
    except:
        code = -2
        result = '参数错误'

    return_dict = {
        'code': code,
        'result': result
    }
    return return_dict

