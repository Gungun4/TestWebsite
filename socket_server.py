import threading
import time

from flask import Flask
from flask_sockets import Sockets
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler

from src.test_redis import GetCom

app = Flask(__name__)
socket = Sockets(app)


@app.route('/', methods=["GET", "POST"])
def hello_world():  # put application's code here
    return ''


@socket.route('/task')
def echo_socket(ws):
    def send():
        while not ws.closed:
            time.sleep(1)
            ws.send(str(threading.current_thread().ident))

    threading.Thread(target=send).start()

    while not ws.closed:
        msg = ws.receive()
        if msg:
            print(msg)
            if msg == 'close':
                ws.close()
        else:
            print('not receive')


if __name__ == '__main__':
    server = pywsgi.WSGIServer(('0.0.0.0', 5050), application=app, handler_class=WebSocketHandler)
    print('server start')
    server.serve_forever()
