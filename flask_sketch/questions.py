from helpers import has_answers


questions = [
    {
        "type": "list",
        "message": "Select the type of your project",
        "name": "application_type",
        "choices": [
            {"name": "API Only (no frontend)", "value": "api_only"},
            {
                "name": "Web Only (no API)",
                "value": "web_only",
                "disabled": "Not yet supported",
            },
            {
                "name": "Web and API",
                "value": "web_and_api",
                "disabled": "Not yet supported",
            },
        ],
        "validate": lambda answer: "You must choose at least one topping."
        if len(answer) == 0
        else True,
    },
    {
        "type": "list",
        "message": "Select your database",
        "name": "database",
        "choices": [
            {"name": "SQLite", "value": "sqlite"},
            {
                "name": "Postgres",
                "value": "postgres",
                "disabled": "Not yet supported",
            },
            {
                "name": "MySQL",
                "value": "mysql",
                "disabled": "Not yet supported",
            },
            {
                "name": "MongoDB",
                "value": "mongodb",
                "disabled": "Not yet supported",
            },
            {"name": "None (no database)", "value": "no_database"},
        ],
        "validate": lambda answer: "You must choose at least one topping."
        if len(answer) == 0
        else True,
    },
    {
        "type": "list",
        "message": "Select the Authentication Framework",
        "name": "auth_framework",
        "choices": [
            {"name": "Flask-Login", "value": "flask_login"},
            {
                "name": "Flask-Security-Too (aka Flask-Security)",
                "value": "flask_security_too",
            },
            {"name": "Flask-HTTPAuth", "value": "flask_httpauth"},
            {"name": "None", "value": "no_security"},
        ],
        "when": lambda answers: has_answers(
            answers, have={"application_type": "web_only"}
        ),
        "validate": lambda answer: "You must choose at least one topping."
        if len(answer) == 0
        else True,
    },
    {
        "type": "list",
        "message": "Select the Authentication Framework",
        "name": "auth_framework",
        "choices": [
            {
                "name": "Flask-Praetorian (recommended)",
                "value": "flask_praetorian",
            },
            {
                "name": "PyJWT",
                "value": "pyjwt",
                "disabled": "Not yet supported",
            },
            {"name": "None", "value": "no_security"},
        ],
        "when": lambda answers: has_answers(
            answers, have={"application_type": "api_only"}
        ),
        "validate": lambda answer: "You must choose at least one topping."
        if len(answer) == 0
        else True,
    },
    {
        "type": "list",
        "message": "Select the Authentication Framework",
        "name": "auth_framework",
        "choices": [
            {
                "name": "Flask-Login + PyJWT (for api auth)",
                "value": "flask_login_pyjwt",
            },
            {
                "name": "Flask-Security-Too (aka Flask-Security)",
                "value": "flask_security_too",
            },
            {"name": "Flask-HTTPAuth", "value": "flask_httpauth"},
            {"name": "None"},
        ],
        "when": lambda answers: has_answers(
            answers, have={"application_type": "web_and_api"}
        ),
        "validate": lambda answer: "You must choose at least one topping."
        if len(answer) == 0
        else True,
    },
    {
        "type": "list",
        "message": "Select your API Framework",
        "name": "api_framework",
        "choices": [
            {
                "name": "Flask-Restx (aka Flask-Restplus)",
                "value": "flask_restx",
            },
            {
                "name": "Flask-RESTful",
                "value": "flask_restful",
                "disabled": "Not yet supported",
            },
            {
                "name": "Flask-Restless",
                "value": "flask_restless",
                "disabled": "Not yet supported",
            },
        ],
        "when": lambda answers: "api" in answers.get("application_type"),
        "validate": lambda answer: "You must choose at least one topping."
        if len(answer) == 0
        else True,
    },
    {
        "type": "checkbox",
        "message": "Select the frontend features.",
        "name": "frontend_features",
        "choices": [
            {"name": "Flask-CORS", "disabled": "Not yet supported"},
            {"name": "Flask-HTMLmin", "disabled": "Not yet supported"},
            {"name": "Flask-Assets", "disabled": "Not yet supported"},
            {"name": "Flask-Talisman", "disabled": "Not yet supported"},
        ],
        "when": lambda answers: "web" in answers.get("application_type"),
    },
    {
        "type": "checkbox",
        "message": "Select some more features for your project",
        "name": "features",
        "choices": [
            {"name": "Migrations (Flask-Migrate)"},
            {"name": "Admin Interface (Flask-Admin)"},
            {"name": "Cache (Flask-Caching)"},
            {"name": "Pyctuator (integration with Spring Boot Admin"},
            {"name": "Rate Limiting (Flask-Limiter)"},
            {"name": "Flask-DebugToolbar"},
            {
                "name": "Flask-MonitoringDashboard",
                "disabled": "Not yet supported",
            },
        ],
        "when": lambda answers: has_answers(
            answers,
            have={"application_type": "web_only"},
            not_have={"database": "no_database"},
        ),
    },
    {
        "type": "checkbox",
        "message": "Select some more features for your project",
        "name": "features",
        "choices": [
            {"name": "Cache (Flask-Caching)"},
            {"name": "Pyctuator (integration with Spring Boot Admin"},
            {"name": "Rate Limiting (Flask-Limiter)"},
            {"name": "Flask-DebugToolbar"},
            {
                "name": "Flask-MonitoringDashboard",
                "disabled": "Not yet supported",
            },
        ],
        "when": lambda answers: has_answers(
            answers,
            have={"application_type": "web_only", "database": "no_database"},
        ),
    },
    {
        "type": "checkbox",
        "message": "Select some more features for your project",
        "name": "features",
        "choices": [
            {"name": "Migrations (Flask-Migrate)"},
            {"name": "Admin Interface (Flask-Admin)"},
            {"name": "Cache (Flask-Caching)"},
            {"name": "Pyctuator (integration with Spring Boot Admin"},
            {"name": "Rate Limiting (Flask-Limiter)"},
        ],
        "when": lambda answers: has_answers(
            answers,
            have={"application_type": "api_only"},
            not_have={"database": "no_database"},
        ),
    },
    {
        "type": "checkbox",
        "message": "Select some more features for your project",
        "name": "features",
        "choices": [
            {"name": "Cache (Flask-Caching)"},
            {"name": "Pyctuator (for integration with Spring Boot Admin"},
            {"name": "Rate Limiting (Flask-Limiter)"},
        ],
        "when": lambda answers: has_answers(
            answers,
            have={"application_type": "api_only", "database": "no_database"},
        ),
    },
    {
        "type": "checkbox",
        "message": "Select some more features for your project",
        "name": "features",
        "choices": [
            {"name": "Migrations (Flask-Migrate)"},
            {"name": "Admin Interface (Flask-Admin)"},
            {"name": "Cache (Flask-Caching)"},
            {"name": "Pyctuator (integration with Spring Boot Admin"},
            {"name": "Rate Limiting (Flask-Limiter)"},
            {"name": "Flask-DebugToolbar"},
            {
                "name": "Flask-MonitoringDashboard",
                "disabled": "Not yet supported",
            },
            {"name": "Flasgger", "disabled": "Not yet supported"},
        ],
        "when": lambda answers: has_answers(
            answers,
            have={"application_type": "web_and_api"},
            not_have={"database": "no_database"},
        ),
    },
    {
        "type": "checkbox",
        "message": "Select some more features for your project",
        "name": "features",
        "choices": [
            {"name": "Cache (Flask-Caching)"},
            {"name": "Pyctuator (integration with Spring Boot Admin"},
            {"name": "Rate Limiting (Flask-Limiter)"},
            {"name": "Flask-DebugToolbar"},
            {
                "name": "Flask-MonitoringDashboard",
                "disabled": "Not yet supported",
            },
            {"name": "Flasgger", "disabled": "Not yet supported"},
        ],
        "when": lambda answers: has_answers(
            answers,
            have={
                "application_type": "web_and_api",
                "database": "no_database",
            },
        ),
    },
]
