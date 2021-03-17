.PHONY:install_editable
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
	@tar -zxvf dist/flask-sketch-*.tar.gz \
		&& mv flask-sketch-*/setup.py setup.py \
		&& rm -rf flask-sketch-*
	pip install -e .[dev] --upgrade --no-cache
	mv _pyproject.toml pyproject.toml

.PHONY:format
format:
	isort **/*.py
	black -l 79 **/*.py

.PHONY:test_project_sketch
test_project_sketch: clean_test_sketch
	flask-sketch test_sketch_project

.PHONY:clean_test_sketch
clean_test_sketch:
	rm -rf test_sketch_project