from datetime import datetime
from sqlalchemy import create_engine
from pyctuator.pyctuator import Pyctuator
from pyctuator.health.db_health_provider import DbHealthProvider


def init_app(app):

    engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])

    pyact = Pyctuator(
        app,
        "myappname",
        app_url="http://127.0.0.1:5000",
        pyctuator_endpoint_url="http://127.0.0.1:5000/pyctuator",
        registration_url="http://localhost:8080/instances",
    )

    pyact.set_build_info(
        name="myappname",
        version="0.1.0",
        time=datetime.fromisoformat("2019-12-21T10:09:54.876091"),
    )

    pyact.register_health_provider(DbHealthProvider(engine))
