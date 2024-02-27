from flask import Blueprint, request, jsonify
import traceback
from models.modelUtils import Models, MODELS_DIC

backend = Blueprint('backend', __name__)

@backend.route('/text', methods=['POST'])
def text():
    if request.content_type == 'application/json':
        data = request.get_json(silent=True)
        if data and ('question' in data) and ('history' in data) and ('model_name' in data):
            history = data['history']
            model_name = data['model_name']
            print(history)
            try:
                m = Models(model_name)
                result = m.text(history)
                return jsonify({'result': result}), 200
            except:
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
        if data and ('question' in data) and ('imgs' in data) and ('model_name' in data):
            question = data['question']
            imgs = data['imgs']
            model_name = data['model_name']
            try:
                m = Models(model_name)
                result = m.vision(question, imgs)
                return jsonify({'result': result}), 200
            except:
                traceback.print_exc()
                result = 'Something Wrong!'
                return jsonify({'result': result}), 200
        else:
            return jsonify({'message': 'Invalid JSON or missing question/history keys'}), 400
    else:
        return jsonify({'message': 'Content-Type must be application/json'}), 415

@backend.route('/models_name', methods=['GET'])
def models_name():
    return jsonify(list(MODELS_DIC.keys()))
