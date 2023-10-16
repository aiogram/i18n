from __future__ import annotations

import re
from copy import copy
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Final, List, Optional, Sequence, Set, Tuple, cast

from click import echo
from libcst import Arg, Attribute, CSTNode, Name, SimpleString

RE_LINE: Final[re.Pattern[str]] = re.compile(r"([^#]+) =")
DIR_SEPARATOR: Final[str] = "--"


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
            f"({'|'.join(keys)}){sep}",
            "",
            self.full_attr_name(cast(Attribute, self.attribute), sep=sep),
        )

    def extract_keywords(self) -> List[str]:
        return [cast(Name, arg.keyword).value for arg in self.keywords]


@dataclass
class FluentKeywords:
    keywords: List[str] = field(default_factory=list)

    def get_placeholders(self) -> Sequence[str]:
        return [f"{{ ${p} }}" for p in set(self.keywords)]


@dataclass
class FluentTemplate:
    filename: Path
    keys: Dict[str, FluentKeywords]
    exclude_keys: List[str] = field(default_factory=list)

    def need_comment(self, key: str, text: str) -> bool:
        return key not in self.keys and not re.search(rf"{{\s*{key}\s*}}", text)

    def update(self) -> List[str]:
        lines: List[str] = []
        removed = 0

        with self.filename.open(mode="r", encoding="utf-8") as template:
            raw_lines = template.readlines()
            raw_text = "".join(raw_lines)
            comment: bool = False

            for line in raw_lines:
                match = RE_LINE.match(line)
                if match:
                    key = match.group(1)
                    comment = self.need_comment(key, raw_text)
                    if comment:
                        removed += 1
                    self.exclude_keys.append(key)
                if comment:
                    line = f"# {line}"
                lines.append(line)

        echo(f"Removed {removed} keys.")
        return lines

    def write(self, create_missing_dirs: bool = False) -> None:
        for key, kw in self.keys.items():
            for keyword in copy(kw.keywords):
                if keyword == "locale":
                    kw.keywords.remove(keyword)

        lines: List[str] = []
        if self.filename.exists():
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

        if create_missing_dirs:
            self.filename.parent.mkdir(parents=True, exist_ok=True)

        with self.filename.open(mode="w", encoding="utf-8") as template:
            echo(f"Writing '{self.filename.name}' template.")
            template.write("".join(lines))


@dataclass
class FluentTemplateDir:
    path: Path
    separator: str
    keys: Dict[str, FluentKeywords]
    exclude_keys: List[str] = field(default_factory=list)
    default_ftl_file: str = "_default.ftl"
    ftl_files: Sequence[Path] = field(default_factory=tuple)

    def write(self, create_missing_dirs: bool = False) -> None:
        filepaths: Dict[Path, List[str]] = {}

        for key in [key for key in self.keys.keys() if key not in self.exclude_keys]:
            if len(dir_keys := key.split(DIR_SEPARATOR, maxsplit=1)) == 1:
                filepaths.setdefault(Path(self.default_ftl_file), []).append(key)
                continue

            filepath = Path()

            for dir_key in dir_keys[0].split(self.separator):
                filepath /= dir_key

            else:
                filepath = filepath.with_suffix(".ftl")

            filepaths.setdefault(filepath, []).append(key)

        for filepath, keys in filepaths.items():
            template = FluentTemplate(
                self.path / filepath.with_suffix(".ftl"),
                {key: kw for key, kw in self.keys.items() if key in keys},
                self.exclude_keys.copy(),
            )
            template.write(create_missing_dirs=create_missing_dirs)
            for key in keys:
                self.keys.pop(key)

        ftl_files = {ftl_file.relative_to(self.path) for ftl_file in self.ftl_files}
        ftl_files -= set(filepaths.keys())

        for ftl_file in ftl_files:
            template = FluentTemplate(
                self.path / ftl_file,
                self.keys,
                self.exclude_keys.copy(),
            )
            template.write(create_missing_dirs=create_missing_dirs)
