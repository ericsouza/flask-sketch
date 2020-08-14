from flask_sketch.templates import ext  # noqa
from flask_sketch.utils import Answers, GenericHandler, write_tpl, pjoin
from flask_sketch import templates


def login_handler(answers: Answers):
    if answers.auth_framework == "login_web":

        return True


def security_web_handler(answers: Answers):
    if answers.auth_framework == "security_web":
        write_tpl(
            "security_web_only_tpl",
            templates.commands,
            pjoin(
                answers.application_project_folder, "commands", "__init__.py",
            ),
        )

        write_tpl(
            "ext_security_web_only_tpl",
            templates.ext,
            pjoin(answers.application_project_folder, "ext", "auth.py"),
        )

        write_tpl(
            "models_security_web_only_tpl",
            templates.models,
            pjoin(answers.application_project_folder, "models", "user.py"),
        )

        return True


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
        if not answers.database == "none":
            write_tpl(
                "no_auth_tpl",
                templates.commands,
                pjoin(
                    answers.application_project_folder,
                    "commands",
                    "__init__.py",
                ),
            )

        return True


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
