install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=search_engine --cov-report xml

lint:
	poetry run flake8 search_engine

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

.PHONY: install test lint selfcheck check build
