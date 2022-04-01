import json
import time
import logging
from logging import FileHandler
from flask import Flask, render_template
from flask_sockets import Sockets
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler
import config
from api.api import api
from exts import db

app = Flask(__name__)
socket = Sockets(app)
app.register_blueprint(api, url_prefix='/api/v1')
app.config.from_object(config)
db.init_app(app)


@app.route('/', methods=["GET", "POST"])
def hello_world():  # put application's code here
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    handler = logging.FileHandler('flask.log')
    app.logger.addHandler(handler)
    app.run()
