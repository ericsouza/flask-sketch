import os
import importlib.resources as pkg_resources
from typing import Callable


class Answers:
    def __init__(self, pf, apf, answers: dict):
        self.project_folder = pf
        self.application_project_folder = apf
        self.application_type: str = answers.get("application_type")
        self.database: str = answers.get("database")
        self.auth_framework: str = answers.get("auth_framework")
        self.api_framework: str = answers.get("api_framework")
        self.config_framework: str = answers.get("config_framework")
        self.features: list = answers.get("features")


class GenericHandler:
    def __init__(self, *handlers: Callable):
        self.handlers = handlers

    def __call__(self, answers: Answers):
        for handler in self.handlers:
            if r := handler(answers):
                return r


def has_answers(answers: dict, have: dict = {}, not_have: dict = {}):

    for da in have:
        if not answers.get(da).lower() in have.get(da).lower().split(";"):
            return False

    for nda in not_have:
        if answers.get(nda).lower() in not_have.get(nda).lower().split(";"):
            return False

    return True


def write_tpl(tpl, tpl_location, path):
    template = pkg_resources.read_text(tpl_location, tpl)
    with open(path, "a") as file:
        file.writelines(template)


def pjoin(*args):
    return "/".join(list(args))


def make_commom_folders(paf, pf):
    os.makedirs(pjoin(pf, "tests"))
    os.makedirs(paf)
    os.makedirs(pjoin(paf, "ext"))
    os.makedirs(pjoin(paf, "models"))
    os.makedirs(pjoin(paf, "config"))
    os.makedirs(pjoin(paf, "commands"))

    open(pjoin(paf, "ext", "__init__.py"), 'a').close()
    open(pjoin(paf, "models", "__init__.py"), 'a').close()
    open(pjoin(paf, "config", "__init__.py"), 'a').close()
    open(pjoin(paf, "commands", "__init__.py"), 'a').close()
