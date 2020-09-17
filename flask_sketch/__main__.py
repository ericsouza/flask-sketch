#!/usr/bin/python3
# from pprint import pprint
import argparse
import shutil
import traceback
from pyfiglet import Figlet
from PyInquirer import prompt

from flask_sketch.config import cli_style_2
from flask_sketch.make import create_project
from flask_sketch.questions import get_questions

parser = argparse.ArgumentParser(description="Flask Sketch CLI")
parser.add_argument("project_name", type=str)
parser.add_argument("-e", action="store_true", help="Create examples endpoints")
parser.add_argument(
    "-p", action="store_true", help="Create a pyproject.toml to work with poetry",
)
parser.add_argument(
    "-v", action="store_true", help="Create a virtualenv.",
)

f = Figlet(font="slant")


def main(args):
    print(f.renderText("Flask Sketch"))

    answers = prompt(get_questions(), style=cli_style_2)
    if answers:
        create_project(args, answers)


def flask_sketch():
    args = parser.parse_args()
    args.project_name = args.project_name.lower()
    try:
        main(args)
    except FileExistsError as e:
        print("\n\nAn error occurred during generating files:")
        print(e)
        tb = traceback.format_exc()
    except Exception as e:
        print("\n\nAn error occurred during generating files:")
        print(e)
        shutil.rmtree(args.project_name)
        tb = traceback.format_exc()
    else:
        tb = None
    finally:
        if tb:
            print("\n\n", tb)


if __name__ == "__main__":
    flask_sketch()
