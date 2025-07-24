src_dir := src
package_dir := aiogram_i18n
tests_dir := tests
examples_dir := examples

.PHONY: lint
lint:
	echo "Running ruff..."
	uv run ruff check --config pyproject.toml --diff

	echo "Running MyPy..."
	uv run mypy --config-file pyproject.toml

.PHONY: format
format:
	echo "Running ruff check with --fix..."
	uv run ruff check --config pyproject.toml --fix --unsafe-fixes

	echo "Running ruff..."
	uv run ruff format --config pyproject.toml

	echo "Running isort..."
	uv run isort --settings-file pyproject.toml $(src_dir)/$(package_dir)

.PHONY: outdated
outdated:
	uv tree --outdated --universal

.PHONY: sync
sync:
	uv sync \
		--extra dev \
		--extra test \
		--extra compiler \
		--extra runtime \
		--extra jinja2 \
		--extra docs

.PHONY: test
test:
	echo "Running tests..."
	uv run pytest -vv --cov=$(package_dir) --cov-report=html --cov-report=term --cov-config=.coveragerc $(tests_dir)

.PHONY: test-ci
test-ci:
	echo "Running ci tests..."
	uv run pytest --cov=$(package_dir) --cov-config .coveragerc --cov-report=xml
