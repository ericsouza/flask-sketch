from flask_security import Security, SQLAlchemySessionUserDatastore
from application_tpl.models import User, Role
from application_tpl.ext.database import db


security = Security()
user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)


def init_app(app):
    security.init_app(app, user_datastore)
