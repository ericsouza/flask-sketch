from flask_sketch.utils import has_answers

api_framework_questions = [
    {
        "type": "list",
        "message": "Select your API Framework",
        "name": "api_framework",
        "choices": [
            {"name": "Flask-Restx (aka Flask-Restplus)", "value": "restx"},
            {"name": "Flask-Smorest", "value": "smorest"},
            {
                "name": "Flask-RESTful",
                "value": "restful",
                "disabled": "Not yet supported",
            },
            {"name": "None", "value": "none"},
        ],
        "when": lambda answers: has_answers(answers, have={"have_api": True}),
        "validate": lambda answer: "You must choose at least one topping."
        if len(answer) == 0
        else True,
    }
]
