import json
import logging
import os
from configparser import ConfigParser

import redis
from flask import Flask, render_template, jsonify, request

from src.test_redis import GetCom

logging.basicConfig(level=logging.DEBUG)
r = redis.Redis(host='127.0.0.1', port=6379, db=4, decode_responses=True)
app = Flask(__name__)
app.debug = True

cf = ConfigParser()
cf.read("D:/PycharmProjects/TestWebsite/config/config.ini")
case_path = cf.get("PATH", "case_path")
script_path = cf.get("PATH", "script_path")
report_path = cf.get("PATH", "report_path")


@app.route('/', methods=["GET", "POST"])
def hello_world():  # put application's code here
    res = {
        "data": []
    }
    for root, dirs, files in os.walk(case_path):
        for file in files:
            if os.path.splitext(file)[1] == '.py':
                l = ["智慧安监", file, file.replace(".py", ".html")]
                res["data"].append(l)
    return render_template('index.html', **res)


# 执行脚本
@app.route('/api/v1/record', methods=["POST"])
def record():
    sid = json.loads(request.data)["case_name"]
    if "aj" not in sid:
        res = {"code":200}
        return res
    g = GetCom(sid, script_path, "suiteMain.py")
    g.run()
    res = {"code": 100}
    return jsonify(res)


# 执行过程数据
@app.route('/api/v1/getmsg', methods=["GET", "POST"])
def getmsg(project):
    data = r.rpop(project, 10)
    return jsonify({"code": 100, "data": data})


# 脚本
@app.route('/api/v1/get_list', methods=["GET", "POST"])
def get_list():
    res = {"code": 100,
           "data": [["1", "sjsj", "dfa.report"], ["1", "sjsj", "dfa.report"]]
           }
    if request.method == "POST":
        return jsonify(res)


if __name__ == '__main__':
    for root, dirs, files in os.walk(case_path):
        for file in files:
            if os.path.splitext(file)[1] == '.py':
                print(file, '---------------------------------')
                ll = ["智慧安监", file, file.replace(".py", "报告")]
    app.run()
