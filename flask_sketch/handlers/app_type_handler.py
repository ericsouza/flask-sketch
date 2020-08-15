from flask_sketch import templates
from flask_sketch.utils import (
    Answers,
    GenericHandler,
    write_tpl,
    pjoin,
)
import os


def web_only_handler(answers: Answers):
    if answers.application_type == "web_only":
        os.makedirs(pjoin(answers.application_project_folder, "site"))
        write_tpl(
            answers.args.project_name,
            "site_web_only_init_tpl",
            templates.site,
            pjoin(answers.application_project_folder, "site", "__init__.py"),
        )
        write_tpl(
            answers.args.project_name,
            "site_web_only_views_tpl",
            templates.site,
            pjoin(answers.application_project_folder, "site", "views.py"),
        )
        return True


def api_only_handler(answers: Answers):
    if answers.application_type == "api_only":
        os.makedirs(
            pjoin(answers.application_project_folder, "api", "resources")
        )
        return True


def web_api_handler(answers: Answers):
    if answers.application_type == "web_and_api":
        os.makedirs(
            pjoin(answers.application_project_folder, "api", "resources")
        )
        os.makedirs(pjoin(answers.application_project_folder, "site"))
        return True


class AppTypeHandler(GenericHandler):
    ...


app_type_handler = AppTypeHandler(
    web_only_handler, api_only_handler, web_api_handler,
)
