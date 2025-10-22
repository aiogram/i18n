from collections.abc import Sequence
from pathlib import Path

from aiogram_i18n.exceptions import NoModuleError
from aiogram_i18n.utils.stub_tree import Key

try:
    from fluent.syntax import FluentParser

    from aiogram_i18n.utils.fluent_stub.visitor import FluentVisitor
except ImportError:
    raise NoModuleError(name="Fluent stub generator", module_name="fluent.syntax") from None

MESSAGES = dict[str, set[str]]


def parse(text: str) -> MESSAGES:
    resource = FluentParser().parse(text)
    if not resource.body:
        msg = "no body"
        raise ValueError(msg)

    ftl_visitor = FluentVisitor()
    ftl_visitor.visit(resource)

    return ftl_visitor.messages


def parse_file(file: str) -> MESSAGES:
    return parse(text=Path(file).read_text(encoding="utf8"))


def from_files_to_file_ex(files: Sequence[str], to_file: str) -> None:
    if file_dir := Path(to_file).parent:
        file_dir.mkdir(exist_ok=True, parents=True)
    Path(to_file).write_text(
        Key().run(
            messages={k: list(v) for file in files for k, v in parse_file(file).items()},
        ),
        encoding="utf8",
    )
