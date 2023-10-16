from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict, Sequence, Union, cast

from click import echo
from libcst import Module, parse_module
from libcst import matchers as m

from aiogram_i18n import LazyProxy

from .models import FluentKeywords, FluentMatch


class BaseFluentKeyParser(ABC):
    def __init__(
        self,
        exclude_dirs: Sequence[Path],
        i18n_keys: Sequence[str],
        separator: str,
        locales: Union[Sequence[str], None],
    ) -> None:
        self.exclude_dirs = exclude_dirs
        self.i18n_keys = set(i18n_keys)
        self.separator = separator
        self.locales = locales
        self.result: Dict[str, FluentKeywords] = {}

    @property
    def _matcher(self) -> m.OneOf[m.Call]:
        keywords = m.SaveMatchedNode(m.ZeroOrMore(m.Arg(keyword=m.Name())), name="keywords")

        return m.Call(
            func=m.OneOf(
                m.Attribute(
                    value=m.OneOf(*map(m.Name, self.i18n_keys)),
                    attr=m.Name(value="get"),
                ),
                m.Name(value=LazyProxy.__name__),
                *map(m.Name, self.i18n_keys),
            ),
            args=[
                m.Arg(value=m.SaveMatchedNode(m.SimpleString(), name="string")),
                keywords,
            ],
        ) | m.Call(
            func=m.Attribute(
                value=m.OneOf(*map(m.Name, self.i18n_keys)),
                attr=(m.SaveMatchedNode(m.Name(), name="name")),
            )
            | m.SaveMatchedNode(
                m.Attribute(
                    value=m.Attribute(value=m.OneOf(*map(m.Name, self.i18n_keys))),
                ),
                name="attribute",
            ),
            args=[keywords],
        )

    def parse_tree(self, tree: Module) -> None:
        keys: Dict[str, FluentKeywords] = {}
        matches = tuple(
            FluentMatch(**cast(Dict[str, Any], match))
            for match in m.extractall(tree, self._matcher)
        )

        for _i, match in enumerate(matches):
            key = match.extract_key(self.separator, self.i18n_keys)
            kw = keys.get(key, None)
            if kw is not None:
                kw.keywords.extend(match.extract_keywords())
                continue

            keys[key] = FluentKeywords(keywords=match.extract_keywords())

        self.result.update(keys)

    def parse_file(self, path: Path) -> None:
        try:
            with path.open(mode="r", encoding="utf-8") as py:
                tree = parse_module(py.read())
                self.parse_tree(tree)

        except PermissionError as e:
            echo(f"Can't parse file {path}: {e}")

    def search_py_files(self, path: Path) -> Sequence[Path]:
        return tuple(
            filter(
                lambda x: not x.name.startswith(".") and x.parent not in self.exclude_dirs,
                path.rglob("*.py"),
            )
        )

    @abstractmethod
    def run(self) -> None:
        pass
