# flask-sketch

A Python CLI for auto-generate folders structure and boilerplate code for Flask Applications.

## Installation

Flask Sketch is available on PyPi. Simply use pip to install Flask Sketch:

```
pip install flask-sketch
```

## Usage

Flask-Sketch have a single command to create a new project

```
python -m flask_sketch myprojectname
```

This will start a CLI which ask some questions about what you want in your new application like database choice, login framework, REST framework and some other features you might want. The name of your project will be `myprojectname` (note: the name of project can only contains letters, numbers and underscore but have to start with a letter)

Some questions depends on past answers you gave (example: if you choose a SQL database you will be asked if you want flask-migrate to help with migrations)

## Demo

A simple demo using Flask Sketch

![Alt Text](docs/assets/sketch-demo.gif)

## Future

For now Flask-Sketch is basic a study project for myself but I want to add support for:

- Authlib (to deal with OAuth2)
- More options to deal with migrations
- Environs lib (another alternative for settings)
- Others features extensions to flask:
    - Flask-Talisman
    - Pytest-Flask
    - Flask-Babel
    - Flask-File-Upload
    - Flask-HTMLmin (to minifier HTML)
    - Flask-Static-Digest
    - Something to help with text search.
    - Something to help with GraphQL
