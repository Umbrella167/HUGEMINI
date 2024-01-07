from flask import Flask, redirect, url_for
import config
from backend import Backend
from website import Website

app = Flask(__name__)
app.config['SECRET_KEY'] = config.SECRET_KEY

urls = [Website, Backend]
for url in urls:
    app.register_blueprint(url)



if __name__ == '__main__':
    app.run(port=config.PORT, host=config.HOST, debug=config.DEBUG)