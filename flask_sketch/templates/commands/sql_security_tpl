import click
from flask.cli import with_appcontext
from application_tpl.ext.database import db
from application_tpl.ext.auth import user_datastore
from flask_security.utils import hash_password


@click.command(name="create_db")
@with_appcontext
def create_database():
    db.create_all()


@click.command(name="create_users")
@with_appcontext
def create_users():

    user_datastore.create_role(name="admin")
    user_datastore.create_role(name="editor")

    user_datastore.create_user(
        email="admin@email.com",
        password=hash_password("password"),
        roles=["admin"],
    )
    user_datastore.create_user(
        email="editor@email.com",
        password=hash_password("12345678"),
        roles=["editor"],
    )
    user_datastore.create_user(
        email="user@email.com", password=hash_password("12345678")
    )

    db.session.commit()


def register_commands(app):
    app.cli.add_command(create_database)
    app.cli.add_command(create_users)
