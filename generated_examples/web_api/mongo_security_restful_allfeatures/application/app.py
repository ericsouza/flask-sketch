from flask import Flask
from application import config


def create_app():
    app = Flask(__name__)
    config.set_conf(app)

    return app
