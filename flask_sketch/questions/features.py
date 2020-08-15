from flask_sketch.utils import has_answers

features_questions = [
    {
        "type": "checkbox",
        "message": "Select the frontend features.",
        "name": "frontend_features",
        "choices": [
            {"name": "Flask-HTMLmin", "disabled": "Not yet supported"},
            {"name": "Flask-Assets", "disabled": "Not yet supported"},
            {"name": "Flask-Talisman", "disabled": "Not yet supported"},
        ],
        "when": lambda answers: "TODO_IN_FUTURE"
        in answers.get("application_type"),
    },
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
            answers,
            have={"application_type": "web_only"},
            not_have={"database": "none"},
        ),
    },
    {
        "type": "checkbox",
        "message": "Select some more features for your project",
        "name": "features",
        "choices": [
            {"name": "Cache (Flask-Caching)"},
            {"name": "Rate Limiting (Flask-Limiter)"},
            {"name": "Flask-DebugToolbar"},
        ],
        "when": lambda answers: has_answers(
            answers, have={"application_type": "web_only", "database": "none"},
        ),
    },
    {
        "type": "checkbox",
        "message": "Select some more features for your project",
        "name": "features",
        "choices": [
            {"name": "Flask-CORS"},
            {"name": "Migrations (Flask-Migrate)"},
            {"name": "Admin Interface (Flask-Admin)"},
            {"name": "Cache (Flask-Caching)"},
            {"name": "Rate Limiting (Flask-Limiter)"},
        ],
        "when": lambda answers: has_answers(
            answers,
            have={"application_type": "api_only"},
            not_have={"database": "none"},
        ),
    },
    {
        "type": "checkbox",
        "message": "Select some more features for your project",
        "name": "features",
        "choices": [
            {"name": "Flask-CORS"},
            {"name": "Cache (Flask-Caching)"},
            {"name": "Rate Limiting (Flask-Limiter)"},
        ],
        "when": lambda answers: has_answers(
            answers, have={"application_type": "api_only", "database": "none"},
        ),
    },
    {
        "type": "checkbox",
        "message": "Select some more features for your project",
        "name": "features",
        "choices": [
            {"name": "Flask-CORS"},
            {"name": "Migrations (Flask-Migrate)"},
            {"name": "Admin Interface (Flask-Admin)"},
            {"name": "Cache (Flask-Caching)"},
            {"name": "Rate Limiting (Flask-Limiter)"},
            {"name": "Flask-DebugToolbar"},
        ],
        "when": lambda answers: has_answers(
            answers,
            have={"application_type": "web_and_api"},
            not_have={"database": "none"},
        ),
    },
    {
        "type": "checkbox",
        "message": "Select some more features for your project",
        "name": "features",
        "choices": [
            {"name": "Flask-CORS"},
            {"name": "Cache (Flask-Caching)"},
            {"name": "Rate Limiting (Flask-Limiter)"},
            {"name": "Flask-DebugToolbar"},
        ],
        "when": lambda answers: has_answers(
            answers,
            have={"application_type": "web_and_api", "database": "none"},
        ),
    },
]
