import os
import pathlib
from flask_sketch.handlers import (
    app_type_handler,
    database_handler,
    auth_handler,
    api_framework_handler,
    config_handler,
)
from flask_sketch.utils import Answers


def write_tpl(path, content):
    with open(path, "w") as file:
        file.writelines(content)


def pjoin(*args):
    return "/".join(list(args))


def make_commom_folders(paf, pf):
    os.makedirs(pjoin(pf, "tests"))
    os.makedirs(paf)
    os.makedirs(pjoin(paf, "ext"))
    os.makedirs(pjoin(paf, "models"))
    os.makedirs(pjoin(paf, "config"))
    os.makedirs(pjoin(paf, "commands"))


def create_project(project_name, asws):
    paf = pjoin(str(pathlib.Path().absolute()), project_name, project_name)
    pf = pjoin(str(pathlib.Path().absolute()), project_name)

    # make_commom_folders(paf, pf)
    answers = Answers(asws)
    print(app_type_handler(answers))
    print(database_handler(answers))
    print(auth_handler(answers))
    if "api" in answers.application_type:
        print(api_framework_handler(answers))
    print(config_handler(answers))
