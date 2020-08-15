from uuid import uuid4

from flask_sketch.utils import (
    Answers,
    GenericHandler,
    write_tpl,
    pjoin,
    add_requirements,
)
from flask_sketch import templates


def login_handler(answers: Answers):
    if answers.auth_framework == "login_web":
        return True


def security_web_handler(answers: Answers):
    if answers.auth_framework == "security_web":
        add_requirements(
            answers.project_folder, "flask-security-too", "bcrypt"
        )

        answers.settings["default"]["SECURITY_REGISTERABLE"] = True
        answers.settings["default"]["SECURITY_POST_LOGIN_VIEW"] = "/"
        answers.settings["default"]["EXTENSIONS"].extend(
            [f"{answers.args.project_name}.ext.auth:init_app"]
        )

        answers.secrets["default"]["SECURITY_PASSWORD_SALT"] = str(uuid4())

        write_tpl(
            answers.args.project_name,
            "security_web_only_tpl",
            templates.commands,
            pjoin(
                answers.application_project_folder, "commands", "__init__.py",
            ),
        )

        write_tpl(
            answers.args.project_name,
            "ext_security_web_only_tpl",
            templates.ext,
            pjoin(answers.application_project_folder, "ext", "auth.py"),
        )

        write_tpl(
            answers.args.project_name,
            "models_security_web_only_tpl",
            templates.models,
            pjoin(answers.application_project_folder, "models", "user.py"),
        )

        write_tpl(
            answers.args.project_name,
            "examples_security_auth_tpl",
            templates.examples,
            pjoin(
                answers.application_project_folder,
                "examples",
                "auth_examples.py",
            ),
        )

        write_tpl(
            answers.args.project_name,
            "examples_init_security_tpl",
            templates.examples,
            pjoin(
                answers.application_project_folder, "examples", "__init__.py",
            ),
        )

        return True


def basicauth_web_handler(answers: Answers):
    if answers.auth_framework == "basicauth_web":
        add_requirements(answers.project_folder, "flask-basicAuth")
        return True


def praetorian_handler(answers: Answers):
    if answers.auth_framework == "praetorian":
        add_requirements(answers.project_folder, "flask-praetorian")
        return True


def jwt_extended_handler(answers: Answers):
    if answers.auth_framework == "jwt_extended":
        add_requirements(answers.project_folder, "flask-jwt-extended")
        return True


def basicauth_api_handler(answers: Answers):
    if answers.auth_framework == "basicauth_api":
        add_requirements(answers.project_folder, "flask-basicauth")
        return True


def security_web_api_handler(answers: Answers):
    if answers.auth_framework == "security_web_api":
        add_requirements(
            answers.project_folder, "flask-security-too", "flask-jwt-extended"
        )
        return True


def login_jwt_extended_handler(answers: Answers):
    if answers.auth_framework == "login_jwt_extended":
        add_requirements(
            answers.project_folder, "flask-login", "flask-jwt-extended"
        )
        return True


def basicauth_web_api_handler(answers: Answers):
    if answers.auth_framework == "basicauth_web_api":
        add_requirements(answers.project_folder, "flask-BasicAuth")
        return True


def none_handler(answers: Answers):
    if answers.auth_framework == "none":
        if not answers.database == "none":
            write_tpl(
                answers.args.project_name,
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
    def __call__(self, answers: Answers):
        for handler in self.handlers:
            r = handler(answers)
            if r:
                if not handler.__name__ == "none_handler":
                    write_tpl(
                        answers.args.project_name,
                        "models_auth_tpl",
                        templates.models,
                        pjoin(
                            answers.application_project_folder,
                            "models",
                            "__init__.py",
                        ),
                    )
                return r


auth_handler = AuthHandler(
    login_handler,
    security_web_handler,
    basicauth_web_handler,
    praetorian_handler,
    jwt_extended_handler,
    basicauth_api_handler,
    security_web_api_handler,
    login_jwt_extended_handler,
    basicauth_web_api_handler,
    none_handler,
)
