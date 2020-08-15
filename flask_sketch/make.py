import os
import pathlib
from argparse import Namespace

from flask_sketch.handlers import (
    api_framework_handler,
    app_type_handler,
    auth_handler,
    config_handler,
    database_handler,
    handle_features,
)
from flask_sketch.utils import Answers, cleanup, make_commom, pjoin


def create_project(args: Namespace, asws: dict):
    pf = pjoin(str(pathlib.Path().absolute()), args.project_name)
    apf = pjoin(
        str(pathlib.Path().absolute()),
        args.project_name,
        args.project_name.replace("-", "_"),
    )

    answers = Answers(pf, apf, asws, args)

    make_commom(answers)

    answers.settings["default"]["DEBUG"] = False
    answers.settings["development"]["DEBUG"] = True
    answers.secrets["default"]["SECRET_KEY"] = os.urandom(32)

    app_type_handler(answers)
    database_handler(answers)
    auth_handler(answers)
    if "api" in answers.application_type:
        api_framework_handler(answers)
    handle_features(answers)
    config_handler(answers)
    cleanup(answers)

    if args.e:
        os.system(f"python -m venv {pf}/.venv")
