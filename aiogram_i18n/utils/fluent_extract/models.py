
from __future__ import annotations

import os
import re
from typing import List, Sequence, Dict

from libcst import Arg
from pydantic import BaseModel, Field


class FluentKey(BaseModel):
    key: str
    keywords: List[str] = Field(default_factory=list)

    def get_placeholders(self) -> Sequence[str]:
        return [f"{{ ${p} }}" for p in set(self.keywords)]

    @classmethod
    def from_args(cls, key: str, args: Sequence[Arg]) -> FluentKey:
        return cls(
            key=key,
            keywords=[a.keyword.value for a in args if a.keyword]
        )


class FluentTemplate(BaseModel):
    filename: str
    keys: Dict[str, FluentKey]
    exclude_keys: List[str] = Field(default_factory=list)

    def need_comment(self, key: str, text: str) -> bool:
        return key not in self.keys and not re.search(rf"{{\s*{key}\s*}}", text)

    def update(self) -> List[str]:
        lines: List[str] = []
        comment: bool = False
        removed = 0

        with open(self.filename, mode="r", encoding="utf-8") as template:
            raw_lines = template.readlines()
            raw_text = "".join(raw_lines)

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

        print(f"Removed {removed} keys.")
        return lines

    def write(self) -> None:
        lines: List[str] = []
        if os.path.exists(self.filename):
            lines.extend(self.update())

        counter = 0
        for key in self.keys.values():
            if key.key in self.exclude_keys:
                continue
            counter += 1
            placeholders = key.get_placeholders()
            value = key.key if not placeholders else f"{key.key} {' '.join(placeholders)}"
            lines.append(f"{key.key} = {value}\n")

        print(f"Found {counter} new keys.")
        with open(self.filename, mode="w", encoding="utf-8") as template:
            print(f"Writing '{self.filename}' template.")
            template.write("".join(lines))
