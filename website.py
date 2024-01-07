from flask import Blueprint, render_template

Website = Blueprint('Website', __name__)

@Website.route('/', methods=["GET", "POST"])
def Index():
    return render_template('index.html')