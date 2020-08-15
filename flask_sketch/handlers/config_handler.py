import toml
from flask_sketch import templates
from flask_sketch.utils import (
    Answers,
    GenericHandler,
    write_tpl,
    pjoin,
    add_requirements,
    FlaskSketchTomlEncoder,
)


def clean_settings(settings: dict):
    s = settings
    for k in s:
        s[k] = {
            key: val for key, val in s[k].items() if val != "not_overridden"
        }
    return s


def dynaconf_handler(answers: Answers):
    if answers.config_framework == "dynaconf":
        add_requirements(answers.project_folder, "dynaconf")

        settings_toml = clean_settings(answers.settings)
        secrets_toml = clean_settings(answers.secrets)

        with open(
            pjoin(answers.project_folder, "settings.toml"),
            "w",
            encoding="utf-8",
        ) as file:
            toml.dump(settings_toml, file, encoder=FlaskSketchTomlEncoder())

        with open(
            pjoin(answers.project_folder, ".secrets.toml"),
            "w",
            encoding="utf-8",
        ) as file:
            toml.dump(secrets_toml, file, encoder=FlaskSketchTomlEncoder())

        write_tpl(
            answers.args.project_name,
            "config_dynaconf_tpl",
            templates.config,
            pjoin(
                answers.application_project_folder, "config", "__init__.py",
            ),
        )
        write_tpl(
            answers.args.project_name,
            "app_web_only_dynaconf_tpl",
            templates.app,
            pjoin(answers.application_project_folder, "app.py"),
        )

        return True


def environs_handler(answers: Answers):
    if answers.config_framework == "environs":
        return True


def none_handler(answers: Answers):
    if answers.config_framework == "none":
        return True


class ConfigHandler(GenericHandler):
    ...


config_handler = ConfigHandler(
    dynaconf_handler, environs_handler, none_handler,
)
