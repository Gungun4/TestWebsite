import time
from flask import Flask
from flask_sockets import Sockets
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler
import json
from src.test_redis import GetCom

app = Flask(__name__)
sockets = Sockets(app)


@app.route('/', methods=["GET", "POST"])
def hello_world():  # put application's code here
    return ''


@sockets.route('/task')
def echo_socket(ws):
    while not ws.closed:
        g = GetCom("\\test_cases\智慧安监",ws.send)
        g.run()
        message = ws.receive()  # 接收到消息
        if message is not None:
            print(message)
        else:
            print("no receive")


if __name__ == '__main__':
    server = pywsgi.WSGIServer(('0.0.0.0', 5050), application=app, handler_class=WebSocketHandler)
    print('server start')
    server.serve_forever()
