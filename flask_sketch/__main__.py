#!/usr/bin/python3

import click
import os


@click.command()
@click.argument("project_name")
def flask_sketch(project_name):
    project_app_folder = project_name + "/" + project_name
    os.makedirs(project_name + "/" + "tests")
    os.makedirs(project_app_folder)
    os.makedirs(project_app_folder + "/" + "ext")

    init_app = """from flask import Flask

app = Flask()

@app.route("/")
def hello():
    return "hello world"

if __name__ == "__main__":
    app.run()"""

    with open(project_app_folder + "/__init__.py", "w") as file:
        file.writelines(init_app)

    with open(project_name + "/requirements.txt", "w") as file:
        file.writelines("Flask")


    print(f"All done! cd into {project_name} folder, create a virtualenv and run pip install -r requirements.txt")
if __name__ == "__main__":
    flask_sketch()