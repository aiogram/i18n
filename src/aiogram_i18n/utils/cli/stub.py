from collections.abc import Callable, Sequence
from pathlib import Path

import click

from aiogram_i18n.utils.cli import main

STUB_GENERATOR = Callable[[Sequence[str], str], None]


def lazy_import(name: str, func: str) -> STUB_GENERATOR:
    def generator_run(files: Sequence[str], to_file: str) -> None:
        getattr(__import__(name=name, fromlist=[func]), func)(files, to_file)

    return generator_run


@main.command(help="Generate stubs from .mo/.po/.pot files")
@click.option("-i", "--input-files", required=True, multiple=True)
@click.option("-o", "--output-file", required=True)
def stub(input_files: tuple[str, ...], output_file: str) -> None:
    allow_formats: dict[str, Callable[[Sequence[str], str], None]] = {
        "mo": lazy_import("aiogram_i18n.utils.gnutext_stub", "from_mo_files_to_file_ex"),
        "po": lazy_import("aiogram_i18n.utils.gnutext_stub", "from_po_files_to_file_ex"),
        "pot": lazy_import("aiogram_i18n.utils.gnutext_stub", "from_po_files_to_file_ex"),
    }

    suffixes: set[str] = set()
    for input_file in input_files:
        path = Path(input_file)
        suffix = path.suffix[1:]
        if not suffix:
            msg = f"only files with this extension are allowed ({', '.join(allow_formats.keys())})"
            raise click.ClickException(msg)
        if suffix not in allow_formats:
            msg = f"unknown file extension {path.suffix}"
            raise click.ClickException(msg)
        if not path.is_file():
            msg = "only files allowed"
            raise click.ClickException(msg)
        suffixes.add(suffix)

    if len(suffixes) != 1:
        msg = "all input files must have the same extension"
        raise click.ClickException(msg)

    suffix = suffixes.pop()

    path = Path(output_file)
    if path.suffix != ".pyi":
        msg = 'output file must have the extension "pyi"'
        raise click.ClickException(msg)

    allow_formats[suffix](input_files, output_file)
