from flask import Flask, redirect, url_for
import config
from backend import backend
from website import website
import os

os.environ["http_proxy"] = config.HTTP_PROXY
os.environ["https_proxy"] = config.HTTP_PROXY

app = Flask(__name__)
app.config['SECRET_KEY'] = config.SECRET_KEY

urls = [website, backend]
for url in urls:
    app.register_blueprint(url)


if __name__ == '__main__':
    app.run(port=config.PORT, host=config.HOST, debug=config.DEBUG)