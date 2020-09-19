from os.path import join as pjoin
from flask_sketch.sketch import Sketch
from flask_sketch.utils import snake_to_camel
from flask_sketch import templates
from uuid import uuid4


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
    sketch.settings["development"]["ADMIN_NAME"] = "{} (Dev)".format(
        snake_to_camel(sketch.project_name)
    )
    sketch.settings["testing"]["ADMIN_NAME"] = "{} (Testing)".format(
        snake_to_camel(sketch.project_name)
    )
    sketch.settings["production"]["ADMIN_NAME"] = snake_to_camel(
        sketch.project_name
    )

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

    if sketch.auth_framework == "none":
        sketch.add_requirements("flask-basicauth")
        sketch.add_extensions("admin.basic_auth")
        sketch.secrets["default"]["BASIC_AUTH_USERNAME"] = "admin"
        sketch.secrets["default"]["BASIC_AUTH_PASSWORD"] = str(uuid4())

        sketch.write_template(
            "ext_basicauth_tpl",
            templates.ext.admin,
            pjoin(sketch.app_folder, "ext", "admin", "basic_auth.py",),
        )

        sketch.write_template(
            "ext_admin_basicauth_tpl",
            templates.ext.admin,
            pjoin(sketch.app_folder, "ext", "admin", "__init__.py",),
        )


def handle_debugtoolbar(sketch: Sketch):
    sketch.add_requirements("flask-debugtoolbar", dev=True)

    sketch.add_extensions("debugtoolbar", dev=True)

    sketch.settings["development"]["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

    if sketch.database == "mongodb":
        sketch.settings["development"]["DEBUG_TB_PANELS"] = [
            "flask_debugtoolbar.panels.versions.VersionDebugPanel",
            "flask_debugtoolbar.panels.timer.TimerDebugPanel",
            "flask_debugtoolbar.panels.headers.HeaderDebugPanel",
            "flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel",
            "flask_debugtoolbar.panels.template.TemplateDebugPanel",
            "flask_debugtoolbar.panels.route_list.RouteListDebugPanel",
            "flask_debugtoolbar.panels.logger.LoggingPanel",
            "flask_debugtoolbar.panels.profiler.ProfilerDebugPanel",
            "flask_debugtoolbar.panels.config_vars.ConfigVarsDebugPanel",
        ]

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
