from .helpers import has_answers


questions = [
    {
        "type": "list",
        "message": "Select the type of your project",
        "name": "application_type",
        "choices": [
            {"name": "Web Only (no API)", "value": "web_only"},
            {"name": "API Only (no frontend)", "value": "api_only"},
            {"name": "Web and API", "value": "web_and_api"},
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
            {"name": "Postgres"},
            {"name": "MySQL"},
            {"name": "SQLite"},
            {"name": "MongoDB"},
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
            {"name": "Flask-Login"},
            {"name": "Flask-Security-Too (aka Flask-Security)"},
            {"name": "Flask-HTTPAuth"},
            {"name": "None"},
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
            {"name": "Flask-Praetorian (recommended)"},
            {"name": "PyJWT"},
            {"name": "None"},
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
            {"name": "Flask-Login + PyJWT (for api auth)"},
            {"name": "Flask-Security-Too (aka Flask-Security)"},
            {"name": "Flask-HTTPAuth"},
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
            {"name": "Flask-RESTful"},
            {"name": "Flask-Restless"},
            {
                "name": "Flask-Restx (aka Flask-Restplus)",
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
            {"name": "Flask-CORS"},
            {"name": "Flask-HTMLmin"},
            {"name": "Flask-Assets"},
            {"name": "Flask-Talisman"},
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
            {"name": "Flask-MonitoringDashboard"},
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
            {"name": "Flask-MonitoringDashboard"},
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
            {"name": "Flasgger", "disabled": "Not yet supported"},
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
            {"name": "Pyctuator (integration with Spring Boot Admin"},
            {"name": "Rate Limiting (Flask-Limiter)"},
            {"name": "Flasgger", "disabled": "Not yet supported"},
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
            {"name": "Flask-MonitoringDashboard"},
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
            {"name": "Flask-MonitoringDashboard"},
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
