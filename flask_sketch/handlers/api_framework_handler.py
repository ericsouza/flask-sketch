from flask_sketch import templates  # noqa
from flask_sketch.utils import Answers
from flask_sketch.utils import GenericHandler


def restful_handler(answers: Answers):
    if answers.api_framework == "restful":
        return True


def restx_handler(answers: Answers):
    if answers.api_framework == "restx":
        return True


def restless_handler(answers: Answers):
    if answers.api_framework == "restless":
        return True


def none_handler(answers: Answers):
    if answers.api_framework == "none":
        return True


class ApiFrameworkHandler(GenericHandler):
    ...


api_framework_handler = ApiFrameworkHandler(
    restful_handler, restx_handler, restless_handler, none_handler,
)
