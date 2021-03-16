install_editable:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build
	poetry build
	mv pyproject.toml _pyproject.toml
	tar --wildcards -zxvf dist/flask-sketch-*.tar.gz flask-sketch-*/setup.py \
		&& mv flask-sketch-*/setup.py setup.py \
		&& rm -rf flask-sketch-*
	pip install -e .[dev] --upgrade --no-cache
	mv _pyproject.toml pyproject.toml

format:
	isort **/*.py
	black -l 79 **/*.py

test_project_sketch:
	flask-sketch test_sketch_project

clear_test_sketch:
	rm -rf test_sketch_project