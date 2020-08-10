from flask_praetorian import Praetorian
from application.models import User

guard = Praetorian()


def init_app(app):
    guard.init_app(app, User)
