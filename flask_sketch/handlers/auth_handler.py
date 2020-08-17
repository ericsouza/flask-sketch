from flask_sketch.utils import (
    Sketch,
    GenericHandler,
    pjoin,
    random_string,
)
from flask_sketch import templates


def login_handler(sketch: Sketch):
    if sketch.auth_framework == "login_web":
        return True


def security_web_handler(sketch: Sketch):
    if sketch.auth_framework == "security_web":
        sketch.add_requirements("flask-security-too", "argon2-cffi")

        sketch.settings["default"]["SECURITY_REGISTERABLE"] = True
        sketch.settings["default"]["SECURITY_POST_LOGIN_VIEW"] = "/"
        sketch.settings["default"]["SECURITY_PASSWORD_HASH"] = "argon2"

        sketch.add_extensions("auth")

        sketch.secrets["default"]["SECURITY_PASSWORD_SALT"] = random_string()

        sketch.write_template(
            "security_web_only_tpl",
            templates.commands,
            pjoin(sketch.app_folder, "commands", "__init__.py",),
        )

        sketch.write_template(
            "ext_security_web_only_tpl",
            templates.ext,
            pjoin(sketch.app_folder, "ext", "auth.py"),
        )

        sketch.write_template(
            "models_security_web_only_tpl",
            templates.models,
            pjoin(sketch.app_folder, "models", "user.py"),
        )

        sketch.write_template(
            "examples_security_auth_tpl",
            templates.examples,
            pjoin(sketch.app_folder, "examples", "auth_examples.py",),
        )

        sketch.write_template(
            "examples_init_security_tpl",
            templates.examples,
            pjoin(sketch.app_folder, "examples", "__init__.py",),
        )

        return True


def basicauth_web_handler(sketch: Sketch):
    if sketch.auth_framework == "basicauth_web":
        sketch.add_requirements("flask-basicAuth")
        sketch.secrets["default"]["BASIC_AUTH_PASSWORD"] = "admin"
        sketch.secrets["default"]["BASIC_AUTH_PASSWORD"] = random_string()
        return True


def jwt_extended_handler(sketch: Sketch):
    if sketch.auth_framework == "jwt_extended":
        sketch.add_requirements("flask-jwt-extended")
        return True


def basicauth_api_handler(sketch: Sketch):
    if sketch.auth_framework == "basicauth_api":
        sketch.add_requirements("flask-basicauth")
        return True


def security_jwt_extended_handler(sketch: Sketch):
    if sketch.auth_framework == "security_jwt_extended":
        sketch.add_requirements("flask-security-too", "flask-jwt-extended")
        return True


def login_jwt_extended_handler(sketch: Sketch):
    if sketch.auth_framework == "login_jwt_extended":
        sketch.add_requirements("flask-login", "flask-jwt-extended")
        return True


def basicauth_web_api_handler(sketch: Sketch):
    if sketch.auth_framework == "basicauth_web_api":
        sketch.add_requirements("flask-basicauth")
        return True


def none_handler(sketch: Sketch):
    if sketch.auth_framework == "none":
        if not sketch.database == "none":
            sketch.write_template(
                "no_auth_tpl",
                templates.commands,
                pjoin(sketch.app_folder, "commands", "__init__.py",),
            )

        return True


class AuthHandler(GenericHandler):
    def __call__(self, sketch: Sketch):
        for handler in self.handlers:
            r = handler(sketch)
            if r:
                if not handler.__name__ == "none_handler":
                    sketch.write_template(
                        "models_auth_tpl",
                        templates.models,
                        pjoin(sketch.app_folder, "models", "__init__.py",),
                    )
                return r


auth_handler = AuthHandler(
    login_handler,
    security_web_handler,
    basicauth_web_handler,
    jwt_extended_handler,
    basicauth_api_handler,
    security_jwt_extended_handler,
    login_jwt_extended_handler,
    basicauth_web_api_handler,
    none_handler,
)
