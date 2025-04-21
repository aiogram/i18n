from pathlib import Path
from typing import Tuple, Union

import click
from click import echo, style

from .base import main


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
    input_paths: Tuple[str, ...],
    output_dir: str,
    i18n_keys: Tuple[str, ...],
    separator: str,
    locales: Union[Tuple[str, ...], None],
    exclude_dirs: Tuple[str, ...],
    exclude_keys: Tuple[str, ...],
    create_missing_dirs: bool,
    default_ftl_file: str,
) -> None:
    echo(
        style(
            text="This function is removed. Use FTL-Extract instead.\n"
            "pip install ftl-extract\n"
            "https://pypi.org/project/FTL-Extract/",
            fg="red",
        ),
        err=True,
        color=True,
    )
