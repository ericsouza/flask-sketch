from os.path import join as pjoin
from flask_sketch.utils import GenericHandler
from flask_sketch.sketch import Sketch
from flask_sketch import templates


def handle_mongo_default(sketch: Sketch):
    if sketch.database == "mongodb" and sketch.auth_framework not in [
        "security",
        "none",
    ]:
        sketch.write_template(
            "mongo_default_tpl",
            templates.commands,
            pjoin(sketch.app_folder, "commands", "__init__.py",),
        )
        return True


def handle_mongo_jwt_default(sketch: Sketch):
    if (
        sketch.database == "mongodb"
        and sketch.auth_framework == "none"
        and sketch.api_auth_framework != "none"
    ):
        print("é vdd esse bilete")
        sketch.write_template(
            "mongo_default_tpl",
            templates.commands,
            pjoin(sketch.app_folder, "commands", "__init__.py",),
        )
        return True


def handle_sql_default(sketch: Sketch):
    if sketch.database in [
        "sqlite",
        "postgres",
        "mysql",
    ] and sketch.auth_framework not in ["security", "none"]:
        sketch.write_template(
            "sql_default_tpl",
            templates.commands,
            pjoin(sketch.app_folder, "commands", "__init__.py",),
        )

        return True


def handle_sql_jwt_default(sketch: Sketch):
    if (
        sketch.database in ["sqlite", "postgres", "mysql"]
        and sketch.auth_framework == "none"
        and sketch.api_auth_framework != "none"
    ):
        sketch.write_template(
            "sql_default_tpl",
            templates.commands,
            pjoin(sketch.app_folder, "commands", "__init__.py",),
        )
        return True


def handle_mongo_security(sketch: Sketch):
    if sketch.database == "mongodb" and sketch.auth_framework == "security":
        sketch.write_template(
            "mongo_security_tpl",
            templates.commands,
            pjoin(sketch.app_folder, "commands", "__init__.py",),
        )
        return True


def handle_sql_security(sketch: Sketch):
    if (
        sketch.database in ["sqlite", "postgres", "mysql"]
        and sketch.auth_framework == "security"
    ):
        sketch.write_template(
            "sql_security_tpl",
            templates.commands,
            pjoin(sketch.app_folder, "commands", "__init__.py",),
        )
        return True


def handle_sql_noauth(sketch: Sketch):
    if (
        sketch.database in ["sqlite", "postgres", "mysql"]
        and sketch.auth_framework == "none"
        and sketch.api_auth_framework == "none"
    ):
        sketch.write_template(
            "sql_noauth_tpl",
            templates.commands,
            pjoin(sketch.app_folder, "commands", "__init__.py",),
        )


def handle_mongo_noauth(sketch: Sketch):
    if (
        sketch.database == "mongodb"
        and sketch.auth_framework == "none"
        and sketch.api_auth_framework == "none"
    ):
        sketch.write_template(
            "mongo_noauth_tpl",
            templates.commands,
            pjoin(sketch.app_folder, "commands", "__init__.py",),
        )


class CommandsHandler(GenericHandler):
    ...


commands_handler = CommandsHandler(
    handle_mongo_default,
    handle_sql_default,
    handle_mongo_jwt_default,
    handle_sql_jwt_default,
    handle_mongo_security,
    handle_sql_security,
    handle_sql_noauth,
    handle_mongo_noauth,
)
