import click
from flask.cli import with_appcontext
from application.models import User
from application.ext.database import db
from application.ext.auth import guard


@click.command(name="create_database")
@with_appcontext
def create_database():
    db.create_all()


@click.command(name="create_users")
@with_appcontext
def create_users():
    db.create_all()
    db.session.add(
        User(username='TheDude', password=guard.hash_password('abides'),)
    )
    db.session.add(
        User(
            username='Walter',
            password=guard.hash_password('calmerthanyouare'),
            roles='admin',
        )
    )
    db.session.add(
        User(
            username='Donnie',
            password=guard.hash_password('iamthewalrus'),
            roles='operator',
        )
    )
    db.session.add(
        User(
            username='Maude',
            password=guard.hash_password('andthorough'),
            roles='operator,admin',
        )
    )
    db.session.commit()


def register_commands(app):
    app.cli.add_command(create_database)
    app.cli.add_command(create_users)
