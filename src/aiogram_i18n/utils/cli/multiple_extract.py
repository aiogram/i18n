from pathlib import Path

import click
from click import echo, style

from aiogram_i18n.utils.cli import main


@main.command(help="Extract all used fluent keys from code and split them by files")
@click.option(
    "-i",
    "--input-paths",
    multiple=True,
    required=True,
    type=click.Path(exists=True),
)
@click.option(
    "-o",
    "--output-dir",
    required=True,
    type=click.Path(),
)
@click.option(
    "-k",
    "--i18n-keys",
    default=["i18n", "L"],
    multiple=True,
    show_default=True,
)
@click.option(
    "-s",
    "--separator",
    default="-",
    show_default=True,
)
@click.option(
    "-l",
    "--locales",
    multiple=True,
)
@click.option(
    "-ed",
    "--exclude-dirs",
    default=(Path("venv"), Path(".venv")),
    multiple=True,
    type=click.Path(),
)
@click.option(
    "-ek",
    "--exclude-keys",
    multiple=True,
)
@click.option(
    "-cm",
    "--create-missing-dirs",
    is_flag=True,
    default=False,
)
@click.option(
    "--default-ftl-file",
    default="_default.ftl",
    show_default=True,
)
def multiple_extract(
    input_paths: tuple[str, ...],  # noqa: ARG001
    output_dir: str,  # noqa: ARG001
    i18n_keys: tuple[str, ...],  # noqa: ARG001
    separator: str,  # noqa: ARG001
    locales: tuple[str, ...] | None,  # noqa: ARG001
    exclude_dirs: tuple[str, ...],  # noqa: ARG001
    exclude_keys: tuple[str, ...],  # noqa: ARG001
    create_missing_dirs: bool,  # noqa: ARG001
    default_ftl_file: str,  # noqa: ARG001
) -> None:
    echo(
        style(
            text="This function is removed. Use FTL-Extract instead.\n"
            "pip install ftl-extract\n"
            "\n"
            "ftl extract <code_path> <output_file> [OPTIONS]\n"
            "\n"
            "https://pypi.org/project/FTL-Extract/",
            fg="red",
        ),
        err=True,
        color=True,
    )
