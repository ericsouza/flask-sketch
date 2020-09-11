from collections import OrderedDict
import toml
from os.path import join as pjoin
from flask_sketch import templates
from flask_sketch.sketch import Sketch, FlaskSketchTomlEncoder
from flask_sketch.utils import GenericHandler


def sort_settings(settings: dict):
    s = settings
    for k in s:
        s[k] = OrderedDict(sorted(s[k].items()))
    return s


def dynaconf_handler(sketch: Sketch):
    if sketch.config_framework == "dynaconf":
        sketch.add_requirements("dynaconf")

        settings_toml = sort_settings(sketch.settings)
        secrets_toml = sort_settings(sketch.secrets)

        try:
            sketch.dev_extensions.remove("debugtoolbar")
            settings_toml["development"]["EXTENSIONS"] = [
                "flask_debugtoolbar:DebugToolbarExtension",
                "dynaconf_merge_unique",
            ]

        except ValueError:
            settings_toml["development"]["EXTENSIONS"] = [
                "dynaconf_merge_unique"
            ]

        for extension in sketch.extensions:
            ext = extension.rsplit(".", 1)[-1]
            aux = ""
            if len(extension.rsplit(".", 1)) > 1:
                aux = "." + extension.rsplit(".", 1)[0]
            settings_toml["default"]["EXTENSIONS"].append(
                "{}.ext{}.{}:init_app".format(sketch.app_folder_name, aux, ext)
            )

        with open(pjoin(sketch.project_folder, "settings.toml"), "w") as f:
            toml.dump(settings_toml, f, encoder=FlaskSketchTomlEncoder())

        with open(pjoin(sketch.project_folder, ".secrets.toml"), "w") as f:
            toml.dump(secrets_toml, f, encoder=FlaskSketchTomlEncoder())

        sketch.write_template(
            "config_dynaconf_tpl",
            templates.config,
            pjoin(sketch.app_folder, "config", "__init__.py",),
        )
        sketch.write_template(
            "app_dynaconf_conf_tpl",
            templates.app,
            pjoin(sketch.app_folder, "app.py"),
        )

        return True


def environs_handler(sketch: Sketch):
    if sketch.config_framework == "environs":
        return True


def none_handler(sketch: Sketch):
    if sketch.config_framework == "none":

        secrets_cfg = sort_settings(sketch.secrets)["default"]

        settings_cfg = {"default": {}}
        settings_cfg["default"].update(sketch.settings["default"])
        settings_cfg["default"].update(sketch.settings["production"])
        del settings_cfg["default"]["EXTENSIONS"]
        settings_cfg = sort_settings(settings_cfg)

        dev_settings_cfg = {"default": {}}
        dev_settings_cfg["default"].update(sketch.settings["default"])
        dev_settings_cfg["default"].update(sketch.settings["development"])
        del dev_settings_cfg["default"]["EXTENSIONS"]
        dev_settings_cfg = sort_settings(dev_settings_cfg)

        secrets_cfg_output = []
        for k, val in secrets_cfg.items():
            secrets_cfg_output.append(f"{k} = {repr(val)}\n")

        settings_cfg_output = []
        for k, val in settings_cfg["default"].items():
            settings_cfg_output.append(f"{k} = {repr(val)}\n")

        dev_settings_cfg_output = []
        for k, val in dev_settings_cfg["default"].items():
            dev_settings_cfg_output.append(f"{k} = {repr(val)}\n")

        with open(pjoin(sketch.project_folder, ".secrets.cfg"), "w",) as f:
            f.writelines(secrets_cfg_output)

        with open(pjoin(sketch.project_folder, "settings.cfg"), "w",) as f:
            f.writelines(settings_cfg_output)

        with open(pjoin(sketch.project_folder, "settings-dev.cfg"), "w",) as f:
            f.writelines(dev_settings_cfg_output)

        sketch.write_template(
            "config_none_tpl",
            templates.config,
            pjoin(sketch.app_folder, "config", "__init__.py",),
        )

        sketch.write_template(
            "app_none_conf_framework_tpl",
            templates.app,
            pjoin(sketch.app_folder, "app.py"),
        )

        return True


class ConfigHandler(GenericHandler):
    ...


config_handler = ConfigHandler(
    dynaconf_handler, environs_handler, none_handler,
)
