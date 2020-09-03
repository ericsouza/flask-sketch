from flask_sketch.utils import has_answers

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
            {"name": "Migrations (Flask-Migrate)", "value": "migrate"},
            {"name": "Admin Interface (Flask-Admin)", "value": "admin"},
            {"name": "Cache (Flask-Caching)", "value": "caching"},
            {"name": "Rate Limiting (Flask-Limiter)", "value": "limiter"},
            {"name": "Flask-DebugToolbar", "value": "debugtoolbar"},
        ],
        "when": lambda answers: has_answers(
            answers, have={"have_api": False}, not_have={"database": "none"},
        ),
    },
    {
        "type": "checkbox",
        "message": "Select some more features for your project",
        "name": "features",
        "choices": [
            {"name": "Cache (Flask-Caching)", "value": "caching"},
            {"name": "Rate Limiting (Flask-Limiter)", "value": "limiter"},
            {"name": "Flask-DebugToolbar", "value": "debugtoolbar"},
        ],
        "when": lambda answers: has_answers(
            answers, have={"have_api": False, "database": "none"},
        ),
    },
    {
        "type": "checkbox",
        "message": "Select some more features for your project",
        "name": "features",
        "choices": [
            {"name": "Flask-CORS", "value": "cors"},
            {"name": "Migrations (Flask-Migrate)", "value": "migrate"},
            {"name": "Admin Interface (Flask-Admin)", "value": "admin"},
            {"name": "Cache (Flask-Caching)", "value": "caching"},
            {"name": "Rate Limiting (Flask-Limiter)", "value": "limiter"},
            {"name": "Flask-DebugToolbar", "value": "debugtoolbar"},
        ],
        "when": lambda answers: has_answers(
            answers, have={"have_api": True}, not_have={"database": "none"},
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
            {"name": "Cache (Flask-Caching)", "value": "caching"},
            {"name": "Rate Limiting (Flask-Limiter)", "value": "limiter"},
            {"name": "Flask-DebugToolbar", "value": "debugtoolbar"},
        ],
        "when": lambda answers: has_answers(
            answers, have={"have_api": True, "database": "none"},
        ),
    },
]
