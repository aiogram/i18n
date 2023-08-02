
from pathlib import Path
from typing import Callable, Dict, Sequence, Tuple

import click

from .base import main


@main.command(help="Generate stubs from .ftl files")
@click.option("-i", "--input-files", required=True, multiple=True)
@click.option("-o", "--output-file", required=True)
def stub(input_files: Tuple[str, ...], output_file: str) -> None:
    from aiogram_i18n.utils.fluent_stub import from_files_to_file_ex

    allow_formats: Dict[str, Callable[[Sequence[str], str], None]] = {
        "ftl": from_files_to_file_ex,
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
