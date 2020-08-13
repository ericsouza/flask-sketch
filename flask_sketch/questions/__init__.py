from flask_sketch.questions.commom import commom_questions
from flask_sketch.questions.api_framework import api_framework_questions
from flask_sketch.questions.auth_framework import auth_framework_questions
from flask_sketch.questions.config import config_questions
from flask_sketch.questions.features import features_questions

questions = []

questions.extend(commom_questions)
questions.extend(api_framework_questions)
questions.extend(auth_framework_questions)
questions.extend(config_questions)
questions.extend(features_questions)


def get_questions():
    return questions
