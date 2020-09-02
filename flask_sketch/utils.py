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
        self.app_type: str = "web_only" if not answers.get(
            "have_api"
        ) else "web_and_api"
        self.have_api = answers.get("have_api")
        self.database: str = answers.get("database")
        self.auth_framework: str = answers.get("auth_framework")
        self.api_auth_framework: str = answers.get("api_auth_framework")
        self.api_framework: str = answers.get("api_framework")
        self.config_framework: str = answers.get("config_framework")
        self.features: list = answers.get("features")
        self.secret_key = random_string(32)
        self.create_examples = args.e
        self.create_virtualenv = args.v
        self.create_pyproject = args.p
        self.requirements = set()
        self.dev_requirements = set()
        self.extensions = []
        self.dev_extensions = []
        self.blueprints = []
        self.template_args = {
            "PWD_VERIFIER_METHOD_IMPORT": f"from {self.app_folder_name}.utils.security.password_hasher import password_hasher",  # noqa
            "PWD_VERIFIER_METHOD": "password_hasher.verify(user.password, password)",
            "API_RBAC_IMPORT": f"from {self.app_folder_name}.utils.security.api_rbac import roles_required, roles_accepted",
            "ROLES_REQUIRED_DECORATOR": "@roles_required(\"admin\")",
            "ROLES_ACCEPTED_DECORATOR": "@roles_accepted(\"admin\", \"editor\")",
        }
        self.secrets = {"default": {}}
        self.settings = {
            "default": {"EXTENSIONS": []},
            "development": {"EXTENSIONS": []},
            "testing": {},
            "production": {},
        }

    def add_requirements(self, *requirements, dev=False):
        if dev:
            self.dev_requirements.update(requirements)
        else:
            self.requirements.update(requirements)

    def add_extensions(self, *extensions, dev=False):
        if dev:
            self.dev_extensions.extend(extensions)
        else:
            self.extensions.extend(extensions)

    def add_blueprints(self, *blueprints):
        self.blueprints.extend(blueprints)

    def write_template(self, template, template_location, path, mode="a"):

        if mode == "w" and os.path.isfile(path) and os.stat(path).st_size > 0:
            return None
            
        # if os.path.isfile(path):
        #     if os.stat(path).st_size > 0:
        #         return None

        template = pkg_resources.read_text(
            template_location, template
        ).replace("application_tpl", self.app_folder_name)

        with open(path, mode) as file:
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
        if isinstance(answers.get(da), bool):
            if not answers.get(da) == have.get(da):
                return False
        elif not answers.get(da) in have.get(da).split(";"):
            return False

    for nda in not_have:
        if answers.get(nda) in not_have.get(nda).split(";"):
            return False

    return True


def pjoin(*args):
    return "/".join(list(args))


def cleanup(sketch: Sketch):
    files = get_list_of_files(sketch.app_folder)
    for file in files:
        with open(file, "r+") as f:
            template = string.Template(f.read())
            tpl_identifiers = find_template_identifiers(template)
            tpl_dict = {}
            for k in tpl_identifiers:
                tpl_dict[k] = ""

            new_content = template.substitute(**tpl_dict)

            f.seek(0)
            f.write(new_content)
            f.truncate()


def get_list_of_files(dir_name):
    # create a list of file and sub directories
    # names in the given directory
    list_of_file = os.listdir(dir_name)
    all_files = list()
    # Iterate over all the entries
    for entry in list_of_file:
        # Create full path
        full_path = os.path.join(dir_name, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(full_path):
            all_files = all_files + get_list_of_files(full_path)
        else:
            all_files.append(full_path)

    return all_files


def make_requirements(sketch: Sketch):
    requirements = [req + "\n" for req in sorted(list(sketch.requirements))]

    dev_requirements = [
        req + "\n" for req in sorted(list(sketch.dev_requirements))
    ]
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

    dev_extensions_inits_string = ""
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


def find_template_identifiers(template: string.Template):
    return set(
        [
            s[1] or s[2]
            for s in string.Template.pattern.findall(template.template)
            if s[1] or s[2]
        ]
    )


def make_template_args(sketch: Sketch):
    files = get_list_of_files(sketch.app_folder)
    for file in files:
        with open(file, "r+") as f:
            template = string.Template(f.read())
            tpl_identifiers = find_template_identifiers(template)
            args_keys = tpl_identifiers & set(sketch.template_args.keys())
            tpl_dict = {}
            for k in args_keys:
                tpl_dict[k] = sketch.template_args[k]

            new_content = template.substitute(**tpl_dict)

            f.seek(0)
            f.write(new_content)
            f.truncate()


def make_commom(sketch: Sketch):
    paf = sketch.app_folder
    pf = sketch.project_folder

    os.makedirs(pjoin(pf, "tests"))
    os.makedirs(paf)
    os.makedirs(pjoin(paf, "ext"))
    os.makedirs(pjoin(paf, "models", "examples"))
    os.makedirs(pjoin(paf, "config"))
    os.makedirs(pjoin(paf, "commands"))
    os.makedirs(pjoin(paf, "utils", "security"))
    os.makedirs(pjoin(paf, "examples"))
    if "admin" in sketch.features:
        os.makedirs(pjoin(paf, "ext", "admin"))
    open(pjoin(paf, "__init__.py"), "a").close()
    open(pjoin(paf, "app.py"), "a").close()
    open(pjoin(paf, "ext", "__init__.py"), "a").close()
    open(pjoin(paf, "models", "__init__.py"), "a").close()
    open(pjoin(paf, "models", "examples", "__init__.py"), "a").close()
    open(pjoin(paf, "config", "__init__.py"), "a").close()
    open(pjoin(paf, "commands", "__init__.py"), "a").close()
    open(pjoin(paf, "utils", "__init__.py"), "a").close()
    open(pjoin(paf, "utils", "security", "__init__.py"), "a").close()
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
