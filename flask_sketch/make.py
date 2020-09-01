import os
import pathlib
from argparse import Namespace

from flask_sketch.handlers import (
    api_framework_handler,
    app_type_handler,
    auth_handler,
    api_auth_handler,
    config_handler,
    database_handler,
    handle_features,
)
from flask_sketch.utils import (
    Sketch,
    cleanup,
    make_commom,
    make_requirements,
    make_app,
    make_template_args,
    random_string,
    pjoin,
)


def create_project(args: Namespace, answers: dict):
    pf = pjoin(str(pathlib.Path().absolute()), args.project_name)
    apf = pjoin(
        str(pathlib.Path().absolute()),
        args.project_name,
        args.project_name.replace("-", "_"),
    )

    sketch = Sketch(pf, apf, answers, args)

    make_commom(sketch)

    sketch.settings["default"]["DEBUG"] = False
    sketch.settings["development"]["DEBUG"] = True
    sketch.settings["default"]["SECRET_KEY"] = random_string(length=32)

    app_type_handler(sketch)
    database_handler(sketch)
    auth_handler(sketch)
    if sketch.have_api:
        api_framework_handler(sketch)
        api_auth_handler(sketch)

    handle_features(sketch)
    config_handler(sketch)

    # if args.e:
    sketch.blueprints.extend(["examples"])
    make_app(sketch)
    make_requirements(sketch)

    make_template_args(sketch)

    cleanup(sketch)

    if args.v:
        print("\ncreating virtual environment...")
        os.system(f"python -m venv {pf}/.venv")

    print("\n\nAll done!")
