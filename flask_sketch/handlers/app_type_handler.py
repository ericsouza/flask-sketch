import importlib.resources as pkg_resources  # noqa
from flask_sketch.templates import ext  # noqa
from flask_sketch.helpers import Answers
from flask_sketch.helpers import GenericHandler


def web_only_handler(answers: Answers):
    if answers.application_type == "web_only":
        return "é web only"


def api_only_handler(answers: Answers):
    if answers.application_type == "api_only":
        return "é api only"


def web_api_handler(answers: Answers):
    if answers.application_type == "web_and_api":
        return "é web and api"


class AppTypeHandler(GenericHandler):
    ...


app_type_handler = AppTypeHandler(
    web_only_handler, api_only_handler, web_api_handler,
)
