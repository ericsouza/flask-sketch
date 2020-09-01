import os
from flask_sketch import templates  # noqa
from flask_sketch.utils import Sketch
from flask_sketch.utils import GenericHandler
from flask_sketch.utils import pjoin


def restx_handler(sketch: Sketch):
    if sketch.api_framework == "restx":
        return True


def smorest_handler(sketch: Sketch):
    if sketch.api_framework == "smorest":
        sketch.add_requirements("flask-smorest")

        sketch.settings["default"]["API_TITLE"] = sketch.project_name
        sketch.settings["default"]["API_VERSION"] = "v1"
        sketch.settings["default"]["OPENAPI_VERSION"] = "3.0.2"
        sketch.settings["default"]["OPENAPI_JSON_PATH"] = "api-spec.json"
        sketch.settings["default"]["OPENAPI_URL_PREFIX"] = "/openapi"
        sketch.settings["default"]["OPENAPI_REDOC_PATH"] = "/redoc"
        sketch.settings["default"][
            "OPENAPI_REDOC_URL"
        ] = "https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js"  # noqa
        sketch.settings["default"]["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
        sketch.settings["default"][
            "OPENAPI_SWAGGER_UI_URL"
        ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

        sketch.add_extensions("api")

        os.makedirs(pjoin(sketch.app_folder, "api", "resources", "examples"))
        open(
            pjoin(
                sketch.app_folder,
                "api",
                "resources",
                "examples",
                "__init__.py",
            ),
            "a",
        ).close()

        sketch.write_template(
            "ext_api_smorest_tpl",
            templates.ext,
            pjoin(sketch.app_folder, "ext", "api.py"),
        )

        sketch.write_template(
            "api_example_smorest_pet_jwt_tpl",
            templates.api.resources.examples,
            pjoin(sketch.app_folder, "api", "resources", "examples", "pet.py"),
        )

        sketch.write_template(
            "models_examples_smorest_pet_tpl",
            templates.models.examples,
            pjoin(sketch.app_folder, "models", "examples", "pet.py"),
        )

        return True


def restful_handler(sketch: Sketch):
    if sketch.api_framework == "restful":
        return True


def none_handler(sketch: Sketch):
    if sketch.api_framework == "none":
        return True


class ApiFrameworkHandler(GenericHandler):
    ...


api_framework_handler = ApiFrameworkHandler(
    restx_handler, smorest_handler, restful_handler, none_handler,
)
