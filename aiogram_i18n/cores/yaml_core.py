from pathlib import Path
from typing import Any, Dict, Optional, Union

from aiogram_i18n.cores.base import BaseCore
from aiogram_i18n.exceptions import KeyNotFoundError, NoModuleError

try:
    from yaml import safe_load
except ImportError as e:
    raise NoModuleError(name="YamlCore", module_name="pyyaml") from e


class YamlCore(BaseCore[Dict[str, Any]]):
    def __init__(
        self,
        path: Union[str, Path],
        default_locale: Optional[str] = None,
        raise_key_error: bool = True,
        locales_map: Optional[Dict[str, str]] = None,
    ) -> None:
        super().__init__(path=path, default_locale=default_locale, locales_map=locales_map)
        self.raise_key_error = raise_key_error

    # з цими функціями працює, але з оригінальними баг
    # def _extract_locales(self, path: Path) -> list[str]:
    #     return [p.stem for p in path.glob("*.yaml")] + [p.stem for p in path.glob("*.yml")]

    # def _find_locales(
    #     self,
    #     path: Path,
    #     locales: list[str],
    #     extensions: tuple[str, ...] = (".yaml", ".yml")
    # ) -> Dict[str, list[Path]]:
    #     found = {}
    #     for loc in locales:
    #         found[loc] = []
    #         for ext in extensions:
    #             file_path = path / f"{loc}{ext}"
    #             if file_path.is_file():
    #                 found[loc].append(file_path)
    #     return found

    def find_locales(self) -> Dict[str, Dict[str, Any]]:
        translations: Dict[str, Dict[str, Any]] = {}
        locales = self._extract_locales(self.path)
        for file_ext in (".yaml", ".yml"):
            for locale, paths in self._find_locales(self.path, locales, file_ext).items():

                if locale not in translations:
                    translations[locale] = {}
                for file in paths:
                    with file.open(encoding="utf-8") as f:
                        content = safe_load(f) or {}
                    translations[locale].update(content)
        return translations

    def get(self, message_id: str, locale: Optional[str] = None, /, **kwargs: Any) -> str:
        locale = self.get_locale(locale)
        translator = self.get_translator(locale)
        try:
            text = translator[message_id]
        except KeyError:
            if mapped := self.locales_map.get(locale):
                return self.get(message_id, mapped, **kwargs)
            if self.raise_key_error:
                raise KeyNotFoundError(message_id) from None
            return message_id
        try:
            return text.format_map(kwargs)
        except Exception:
            return text
