
# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')


setup(
    long_description=readme,
    name='flask-sketch',
    version='0.3.20',
    description='A CLI for autogenerate folder structure and boilerplate for Flask applications',
    python_requires='<4.0,>=3.7',
    project_urls={"repository": "https://github.com/ericsouza/flask-sketch"},
    author='Eric Souza',
    author_email='ericsouza0801@gmail.com',
    license='MIT License',
    keywords='flask-sketch flask_sketch flask boilerplate',
    entry_points={"console_scripts": ["flask-sketch = flask_sketch.__main__:main"]},
    packages=['flask_sketch', 'flask_sketch.handlers', 'flask_sketch.questions', 'flask_sketch.templates', 'flask_sketch.templates.api', 'flask_sketch.templates.api.resources', 'flask_sketch.templates.api.resources.examples', 'flask_sketch.templates.app', 'flask_sketch.templates.commands', 'flask_sketch.templates.config', 'flask_sketch.templates.examples', 'flask_sketch.templates.ext', 'flask_sketch.templates.ext.admin', 'flask_sketch.templates.models', 'flask_sketch.templates.models.examples', 'flask_sketch.templates.site', 'flask_sketch.templates.site.templates', 'flask_sketch.templates.utils', 'flask_sketch.templates.utils.security'],
    package_dir={"": "."},
    package_data={},
    install_requires=['pyfiglet==0.*,>=0.8.0', 'pyinquirer==1.*,>=1.0.3', 'toml==0.*,>=0.10.1'],
    extras_require={"dev": ["black==19.*,>=19.10.0.b0", "flake8==3.*,>=3.8.3", "isort==5.*,>=5.5.2"]},
)
