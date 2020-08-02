def is_selected(answers, question, check_selected):
    return answers.get(question).lower() == check_selected.lower()
