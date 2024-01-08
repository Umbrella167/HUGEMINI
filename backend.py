from flask import Blueprint, request
from models import Gemini

backend = Blueprint('backend', __name__)

@backend.route('/Gemini/text', methods=['POST'])
def text():
    a = Gemini('AIzaSyBf1eFP8q-tl7z1lpioS14jHYHA9MONIKU')
    request.form.get("key", type=str, default=None)
    question = request.form['question']
    res = a.gemini_pro(question)
    return res

