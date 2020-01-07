from flask import Flask

from app.exception import MyException
from app.models import db


def register_plugin(app: Flask):
    db.init_app(app)


def create_app():
    app = Flask(__name__)

    @app.errorhandler(MyException)
    def error_handler(e):
        return e.args[0]

    # 加载配置
    app.config.from_object('config.setting')
    app.config.from_object('config.security')

    # 注册插件
    register_plugin(app)

    return app
