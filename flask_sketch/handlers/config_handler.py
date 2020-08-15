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


def dynaconf_handler(answers: Answers):
    if answers.config_framework == "dynaconf":
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
            pjoin(answers.application_project_folder, "app.py",),
        )

        write_tpl(
            answers.args.project_name,
            "dynaconf_secrets_tpl",
            templates,
            pjoin(answers.project_folder, ".secrets.toml"),
        )

        # write_tpl(
        #     answers.args.project_name,
        #     "dynaconf_settings_tpl",
        #     templates,
        #     pjoin(answers.project_folder, "settings.toml"),
        # )

        settings_toml = answers.settings

        def_cleaned = {
            key: val
            for key, val in settings_toml["default"].items()
            if val != "not_overridden"
        }

        dev_cleaned = {
            key: val
            for key, val in settings_toml["development"].items()
            if val != "not_overridden"
        }

        test_cleaned = {
            key: val
            for key, val in settings_toml["testing"].items()
            if val != "not_overridden"
        }

        prod_cleaned = {
            key: val
            for key, val in settings_toml["production"].items()
            if val != "not_overridden"
        }

        settings_toml["default"] = def_cleaned
        settings_toml["development"] = dev_cleaned
        settings_toml["testing"] = test_cleaned
        settings_toml["production"] = prod_cleaned

        with open(
            pjoin(answers.project_folder, "settings.toml"),
            "w",
            encoding="utf-8",
        ) as file:
            toml.dump(settings_toml, file, encoder=FlaskSketchTomlEncoder())

        add_requirements(answers.project_folder, "dynaconf")

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
