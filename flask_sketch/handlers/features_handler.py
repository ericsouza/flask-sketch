from flask_sketch.utils import (
    Sketch,
    pjoin,
)
from flask_sketch import templates


def handle_caching(sketch: Sketch):
    sketch.add_requirements("flask-caching")

    sketch.settings["development"]["CACHE_TYPE"] = "simple"
    sketch.settings["testing"]["CACHE_TYPE"] = "simple"
    sketch.settings["production"]["CACHE_TYPE"] = "simple"

    sketch.add_extensions("caching")

    sketch.write_template(
        "ext_caching_tpl",
        templates.ext,
        pjoin(sketch.app_folder, "ext", "caching.py"),
    )
    sketch.write_template(
        "examples_caching_tpl",
        templates.examples,
        pjoin(sketch.app_folder, "examples", "caching_examples.py",),
    )
    sketch.write_template(
        "examples_init_caching_tpl",
        templates.examples,
        pjoin(sketch.app_folder, "examples", "__init__.py",),
    )


def handle_limiter(sketch: Sketch):
    sketch.add_requirements("flask-limiter")

    sketch.settings["default"]["RATELIMIT_DEFAULT"] = "200 per day;50 per hour"
    sketch.settings["default"]["RATELIMIT_ENABLED"] = True
    sketch.settings["development"]["RATELIMIT_ENABLED"] = False

    sketch.add_extensions("limiter")

    sketch.write_template(
        "ext_limiter_tpl",
        templates.ext,
        pjoin(sketch.app_folder, "ext", "limiter.py"),
    )
    sketch.write_template(
        "examples_limiter_tpl",
        templates.examples,
        pjoin(sketch.app_folder, "examples", "limiter_examples.py",),
    )
    sketch.write_template(
        "examples_init_limiter_tpl",
        templates.examples,
        pjoin(sketch.app_folder, "examples", "__init__.py",),
    )


def handle_migrate(sketch: Sketch):
    sketch.add_requirements("flask-migrate")

    sketch.add_extensions("migrate")

    sketch.write_template(
        "ext_migrate_tpl",
        templates.ext,
        pjoin(sketch.app_folder, "ext", "migrate.py"),
    )


def handle_admin(sketch: Sketch):
    sketch.add_requirements("flask-admin")

    sketch.add_extensions("admin")

    sketch.settings["default"]["ADMIN_TEMPLATE_MODE"] = "bootstrap3"
    sketch.settings["development"][
        "ADMIN_NAME"
    ] = f"{sketch.project_name} (Dev)"
    sketch.settings["testing"][
        "ADMIN_NAME"
    ] = f"{sketch.project_name} (Testing)"
    sketch.settings["production"]["ADMIN_NAME"] = sketch.project_name

    # TODO refact this part to not use a lot of if statements
    if sketch.auth_framework == "security":
        sketch.write_template(
            "ext_admin_security_tpl",
            templates.ext.admin,
            pjoin(sketch.app_folder, "ext", "admin", "__init__.py",),
        )

    if sketch.auth_framework == "login":
        sketch.write_template(
            "ext_admin_login_tpl",
            templates.ext.admin,
            pjoin(sketch.app_folder, "ext", "admin", "__init__.py",),
        )


def handle_debugtoolbar(sketch: Sketch):
    sketch.add_requirements("flask-debugtoolbar", dev=True)

    sketch.add_extensions("debugtoolbar", dev=True)

    sketch.settings["development"]["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
    if sketch.config_framework != "dynaconf":
        sketch.write_template(
            "ext_debugtoolbar_tpl",
            templates.ext,
            pjoin(sketch.app_folder, "ext", "debugtoolbar.py",),
        )


def handle_cors(sketch: Sketch):
    sketch.add_requirements("flask-cors")
    sketch.add_extensions("cors")

    sketch.write_template(
        "ext_cors_tpl",
        templates.ext,
        pjoin(sketch.app_folder, "ext", "cors.py",),
    )


def handle_features(sketch: Sketch):
    for feature in sketch.features:
        globals()[f"handle_{feature}"](sketch)
