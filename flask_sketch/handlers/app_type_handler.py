from os.path import join as pjoin
import os
from flask_sketch.sketch import Sketch
from flask_sketch.utils import GenericHandler


def app_handler(sketch: Sketch):
    if sketch.have_api:
        sketch.blueprints.extend(["api"])
        os.makedirs(pjoin(sketch.app_folder, "api", "resources"))
        open(pjoin(sketch.app_folder, "api", "__init__.py"), "a").close()
        open(
            pjoin(sketch.app_folder, "api", "resources", "__init__.py"), "a"
        ).close()

    os.makedirs(pjoin(sketch.app_folder, "site"))
    sketch.blueprints.extend(["site"])

    return True


class AppTypeHandler(GenericHandler):
    ...


app_type_handler = AppTypeHandler(app_handler)
