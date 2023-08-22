from __future__ import annotations

import os
from pathlib import Path
from typing import Sequence, Union

from .base import BaseFluentKeyParser
from .models import FluentTemplate, FluentTemplateDir


class FluentKeyParser(BaseFluentKeyParser):
    def __init__(
        self,
        input_dirs: Sequence[Path],
        output_file: Path,
        i18n_keys: Sequence[str],
        separator: str,
        locales: Union[Sequence[str], None],
        exclude_dirs: Sequence[Path],
        exclude_keys: Sequence[str],
    ) -> None:
        super().__init__(exclude_dirs, i18n_keys, separator, locales)
        self.input_dirs = set(input_dirs)
        self.output_file = output_file
        self.exclude_dirs = exclude_dirs
        self.exclude_keys = list(exclude_keys)

    def run(self, create_missing_dirs: bool = False) -> None:
        for path in self.input_dirs:
            if os.path.isdir(path):
                self.parse_dir(path)
            else:
                self.parse_file(path)

        if self.locales:
            for locale in self.locales:
                template = FluentTemplate(
                    filename=self.output_file.parent / locale / self.output_file.name,
                    keys=self.result,
                    exclude_keys=self.exclude_keys,
                )
                template.write(create_missing_dirs=create_missing_dirs)

        else:
            template = FluentTemplate(
                filename=self.output_file,
                keys=self.result,
                exclude_keys=self.exclude_keys,
            )
            template.write(create_missing_dirs=create_missing_dirs)


class FluentMultipleKeyParser(BaseFluentKeyParser):
    def __init__(
        self,
        input_paths: Sequence[Path],
        output_dir: Path,
        i18n_keys: Sequence[str],
        separator: str,
        locales: Union[Sequence[str], None],
        exclude_dirs: Sequence[Path],
        exclude_keys: Sequence[str],
    ) -> None:
        super().__init__(exclude_dirs, i18n_keys, separator, locales)
        self.input_paths = set(input_paths)
        self.output_dir = output_dir
        self.exclude_keys = list(exclude_keys)

    def run(self, create_missing_dirs: bool = False) -> None:
        for path in self.input_paths:
            if path.is_dir():
                self.parse_dir(path)
            else:
                self.parse_file(path)

        if self.locales:
            for locale in self.locales:
                template = FluentTemplateDir(
                    path=self.output_dir / locale,
                    separator=self.separator,
                    keys=self.result,
                    exclude_keys=self.exclude_keys,
                )
                template.write(create_missing_dirs=create_missing_dirs)

        else:
            template = FluentTemplateDir(
                path=self.output_dir,
                separator=self.separator,
                keys=self.result,
                exclude_keys=self.exclude_keys,
            )
            template.write(create_missing_dirs=create_missing_dirs)
