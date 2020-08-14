from flask_sketch.make import create_project


def test_web_only_mysql_security_dynaconf_allfeatures():
    answers = {
        'application_type': 'web_only',
        'auth_framework': 'security_web',
        'config_framework': 'dynaconf',
        'database': 'mysql',
        'features': [
            'Migrations (Flask-Migrate)',
            'Admin Interface (Flask-Admin)',
            'Cache (Flask-Caching)',
            'Rate Limiting (Flask-Limiter)',
            'Flask-DebugToolbar',
        ],
    }

    create_project("myproject", answers)


test_web_only_mysql_security_dynaconf_allfeatures()
