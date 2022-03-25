import json
import time

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


@socket.route('/task')  # 指定路由
def echo_socket(ws):
    while not ws.closed:
        i = 0
        while i<10:
            i += 1
            now = time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime(time.time()))
            ws.send(f"{now}: " + ''' File "src\\gevent\\_abstract_linkable.py", line 451, in gevent._gevent_c_abstract_linkable.AbstractLinkable._switch_to_hub\
  File "src\\gevent\\_greenlet_primitives.py", line 61, in gevent._gevent_c_greenlet_primitives.SwitchOutGreenletWithLoop.switch\
  File \"src\\gevent\\_greenlet_primitives.py", line 65, in gevent._gevent_c_greenlet_primitives.SwitchOutGreenletWithLoop.switch\
  File "src\\gevent\\_gevent_c_greenlet_primitives.pxd", line 35, in gevent._gevent_c_greenlet_primitives._greenlet_switch''')
            time.sleep(1)
        ws.close()
        # message = ws.receive()  # 接收到消息
        # if message is not None:
        #     print("%s receive msg==> " % now, str(json.dumps(message)))
        #     ws.send(str(json.dumps(message)))  # 回传给clicent
        # else:
        #     print(now, "no receive")


if __name__ == '__main__':
    server = pywsgi.WSGIServer(('0.0.0.0', 5000), application=app, handler_class=WebSocketHandler)
    print('server start')
    server.serve_forever()
