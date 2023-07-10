
from __future__ import annotations

import re
from typing import Dict, Optional, Set, cast

import libcst as cst

from .models import FluentKey


class FluentKeyVisitor(cst.CSTVisitor):
    def __init__(self, i18n_keys: Set[str], sep: str) -> None:
        super().__init__()
        self.i18n_keys = i18n_keys
        self.separator = sep
        self.keys: Dict[str, FluentKey] = {}

    def get_attribute_name(self, node: cst.CSTNode) -> str:
        if isinstance(node, cst.Attribute):
            return self.get_attribute_name(node.value) + '.' + node.attr.value
        elif isinstance(node, cst.Call):
            return self.get_attribute_name(node.func)
        return cast(cst.Name, node).value

    def get_name(self, node: cst.CSTNode) -> Optional[str]:
        if isinstance(node, cst.Attribute):
            return self.get_name(node.value)
        elif isinstance(node, cst.Name):
            return node.value
        return None

    def visit_Call(self, node: cst.Call) -> None:
        attr = node.func
        if isinstance(attr, cst.Attribute):
            name = self.get_name(attr)
            if name in self.i18n_keys:
                key: Optional[FluentKey] = None
                if attr.attr.value == "get":
                    arg = cast(cst.SimpleString, node.args[0].value)
                    if isinstance(arg, cst.SimpleString):
                        key = FluentKey.from_args(
                            arg.value.strip("'").strip('"'), node.args[1:]
                        )
                else:
                    key = FluentKey.from_args(
                        re.sub(
                            rf"({'|'.join(self.i18n_keys)})\.", "",
                            self.get_attribute_name(node)
                        ).replace(".", self.separator),
                        node.args
                    )

                if key is not None:
                    if key.key in self.keys:
                        self.keys[key.key].keywords.extend(key.keywords)
                    else:
                        self.keys[key.key] = key
