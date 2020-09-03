import os
from flask_sketch import templates  # noqa
from flask_sketch.utils import Sketch
from flask_sketch.utils import GenericHandler
from flask_sketch.utils import pjoin


def restx_handler(sketch: Sketch):
    if sketch.api_framework == "restx":
        sketch.add_requirements("flask-restx")

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

        if sketch.api_auth_framework == "jwt_extended":
            sketch.write_template(
                "api_init_restx_jwtext_tpl",
                templates.api,
                pjoin(sketch.app_folder, "api", "__init__.py"),
            )
        else:
            sketch.write_template(
                "api_init_restx_noauth_tpl",
                templates.api,
                pjoin(sketch.app_folder, "api", "__init__.py"),
            )

        if sketch.api_auth_framework == "none":
            resource_tpl = "api_examples_restx_pet_tpl"
        else:
            resource_tpl = "api_examples_restx_pet_auth_tpl"

        sketch.write_template(
            resource_tpl,
            templates.api.resources.examples,
            pjoin(sketch.app_folder, "api", "resources", "examples", "pet.py"),
        )

        sketch.write_template(
            "models_examples_smorest_pet_tpl",
            templates.models.examples,
            pjoin(sketch.app_folder, "models", "examples", "pet.py"),
        )

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

        if sketch.api_auth_framework == "jwt_extended":
            sketch.write_template(
                "api_init_jwt_extended_tpl",
                templates.api,
                pjoin(sketch.app_folder, "api", "__init__.py"),
            )

        sketch.write_template(
            "ext_api_smorest_tpl",
            templates.ext,
            pjoin(sketch.app_folder, "ext", "api.py"),
        )

        if sketch.api_auth_framework == "none":
            resource_tpl = "api_example_smorest_pet_tpl"
        else:
            resource_tpl = "api_example_smorest_pet_auth_tpl"

        sketch.write_template(
            resource_tpl,
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
