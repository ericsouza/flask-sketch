import os
import pathlib

from flask_sketch.handlers import (
    api_framework_handler,
    app_type_handler,
    auth_handler,
    config_handler,
    database_handler,
)
from flask_sketch.utils import Answers, make_commom_folders, pjoin


def create_project(project_name: str, asws: dict):
    pf = pjoin(str(pathlib.Path().absolute()), project_name)
    apf = pjoin(str(pathlib.Path().absolute()), project_name, project_name)

    answers = Answers(pf, apf, asws)

    make_commom_folders(apf, pf)

    print(app_type_handler(answers))
    print(database_handler(answers))
    print(auth_handler(answers))
    if "api" in answers.application_type:
        print(api_framework_handler(answers))
    print(config_handler(answers))
