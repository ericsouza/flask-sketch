from flask_sketch.const import SQLITE, POSTGRES, MYSQL, MONGODB


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
            {"name": "SQLite", "value": SQLITE},
            {"name": "Postgres", "value": POSTGRES},
            {"name": "MySQL", "value": MYSQL},
            {"name": "MongoDB", "value": MONGODB},
            # {
            #     "name": "None (no database)",
            #     "value": NONE,
            #     "disabled": "Not yet supported",
            # },
        ],
        "validate": lambda answer: "You must choose at least one topping."
        if len(answer) == 0
        else True,
    },
]
