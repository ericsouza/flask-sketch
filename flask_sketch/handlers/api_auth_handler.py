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

        return True


def basicauth_handler(sketch: Sketch):
    if sketch.api_auth_framework == "basicauth":
        sketch.add_requirements("flask-basicauth")
        return True


def none_handler(sketch: Sketch):
    if sketch.api_auth_framework == "none":
        if not sketch.database == "none":
            sketch.write_template(
                "no_auth_tpl",
                templates.commands,
                pjoin(sketch.app_folder, "commands", "__init__.py",),
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
