from flask_sketch import templates
from flask_sketch.utils import Answers, GenericHandler, write_tpl, pjoin


def dynaconf_handler(answers: Answers):
    if answers.config_framework == "dynaconf":
        write_tpl(
            "config_dynaconf_tpl",
            templates.config,
            pjoin(
                answers.application_project_folder, "config", "__init__.py",
            ),
        )
        return True


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
