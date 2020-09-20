from flask_sketch.utils import has_answers
from flask_sketch.const import FLASK_RESTX, FLASK_SMOREST, FLASK_RESTFUL, NONE

api_framework_questions = [
    {
        "type": "list",
        "message": "Select your API Framework",
        "name": "api_framework",
        "choices": [
            {"name": "Flask-Restx (aka Flask-Restplus)", "value": FLASK_RESTX},
            {"name": "Flask-Smorest", "value": FLASK_SMOREST},
            {
                "name": "Flask-RESTful",
                "value": FLASK_RESTFUL,
                "disabled": "Not yet supported",
            },
            {"name": "None", "value": NONE},
        ],
        "when": lambda answers: has_answers(answers, have={"have_api": True}),
        "validate": lambda answer: "You must choose at least one topping."
        if len(answer) == 0
        else True,
    }
]
