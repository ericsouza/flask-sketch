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
            "app_dynaconf_conf_tpl",
            templates.app,
            pjoin(answers.application_project_folder, "app.py"),
        )

        return True


def environs_handler(answers: Answers):
    if answers.config_framework == "environs":
        return True


def none_handler(answers: Answers):
    if answers.config_framework == "none":
        sketch_settings = clean_settings(answers.settings)

        secrets_cfg = dict(clean_settings(answers.secrets)["default"])

        settings_cfg = dict(sketch_settings["default"])
        settings_cfg.update(dict(sketch_settings["production"]))
        del settings_cfg["EXTENSIONS"]

        dev_settings_cfg = dict(sketch_settings["default"])
        dev_settings_cfg.update(dict(sketch_settings["development"]))
        del dev_settings_cfg["EXTENSIONS"]

        secrets_cfg = dict(
            sorted(
                secrets_cfg.items(),
                key=lambda x: x[0].encode('utf-8').decode('unicode_escape'),
            )
        )
        settings_cfg = dict(
            sorted(
                settings_cfg.items(),
                key=lambda x: x[0].encode('utf-8').decode('unicode_escape'),
            )
        )
        dev_settings_cfg = dict(
            sorted(
                dev_settings_cfg.items(),
                key=lambda x: x[0].encode('utf-8').decode('unicode_escape'),
            )
        )

        secrets_cfg_output = []
        for k, val in secrets_cfg.items():
            secrets_cfg_output.append(f'{k} = {repr(val)}\n')

        settings_cfg_output = []
        for k, val in settings_cfg.items():
            settings_cfg_output.append(f'{k} = {repr(val)}\n')

        dev_settings_cfg_output = []
        for k, val in dev_settings_cfg.items():
            dev_settings_cfg_output.append(f'{k} = {repr(val)}\n')

        with open(pjoin(answers.project_folder, ".secrets.cfg"), "w",) as file:
            file.writelines(secrets_cfg_output)

        with open(pjoin(answers.project_folder, "settings.cfg"), "w",) as file:
            file.writelines(settings_cfg_output)

        with open(
            pjoin(answers.project_folder, "settings-dev.cfg"), "w",
        ) as file:
            file.writelines(dev_settings_cfg_output)

        write_tpl(
            answers.args.project_name,
            "config_none_tpl",
            templates.config,
            pjoin(
                answers.application_project_folder, "config", "__init__.py",
            ),
        )

        write_tpl(
            answers.args.project_name,
            "app_none_conf_framework_tpl",
            templates.app,
            pjoin(answers.application_project_folder, "app.py"),
        )

        return True


class ConfigHandler(GenericHandler):
    ...


config_handler = ConfigHandler(
    dynaconf_handler, environs_handler, none_handler,
)
