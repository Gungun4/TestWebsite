import os
from flask import Flask, render_template, request

import config
from exts import db
from api.api import api

app = Flask(__name__)
app.register_blueprint(api, url_prefix='/api/v1')
app.config.from_object(config)
db.init_app(app)


app.debug = True


@app.route('/', methods=["GET", "POST"])
def hello_world():  # put application's code here

    return render_template('index.html')


if __name__ == '__main__':
    app.run()
