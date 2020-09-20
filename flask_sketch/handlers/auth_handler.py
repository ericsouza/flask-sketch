import os
from os.path import join as pjoin
from flask_sketch.sketch import Sketch
from flask_sketch.utils import GenericHandler, random_string
from flask_sketch import templates


def login_handler(sketch: Sketch):
    if sketch.auth_framework == "login":
        sketch.add_requirements(
            "flask-login", "argon2-cffi", "flask-wtf", "email_validator"
        )
        sketch.add_extensions("auth")

        sketch.write_template(
            "ext_login_tpl",
            templates.ext,
            pjoin(sketch.app_folder, "ext", "auth.py"),
        )

        sketch.write_template(
            "examples_login_auth_tpl",
            templates.examples,
            pjoin(sketch.app_folder, "examples", "auth_examples.py",),
        )

        sketch.write_template(
            "examples_init_auth_tpl",
            templates.examples,
            pjoin(sketch.app_folder, "examples", "__init__.py",),
        )

        sketch.write_template(
            "utils_security_login_rbac_tpl",
            templates.utils.security,
            pjoin(sketch.app_folder, "utils", "security", "rbac.py"),
        )

        sketch.write_template(
            "utils_security_password_hasher_tpl",
            templates.utils.security,
            pjoin(
                sketch.app_folder, "utils", "security", "password_hasher.py"
            ),
            mode="w",
        )

        sketch.write_template(
            "site_login_auth_views_tpl",
            templates.site,
            pjoin(sketch.app_folder, "site", "views.py",),
        )

        sketch.write_template(
            "site_login_auth_forms_tpl",
            templates.site,
            pjoin(sketch.app_folder, "site", "forms.py",),
        )

        sketch.write_template(
            "site_login_init_tpl",
            templates.site,
            pjoin(sketch.app_folder, "site", "__init__.py",),
        )

        os.makedirs(pjoin(sketch.app_folder, "site", "templates"))

        sketch.write_template(
            "login_html_tpl",
            templates.site.templates,
            pjoin(sketch.app_folder, "site", "templates", "login.html",),
        )

        sketch.write_template(
            "register_html_tpl",
            templates.site.templates,
            pjoin(sketch.app_folder, "site", "templates", "register.html",),
        )

        sketch.write_template(
            "dashboard_html_tpl",
            templates.site.templates,
            pjoin(sketch.app_folder, "site", "templates", "dashboard.html",),
        )

        return True


def security_web_handler(sketch: Sketch):
    if sketch.auth_framework == "security":
        sketch.add_requirements("flask-security-too", "argon2-cffi")

        sketch.settings["default"]["SECURITY_REGISTERABLE"] = True
        sketch.settings["default"]["SECURITY_POST_LOGIN_VIEW"] = "/"
        sketch.settings["default"]["SECURITY_PASSWORD_HASH"] = "argon2"

        sketch.add_extensions("auth")

        sketch.secrets["default"]["SECURITY_PASSWORD_SALT"] = random_string(
            length=32
        )

        sketch.template_args[
            "PWD_VERIFIER_METHOD_IMPORT"
        ] = "from flask_security import verify_password"

        sketch.template_args[
            "PWD_VERIFIER_METHOD"
        ] = "verify_password(password, user.password)"

        sketch.write_template(
            "site_web_only_init_tpl",
            templates.site,
            pjoin(sketch.app_folder, "site", "__init__.py"),
        )

        sketch.write_template(
            "site_web_only_views_tpl",
            templates.site,
            pjoin(sketch.app_folder, "site", "views.py"),
        )

        if sketch.database == "mongodb":
            auth_tpl = "ext_auth_security_mongo_tpl"
        else:
            auth_tpl = "ext_security_web_only_tpl"

        sketch.write_template(
            auth_tpl,
            templates.ext,
            pjoin(sketch.app_folder, "ext", "auth.py"),
        )

        sketch.write_template(
            "examples_security_auth_tpl",
            templates.examples,
            pjoin(sketch.app_folder, "examples", "auth_examples.py",),
        )

        sketch.write_template(
            "examples_init_auth_tpl",
            templates.examples,
            pjoin(sketch.app_folder, "examples", "__init__.py",),
        )

        return True


def basicauth_web_handler(sketch: Sketch):
    if sketch.auth_framework == "basicauth":
        sketch.add_requirements("flask-basicAuth")
        sketch.secrets["default"]["BASIC_AUTH_PASSWORD"] = "admin"
        sketch.secrets["default"]["BASIC_AUTH_PASSWORD"] = random_string()
        return True


def none_handler(sketch: Sketch):
    if sketch.auth_framework == "none":
        sketch.write_template(
            "site_web_only_init_tpl",
            templates.site,
            pjoin(sketch.app_folder, "site", "__init__.py"),
        )

        sketch.write_template(
            "site_web_only_views_tpl",
            templates.site,
            pjoin(sketch.app_folder, "site", "views.py"),
        )

        return True


class AuthHandler(GenericHandler):
    def __call__(self, sketch: Sketch):
        for handler in self.handlers:
            r = handler(sketch)
            if r:
                if not handler.__name__ == "none_handler":
                    sketch.write_template(
                        "models_init_tpl",
                        templates.models,
                        pjoin(sketch.app_folder, "models", "__init__.py",),
                        mode="w",
                    )
                return r


auth_handler = AuthHandler(
    login_handler, security_web_handler, basicauth_web_handler, none_handler,
)
