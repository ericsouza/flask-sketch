import importlib.resources as pkg_resources
import os
import random
import string
from argparse import Namespace
from typing import Callable

import toml

from flask_sketch import templates

LETTERS = string.ascii_letters
NUMBERS = string.digits
PUNCTUATION = string.punctuation


class Sketch:
    def __init__(self, pf: str, apf: str, answers: dict, args: Namespace):
        self.project_name: str = args.project_name
        self.app_folder_name: str = args.project_name.replace("-", "_")
        self.project_folder: str = pf
        self.app_folder: str = apf
        self.app_type: str = answers.get("application_type")
        self.database: str = answers.get("database")
        self.auth_framework: str = answers.get("auth_framework")
        self.api_framework: str = answers.get("api_framework")
        self.config_framework: str = answers.get("config_framework")
        self.features: list = answers.get("features")
        self.secret_key = random_string(32)
        self.create_examples = args.e
        self.create_virtualenv = args.v
        self.create_pyproject = args.p
        self.requirements = []
        self.dev_requirements = []
        self.extensions = []
        self.blueprints = []
        self.secrets = {"default": {}}
        self.settings = {
            "default": {"EXTENSIONS": []},
            "development": {"EXTENSIONS": []},
            "testing": {},
            "production": {},
        }

    def add_requirements(self, *requirements, dev=False):
        if dev:
            self.dev_requirements.extend(requirements)
        else:
            self.requirements.extend(requirements)

    def add_extensions(self, *extensions):
        self.extensions.extend(extensions)

    def add_blueprints(self, *blueprints):
        self.blueprints.extend(blueprints)

    def write_template(self, template, template_location, path):
        template = pkg_resources.read_text(
            template_location, template
        ).replace("application_tpl", self.app_folder_name)
        with open(path, "a") as file:
            file.writelines(template)


class GenericHandler:
    def __init__(self, *handlers: Callable):
        self.handlers = handlers

    def __call__(self, sketch: Sketch):
        for handler in self.handlers:
            r = handler(sketch)
            if r:
                return r


class FlaskSketchTomlEncoder(toml.TomlEncoder):
    def __init__(self, _dict=dict, preserve=False, separator=",\r\n"):
        super(FlaskSketchTomlEncoder, self).__init__(_dict, preserve)
        if separator.strip() == "":
            separator = "," + separator
        elif separator.strip(" \t\n\r,"):
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


def random_string(length=16):
    """
    Generates a random password having the specified length
    :length -> length of password to be generated. Defaults to 8
        if nothing is specified.
    :returns string <class 'str'>
    """
    # create alphanumerical from string constants
    printable = f"{LETTERS}{NUMBERS}{PUNCTUATION}"

    # convert printable from string to list and shuffle
    printable = list(printable)
    random.shuffle(printable)

    # generate random password and convert to string
    rstring = random.choices(printable, k=length)
    rstring = "".join(rstring)
    return rstring


def has_answers(answers: dict, have: dict = {}, not_have: dict = {}):

    for da in have:
        if not answers.get(da).lower() in have.get(da).lower().split(";"):
            return False

    for nda in not_have:
        if answers.get(nda).lower() in not_have.get(nda).lower().split(";"):
            return False

    return True


"""
def write_tpl(project_name, tpl, tpl_location, path):
    template = pkg_resources.read_text(tpl_location, tpl).replace(
        "application_tpl", project_name.replace("-", "_")
    )
    with open(path, "a") as file:
        file.writelines(template)


 maybe useful
def write_templates(project_name: str, tpl_location, templates_paths: list):
    for tpl_path in templates_paths():
        tpl, path = tpl_path
        write_tpl(project_name, tpl, tpl_location, path)
"""


def pjoin(*args):
    return "/".join(list(args))


def cleanup(sketch: Sketch):
    ...


def make_requirements(sketch: Sketch):
    requirements = [req + "\n" for req in sorted(sketch.requirements)]

    dev_requirements = [req + "\n" for req in sorted(sketch.dev_requirements)]
    dev_requirements.insert(0, "-r requirements.txt\n\n")

    with open(f"{sketch.project_folder}/requirements.txt", "w") as file:
        file.writelines(requirements)

    with open(f"{sketch.project_folder}/requirements-dev.txt", "w") as file:
        file.writelines(dev_requirements)


def make_app(sketch: Sketch):
    aux = ",\n    ".join(sketch.extensions)
    extensions_imports_string = (
        f"from {sketch.app_folder_name}.ext import (\n    {aux}\n)"
    )

    blueprints = [
        f"from {sketch.app_folder_name}.{bp} import {bp}bp"
        for bp in sketch.blueprints
    ]
    blueprints_imports_string = "\n".join(blueprints)

    extensions_inits = [f"{ext}.init_app(app)" for ext in sketch.extensions]
    extensions_inits_string = "\n    ".join(extensions_inits)

    if "debugtoolbar" in sketch.features:
        dev_extensions_inits_string = "if app.debug:\n\
        from {}.ext import debugtoolbar \n\
        debugtoolbar.init_app(app)".format(
            sketch.app_folder_name
        )

    blueprints_register = [
        f"app.register_blueprint({bp}bp)" for bp in sketch.blueprints
    ]

    blueprints_register_string = "\n    ".join(blueprints_register)

    with open(pjoin(sketch.app_folder, "app.py"), "r+") as f:
        template = string.Template(f.read())

        if sketch.config_framework == "dynaconf":
            app_content = template.substitute(
                blueprints_imports=blueprints_imports_string,
                blueprint_registers=blueprints_register_string,
            )
        else:
            app_content = template.substitute(
                extensions_imports=extensions_imports_string,
                blueprints_imports=blueprints_imports_string,
                extensions_inits=extensions_inits_string,
                dev_extentions_inits=dev_extensions_inits_string,
                blueprint_registers=blueprints_register_string,
            )
        f.seek(0)
        f.write(app_content)
        f.truncate()


def make_commom(sketch: Sketch):
    paf = sketch.app_folder
    pf = sketch.project_folder

    os.makedirs(pjoin(pf, "tests"))
    os.makedirs(paf)
    os.makedirs(pjoin(paf, "ext"))
    os.makedirs(pjoin(paf, "models"))
    os.makedirs(pjoin(paf, "config"))
    os.makedirs(pjoin(paf, "commands"))
    os.makedirs(pjoin(paf, "examples"))
    if "admin" in sketch.features:
        os.makedirs(pjoin(paf, "ext", "admin"))
    open(pjoin(paf, "__init__.py"), "a").close()
    open(pjoin(paf, "app.py"), "a").close()
    open(pjoin(paf, "ext", "__init__.py"), "a").close()
    open(pjoin(paf, "models", "__init__.py"), "a").close()
    open(pjoin(paf, "config", "__init__.py"), "a").close()
    open(pjoin(paf, "commands", "__init__.py"), "a").close()
    open(pjoin(paf, "examples", "__init__.py"), "a").close()
    sketch.add_requirements("flask")
    sketch.add_requirements("black", "isort", "flake8", dev=True)

    sketch.write_template(".gitignore_tpl", templates, pjoin(pf, ".gitignore"))
    sketch.write_template("wsgi_tpl", templates, pjoin(pf, "wsgi.py"))
    sketch.write_template(
        "examples_init_tpl",
        templates.examples,
        pjoin(paf, "examples", "__init__.py"),
    )
