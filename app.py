import redis
from flask import Flask, render_template, jsonify, request
from src.test_redis import GetCom
import os

r = redis.Redis(host='127.0.0.1', port=6379, db=4, decode_responses=True)
app = Flask(__name__)

file_dir = r"D:\PycharmProjects\AutomatedTesting\test_cases"

@app.route('/', methods=["GET", "POST"])
def hello_world():  # put application's code here
    res = {
        "data": []
    }
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.py':  # 想要保存的文件格式
                print(file)
                l= ["智慧安监",file,file.replace(".py","报告")]
                res["data"].append(l)
    return render_template('index.html', **res)


# 执行脚本
@app.route('/api/v1/record/<file>', methods=["GET", "POST"])
def record(file):
    g = GetCom(file)
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
    app.run()
