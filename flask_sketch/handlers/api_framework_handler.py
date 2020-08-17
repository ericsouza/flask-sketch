from flask_sketch import templates  # noqa
from flask_sketch.utils import Sketch
from flask_sketch.utils import GenericHandler


def restful_handler(sketch: Sketch):
    if sketch.api_framework == "restful":
        return True


def restx_handler(sketch: Sketch):
    if sketch.api_framework == "restx":
        return True


def restless_handler(sketch: Sketch):
    if sketch.api_framework == "restless":
        return True


def none_handler(sketch: Sketch):
    if sketch.api_framework == "none":
        return True


class ApiFrameworkHandler(GenericHandler):
    ...


api_framework_handler = ApiFrameworkHandler(
    restful_handler, restx_handler, restless_handler, none_handler,
)
