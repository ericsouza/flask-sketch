from flask_basicauth import BasicAuth
from werkzeug.exceptions import HTTPException
from flask import Response


class AuthException(HTTPException):
    def __init__(self, message):
        super().__init__(
            message,
            Response(
                "You could not be authenticated. Please refresh the page.",
                401,
                {'WWW-Authenticate': 'Basic realm="Login Required"'},
            ),
        )


basic_auth = BasicAuth()


def init_app(app):
    basic_auth.init_app(app)
