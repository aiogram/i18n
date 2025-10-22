package_dir := aiogram_i18n
tests_dir := tests
examples_dir := examples
code_dir := $(package_dir) $(tests_dir) $(examples_dir)

.PHONY: lint
lint:
	echo "Running ruff..."
	uv run ruff check --config pyproject.toml --show-fixes --preview $(package_dir) $(tests_dir)
	uv run mypy --strict $(package_dir)

.PHONY: reformat
reformat:
	echo "Running ruff check with --fix..."
	uv run ruff check --config pyproject.toml --fix --unsafe-fixes $(package_dir) $(tests_dir)

	echo "Running ruff..."
	uv run ruff format --config pyproject.toml $(package_dir) $(tests_dir)

	echo "Running isort..."
	uv run isort --settings-file pyproject.toml $(package_dir) $(tests_dir)

.PHONY: outdated
outdated:
	uv tree --outdated --universal --no-cache

.PHONY: sync
sync:
	uv sync --reinstall-package aiogram_i18n --all-extras

.PHONY: pull
pull:
	git pull origin master
	git submodule update --init --recursive

.PHONY: test
test:
	echo "Running tests..."
	uv run pytest -vv --cov=$(package_dir) --cov-report=html --cov-report=term --cov-config=.coveragerc $(tests_dir)

.PHONY: test-ci
test-ci:
	echo "Running ci tests..."
	uv run pytest --cov=$(package_dir) --cov-config .coveragerc --cov-report=xml
