import importlib.resources as pkg_resources  # noqa
from flask_sketch.templates import ext  # noqa
from flask_sketch.utils import Answers
from flask_sketch.utils import GenericHandler


def dynaconf_handler(answers: Answers):
    if answers.config_framework == "dynaconf":
        return "é dynaconf"


def environs_handler(answers: Answers):
    if answers.config_framework == "environs":
        return "é environs"


def none_handler(answers: Answers):
    if answers.config_framework == "none":
        return "é none"


class ConfigHandler(GenericHandler):
    ...


config_handler = ConfigHandler(
    dynaconf_handler, environs_handler, none_handler,
)
