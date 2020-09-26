from os.path import join as pjoin
from flask_sketch import templates
from flask_sketch.sketch import Sketch
from flask_sketch.utils import GenericHandler


def handle_sql_db(sketch: Sketch):
    sketch.add_requirements("flask-sqlalchemy")

    sketch.settings["default"]["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    sketch.settings["development"]["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    sketch.settings["default"][
        "SQLALCHEMY_DATABASE_URI"
    ] = "sqlite:///db.sqlite3"

    sketch.add_extensions("database")

    sketch.write_template(
        "ext_sqlalchemy_tpl",
        templates.ext,
        pjoin(sketch.app_folder, "ext", "database.py"),
    )

    sketch.write_template(
        "utils_sql_tpl",
        templates.models,
        pjoin(sketch.app_folder, "models", "utils.py"),
    )

    sketch.template_args["ADMIN_MODEL_ENGINE"] = "sqla"
    sketch.template_args[
        "ADMIN_DATABASE_IMPORT"
    ] = "from {}.ext.database import db".format(sketch.app_folder_name)

    sketch.template_args[
        "ADMIN_VIEW_USER"
    ] = "admin.add_view(ProtectedModelView(User, db.session))"
    sketch.template_args[
        "ADMIN_VIEW_ROLE"
    ] = "admin.add_view(ProtectedModelView(Role, db.session))"


def sqlite_handler(sketch: Sketch):
    if sketch.database == "sqlite":
        handle_sql_db(sketch)
        sketch.settings["production"][
            "SQLALCHEMY_DATABASE_URI"
        ] = "sqlite:///production_db.sqlite3"
        return True


def mysql_handler(sketch: Sketch):
    if sketch.database == "mysql":
        sketch.add_requirements("mysqlclient")
        handle_sql_db(sketch)
        sketch.settings["production"][
            "SQLALCHEMY_DATABASE_URI"
        ] = "mysql+mysqldb://<user>:<password>@<server_ip>/MY_DATABASE"
        return True


def postgres_handler(sketch: Sketch):
    if sketch.database == "postgres":
        sketch.add_requirements("psycopg2")
        handle_sql_db(sketch)
        sketch.settings["production"][
            "SQLALCHEMY_DATABASE_URI"
        ] = "postgres://<user>:<password>@<server_ip>/MY_DATABASE"
        return True


def mongodb_handler(sketch: Sketch):
    if sketch.database == "mongodb":
        sketch.add_requirements("flask-mongoengine")
        sketch.add_extensions("database")

        sketch.settings["default"][
            "MONGODB_HOST"
        ] = "mongodb://root:password@127.0.0.1:27017/database?authSource=admin"

        sketch.write_template(
            "ext_mongoengine_tpl",
            templates.ext,
            pjoin(sketch.app_folder, "ext", "database.py"),
        )

        sketch.write_template(
            "utils_mongo_tpl",
            templates.models,
            pjoin(sketch.app_folder, "models", "utils.py"),
        )

        sketch.template_args["ADMIN_MODEL_ENGINE"] = "mongoengine"
        sketch.template_args["ADMIN_DATABASE_IMPORT"] = ""
        sketch.template_args[
            "ADMIN_VIEW_USER"
        ] = "admin.add_view(ProtectedModelView(User))"
        sketch.template_args[
            "ADMIN_VIEW_ROLE"
        ] = "admin.add_view(ProtectedModelView(Role))"

        return True


def none_handler(sketch: Sketch):
    if sketch.database == "none":
        return True


class DatabaseHandler(GenericHandler):
    ...


database_handler = DatabaseHandler(
    sqlite_handler,
    mysql_handler,
    postgres_handler,
    mongodb_handler,
    none_handler,
)
