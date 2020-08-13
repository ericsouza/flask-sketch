from typing import Callable


def has_answers(answers: dict, have: dict = {}, not_have: dict = {}):

    for da in have:
        if not answers.get(da).lower() in have.get(da).lower().split(";"):
            return False

    for nda in not_have:
        if answers.get(nda).lower() in not_have.get(nda).lower().split(";"):
            return False

    return True


class Answers:
    def __init__(self, answers: dict):
        self.application_type: str = answers.get("application_type")
        self.database: str = answers.get("database")
        self.auth_framework: str = answers.get("auth_framework")
        self.api_framework: str = answers.get("api_framework")
        self.config_framework: str = answers.get("config_framework")
        self.features: list = answers.get("features")


class GenericHandler:
    def __init__(self, *handlers: Callable):
        self.handlers = handlers

    def __call__(self, answers: Answers):
        for handler in self.handlers:
            if r := handler(answers):
                return r
