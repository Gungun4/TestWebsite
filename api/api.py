import hashlib
import json
import mimetypes

from flask import Blueprint, request, jsonify, make_response, send_from_directory, render_template

from config import SCRIPT_PATH
from exts import db
from models import Access, Module, Documents, Project
from src.test_redis import GetCom

api = Blueprint('api', __name__)


@api.route('/ip')
def ip_handle():
    ip = request.remote_addr
    exist = Access.query.filter(Access.ip_addr == ip)
    if exist.first():
        exist.update({'times': Access.times + 1})
    else:
        record = Access(ip_addr=ip)
        db.session.add(record)
    db.session.commit()
    return jsonify({"code": 100})


# 执行脚本
@api.route('/record', methods=["POST"])
def record():
    sid = json.loads(request.data)["case_name"]
    if "aj" not in sid:
        res = {"code": 200}
        return res
    g = GetCom(sid, SCRIPT_PATH, "suiteMain.py")
    g.run()
    res = {"code": 100}
    return jsonify(res)


# 上传文件
@api.route('/upload', methods=["POST"])
def upload():
    data = request.form
    file = request.files["file"]
    extension = file.filename.split('.')[-1]
    f_byte = file.filename.encode("utf8")
    id = hashlib.md5(file.read() + f_byte).hexdigest()
    file.seek(0)
    mid, user, status, name = data.get('module'), request.remote_addr, data.get('type'), data.get('file_name')
    try:
        exist = Documents.query.filter(Documents.id == id).first()
        m = Module.query.filter_by(id=int(mid)).first()

        if not exist:
            upload = Documents(id=id, display_name=name, upload_user=user, file=file.read(), status=status,
                               extension=extension)
            m.docs.append(upload)
            db.session.add(upload)

        else:
            m = Module.query.filter_by(id=int(mid)).first()
            m.docs.append(exist)

        db.session.commit()
        res = {"code":100,"msg":"上传成功"}
    except Exception as e:
        print(e)
        res = {"code": 200, "msg": "上传失败"}
    finally:
        file.close()
        return jsonify(res)


# 创建项目 模块
@api.route('/create_pm', methods=["POST"])
def create_pm():
    """
    pid:项目id
    pname:项目名称
    mname:模块名称
    :return:
    """
    data = request.json
    pid, pname, mname = data["pid"], data["pname"], data["mname"]
    # print(pid,pname,mname)
    try:
        if pid and mname:
            # pid不存在判断
            exits = Project.query.filter(Project.id == pid and Project.status == 0).first()
            if not exits:
                return jsonify({"code": 205, "msg": "项目不存在"})
            # 模块名称重复判断
            exits = Module.query.filter(Module.module_name == mname, Module.project_id == pid,
                                        Module.status == 0).first()
            if exits:
                return jsonify({"code": 201, "msg": "同一项目下模块名称不允许重复"})

            m = Module(create_user=request.remote_addr, project_id=pid, module_name=mname)
            db.session.add(m)
            db.session.commit()
        elif not pid and not pname:
            return jsonify({"code": 201, "msg": "项目名称不能为空"})
        elif not pid and pname:
            exits = Project.query.filter(Project.project_name == pname and Project.status == 0).first()
            if exits:
                return jsonify({"code": 201, "msg": "项目名称重复"})
            p = Project(project_name=pname, create_user=request.remote_addr)
            db.session.add(p)
            db.session.commit()
            if mname:
                get_p = Project.query.filter(Project.project_name == pname and Project.status == 0).first()
                print(get_p.id)
                m = Module(create_user=request.remote_addr, project_id=get_p.id, module_name=mname)
                db.session.add(m)
                db.session.commit()
        return jsonify({"code": 100, "msg": "操作成功"})
    except Exception as e:
        print(e)
        return jsonify({"code": 205, "msg": "操作失败"})


# 获取文件列表
@api.route("/get_list", methods=["GET"])
def get_list():
    type = request.args["name"]
    data = {}

    try:
        modules = Module.query.filter_by(status='0').all()
        for m in modules:
            mname = m.module_name
            pid = m.project_id
            pname = Project.query.filter_by(id=pid).first().project_name
            data[mname] = []
            doc = m.docs
            for d in doc:
                if d.status == type:
                    if type == '0':
                        li = [pname, str(d.upload_time), d.display_name, "下载", d.id]
                    else:
                        li = [pname, d.display_name, d.display_name + '.html', "运行", d.id]
                    data[mname].append(li)
        return jsonify({"code": 100, "data": data, "msg": "操作成功"})
    except Exception as e:
        print(e)
        return jsonify({"code": 200, "data": data, "msg": ""})


# 获取所有项目模块
@api.route("get_pm", methods=["GET"])
def get_pm():
    data = {}
    try:

        project = Project.query.filter(Project.status == '0').all()

        for p in project:
            data[p.project_name] = []
            modules = Module.query.filter_by(project_id=p.id, status='0').all()
            for m in modules:
                data[p.project_name].append({m.id: m.module_name})
        return jsonify({"code": 100, "data": data, "msg": ""})
    except Exception as e:
        print(e)
        return jsonify({"code": 200, "msg": "操作失败"})
    pass


# 下载文件
@api.route("download/<fid>", methods=["GET"])
def download(fid):
    try:
        file = Documents.query.get(fid)
        file_name = file.display_name +'.' + file.extension
        file_byte = file.file
        response = make_response(file_byte)
        mime_type = file.extension
        print(mime_type)
        response.headers["Content-Type"] = mime_type
        response.headers["Content-Disposition"] = 'attachment; filename={}'.format(file_name.encode().decode('latin-1'))
        return response

    except Exception as e:
        print(e)
        return jsonify({"code": 205, "msg": "下载失败"})

