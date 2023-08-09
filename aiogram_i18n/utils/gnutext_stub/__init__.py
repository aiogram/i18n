from os import makedirs, path
from typing import Sequence

from aiogram_i18n.utils.stub_tree import Key

from .parser import parse_mo_file, parse_po_file


def from_po_files_to_file_ex(files: Sequence[str], to_file: str) -> None:
    if file_dir := path.dirname(to_file):
        makedirs(file_dir, exist_ok=True)
    with open(file=to_file, mode="w", encoding="utf8") as w:
        w.write(
            Key().run(
                messages={k: v for file in files for k, v in parse_po_file(file).items()},
            )
        )


def from_mo_files_to_file_ex(files: Sequence[str], to_file: str) -> None:
    if file_dir := path.dirname(to_file):
        makedirs(file_dir, exist_ok=True)
    with open(file=to_file, mode="w", encoding="utf8") as w:
        w.write(
            Key().run(
                messages={k: v for file in files for k, v in parse_mo_file(file).items()},
            )
        )
