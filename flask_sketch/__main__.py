#!/usr/bin/python3

# from __future__ import print_function, unicode_literals
import sys
from pprint import pprint

from config import cli_style
from make import create_project
from pyfiglet import Figlet
from PyInquirer import prompt
from questions import questions

f = Figlet(font="slant")


def flask_sketch(project_name):
    print(f.renderText("Flask Sketch"))

    if answers := prompt(questions, style=cli_style):
        pprint(answers)
        create_project(project_name, answers)


if __name__ == "__main__":
    flask_sketch(sys.argv[1])
