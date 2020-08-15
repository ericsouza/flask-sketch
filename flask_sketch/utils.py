import os
import toml
import importlib.resources as pkg_resources
from typing import Callable
from argparse import Namespace
from flask_sketch import templates


class Answers:
    def __init__(self, pf: str, apf: str, answers: dict, args: Namespace):
        self.project_folder = pf
        self.application_project_folder = apf
        self.application_type: str = answers.get("application_type")
        self.database: str = answers.get("database")
        self.auth_framework: str = answers.get("auth_framework")
        self.api_framework: str = answers.get("api_framework")
        self.config_framework: str = answers.get("config_framework")
        self.features: list = answers.get("features")
        self.args = args
        self.settings = {
            "default": {
                "DEBUG": "not_overridden",
                "SQLALCHEMY_TRACK_MODIFICATIONS": "not_overridden",
                "SECURITY_REGISTERABLE": "not_overridden",
                "SECURITY_POST_LOGIN_VIEW": "not_overridden",
                "FLASK_ADMIN_TEMPLATE_MODE": "not_overridden",
                "RATELIMIT_DEFAULT": "not_overridden",
                "RATELIMIT_ENABLED": "not_overridden",
                "EXTENSIONS": "not_overridden",
            },
            "development": {
                "DEBUG": "not_overridden",
                "SQLALCHEMY_DATABASE_URI": "not_overridden",
                "SQLALCHEMY_TRACK_MODIFICATIONS": "not_overridden",
                "FLASK_ADMIN_NAME": "not_overridden",
                "CACHE_TYPE": "not_overridden",
                "RATELIMIT_ENABLED": "not_overridden",
                "EXTENSIONS": "not_overridden",
                "DEBUG_TOOLBAR_ENABLED": "not_overridden",
                "DEBUG_TB_INTERCEPT_REDIRECTS": "not_overridden",
                "DEBUG_TB_PROFILER_ENABLED": "not_overridden",
                "DEBUG_TB_TEMPLATE_EDITOR_ENABLED": "not_overridden",
                "DEBUG_TB_PANELS": "not_overridden",
            },
            "testing": {
                "FLASK_ADMIN_NAME": "not_overridden",
                "SQLALCHEMY_DATABASE_URI": "not_overridden",
                "CACHE_TYPE": "not_overridden",
            },
            "production": {
                "FLASK_ADMIN_NAME": "not_overridden",
                "CACHE_TYPE": "not_overridden",
                "SQLALCHEMY_DATABASE_URI": "not_overridden",
            },
        }


class GenericHandler:
    def __init__(self, *handlers: Callable):
        self.handlers = handlers

    def __call__(self, answers: Answers):
        for handler in self.handlers:
            r = handler(answers)
            if r:
                return r


class FlaskSketchTomlEncoder(toml.TomlEncoder):
    def __init__(self, _dict=dict, preserve=False, separator=",\r\n"):
        super(FlaskSketchTomlEncoder, self).__init__(_dict, preserve)
        if separator.strip() == "":
            separator = "," + separator
        elif separator.strip(' \t\n\r,'):
            raise ValueError("Invalid separator for arrays")
        self.separator = separator

    def dump_list(self, v):
        t = []
        retval = "[\r\n"
        for u in v:
            t.append(self.dump_value(u))
        while t != []:
            s = []
            for u in t:
                if isinstance(u, list):
                    for r in u:
                        s.append(r)
                else:
                    retval += "\t" + str(u) + self.separator
            t = s
        retval += "]"
        return retval


def has_answers(answers: dict, have: dict = {}, not_have: dict = {}):

    for da in have:
        if not answers.get(da).lower() in have.get(da).lower().split(";"):
            return False

    for nda in not_have:
        if answers.get(nda).lower() in not_have.get(nda).lower().split(";"):
            return False

    return True


def write_tpl(project_name, tpl, tpl_location, path):
    template = pkg_resources.read_text(tpl_location, tpl).replace(
        "application_tpl", project_name
    )
    with open(path, "a") as file:
        file.writelines(template)


def pjoin(*args):
    return "/".join(list(args))


def add_dev_requirements(pf: str, *requirements):
    with open(f"{pf}/requirements-dev.txt", "a") as file:
        for requirement in requirements:
            file.write("{}\r\n".format(requirement))


def add_requirements(pf: str, *requirements):
    with open(f"{pf}/requirements.txt", "a") as file:
        for requirement in requirements:
            file.write("{}\r\n".format(requirement))


def cleanup(answers: Answers):
    ...


def make_commom_folders(answers: Answers):
    paf = answers.application_project_folder
    pf = answers.project_folder
    os.makedirs(pjoin(pf, "tests"))
    os.makedirs(paf)
    os.makedirs(pjoin(paf, "ext"))
    os.makedirs(pjoin(paf, "models"))
    os.makedirs(pjoin(paf, "config"))
    os.makedirs(pjoin(paf, "commands"))
    os.makedirs(pjoin(paf, "examples"))
    if "admin" in answers.features:
        os.makedirs(pjoin(paf, "ext", "admin"))

    open(pjoin(paf, "__init__.py"), 'a').close()
    open(pjoin(paf, "app.py"), 'a').close()
    open(pjoin(paf, "ext", "__init__.py"), 'a').close()
    open(pjoin(paf, "models", "__init__.py"), 'a').close()
    open(pjoin(paf, "config", "__init__.py"), 'a').close()
    open(pjoin(paf, "commands", "__init__.py"), 'a').close()
    open(pjoin(paf, "examples", "__init__.py"), 'a').close()

    write_tpl("", ".gitignore_tpl", templates, pjoin(pf, ".gitignore"))
    write_tpl(
        answers.args.project_name, "wsgi_tpl", templates, pjoin(pf, "wsgi.py")
    )
    write_tpl(
        answers.args.project_name,
        "examples_init_tpl",
        templates.examples,
        pjoin(paf, "examples", "__init__.py"),
    )

    add_requirements(pf, "flask")
    add_dev_requirements(pf, "black", "isort", "flake8")
