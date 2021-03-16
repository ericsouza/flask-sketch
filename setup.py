# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flask_sketch',
 'flask_sketch.handlers',
 'flask_sketch.questions',
 'flask_sketch.templates',
 'flask_sketch.templates.api',
 'flask_sketch.templates.api.resources',
 'flask_sketch.templates.api.resources.examples',
 'flask_sketch.templates.app',
 'flask_sketch.templates.commands',
 'flask_sketch.templates.config',
 'flask_sketch.templates.examples',
 'flask_sketch.templates.ext',
 'flask_sketch.templates.ext.admin',
 'flask_sketch.templates.models',
 'flask_sketch.templates.models.examples',
 'flask_sketch.templates.site',
 'flask_sketch.templates.site.templates',
 'flask_sketch.templates.utils',
 'flask_sketch.templates.utils.security']

package_data = \
{'': ['*']}

install_requires = \
['pyfiglet>=0.8.post1,<0.9', 'pyinquirer>=1.0.3,<2.0.0', 'toml>=0.10.1,<0.11.0']

entry_points = \
{'console_scripts': ['flask-sketch = flask_sketch.__main__:main']}

setup_kwargs = {
    'name': 'flask-sketch',
    'version': '0.3.28',
    'description': 'A CLI for autogenerate folder structure and boilerplate for Flask applications',
    'long_description': '# flask-sketch\n\nA Python CLI for auto-generate folders structure and boilerplate code for Flask Applications.\n\n## Installation\n\nFlask Sketch is available on PyPi. Simply use pip to install Flask Sketch:\n\n```\npip install flask-sketch\n```\n\n## Usage\n\nFlask-Sketch have a single command to create a new project\n\n```\npython -m flask_sketch myprojectname\n```\n\nThis will start a CLI which ask some questions about what you want in your new application like database choice, login framework, REST framework and some other features you might want. The name of your project will be `myprojectname` (note: the name of project can only contains letters, numbers and underscore but have to start with a letter)\n\nSome questions depends on past answers you gave (example: if you choose a SQL database you will be asked if you want flask-migrate to help with migrations)\n\n## Demo\n\nA simple demo using Flask Sketch\n\n![Alt Text](docs/assets/sketch-demo.gif)\n\n## Future\n\nFor now Flask-Sketch is basic a study project for myself but I want to add support for:\n\n- Authlib (to deal with OAuth2)\n- More options to deal with migrations\n- Environs lib (another alternative for settings)\n- Others features extensions to flask:\n    - Flask-Talisman\n    - Pytest-Flask\n    - Flask-Babel\n    - Flask-File-Upload\n    - Flask-HTMLmin (to minifier HTML)\n    - Flask-Static-Digest\n    - Something to help with text search.\n    - Something to help with GraphQL\n',
    'author': 'Eric Souza',
    'author_email': 'ericsouza0801@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ericsouza/flask-sketch',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
