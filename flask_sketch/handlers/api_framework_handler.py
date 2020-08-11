import importlib.resources as pkg_resources  # noqa
from flask_sketch.templates import ext  # noqa
from flask_sketch.utils import Answers
from flask_sketch.utils import GenericHandler


def restful_handler(answers: Answers):
    if answers.api_framework == "restful":
        return "é restful"


def restx_handler(answers: Answers):
    if answers.api_framework == "restx":
        return "é restx"


def restless_handler(answers: Answers):
    if answers.api_framework == "restless":
        return "é restless"


def none_handler(answers: Answers):
    if answers.api_framework == "none":
        return "é none"


class ApiFrameworkHandler(GenericHandler):
    ...


api_framework_handler = ApiFrameworkHandler(
    restful_handler, restx_handler, restless_handler, none_handler,
)
