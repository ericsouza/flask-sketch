from flask_sketch import templates
from flask_sketch.utils import (
    Sketch,
    GenericHandler,
    pjoin,
)
import os


def web_only_handler(sketch: Sketch):
    if sketch.app_type == "web_and_api":
        os.makedirs(pjoin(sketch.app_folder, "api", "resources"))

    os.makedirs(pjoin(sketch.app_folder, "site"))
    sketch.blueprints.extend(["site"])

    sketch.write_template(
        "site_web_only_init_tpl",
        templates.site,
        pjoin(sketch.app_folder, "site", "__init__.py"),
    )
    sketch.write_template(
        "site_web_only_views_tpl",
        templates.site,
        pjoin(sketch.app_folder, "site", "views.py"),
    )

    return True


class AppTypeHandler(GenericHandler):
    ...


app_type_handler = AppTypeHandler(web_only_handler)
