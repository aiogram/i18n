
from pathlib import Path
from typing import List, Dict, Callable, Tuple

import click


@click.group()
def main() -> None:
    ...


@main.command(help="Generate stubs from .ftl files")
@click.option("-i", "--input-files", required=True, multiple=True)
@click.option("-o", "--output-file", required=True)
def stub(input_files: Tuple[str], output_file: str) -> None:
    from aiogram_i18n.utils.fluent_stub import from_files_to_file

    allow_formats: Dict[str, Callable[[List[str], str], None]] = {
        "ftl": from_files_to_file,
        # "mo"
    }

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

    allow_formats[suffix](input_files, output_file) # noqa


@main.command(help="Extract all used fluent keys from code")
@click.option("-i", "--input-dirs", required=True, multiple=True)
@click.option("-o", "--output-file", required=True)
@click.option("-k", "--i18n-keys", default=["i18n"], multiple=True, show_default=True)
@click.option("-s", "--separator", default="-", show_default=True)
@click.option("-ed", "--exclude-dirs", multiple=True)
@click.option("-ek", "--exclude-keys", multiple=True)
def extract(
    input_dirs: Tuple[str], output_file: str,
    i18n_keys: Tuple[str], separator: str,
    exclude_dirs: Tuple[str], exclude_keys: Tuple[str]
) -> None:
    from aiogram_i18n.utils.fluent_extract import FluentKeyParser

    fkp = FluentKeyParser(
        input_dirs=input_dirs,
        output_file=output_file,
        i18n_keys=i18n_keys,
        separator=separator,
        exclude_dirs=exclude_dirs + ("venv", "__pycache__"),
        exclude_keys=exclude_keys
    )
    fkp.run()


if __name__ == '__main__':
    main()
