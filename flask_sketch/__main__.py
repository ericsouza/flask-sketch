#!/usr/bin/python3
# from pprint import pprint
import argparse
import shutil
from pyfiglet import Figlet
from PyInquirer import prompt

from flask_sketch.config import cli_style_2
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

    answers = prompt(get_questions(), style=cli_style_2)
    if answers:
        create_project(args, answers)


if __name__ == "__main__":

    args = parser.parse_args()
    args.project_name = args.project_name.lower()
    try:
        flask_sketch(args)
    except Exception as e:
        print("\n\nAn error occurred during generating files:")
        print(e)
        shutil.rmtree(args.project_name)
