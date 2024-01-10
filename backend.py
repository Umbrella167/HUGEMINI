from flask import Blueprint, request, jsonify
import traceback
from models import Gemini
from config import GEMINI_API_KEY
from random import choice
import json

backend = Blueprint('backend', __name__)

def history_factory(history):
    """
    Process message logging
    :param history: A Json list
    :return: Returns a chat log format that conforms to Gemini's official format
    """
    history_dictionary = [{'role': 'user',
                           'parts': "You are a humorous and very enthusiastic robot assistant at Huzhou Normal "
                                    "University, and if someone asks you a question, you will explain it to them in "
                                    "great detail."
                           },
                          {'role': 'model',
                           'parts': "OK"
                           },
                          {'role': 'user',
                           'parts': "你好"
                           },
                          {'role': 'model',
                           'parts': "你好呀！我是来自湖州师范学院的机器人助理，请问你您需要什么帮助吗？"
                           },
                          {'role': 'user',
                           'parts': "你是谁？"
                           },
                          {'role': 'model',
                           'parts': "你好你好呀！我是来自湖州师范学院的机器人助理，内核来自Google公司的Gemini大语言模型，"
                                    "我可以为你做很多事情，请问您需要什么帮助吗？"
                           },
                          ]
    role_count = 0
    for i in range(len(history)):
        if i % 2 != 0:
            history_dictionary.append({'role': 'model', 'parts': [history[i]]})
        else:
            history_dictionary.append({'role': 'user', 'parts': [history[i]]})
    history_dictionary[-1]['role'] = 'user'
    return history_dictionary

@backend.route('/text', methods=['POST'])
def text():
    if request.content_type == 'application/json':
        data = request.get_json(silent=True)
        result = ""
        if data and 'question' in data and 'history' in data:
            question = data['question']
            history = data['history']
            history_processed = history_factory(history)
            print(question, history_processed)
            try:
                api_key = choice(GEMINI_API_KEY)
                m = Gemini(api_key)
                result = m.gemini_pro(history_processed)
                return jsonify({'result': result}), 200
            except Exception as e:
                traceback.print_exc()
                result = 'Something Wrong!'
                return jsonify({'result': result}), 200
        else:
            return jsonify({'message': 'Invalid JSON or missing question/history keys'}), 400
    else:
        return jsonify({'message': 'Content-Type must be application/json'}), 415

@backend.route('/version', methods=['POST'])
def version():
    if request.content_type == 'application/json':
        data = request.get_json(silent=True)
        result = ""
        if data and 'question' in data and 'imgs' in data:
            question = data['question']
            imgs = data['imgs']
            try:
                api_key = choice(GEMINI_API_KEY)
                m = Gemini(api_key)
                result = m.gemini_pro_vision(question, imgs)
                return jsonify({'result': result}), 200
            except Exception as e:
                traceback.print_exc()
                result = 'Something Wrong!'
                return jsonify({'result': result}), 200
        else:
            return jsonify({'message': 'Invalid JSON or missing question/history keys'}), 400
    else:
        return jsonify({'message': 'Content-Type must be application/json'}), 415

