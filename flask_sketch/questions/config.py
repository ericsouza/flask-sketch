config_questions = [
    {
        "type": "list",
        "message": "Select your Configuration Framework",
        "name": "config_framework",
        "choices": [
            {"name": "Dynaconf", "value": "dynaconf"},
            {"name": "None: Use Settings File", "value": "none"},
            {
                "name": "Environs",
                "value": "environs",
                "disabled": "Not yet supported",
            },
        ],
        "validate": lambda answer: "You must choose at least one topping."
        if len(answer) == 0
        else True,
    },
]
