from __future__ import annotations

import os
from typing import Sequence, Dict, cast, Any

from click import echo
from libcst import parse_module, matchers as m, Module

from .models import FluentTemplate, FluentMatch, FluentKeywords
from ... import LazyProxy


class FluentKeyParser:
    def __init__(
        self,
        input_dirs: Sequence[str], output_file: str,
        i18n_keys: Sequence[str], separator: str,
        exclude_dirs: Sequence[str], exclude_keys: Sequence[str]
    ) -> None:
        self.input_dirs = set(input_dirs)
        self.output_file = output_file
        self.i18n_keys = set(i18n_keys)
        self.separator = separator
        self.exclude_dirs = exclude_dirs
        self.exclude_keys = list(exclude_keys)
        self.result: Dict[str, FluentKeywords] = {}

    @property
    def _matcher(self) -> m.OneOf[m.Call]:
        keywords = m.SaveMatchedNode(
            m.ZeroOrMore(m.Arg(keyword=m.Name())), name="keywords"
        )

        return m.Call(
            func=m.Attribute(
                value=m.OneOf(*map(m.Name, self.i18n_keys)),
                attr=m.Name(value="get"),
            ) | m.Name(value=LazyProxy.__name__),
            args=[
                m.Arg(value=m.SaveMatchedNode(m.SimpleString(), name="key")),
                keywords
            ]
        ) | m.Call(
            func=m.Attribute(
                value=m.OneOf(*map(m.Name, self.i18n_keys)),
                attr=m.SaveMatchedNode(m.Name(), name="key"),
            ),
            args=[keywords]
        )

    def parse_tree(self, tree: Module) -> None:
        keys: Dict[str, FluentKeywords] = {}
        matches = tuple(
            FluentMatch(**cast(Dict[str, Any], match)) for match in
            m.extractall(tree, self._matcher)
        )

        for match in matches:
            key = match.extract_key(self.separator)
            kw = keys.get(key)
            if not kw:
                keys[key] = FluentKeywords(keywords=match.extract_keywords())
            else:
                kw.keywords.extend(match.extract_keywords())

        self.result.update(keys)

    def parse_file(self, path: str) -> None:
        try:
            with open(path, mode="r", encoding="utf-8") as py:
                tree = parse_module(py.read())
                self.parse_tree(tree)

        except PermissionError as e:
            echo(f"Can't parse file {path}: {e}")

    def parse_dir(self, path: str) -> None:
        for p in os.listdir(path):
            _path = os.path.join(path, p)

            if p.startswith(".") or p in self.exclude_dirs:
                continue

            if os.path.isdir(_path):
                self.parse_dir(_path)

            elif _path.endswith(".py"):
                self.parse_file(os.path.join(path, p))

    def run(self) -> None:
        for path in self.input_dirs:
            if os.path.isdir(path):
                self.parse_dir(path)
            else:
                self.parse_file(path)

        template = FluentTemplate(
            filename=self.output_file,
            keys=self.result,
            exclude_keys=self.exclude_keys
        )
        template.write()
