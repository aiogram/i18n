from __future__ import annotations

import os
from typing import Sequence

try:
    from libcst import parse_module
except ImportError:
    raise ImportError(
        "Fluent keys extractor can be used only when libcst installed\n"
        "Just install libcst (`pip install libcst`)"
    )

from .models import FluentTemplate
from .visitor import FluentKeyVisitor


class FluentKeyParser:
    def __init__(
        self,
        input_dirs: Sequence[str], output_file: str,
        i18n_keys: Sequence[str], separator: str,
        exclude_dirs: Sequence[str], exclude_keys: Sequence[str]
    ) -> None:
        self.input_dirs = set(input_dirs)
        self.output = output_file
        self.exclude_dirs = exclude_dirs
        self.exclude_keys = list(exclude_keys)
        self.visitor = FluentKeyVisitor(set(i18n_keys), separator)

    def parse_file(self, path: str) -> None:
        try:
            with open(path, mode="r", encoding="utf-8") as py:
                tree = parse_module(py.read())
                tree.visit(self.visitor)

        except PermissionError as e:
            print(f"Can't parse file {path}: {e}")

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
            filename=self.output,
            keys=self.visitor.keys,
            exclude_keys=self.exclude_keys
        )
        template.write()
