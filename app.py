import os
from configparser import ConfigParser

from flask import Flask, render_template, request

import config
from exts import db
from api.api import api

app = Flask(__name__)
app.register_blueprint(api, url_prefix='/api/v1')
app.config.from_object(config)
db.init_app(app)
# app.debug = True


cf = ConfigParser()
cf.read("D:/PycharmProjects/TestWebsite/config/config.ini")
case_path = cf.get("PATH", "case_path")
script_path = cf.get("PATH", "script_path")
report_path = cf.get("PATH", "report_path")


@app.route('/', methods=["GET", "POST"])
def hello_world():  # put application's code here
    ip = request.remote_addr
    res = {
        "data": []
    }
    for root, dirs, files in os.walk(case_path):
        for file in files:
            if os.path.splitext(file)[1] == '.py':
                l = ["智慧安监", "运维巡查", file, file.replace(".py", ".html")]
                res["data"].append(l)

    return render_template('index.html', **res)


if __name__ == '__main__':
    app.run()
