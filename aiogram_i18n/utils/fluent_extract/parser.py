from __future__ import annotations

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
            py_files = self.search_py_files(path)

            for py_file in py_files:
                self.parse_file(py_file)

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
        default_ftl_file: str,
    ) -> None:
        super().__init__(exclude_dirs, i18n_keys, separator, locales)
        self.input_paths = set(input_paths)
        self.output_dir = output_dir
        self.exclude_keys = list(exclude_keys)
        self.default_ftl_file = default_ftl_file

    def run(self, create_missing_dirs: bool = False) -> None:
        for path in self.input_paths:
            py_files = self.search_py_files(path)

            for py_file in py_files:
                self.parse_file(py_file)

        if self.locales:
            for locale in self.locales:
                path = self.output_dir / locale
                template = FluentTemplateDir(
                    path=path,
                    separator=self.separator,
                    keys=self.result.copy(),
                    exclude_keys=self.exclude_keys.copy(),
                    default_ftl_file=self.default_ftl_file,
                    ftl_files=tuple(path.rglob("*.ftl")),
                )
                template.write(create_missing_dirs=create_missing_dirs)

        else:
            template = FluentTemplateDir(
                path=self.output_dir,
                separator=self.separator,
                keys=self.result.copy(),
                exclude_keys=self.exclude_keys.copy(),
                default_ftl_file=self.default_ftl_file,
                ftl_files=tuple(self.output_dir.rglob("*.ftl")),
            )
            template.write(create_missing_dirs=create_missing_dirs)
