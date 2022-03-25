import time
from flask import Flask
from flask_sockets import Sockets
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler
import json

app = Flask(__name__)
sockets = Sockets(app)


@app.route('/', methods=["GET", "POST"])
def hello_world():  # put application's code here
    return ''


@sockets.route('/task')
def echo_socket(ws):
    while not ws.closed:
        message = ws.receive()  # 接收到消息
        if message is not None:
            if message == 'close':
                ws.close()
            ws.send(message)  # 回传给clicent
        else:
            print("no receive")


if __name__ == '__main__':
    server = pywsgi.WSGIServer(('0.0.0.0', 5050), application=app, handler_class=WebSocketHandler)
    print('server start')
    server.serve_forever()
