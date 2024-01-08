from flask import Flask, redirect, url_for
import config
from backend import backend
from website import website
import os

os.environ["http_proxy"] = config.HTTP_PROXY
os.environ["https_proxy"] = config.HTTP_PROXY

app = Flask(__name__)
app.config['SECRET_KEY'] = config.SECRET_KEY
app.config['GEMINI_API_KEY'] = config.GEMINI_API_KEY

app.register_blueprint(website, url_prefix='/')
app.register_blueprint(backend, url_prefix='/gemini')

if __name__ == '__main__':
    app.run(port=config.PORT, host=config.HOST, debug=config.DEBUG)