from flask_sketch.utils import (
    Sketch,
    GenericHandler,
    pjoin,
)
from flask_sketch import templates


def jwt_extended_handler(sketch: Sketch):
    if sketch.api_auth_framework == "jwt_extended":
        sketch.add_requirements("flask-jwt-extended", "argon2-cffi")
        sketch.settings["default"]["JWT_ACCESS_TOKEN_EXPIRES"] = 3600
        sketch.settings["default"]["JWT_REFRESH_TOKEN_EXPIRES"] = 2592000

        sketch.add_extensions("api_auth")

        sketch.write_template(
            "commands_default_tpl",
            templates.commands,
            pjoin(sketch.app_folder, "commands", "__init__.py",),
            mode="w",
        )

        sketch.write_template(
            "ext_api_auth_jwt_extended_tpl",
            templates.ext,
            pjoin(sketch.app_folder, "ext", "api_auth.py"),
        )

        sketch.write_template(
            "utils_security_jwt_extended_rbac_tpl",
            templates.utils.security,
            pjoin(sketch.app_folder, "utils", "security", "api_rbac.py"),
        )

        if sketch.auth_framework != "security":
            sketch.write_template(
                "utils_security_password_hasher_tpl",
                templates.utils.security,
                pjoin(
                    sketch.app_folder,
                    "utils",
                    "security",
                    "password_hasher.py",
                ),
                mode="w",
            )

        return True


def basicauth_handler(sketch: Sketch):
    if sketch.api_auth_framework == "basicauth":
        sketch.add_requirements("flask-basicauth")
        return True


def none_handler(sketch: Sketch):
    if sketch.api_auth_framework == "none":
        sketch.template_args["API_RBAC_IMPORT"] = ""
        sketch.template_args["ROLES_REQUIRED_DECORATOR"] = ""
        sketch.template_args["ROLES_ACCEPTED_DECORATOR"] = ""

        if sketch.api_framework == "none":
            sketch.write_template(
                "api_init_noauth_tpl",
                templates.api,
                pjoin(sketch.app_folder, "api", "__init__.py"),
            )

        return True


class ApiAuthHandler(GenericHandler):
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


api_auth_handler = ApiAuthHandler(
    jwt_extended_handler, basicauth_handler, none_handler,
)
