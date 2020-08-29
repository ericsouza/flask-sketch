commom_questions = [
    {
        "type": "confirm",
        "name": "have_api",
        "message": "This project have an API?",
        "default": False,
    },
    {
        "type": "list",
        "message": "Select your database",
        "name": "database",
        "choices": [
            {"name": "SQLite", "value": "sqlite"},
            {"name": "Postgres", "value": "postgres"},
            {"name": "MySQL", "value": "mysql"},
            {
                "name": "MongoDB",
                "value": "mongodb",
                "disabled": "Not yet supported",
            },
            {
                "name": "None (no database)",
                "value": "none",
                "disabled": "Not yet supported",
            },
        ],
        "validate": lambda answer: "You must choose at least one topping."
        if len(answer) == 0
        else True,
    },
]
