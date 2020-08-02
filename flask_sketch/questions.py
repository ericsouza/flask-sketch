from helpers import is_selected


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
        "message": "Select the type of your database",
        "name": "database_type",
        "choices": [
            {"name": "SQL Database (MySQL, Postgres, SQLite)", "value": "sql_database"},
            {"name": "Mongo database", "value": "mongo_database"},
            {"name": "None (no database)", "value": "no_database"},
        ],
        "validate": lambda answer, answers: "You must choose at least one topping."
        if len(answer) == 0
        else True,
    },
    {
        "type": "list",
        "message": "Select your SQL database",
        "name": "sql_database",
        "choices": [{"name": "Postgres"}, {"name": "MySQL",}, {"name": "SQLite"},],
        "when": lambda answers: is_selected(answers, "database_type", "sql_database"),
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
            {"name": "Flask-Restx (Flask-Restplus)",},
            {"name": "Flask-Restless"},
        ],
        "when": lambda answers: "api" in answers.get("application_type"),
        "validate": lambda answer: "You must choose at least one topping."
        if len(answer) == 0
        else True,
    },
    {
        "type": "list",
        "message": "Select Authentication Method",
        "name": "api_auth",
        "choices": [
            {"name": "Flask-Praetorian (recommended)"},
            {"name": "PyJWT",},
            {"name": "None"},
        ],
        "when": lambda answers: "api" in answers.get("application_type"),
        "validate": lambda answer: "You must choose at least one topping."
        if len(answer) == 0
        else True,
    },
    {
        "type": "checkbox",
        "message": "Select the features you need for your project",
        "name": "api_only_features_no_db",
        "choices": [
            {"name": "Caching"},
            {"name": "Pyctuator (integration with Spring Boot Admin"},
            {"name": "Rate Limiting"},
        ],
        "when": lambda answers: is_selected(answers, "database_type", "no_database"),
        "validate": lambda answer: "You must choose at least one topping."
        if len(answer) == 0
        else True,
    },
    {
        "type": "checkbox",
        "message": "Select the features you need for your project",
        "name": "api_only_features",
        "choices": [
            {"name": "Migrations"},
            {"name": "Admin Interface"},
            {"name": "Caching"},
            {"name": "Pyctuator (integration with Spring Boot Admin"},
            {"name": "Rate Limiting"},
        ],
        "when": lambda answers: not is_selected(
            answers, "database_type", "no_database"
        ),
        "validate": lambda answer: "You must choose at least one topping."
        if len(answer) == 0
        else True,
    },
]
