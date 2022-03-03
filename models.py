import datetime

from exts import db


class Access(db.Model):
    __tablename__ = 'access_record'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ip_addr = db.Column(db.String(20))
    user = db.Column(db.String(20))
    first_access_at = db.Column(db.DateTime, index=True, default=datetime.datetime.now)
    last_access_at = db.Column(db.DateTime, index=True, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    times = db.Column(db.Integer, default=1)
    status = db.Column(db.Enum("0", "1", "2"), server_default="0", nullable=False)

    def __repr__(self):
        return f'<Access>'


class Project(db.Model):
    __tablename__ = 'project'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    project_name = db.Column(db.String(30))
    create_time = db.Column(db.DateTime, index=True, default=datetime.datetime.now)
    create_user = db.Column(db.String(20))
    update_time = db.Column(db.DateTime, index=True, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    status = db.Column(db.Enum("0", "1", "2"), server_default="0", nullable=False)
    modulees = db.relationship("Module", backref="project", lazy=True)

    def __repr__(self):
        return f'<Project>'


docs = db.Table('docs',
                db.Column("documents_id", db.String(32), db.ForeignKey('documents.id'), primary_key=True,nullable=False),
                db.Column("module_id", db.Integer, db.ForeignKey('module.id'), primary_key=True,nullable=False),
                )


class Module(db.Model):
    __tablename__ = 'module'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    module_name = db.Column(db.String(40))
    create_time = db.Column(db.DateTime, index=True, default=datetime.datetime.now)
    create_user = db.Column(db.String(20))
    update_time = db.Column(db.DateTime, index=True, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    status = db.Column(db.Enum("0", "1", "2"), server_default="0", nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey("project.id"), nullable=False)
    docs = db.relationship('Documents', secondary=docs, lazy='dynamic',
                           backref=db.backref('module', lazy="dynamic"))

    # def __repr__(self):
    #     return f'<Module>'


class Documents(db.Model):
    __tablename__ = 'documents'
    id = db.Column(db.String(32), primary_key=True)
    display_name = db.Column(db.String(50))
    file = db.Column(db.LargeBinary)
    upload_user = db.Column(db.String(20))
    upload_time = db.Column(db.DateTime, index=True, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    status = db.Column(db.Enum("0", "1", "2"), server_default="0", nullable=False)
    extension = db.Column(db.String(10))

    def __repr__(self):
        return f'<Documents>'
