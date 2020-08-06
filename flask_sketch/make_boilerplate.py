import os


def make(project_name, answers):
    # project_app_folder = project_name + "/" + project_name
    # os.makedirs(project_name + "/" + "tests")
    # os.makedirs(project_app_folder)
    # os.makedirs(project_app_folder + "/" + "ext")

    init_app = """from flask import Flask

app = Flask()

@app.route("/")
def hello():
    return "hello world"

if __name__ == "__main__":
    app.run()"""

    # with open(project_app_folder + "/__init__.py", "w") as file:
    #    file.writelines(init_app)

    # with open(project_name + "/requirements.txt", "w") as file:
    #    file.writelines("Flask")
