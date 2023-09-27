from pathlib import Path
from typing import Tuple, Union

import click

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
    """
    Extracts all used fluent keys from code and saves them in the specified paths.

    Key has 2 parts separated by "--".
    First part is the KeyPath, second part is the KeyName.

    KeyPath is separated by `separator` argument. If KeyPath has more than 1 part,
    it will take all parts (except the last one) as directories and the last one as file name.
    If KeyPath has only 1 part, it will be used as file name.
    If KeyPath is not specified, the `default_ftl_file` will be used.

    Example:
        - "cmds-start--greeting" -> will be saved in `cmds/start.ftl`
        file with key "cmds-start--greeting".
        - "cmds--greeting" -> will be saved in `cmds.ftl` file with key "cmds--greeting".
        - "greeting" -> will be saved in `_default.ftl` file with key "greeting".
    """
    from aiogram_i18n import I18nContext
    from aiogram_i18n.utils.fluent_extract import FluentMultipleKeyParser

    input_paths_ = tuple(Path(input_path) for input_path in input_paths)
    output_dir_ = Path(output_dir)

    exclude_dirs_ = (Path("__pycache__"), *[Path(exclude_dir) for exclude_dir in exclude_dirs])
    exclude_keys += tuple(key for key, value in I18nContext.__dict__.items() if callable(value))

    fkp = FluentMultipleKeyParser(
        input_paths=input_paths_,
        output_dir=output_dir_,
        i18n_keys=i18n_keys,
        separator=separator,
        locales=locales,
        exclude_dirs=exclude_dirs_,
        exclude_keys=exclude_keys,
        default_ftl_file=default_ftl_file,
    )
    fkp.run(create_missing_dirs=create_missing_dirs)
