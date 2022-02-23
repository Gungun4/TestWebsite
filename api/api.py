import json

from flask import Blueprint, request, jsonify

from config import SCRIPT_PATH
from exts import db
from model import Access
from src.test_redis import GetCom

api = Blueprint('api', __name__)


@api.route('/ip')
def ip_handle():
    ip = request.remote_addr
    exits = Access.query.filter(Access.ip_addr == ip)
    if exits.first():
        exits.update({'times': Access.times + 1})
    else:
        record = Access(ip_addr=ip)
        db.session.add(record)
    db.session.commit()
    return jsonify({"code": 100})


# 执行脚本
@api.route('/v1/record', methods=["POST"])
def record():
    sid = json.loads(request.data)["case_name"]
    if "aj" not in sid:
        res = {"code": 200}
        return res
    g = GetCom(sid, SCRIPT_PATH, "suiteMain.py")
    g.run()
    res = {"code": 100}
    return jsonify(res)
