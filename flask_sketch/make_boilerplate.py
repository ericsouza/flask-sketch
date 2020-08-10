import os
import pathlib
from templates.ext import database_sqlalchemy_tpl


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


def make_api_only_folders():
    ...


def make_web_only_folders():
    ...


def make_web_api_folders():
    ...


def make_database(paf, answer):
    if not answer == "no_database":
        if not answer == "mongodb":
            write_tpl(
                pjoin(paf, "ext", "database.py"),
                database_sqlalchemy_tpl.get_tpl(),
            )


def make(project_name, answers):
    paf = pjoin(str(pathlib.Path().absolute()), project_name, project_name)
    pf = pjoin(str(pathlib.Path().absolute()), project_name)

    make_commom_folders(paf, pf)
    make_database(paf, answers["database"])

