.venv:
	python -m venv .venv

install: .venv
	pip install --upgrade pip
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

lint:
	black --target-version=py38 --check .
	flake8 --exclude .venv,dependencies

format:
	black --target-version=py38 .

test:
	coverage run --source=src --omit=dependencies -m unittest

coverage: test .coverage
	coverage report -m --fail-under=90

run:
	export FLASK_APP=src.handler && flask run --debugger --reload
