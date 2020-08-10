from flask import Flask
from . import config
from . import commands
from .ext import auth, database, migrate, actuator, limiter, caching
from .ext.admin import admin
from .api import apibp


def create_app():
    app = Flask(__name__)
    config.register_development_config(app)
    auth.init_app(app)
    database.init_app(app)
    migrate.init_app(app)
    caching.init_app(app)
    admin.init_app(app)
    actuator.init_app(app)

    app.register_blueprint(apibp)
    limiter.init_app(app)

    commands.register_commands(app)

    return app
