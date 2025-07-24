from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path
from typing import Callable

import click

from aiogram_i18n.utils.cli.base import main

STUB_GENERATOR = Callable[[Sequence[Path], Path], None]


def lazy_import(name: str, func: str) -> STUB_GENERATOR:
    def generator_run(files: Sequence[Path], to_file: Path) -> None:
        getattr(__import__(name=name, fromlist=[func]), func)(files, to_file)

    return generator_run


@main.command(help="Generate stubs from .ftl files")
@click.option(
    "-i",
    "--input-files",
    required=True,
    multiple=True,
    type=click.Path(exists=True, path_type=Path),
)
@click.option("-o", "--output-file", required=True, type=click.Path(exists=False, path_type=Path))
def stub(input_files: tuple[Path, ...], output_file: Path) -> None:
    allow_formats: dict[str, Callable[[Sequence[Path], Path], None]] = {
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
            raise ValueError(msg)
        if suffix not in allow_formats:
            msg = f"unknown file extension {path.suffix}"
            raise ValueError(msg)
        if not path.is_file():
            msg = "only files allowed"
            raise ValueError(msg)

    path = Path(output_file)
    if path.suffix != ".pyi":
        msg = 'output file must have the extension "pyi"'
        raise ValueError(msg)

    allow_formats[suffix](input_files, output_file)
