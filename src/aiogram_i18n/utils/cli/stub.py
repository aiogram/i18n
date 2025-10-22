from collections.abc import Callable, Sequence
from pathlib import Path

import click

from aiogram_i18n.utils.cli import main

STUB_GENERATOR = Callable[[Sequence[str], str], None]


def lazy_import(name: str, func: str) -> STUB_GENERATOR:
    def generator_run(files: Sequence[str], to_file: str) -> None:
        getattr(__import__(name=name, fromlist=[func]), func)(files, to_file)

    return generator_run


@main.command(help="Generate stubs from .ftl files")
@click.option("-i", "--input-files", required=True, multiple=True)
@click.option("-o", "--output-file", required=True)
def stub(input_files: tuple[str, ...], output_file: str) -> None:
    allow_formats: dict[str, Callable[[Sequence[str], str], None]] = {
        "ftl": lazy_import("aiogram_i18n.utils.fluent_stub", "from_files_to_file_ex"),
        "mo": lazy_import("aiogram_i18n.utils.gnutext_stub", "from_mo_files_to_file_ex"),
        "po": lazy_import("aiogram_i18n.utils.gnutext_stub", "from_po_files_to_file_ex"),
        "pot": lazy_import("aiogram_i18n.utils.gnutext_stub", "from_po_files_to_file_ex"),
    }

    suffix: str = "ftl"
    for input_file in input_files:
        path = Path(input_file)
        suffix = path.suffix[1:]
        if not suffix:
            msg = f"only files with this extension are allowed ({', '.join(allow_formats.keys())})"
            raise Exception(msg)  # noqa: TRY002
        if suffix not in allow_formats:
            msg = f"unknown file extension {path.suffix}"
            raise Exception(msg)  # noqa: TRY002
        if not path.is_file():
            msg = "only files allowed"
            raise Exception(msg)  # noqa: TRY002

    path = Path(output_file)
    if path.suffix != ".pyi":
        msg = 'output file must have the extension "pyi"'
        raise Exception(msg)  # noqa: TRY002

    allow_formats[suffix](input_files, output_file)
