from collections.abc import Sequence
from pathlib import Path

from aiogram_i18n.utils.gnutext_stub.parser import parse_mo_file, parse_po_file
from aiogram_i18n.utils.stub_tree import Key


def from_po_files_to_file_ex(files: Sequence[Path], to_file: Path) -> None:
    if file_dir := to_file.parent:
        file_dir.mkdir(parents=True, exist_ok=True)
    to_file.write_text(
        Key().run(
            messages={k: v for file in files for k, v in parse_po_file(file).items()},
        ),
        encoding="utf8",
    )


def from_mo_files_to_file_ex(files: Sequence[Path], to_file: Path) -> None:
    if file_dir := to_file.parent:
        file_dir.mkdir(parents=True, exist_ok=True)
    to_file.write_text(
        Key().run(
            messages={k: v for file in files for k, v in parse_mo_file(file).items()},
        ),
        encoding="utf8",
    )
