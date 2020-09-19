import importlib.resources as pkg_resources

import os

import string
from argparse import Namespace

import toml

LETTERS = string.ascii_letters
NUMBERS = string.digits
PUNCTUATION = string.punctuation


class Sketch:
    def __init__(self, pf: str, apf: str, answers: dict, args: Namespace):
        self.project_name: str = args.project_name
        self.app_folder_name: str = args.project_name.replace("-", "_")
        self.project_folder: str = pf
        self.app_folder: str = apf
        self.have_api = answers.get("have_api")
        self.database: str = answers.get("database")
        self.auth_framework: str = answers.get("auth_framework")
        self.api_auth_framework: str = answers.get("api_auth_framework")
        self.api_framework: str = answers.get("api_framework")
        self.config_framework: str = answers.get("config_framework")
        self.features: list = answers.get("features")
        self.secret_key = ""
        # self.create_examples = args.e
        self.create_virtualenv = args.v
        # self.create_pyproject = args.p
        self.requirements = set()
        self.dev_requirements = set()
        self.extensions = []
        self.dev_extensions = []
        self.blueprints = []
        self.template_args = {
            "PWD_VERIFIER_METHOD_IMPORT": f"from {self.app_folder_name}.utils.security.password_hasher import password_hasher",  # noqa
            "PWD_VERIFIER_METHOD": "password_hasher.verify(user.password, password)",
            "API_RBAC_IMPORT": f"from {self.app_folder_name}.utils.security.api_rbac import roles_required, roles_accepted",
            "ROLES_REQUIRED_DECORATOR": '@roles_required("admin")',
            "ROLES_ACCEPTED_DECORATOR": '@roles_accepted("admin", "editor")',
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
