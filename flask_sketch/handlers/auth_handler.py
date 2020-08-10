import importlib.resources as pkg_resources  # noqa
from flask_sketch.templates import ext  # noqa
from flask_sketch.helpers import Answers
from flask_sketch.helpers import GenericHandler


def login_handler(answers: Answers):
    if answers.auth_framework == "login_web":
        return "é login_web"


def security_web_handler(answers: Answers):
    if answers.auth_framework == "security_web":
        return "é security_web"


def basicauth_web_handler(answers: Answers):
    if answers.auth_framework == "basicauth_web":
        return "é basicauth_web"


def praetorian_handler(answers: Answers):
    if answers.auth_framework == "praetorian":
        return "é praetorian"


def pyjwt_handler(answers: Answers):
    if answers.auth_framework == "pyjwt":
        return "é pyjwt"


def basicauth_api_handler(answers: Answers):
    if answers.auth_framework == "basicauth_api":
        return "é basicauth_api"


def security_web_api_handler(answers: Answers):
    if answers.auth_framework == "security_web_api":
        return "é security_web_api"


def login_pyjwt_handler(answers: Answers):
    if answers.auth_framework == "login_pyjwt":
        return "é login_pyjwt"


def basicauth_web_api_handler(answers: Answers):
    if answers.auth_framework == "basicauth_web_api":
        return "é basicauth_web_api"


def none_handler(answers: Answers):
    if answers.auth_framework == "none":
        return "é none"


class AuthHandler(GenericHandler):
    ...


auth_handler = AuthHandler(
    login_handler,
    security_web_handler,
    basicauth_web_handler,
    praetorian_handler,
    pyjwt_handler,
    basicauth_api_handler,
    security_web_api_handler,
    login_pyjwt_handler,
    basicauth_web_api_handler,
    none_handler,
)
