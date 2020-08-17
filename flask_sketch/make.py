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
from flask_sketch.utils import (
    Answers,
    cleanup,
    make_app,
    make_commom,
    password_generator,
    pjoin,
)


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
    answers.secrets["default"]["SECRET_KEY"] = password_generator(length=32)

    app_type_handler(answers)
    database_handler(answers)
    auth_handler(answers)
    if "api" in answers.application_type:
        api_framework_handler(answers)
    handle_features(answers)
    config_handler(answers)

    if args.e:
        answers.blueprints.extend(["examples"])
    make_app(answers)

    cleanup(answers)

    if args.v:
        os.system(f"python -m venv {pf}/.venv")
