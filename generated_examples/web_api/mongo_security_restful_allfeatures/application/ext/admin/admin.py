from flask import redirect
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from application.ext.database import db
from application.models import User
from .basic_auth import AuthException, basic_auth


class LyraAdminView(AdminIndexView):
    def is_accessible(self):
        if not basic_auth.authenticate():
            raise AuthException('Not authenticated.')
        else:
            return True

    def inaccessible_callback(self, name, **kwargs):
        return redirect(basic_auth.challenge())


class ProtectedModelView(ModelView):
    def is_accessible(self):
        if not basic_auth.authenticate():
            raise AuthException('Not authenticated.')
        else:
            return True

    def inaccessible_callback(self, name, **kwargs):
        return redirect(basic_auth.challenge())


admin = Admin(name="App", index_view=AdminIndexView())


def init_app(app):
    admin.template_mode = "bootstrap3"
    admin.add_view(ProtectedModelView(User, db.session))
    admin.init_app(app)
