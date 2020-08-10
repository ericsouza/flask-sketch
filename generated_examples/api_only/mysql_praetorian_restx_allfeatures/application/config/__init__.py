from os import environ


class Config:
    SECRET_KEY = environ.get("SECRET_KEY", "mynotsupersecretkey")
    DEBUG = False


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite3"
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite3"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    JWT_ACCESS_LIFESPAN = {"hours": 24}
    JWT_REFRESH_LIFESPAN = {"days": 30}
    BASIC_AUTH_USERNAME = environ.get("ADMIN_USERNAME", "admin")
    BASIC_AUTH_PASSWORD = environ.get("ADMIN_PASSWORD", "admin")
    CACHE_TYPE = "simple"  # rember to use something like redis or memcached


def register_development_config(app):
    app.config.from_object("application.config.DevelopmentConfig")
