from flask_sketch.utils import has_answers

auth_framework_questions = [
    {
        "type": "list",
        "message": "Select the Authentication Framework",
        "name": "auth_framework",
        "choices": [
            {
                "name": "Flask-Security-Too (aka Flask-Security)",
                "value": "security",
            },
            {"name": "Flask-Login", "value": "login"},
            {
                "name": "Flask-BasicAuth",
                "value": "basicauth",
                "disabled": "Not supported yet",
            },
            {"name": "None", "value": "none", "disabled": "Not supported yet"},
        ],
        "validate": lambda answer: "You must choose at least one topping."
        if len(answer) == 0
        else True,
    },
    {
        "type": "list",
        "message": "Select the Authentication Framework",
        "name": "api_auth_framework",
        "choices": [
            {"name": "Flask-JWT-Extended", "value": "jwt_extended"},
            {
                "name": "Flask-BasicAuth",
                "value": "basicauth",
                "disabled": "Not yet supported",
            },
            {
                "name": "Flask-Praetorian",
                "value": "praetorian",
                "disabled": "Not yet supported",
            },
            {"name": "None", "value": "none"},
        ],
        "when": lambda answers: has_answers(answers, have={"have_api": True}),
        "validate": lambda answer: "You must choose at least one topping."
        if len(answer) == 0
        else True,
    },
]
