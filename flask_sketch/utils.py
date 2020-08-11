from typing import Callable


def has_answers(answers, have: dict, not_have: dict = {}):

    for da in have:
        if not answers.get(da).lower() == have.get(da).lower():
            return False

    for nda in not_have:
        if answers.get(nda).lower() == not_have.get(nda).lower():
            return False

    return True


class Answers:
    def __init__(self, answers):
        self.application_type: str = answers["application_type"]
        self.database: str = answers["database"]
        self.auth_framework: str = answers["auth_framework"]
        self.api_framework: str = answers["api_framework"]
        self.config_framework: str = answers["config_framework"]
        self.features: list = answers["features"]


class GenericHandler:
    def __init__(self, *handlers: Callable):
        self.handlers = handlers

    def __call__(self, answers: Answers):
        for handler in self.handlers:
            if r := handler(answers):
                return r
