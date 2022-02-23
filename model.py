import datetime

from exts import db


class Access(db.Model):
    __tablename__ = 'access_record'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ip_addr = db.Column(db.String(20))
    user = db.Column(db.String(20))
    first_access_at = db.Column(db.DateTime, index=True, default=datetime.datetime.now)
    last_access_at = db.Column(db.DateTime, index=True, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    times = db.Column(db.Integer,default=1)
    status = db.Column(db.Enum("0", "1", "2"), server_default="0", nullable=False)

    def __repr__(self):
        return '<Access>'
