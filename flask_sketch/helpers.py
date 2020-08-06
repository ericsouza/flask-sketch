def has_answers(answers, have: dict, not_have: dict = {}):

    for da in have:
        if not answers.get(da).lower() == have.get(da).lower():
            return False

    for nda in not_have:
        if answers.get(nda).lower() == not_have.get(nda).lower():
            return False

    return True
