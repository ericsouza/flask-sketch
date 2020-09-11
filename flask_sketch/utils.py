from os.path import join as pjoin
import os
import random
import string
from typing import Callable

from flask_sketch import templates
from flask_sketch.sketch import Sketch

LETTERS = string.ascii_letters
NUMBERS = string.digits
PUNCTUATION = string.punctuation


class GenericHandler:
    def __init__(self, *handlers: Callable):
        self.handlers = handlers

    def __call__(self, sketch: Sketch):
        for handler in self.handlers:
            r = handler(sketch)
            if r:
                return r


def snake_to_camel(s: str):
    return "".join(x.capitalize() for x in s.split("_"))


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
    extensions_imports_string = ""
    for extension in sketch.extensions:
        ext = extension.rsplit(".", 1)[-1]
        aux = ""
        if len(extension.rsplit(".", 1)) > 1:
            aux = "." + extension.rsplit(".", 1)[0]
        extensions_imports_string += (
            f"from {sketch.app_folder_name}.ext{aux} import {ext}\n"
        )

    blueprints = [
        f"from {sketch.app_folder_name}.{bp} import {bp}bp"
        for bp in sketch.blueprints
    ]
    blueprints_imports_string = "\n".join(blueprints)

    extensions_inits = [
        "{}.init_app(app)".format(ext.split(".")[-1])
        for ext in sketch.extensions
    ]
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

    sketch.secret_key = random_string(32)

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
