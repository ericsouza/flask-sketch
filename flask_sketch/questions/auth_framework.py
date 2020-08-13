from flask_sketch.utils import has_answers

auth_framework_questions = [
    {
        "type": "list",
        "message": "Select the Authentication Framework",
        "name": "auth_framework",
        "choices": [
            {
                "name": "Flask-Security-Too (aka Flask-Security)",
                "value": "security_web",
            },
            {
                "name": "Flask-Login",
                "value": "login_web",
                "disabled": "Not supported yet",
            },
            {"name": "Flask-BasicAuth", "value": "basicauth_web"},
            {"name": "None", "value": "none"},
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
            {"name": "Flask-Praetorian (recommended)", "value": "praetorian"},
            {
                "name": "PyJWT",
                "value": "pyjwt",
                "disabled": "Not yet supported",
            },
            {"name": "Flask-BasicAuth", "value": "basicauth_api"},
            {"name": "None", "value": "none"},
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
                "name": "Flask-Security-Too + Flask-JWT-Extended",
                "value": "security_web_api",
            },
            {
                "name": "Flask-Login + PyJWT (for api auth)",
                "value": "login_pyjwt",
            },
            {"name": "Flask-BasicAuth", "value": "basicauth_web_api"},
            {"name": "None", "value": "none"},
        ],
        "when": lambda answers: has_answers(
            answers, have={"application_type": "web_and_api"}
        ),
        "validate": lambda answer: "You must choose at least one topping."
        if len(answer) == 0
        else True,
    },
]
