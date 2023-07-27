from __future__ import annotations

import os
import re
from dataclasses import dataclass, field
from typing import Dict, List, Tuple, cast, Optional, Sequence, Set

from click import echo
from libcst import Arg, SimpleString, Name, Attribute, CSTNode
from pydantic import BaseModel, Field


@dataclass
class FluentMatch:
    keywords: Tuple[Arg, ...] = field(default_factory=tuple)
    name: Optional[Name] = None
    string: Optional[SimpleString] = None
    attribute: Optional[Attribute] = None

    def full_attr_name(self, node: CSTNode, sep: str) -> str:
        if isinstance(node, Attribute):
            return self.full_attr_name(node.value, sep) + sep + node.attr.value
        return cast(Name, node).value

    def extract_key(self, sep: str, keys: Sequence[str] | Set[str]) -> str:
        if self.name:
            return self.name.value
        if self.string:
            return self.string.raw_value
        return re.sub(
            f"({'|'.join(keys)}){sep}", "",
            self.full_attr_name(cast(Attribute, self.attribute), sep=sep)
        )

    def extract_keywords(self) -> List[str]:
        return [
            cast(Name, arg.keyword).value for arg in self.keywords
        ]


class FluentKeywords(BaseModel):
    keywords: List[str] = Field(default_factory=list)

    def get_placeholders(self) -> Sequence[str]:
        return [f"{{ ${p} }}" for p in set(self.keywords)]


class FluentTemplate(BaseModel):
    filename: str
    keys: Dict[str, FluentKeywords]
    exclude_keys: List[str] = Field(default_factory=list)

    def need_comment(self, key: str, text: str) -> bool:
        return key not in self.keys and not re.search(rf"{{\s*{key}\s*}}", text)

    def update(self) -> List[str]:
        lines: List[str] = []
        removed = 0

        with open(self.filename, mode="r", encoding="utf-8") as template:
            raw_lines = template.readlines()
            raw_text = "".join(raw_lines)
            comment: bool = False

            for line in raw_lines:
                match = re.match(r"([^#]+) =", line)
                if match:
                    key = match.group(1)
                    comment = self.need_comment(key, raw_text)
                    if comment:
                        removed += 1
                    self.exclude_keys.append(key)
                if comment:
                    line = "# " + line
                lines.append(line)

        echo(f"Removed {removed} keys.")
        return lines

    def write(self) -> None:
        lines: List[str] = []
        if os.path.exists(self.filename):
            lines.extend(self.update())

        counter = 0
        for key, kw in self.keys.items():
            if key in self.exclude_keys:
                continue
            counter += 1
            placeholders = kw.get_placeholders()
            value = key if not placeholders else f"{key} {' '.join(placeholders)}"
            lines.append(f"{key} = {value}\n")

        echo(f"Found {counter} new keys.")
        with open(self.filename, mode="w", encoding="utf-8") as template:
            echo(f"Writing '{self.filename}' template.")
            template.write("".join(lines))
