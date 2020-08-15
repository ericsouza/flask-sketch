#!/usr/bin/python3
# from pprint import pprint
import argparse

from pyfiglet import Figlet
from PyInquirer import prompt

from flask_sketch.config import cli_style
from flask_sketch.make import create_project
from flask_sketch.questions import get_questions

parser = argparse.ArgumentParser(description="Flask Sketch CLI")
parser.add_argument("project_name", type=str)
parser.add_argument(
    "-e", action="store_true", help="Create examples endpoints"
)
parser.add_argument(
    "-p",
    action="store_true",
    help="Create a pyproject.toml to work with poetry",
)
parser.add_argument(
    "-v",
    action="store_true",
    help="Create a virtualenv and install requirements",
)

f = Figlet(font="slant")


def flask_sketch(args):
    print(f.renderText("Flask Sketch"))

    answers = prompt(get_questions(), style=cli_style)
    if answers:
        # pprint(answers)
        create_project(args, answers)


if __name__ == "__main__":
    args = parser.parse_args()
    args.project_name = args.project_name.lower()
    flask_sketch(args)
