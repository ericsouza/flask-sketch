from flask_sketch.utils import (
    Answers,
    write_tpl,
    pjoin,
    add_requirements,
    add_dev_requirements,
)
from flask_sketch import templates


def handle_caching(answers: Answers):
    answers.settings["development"]["CACHE_TYPE"] = "simple"
    answers.settings["testing"]["CACHE_TYPE"] = "simple"
    answers.settings["production"]["CACHE_TYPE"] = "simple"
    answers.settings["default"]["EXTENSIONS"].extend(
        [f"{answers.args.project_name}.ext.caching:init_app"]
    )
    write_tpl(
        answers.args.project_name,
        "ext_caching_tpl",
        templates.ext,
        pjoin(answers.application_project_folder, "ext", "caching.py"),
    )
    write_tpl(
        answers.args.project_name,
        "examples_caching_tpl",
        templates.examples,
        pjoin(
            answers.application_project_folder,
            "examples",
            "caching_examples.py",
        ),
    )
    write_tpl(
        answers.args.project_name,
        "examples_init_caching_tpl",
        templates.examples,
        pjoin(answers.application_project_folder, "examples", "__init__.py",),
    )

    add_requirements(answers.project_folder, "flask-caching")


def handle_limiter(answers: Answers):
    answers.settings["default"][
        "RATELIMIT_DEFAULT"
    ] = "200 per day;50 per hour"
    answers.settings["default"]["RATELIMIT_ENABLED"] = True
    answers.settings["development"]["RATELIMIT_ENABLED"] = False
    answers.settings["default"]["EXTENSIONS"].extend(
        [f"{answers.args.project_name}.ext.limiter:init_app"]
    )
    write_tpl(
        answers.args.project_name,
        "ext_limiter_tpl",
        templates.ext,
        pjoin(answers.application_project_folder, "ext", "limiter.py"),
    )
    write_tpl(
        answers.args.project_name,
        "examples_limiter_tpl",
        templates.examples,
        pjoin(
            answers.application_project_folder,
            "examples",
            "limiter_examples.py",
        ),
    )
    write_tpl(
        answers.args.project_name,
        "examples_init_limiter_tpl",
        templates.examples,
        pjoin(answers.application_project_folder, "examples", "__init__.py",),
    )

    add_requirements(answers.project_folder, "flask-limiter")


def handle_migrate(answers: Answers):
    answers.settings["default"]["EXTENSIONS"].extend(
        [f"{answers.args.project_name}.ext.migrate:init_app"]
    )
    write_tpl(
        answers.args.project_name,
        "ext_migrate_tpl",
        templates.ext,
        pjoin(answers.application_project_folder, "ext", "migrate.py"),
    )

    add_requirements(answers.project_folder, "flask-migrate")


def handle_admin(answers: Answers):
    answers.settings["default"]["EXTENSIONS"].extend(
        [f"{answers.args.project_name}.ext.admin:init_app"]
    )
    if answers.auth_framework == "security_web":
        write_tpl(
            answers.args.project_name,
            "ext_admin_security_tpl",
            templates.ext.admin,
            pjoin(
                answers.application_project_folder,
                "ext",
                "admin",
                "__init__.py",
            ),
        )

    add_requirements(answers.project_folder, "flask-admin")

    if answers.config_framework == "dynaconf":
        answers.settings["default"]["FLASK_ADMIN_TEMPLATE_MODE"] = "bootstrap3"
        answers.settings["development"][
            "FLASK_ADMIN_NAME"
        ] = f"{answers.args.project_name} (Dev)"
        answers.settings["testing"][
            "FLASK_ADMIN_NAME"
        ] = f"{answers.args.project_name} (Testing)"
        answers.settings["production"][
            "FLASK_ADMIN_NAME"
        ] = answers.args.project_name


def handle_debugtoolbar_dynaconf(answers: Answers):
    if answers.settings["development"]["EXTENSIONS"] == "not_overridden":
        answers.settings["development"]["EXTENSIONS"] = []

    answers.settings["development"]["EXTENSIONS"].extend(
        ["flask_debugtoolbar:DebugToolbarExtension", "dynaconf_merge_unique"]
    )
    answers.settings["development"]["DEBUG_TOOLBAR_ENABLED"] = True
    answers.settings["development"]["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
    answers.settings["development"]["DEBUG_TB_PROFILER_ENABLED"] = True
    answers.settings["development"]["DEBUG_TB_TEMPLATE_EDITOR_ENABLED"] = True
    answers.settings["development"]["DEBUG_TB_PANELS"] = []
    answers.settings["development"]["DEBUG_TB_PANELS"].extend(
        [
            "flask_debugtoolbar.panels.versions.VersionDebugPanel",
            "flask_debugtoolbar.panels.sqlalchemy.SQLAlchemyDebugPanel",
            "flask_debugtoolbar.panels.timer.TimerDebugPanel",
            "flask_debugtoolbar.panels.headers.HeaderDebugPanel",
            "flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel",
            "flask_debugtoolbar.panels.template.TemplateDebugPanel",
            "flask_debugtoolbar.panels.route_list.RouteListDebugPanel",
            "flask_debugtoolbar.panels.logger.LoggingPanel",
            "flask_debugtoolbar.panels.profiler.ProfilerDebugPanel",
            "flask_debugtoolbar.panels.config_vars.ConfigVarsDebugPanel",
        ]
    )
    add_dev_requirements(answers.project_folder, "flask-debugtoolbar")


def handle_features(answers: Answers):
    features: list = answers.features
    if "debugtoolbar" in features:
        if answers.config_framework == "dynaconf":
            handle_debugtoolbar_dynaconf(answers)
            features.remove("debugtoolbar")
        else:
            ...

    for feature in answers.features:

        globals()[f"handle_{feature}"](answers)
