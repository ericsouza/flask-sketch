from argparse import Namespace

from flask_sketch.make import create_project


def test_web_only_mysql_security_dynaconf_allfeatures():
    answers = {
        "application_type": "web_only",
        "auth_framework": "security_web",
        "config_framework": "dynaconf",
        "database": "mysql",
        "features": ["migrate", "caching", "limiter", "debugtoolbar", "admin"],
    }
    args = Namespace(project_name="myproject", e=False, p=True, v=True)
    create_project(args, answers)


def test_web_only_postgres_security_nosettings_allfeatures():
    answers = {
        "application_type": "web_only",
        "auth_framework": "security_web",
        "config_framework": "none",
        "database": "postgres",
        "features": ["migrate", "caching", "limiter", "debugtoolbar", "admin"],
    }
    args = Namespace(project_name="myproject", e=True, p=True, v=False)
    create_project(args, answers)


test_web_only_postgres_security_nosettings_allfeatures()
