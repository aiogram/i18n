from pathlib import Path
from typing import Dict, Callable, Tuple, Sequence, Union

import click


@click.group(name="main")
def main() -> None:
    ...


@main.command(help="Generate stubs from .ftl files")  # type: ignore[misc]
@click.option("-i", "--input-files", required=True, multiple=True)
@click.option("-o", "--output-file", required=True)
def stub(input_files: Tuple[str, ...], output_file: str) -> None:
    from aiogram_i18n.utils.fluent_stub import from_files_to_file

    allow_formats: Dict[str, Callable[[Sequence[str], str], None]] = {
        "ftl": from_files_to_file,
        # "mo"
    }

    suffix: str = "ftl"
    for input_file in input_files:
        path = Path(input_file)
        suffix = path.suffix[1:]
        if not suffix:
            raise Exception(f"only files with this extension are allowed ({', '.join(allow_formats.keys())})")
        if suffix not in allow_formats:
            raise Exception(f"unknown file extension {path.suffix}")
        if not path.is_file():
            raise Exception("only files allowed")

    path = Path(output_file)
    if path.suffix != ".pyi":
        raise Exception('output file must have the extension "pyi"')

    allow_formats[suffix](input_files, output_file)


@main.command(help="Extract all used fluent keys from code")  # type: ignore[misc]
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

    input_dirs = tuple(Path(input_dir) for input_dir in input_dirs)
    output_file = Path(output_file)

    exclude_dirs = tuple(Path(exclude_dir) for exclude_dir in exclude_dirs)
    exclude_dirs += (Path("__pycache__"),)

    exclude_keys += tuple(
        key for key, value in I18nContext.__dict__.items() if callable(value)
    )

    fkp = FluentKeyParser(
        input_dirs=input_dirs,
        output_file=output_file,
        i18n_keys=i18n_keys,
        separator=separator,
        locales=locales,
        exclude_dirs=exclude_dirs,
        exclude_keys=exclude_keys,
    )
    fkp.run(create_missing_dirs=create_missing_dirs)


@main.command(
    help="Extract all used fluent keys from code and split them by files")  # type: ignore[misc]
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
def multiple_extract(
        input_paths: Tuple[str, ...],
        output_dir: str,
        i18n_keys: Tuple[str, ...],
        separator: str,
        locales: Union[Tuple[str, ...], None],
        exclude_dirs: Tuple[str, ...],
        exclude_keys: Tuple[str, ...],
        create_missing_dirs: bool,
) -> None:
    """
    Extracts all used fluent keys from code and saves them in the specified files.

    Keys should be separated by <type>-<key_name>.
    Keys will be saved in multiple files, depending on the type.
    The type is specified by the first part of the key.

    Example:
        - "buttons-cancel" -> "buttons" is the type, "cancel" is the key name.
        - "checker-no-rights" -> "checker" is the type, "no-rights" is the key name.
    """
    from aiogram_i18n import I18nContext
    from aiogram_i18n.utils.fluent_extract import FluentMultipleKeyParser

    input_paths = tuple(Path(input_path) for input_path in input_paths)
    output_dir = Path(output_dir)

    exclude_dirs = tuple(Path(exclude_dir) for exclude_dir in exclude_dirs)
    exclude_dirs += (Path("__pycache__"),)

    exclude_keys += tuple(
        key for key, value in I18nContext.__dict__.items() if callable(value)
    )

    fkp = FluentMultipleKeyParser(
        input_paths=input_paths,
        output_dir=output_dir,
        i18n_keys=i18n_keys,
        separator=separator,
        locales=locales,
        exclude_dirs=exclude_dirs,
        exclude_keys=exclude_keys,
    )
    fkp.run(create_missing_dirs=create_missing_dirs)


if __name__ == "__main__":
    main()
