from os import makedirs, path
from typing import Sequence

from aiogram_i18n.exceptions import NoModuleError
from aiogram_i18n.utils.stub_tree import Key

try:
    from fluent.syntax import FluentParser

    from .visitor import FluentVisitor
except ImportError:
    raise NoModuleError(name="Fluent stub generator", module_name="fluent.syntax")

MESSAGES = dict[str, list[str]]

STUB_HEADER = """from typing import Any

from aiogram_i18n import I18nContext as _I18nContext
from aiogram_i18n.lazy import LazyProxy, LazyFactory as _LazyFactory


class I18nStubs:
"""

STUB_FOOTER = """

class I18nContext(I18nStubs, _I18nContext):
    ...


class LazyFactory(I18nStubs, _LazyFactory):
    ...


L: LazyFactory
"""


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


def stub_from_messages(messages: MESSAGES, kw_only: bool = True) -> str:
    stub_text = STUB_HEADER
    for name, params in messages.items():
        params = [f"{x}: Any" for x in params]
        if params and kw_only:
            params.insert(0, "*")
        params.insert(0, "self")
        stub_text += (
            f"    def {name.replace('-', '_')}({', '.join(params)}) -> str | LazyProxy: ...\n"
        )
    return stub_text + STUB_FOOTER


def stub_from_file(file: str, kw_only: bool = True) -> str:
    return stub_from_messages(messages=parse_file(file=file), kw_only=kw_only)


def stub_from_string(text: str, kw_only: bool = True) -> str:
    return stub_from_messages(messages=parse(text=text), kw_only=kw_only)


def from_file_to_file(from_file: str, to_file: str, kw_only: bool = True) -> None:
    if file_dir := path.dirname(to_file):
        makedirs(file_dir, exist_ok=True)
    with open(file=to_file, mode="w", encoding="utf8") as w:
        w.write(stub_from_file(file=from_file, kw_only=kw_only))


def from_string_to_file(string: str, to_file: str, kw_only: bool = True) -> None:
    if file_dir := path.dirname(to_file):
        makedirs(file_dir, exist_ok=True)
    with open(file=to_file, mode="w", encoding="utf8") as w:
        w.write(stub_from_string(text=string, kw_only=kw_only))


def from_files_to_file(files: Sequence[str], to_file: str, kw_only: bool = True) -> None:
    if file_dir := path.dirname(to_file):
        makedirs(file_dir, exist_ok=True)
    with open(file=to_file, mode="w", encoding="utf8") as w:
        w.write(
            stub_from_messages(
                messages={k: v for file in files for k, v in parse_file(file).items()},
                kw_only=kw_only,
            )
        )


def from_files_to_file_ex(files: Sequence[str], to_file: str) -> None:
    if file_dir := path.dirname(to_file):
        makedirs(file_dir, exist_ok=True)
    with open(file=to_file, mode="w", encoding="utf8") as w:
        w.write(
            Key().run(
                messages={k: v for file in files for k, v in parse_file(file).items()},
            )
        )
