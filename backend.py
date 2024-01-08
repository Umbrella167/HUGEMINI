from flask import Blueprint, request, jsonify
import traceback
from models import Gemini
from config import GEMINI_API_KEY
from random import choice
import json

backend = Blueprint('backend', __name__)


@backend.route('/text', methods=['POST'])
def text():
    if request.content_type == 'application/json':
        data = request.get_json(silent=True)  # 设置silent=True则不会抛出错误
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
                result = '出错了，请刷新网页！'
                return jsonify({'result': result}), 200

        else:
            return jsonify({'message': 'Invalid JSON or missing question/history keys'}), 400
    else:
        return jsonify({'message': 'Content-Type must be application/json'}), 415


def history_factory(history):
    """
    Process message logging
    :param history: A Json list
    :return: Returns a chat log format that conforms to Gemini's official format
    """
    history_dictionary = []
    role_count = 0
    for i in range(len(history)):
        if i % 2 != 0:
            history_dictionary.append({'role': 'model', 'parts': [history[i]]})
        else:
            history_dictionary.append({'role': 'user', 'parts': [history[i]]})
    history_dictionary[-1]['role'] = 'user'
    return history_dictionary
