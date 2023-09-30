from os import makedirs, path
from typing import Sequence

from aiogram_i18n.exceptions import NoModuleError
from aiogram_i18n.utils.stub_tree import Key

try:
    from fluent.syntax import FluentParser

    from .visitor import FluentVisitor
except ImportError:
    raise NoModuleError(name="Fluent stub generator", module_name="fluent.syntax")

MESSAGES = dict[str, set[str]]


def parse(text: str) -> MESSAGES:
    resource = FluentParser().parse(text)
    if not resource.body:
        raise ValueError("no body")

    ftl_visitor = FluentVisitor()
    ftl_visitor.visit(resource)

    return ftl_visitor.messages


def parse_file(file: str) -> MESSAGES:
    with open(file=file, mode="r", encoding="utf8") as r:
        text = r.read()
    return parse(text=text)


def from_files_to_file_ex(files: Sequence[str], to_file: str) -> None:
    if file_dir := path.dirname(to_file):
        makedirs(file_dir, exist_ok=True)
    with open(file=to_file, mode="w", encoding="utf8") as w:
        w.write(
            Key().run(
                messages={k: list(v) for file in files for k, v in parse_file(file).items()},
            )
        )
