from flask_sketch import templates
from flask_sketch.utils import (
    Sketch,
    GenericHandler,
    pjoin,
)
import os


def app_handler(sketch: Sketch):
    if sketch.app_type == "web_and_api":
        sketch.blueprints.extend(["api"])
        os.makedirs(pjoin(sketch.app_folder, "api", "resources"))
        open(pjoin(sketch.app_folder, "api", "__init__.py"), "a").close()
        open(
            pjoin(sketch.app_folder, "api", "resources", "__init__.py"), "a"
        ).close()

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


app_type_handler = AppTypeHandler(app_handler)
