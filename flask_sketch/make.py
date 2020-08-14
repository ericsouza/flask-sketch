import pathlib
from argparse import Namespace

from flask_sketch.handlers import (
    api_framework_handler,
    app_type_handler,
    auth_handler,
    config_handler,
    database_handler,
)
from flask_sketch.utils import Answers, make_commom_folders, pjoin


def create_project(args: Namespace, asws: dict):
    pf = pjoin(str(pathlib.Path().absolute()), args.project_name)
    apf = pjoin(
        str(pathlib.Path().absolute()), args.project_name, args.project_name
    )

    answers = Answers(pf, apf, asws, args)

    make_commom_folders(apf, pf)

    app_type_handler(answers)
    database_handler(answers)
    auth_handler(answers)
    if "api" in answers.application_type:
        api_framework_handler(answers)
    config_handler(answers)
