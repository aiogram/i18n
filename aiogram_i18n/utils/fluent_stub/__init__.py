
from os import makedirs, path
from typing import Dict, List, Sequence

from aiogram_i18n.exceptions import NoModuleError

try:
    from fluent.syntax import FluentParser
    from .visitor import FluentVisitor
except ImportError:
    raise NoModuleError(name="Fluent stub generator", module_name="fluent.syntax")


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


def parse(text: str) -> Dict[str, List[str]]:
    resource = FluentParser().parse(text)
    if not resource.body:
        raise ValueError("no body")

    ftl_visitor = FluentVisitor()
    ftl_visitor.visit(resource)

    return ftl_visitor.messages


def parse_file(file: str) -> Dict[str, List[str]]:
    with open(file=file, mode="r", encoding="utf8") as r:
        text = r.read()
    return parse(text=text)


def stub_from_messages(messages: Dict[str, List[str]], kw_only: bool = True) -> str:
    stub_text = STUB_HEADER
    for name, params in messages.items():
        params = list(map(lambda x: f'{x}: Any', params))
        if params and kw_only:
            params.insert(0, "*")
        params.insert(0, "self")
        stub_text += f"    def {name.replace('-', '_')}({', '.join(params)}) -> str | LazyProxy: ...\n"
    return stub_text + STUB_FOOTER


def stub_from_file(file: str, kw_only: bool = True) -> str:
    return stub_from_messages(messages=parse_file(file=file), kw_only=kw_only)


def stub_from_string(text: str, kw_only: bool = True) -> str:
    return stub_from_messages(messages=parse(text=text), kw_only=kw_only)


def from_file_to_file(from_file: str, to_file: str, kw_only: bool = True) -> None:
    makedirs(path.dirname(to_file), exist_ok=True)
    with open(file=to_file, mode="w", encoding="utf8") as w:
        w.write(stub_from_file(file=from_file, kw_only=kw_only))


def from_string_to_file(string: str, to_file: str, kw_only: bool = True) -> None:
    makedirs(path.dirname(to_file), exist_ok=True)
    with open(file=to_file, mode="w", encoding="utf8") as w:
        w.write(stub_from_string(text=string, kw_only=kw_only))


def from_files_to_file(files: Sequence[str], to_file: str, kw_only: bool = True) -> None:
    makedirs(path.dirname(to_file), exist_ok=True)
    with open(file=to_file, mode="w", encoding="utf8") as w:
        w.write(stub_from_messages(
            messages={k: v for file in files for k, v in parse_file(file).items()},
            kw_only=kw_only
        ))
