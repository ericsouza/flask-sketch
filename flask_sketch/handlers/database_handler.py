import importlib.resources as pkg_resources  # noqa
from flask_sketch.templates import ext  # noqa
from flask_sketch.helpers import Answers
from flask_sketch.helpers import GenericHandler


def sqlite_handler(answers: Answers):
    if answers.database == "sqlite":
        return "é sqlite"


def mysql_handler(answers: Answers):
    if answers.database == "mysql":
        return "é mysql"


def postgres_handler(answers: Answers):
    if answers.database == "postgres":
        return "é postgres"


def mongodb_handler(answers: Answers):
    if answers.database == "mongodb":
        return "é mongodb"


def none_handler(answers: Answers):
    if answers.database == "none":
        return "é none"


class DatabaseHandler(GenericHandler):
    ...


database_handler = DatabaseHandler(
    sqlite_handler,
    mysql_handler,
    postgres_handler,
    mongodb_handler,
    none_handler,
)
