.venv:
	python -m venv .venv

install: .venv
	pip install --upgrade pip
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

lint:
	black --line-length=100 --target-version=py38 --check .
	flake8 --max-line-length=100 --exclude .venv,dependencies

format:
	black --line-length=100 --target-version=py38 .

test:
	coverage run --source=src --omit=dependencies -m unittest

coverage: test .coverage
	coverage report -m --fail-under=90
