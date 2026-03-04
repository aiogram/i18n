set shell := ["bash", "-c"]
set windows-shell := ["pwsh.exe", "-NoLogo", "-Command"]

src_dir := "src"
tests_dir := "tests"
examples_dir := "examples"

lint:
    echo "Running ruff..."
    uv run ruff check --config pyproject.toml --show-fixes --preview {{src_dir}} {{tests_dir}}
    uv run mypy --config-file pyproject.toml

reformat:
    echo "Running ruff check with --fix..."
    uv run ruff check --config pyproject.toml --fix --unsafe-fixes {{src_dir}} {{tests_dir}}

    echo "Running ruff..."
    uv run ruff format --config pyproject.toml {{src_dir}} {{tests_dir}}

    echo "Running isort..."
    uv run isort --settings-file pyproject.toml {{src_dir}} {{tests_dir}}

outdated:
    uv tree --outdated --universal --no-cache --depth 1

sync:
    uv sync --reinstall-package aiogram_i18n --all-extras

pull:
    git pull origin master
    git submodule update --init --recursive

test:
    echo "Running tests..."
    uv run pytest -vv --cov={{src_dir}} --cov-report=html --cov-report=term --cov-config=.coveragerc {{tests_dir}}

test-ci:
    echo "Running ci tests..."
    uv run pytest --cov={{src_dir}} --cov-config .coveragerc --cov-report=xml
