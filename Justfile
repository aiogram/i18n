set shell := ["bash", "-c"]
set windows-shell := ["pwsh.exe", "-NoLogo", "-Command"]

src_dir := "src"
tests_dir := "tests"
examples_dir := "examples"

lint:
    echo "Running ruff..."
    uv run ruff format --check --diff {{src_dir}} {{tests_dir}}
    uv run ruff check --show-fixes --preview {{src_dir}} {{tests_dir}}
    uv run mypy --native-parser --num-workers 8 {{src_dir}}

reformat:
    echo "Running ruff check with --fix..."
    uv run ruff check --fix --unsafe-fixes {{src_dir}} {{tests_dir}}

    echo "Running ruff..."
    uv run ruff format {{src_dir}} {{tests_dir}}

    echo "Running isort..."
    uv run isort {{src_dir}} {{tests_dir}}

outdated:
    uv tree --outdated --universal --no-cache --depth 1

sync:
    uv sync --reinstall-package aiogram_i18n --all-extras

test:
    echo "Running tests..."
    uv run pytest -vv --cov={{src_dir}} --cov-report=html --cov-report=term --cov-config=.coveragerc {{tests_dir}}

test-ci:
    echo "Running ci tests..."
    uv run pytest --cov={{src_dir}} --cov-config .coveragerc --cov-report=xml
