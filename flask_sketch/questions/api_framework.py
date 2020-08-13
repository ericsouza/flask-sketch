from flask_sketch.utils import has_answers

api_framework_questions = [
    {
        "type": "list",
        "message": "Select your API Framework",
        "name": "api_framework",
        "choices": [
            {"name": "Flask-Restx (aka Flask-Restplus)", "value": "restx"},
            {"name": "Flask-Restless", "value": "restless"},
            {
                "name": "Flask-RESTful",
                "value": "restful",
                "disabled": "Not yet supported",
            },
            {"name": "None", "value": "none"},
        ],
        "when": lambda answers: has_answers(
            answers,
            not_have={
                "application_type": "web_only",
                "database": "mongodb;none",
            },
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
            {"name": "Flask-Restx (aka Flask-Restplus)", "value": "restx"},
            {
                "name": "Flask-RESTful",
                "value": "restful",
                "disabled": "Not yet supported",
            },
            {"name": "None", "value": "none"},
        ],
        "when": lambda answers: has_answers(
            answers,
            have={"database": "none"},
            not_have={"application_type": "web_only"},
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
            {"name": "Flask-Restx (aka Flask-Restplus)", "value": "restx"},
            {
                "name": "Flask-RESTful",
                "value": "restful",
                "disabled": "Not yet supported",
            },
            {"name": "None", "value": "none"},
        ],
        "when": lambda answers: has_answers(
            answers,
            have={"database": "mongodb"},
            not_have={"application_type": "web_only"},
        ),
        "validate": lambda answer: "You must choose at least one topping."
        if len(answer) == 0
        else True,
    },
]
