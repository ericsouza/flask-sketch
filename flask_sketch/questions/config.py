from flask_sketch.const import DYNACONF, NONE

config_questions = [
    {
        "type": "list",
        "message": "Select your Configuration Framework",
        "name": "config_framework",
        "choices": [
            {"name": "Dynaconf", "value": DYNACONF},
            {"name": "None: Use Settings File", "value": NONE},
        ],
        "validate": lambda answer: "You must choose at least one topping."
        if len(answer) == 0
        else True,
    },
]
