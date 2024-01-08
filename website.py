from flask import Blueprint, render_template, redirect

website = Blueprint('website', __name__)

@website.route('/', methods=['GET', 'POST'])
def index():
    return redirect('/chat')

@website.route('/chat/<conversation_id>', methods=['GET', 'POST'])
@website.route('/chat', methods=['GET', 'POST'])
def chat(conversation_id=None):

    return render_template('index.html')
