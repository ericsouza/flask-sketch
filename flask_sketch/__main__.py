#!/usr/bin/python3

# from __future__ import print_function, unicode_literals
from PyInquirer import prompt
from pprint import pprint
import sys
from pyfiglet import Figlet
from config import cli_style
from questions import questions
from make import create_project

f = Figlet(font="slant")


def flask_sketch(project_name):
    print(f.renderText("Flask Sketch"))

    if answers := prompt(questions, style=cli_style):
        pprint(answers)
        create_project(project_name, answers)


if __name__ == "__main__":
    flask_sketch(sys.argv[1])
