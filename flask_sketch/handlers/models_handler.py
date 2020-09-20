from os.path import join as pjoin
from flask_sketch.utils import GenericHandler
from flask_sketch.sketch import Sketch
from flask_sketch import templates


def handle_mongo_login(sketch: Sketch):
    if sketch.database == "mongodb" and sketch.auth_framework == "login":
        sketch.write_template(
            "user_mongo_tpl",
            templates.models,
            pjoin(sketch.app_folder, "models", "user.py"),
        )

        return True


def handle_sql_login(sketch: Sketch):
    if (
        sketch.database in ["sqlite", "postgres", "mysql"]
        and sketch.auth_framework == "login"
    ):
        sketch.write_template(
            "user_sql_tpl",
            templates.models,
            pjoin(sketch.app_folder, "models", "user.py"),
        )

        return True


def handle_mongo_security(sketch: Sketch):
    if sketch.database == "mongodb" and sketch.auth_framework == "security":
        sketch.write_template(
            "user_mongo_security_tpl",
            templates.models,
            pjoin(sketch.app_folder, "models", "user.py"),
        )
        return True


def handle_sql_security(sketch: Sketch):
    if (
        sketch.database in ["sqlite", "postgres", "mysql"]
        and sketch.auth_framework == "security"
    ):
        sketch.write_template(
            "user_sql_security_tpl",
            templates.models,
            pjoin(sketch.app_folder, "models", "user.py"),
        )
        return True


def handle_jwt_mongo(sketch: Sketch):
    if (
        sketch.database == "mongodb"
        and sketch.auth_framework == "none"
        and sketch.api_auth_framework != "none"
    ):
        sketch.write_template(
            "user_mongo_noauth_jwt_tpl",
            templates.models,
            pjoin(sketch.app_folder, "models", "user.py"),
        )
        return True


def handle_jwt_sql(sketch: Sketch):
    if (
        sketch.database in ["sqlite", "postgres", "mysql"]
        and sketch.auth_framework == "none"
        and sketch.api_auth_framework != "none"
    ):
        sketch.write_template(
            "user_sql_noauth_jwt_tpl",
            templates.models,
            pjoin(sketch.app_folder, "models", "user.py"),
        )
        return True


def handle_noauth_nojwt(sketch: Sketch):
    if sketch.api_auth_framework == "none" and sketch.auth_framework == "none":
        sketch.template_args["ADMIN_USER_ROLE_IMPORT"] = ""
        sketch.template_args["ADMIN_VIEW_USER"] = ""
        sketch.template_args["ADMIN_VIEW_ROLE"] = ""
        return True


class ModelsHandler(GenericHandler):
    ...


models_handler = ModelsHandler(
    handle_mongo_login,
    handle_sql_login,
    handle_mongo_security,
    handle_sql_security,
    handle_jwt_mongo,
    handle_jwt_sql,
    handle_noauth_nojwt,
)
