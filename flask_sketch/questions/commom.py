commom_questions = [
    {
        "type": "list",
        "message": "Select the type of your project",
        "name": "application_type",
        "choices": [
            {"name": "API Only (no frontend)", "value": "api_only"},
            {"name": "Web Only (no API)", "value": "web_only"},
            {
                "name": "Web and API",
                "value": "web_and_api",
                "disabled": "Soon will be supported.",
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
            {"name": "Postgres", "value": "postgres"},
            {"name": "MySQL", "value": "mysql"},
            {"name": "MongoDB", "value": "mongodb"},
            {"name": "None (no database)", "value": "none"},
        ],
        "validate": lambda answer: "You must choose at least one topping."
        if len(answer) == 0
        else True,
    },
]
