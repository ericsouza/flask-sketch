from flask_sketch.utils import has_answers
from flask_sketch.const import (
    FLASK_MIGRATE,
    FLASK_ADMIN,
    FLASK_CACHING,
    FLASK_LIMITER,
    FLASK_DEBUGTOOLBAR,
    NONE,
    MONGODB,
)

"""
{
        "type": "checkbox",
        "message": "Select the frontend features.",
        "name": "frontend_features",
        "choices": [
            {"name": "Flask-HTMLmin", "disabled": "Not yet supported"},
            {"name": "Flask-Assets", "disabled": "Not yet supported"},
            {"name": "Flask-Talisman", "disabled": "Not yet supported"},
        ],
    },
"""

features_questions = [
    {
        "type": "checkbox",
        "message": "Select some more features for your project",
        "name": "features",
        "choices": [
            {"name": "Migrations (Flask-Migrate)", "value": FLASK_MIGRATE},
            {"name": "Admin Interface (Flask-Admin)", "value": FLASK_ADMIN},
            {"name": "Cache (Flask-Caching)", "value": FLASK_CACHING},
            {"name": "Rate Limiting (Flask-Limiter)", "value": FLASK_LIMITER},
            {"name": "Flask-DebugToolbar", "value": FLASK_DEBUGTOOLBAR},
        ],
        "when": lambda answers: has_answers(
            answers,
            have={"have_api": False},
            not_have={"database": f"{NONE};{MONGODB}"},
        ),
    },
    {
        "type": "checkbox",
        "message": "Select some more features for your project",
        "name": "features",
        "choices": [
            {"name": "Cache (Flask-Caching)", "value": FLASK_CACHING},
            {"name": "Rate Limiting (Flask-Limiter)", "value": FLASK_LIMITER},
            {"name": "Flask-DebugToolbar", "value": FLASK_DEBUGTOOLBAR},
        ],
        "when": lambda answers: has_answers(
            answers, have={"have_api": False, "database": NONE},
        ),
    },
    {
        "type": "checkbox",
        "message": "Select some more features for your project",
        "name": "features",
        "choices": [
            {"name": "Flask-CORS", "value": "cors"},
            {"name": "Migrations (Flask-Migrate)", "value": FLASK_MIGRATE},
            {"name": "Admin Interface (Flask-Admin)", "value": FLASK_ADMIN},
            {"name": "Cache (Flask-Caching)", "value": FLASK_CACHING},
            {"name": "Rate Limiting (Flask-Limiter)", "value": FLASK_LIMITER},
            {"name": "Flask-DebugToolbar", "value": FLASK_DEBUGTOOLBAR},
        ],
        "when": lambda answers: has_answers(
            answers,
            have={"have_api": True},
            not_have={"database": f"{NONE};{MONGODB}"},
        ),
    },
    {
        "type": "checkbox",
        "message": "Select some more features for your project",
        "name": "features",
        "choices": [
            {
                "name": "Flask-CORS",
                "disabled": "Not supported yet.",
                "value": "cors",
            },
            {"name": "Cache (Flask-Caching)", "value": FLASK_CACHING},
            {"name": "Rate Limiting (Flask-Limiter)", "value": FLASK_LIMITER},
            {"name": "Flask-DebugToolbar", "value": FLASK_DEBUGTOOLBAR},
        ],
        "when": lambda answers: has_answers(
            answers, have={"have_api": True, "database": NONE},
        ),
    },
    {
        "type": "checkbox",
        "message": "Select some more features for your project",
        "name": "features",
        "choices": [
            {"name": "Flask-CORS", "value": "cors"},
            {"name": "Admin Interface (Flask-Admin)", "value": FLASK_ADMIN},
            {"name": "Cache (Flask-Caching)", "value": FLASK_CACHING},
            {"name": "Rate Limiting (Flask-Limiter)", "value": FLASK_LIMITER},
            {"name": "Flask-DebugToolbar", "value": FLASK_DEBUGTOOLBAR},
        ],
        "when": lambda answers: has_answers(
            answers, have={"have_api": True, "database": MONGODB}
        ),
    },
    {
        "type": "checkbox",
        "message": "Select some more features for your project",
        "name": "features",
        "choices": [
            {"name": "Admin Interface (Flask-Admin)", "value": FLASK_ADMIN},
            {"name": "Cache (Flask-Caching)", "value": FLASK_CACHING},
            {"name": "Rate Limiting (Flask-Limiter)", "value": FLASK_LIMITER},
            {"name": "Flask-DebugToolbar", "value": FLASK_DEBUGTOOLBAR},
        ],
        "when": lambda answers: has_answers(
            answers, have={"have_api": False, "database": MONGODB}
        ),
    },
]
