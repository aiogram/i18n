from pathlib import Path
from typing import Tuple, Union

import click

from .base import main


@main.command(help="Extract all used fluent keys from code")
@click.option(
    "-i",
    "--input-dirs",
    multiple=True,
    required=True,
    type=click.Path(exists=True),
)
@click.option(
    "-o",
    "--output-file",
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
def extract(
    input_dirs: Tuple[str, ...],
    output_file: str,
    i18n_keys: Tuple[str, ...],
    separator: str,
    locales: Union[Tuple[str, ...], None],
    exclude_dirs: Tuple[str, ...],
    exclude_keys: Tuple[str, ...],
    create_missing_dirs: bool,
) -> None:
    from aiogram_i18n import I18nContext
    from aiogram_i18n.utils.fluent_extract import FluentKeyParser

    input_dirs_ = tuple(Path(input_dir) for input_dir in input_dirs)
    output_file_ = Path(output_file)

    exclude_dirs_ = (Path("__pycache__"), *(Path(exclude_dir) for exclude_dir in exclude_dirs))
    exclude_keys += tuple(key for key, value in I18nContext.__dict__.items() if callable(value))

    fkp = FluentKeyParser(
        input_dirs=input_dirs_,
        output_file=output_file_,
        i18n_keys=i18n_keys,
        separator=separator,
        locales=locales,
        exclude_dirs=exclude_dirs_,
        exclude_keys=exclude_keys,
    )
    fkp.run(create_missing_dirs=create_missing_dirs)
