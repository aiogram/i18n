from pathlib import Path
from typing import Any

from aiogram_i18n.cores.base import BaseCore
from aiogram_i18n.exceptions import KeyNotFoundError, NoModuleError
from aiogram_i18n.utils.text_decorator import td

try:
    from jinja2 import Environment, Template
except ImportError as e:
    raise NoModuleError(name="Jinja2Core", module_name="jinja2") from e


class Jinja2Core(BaseCore[dict[str, Template]]):
    environment: Environment

    def __init__(
        self,
        path: str | Path,
        default_locale: str | None = None,
        environment: Environment | None = None,
        raise_key_error: bool = True,
        use_td: bool = True,
        locales_map: dict[str, str] | None = None,
    ) -> None:
        super().__init__(path=path, default_locale=default_locale, locales_map=locales_map)
        self.environment = environment or Environment(autoescape=True)
        if use_td:
            for name, func in td.functions.items():
                self.environment.filters[name.lower()] = func
        self.raise_key_error = raise_key_error

    def get(self, message_id: str, locale: str | None = None, /, **kwargs: Any) -> str:
        locale = self.get_locale(locale=locale)
        translator: dict[str, Template] = self.get_translator(locale=locale)
        try:
            message = translator[message_id]
        except KeyError:
            locale: str | None = self.locales_map.get(locale)
            if locale is not None:
                return self.get(message_id, locale, **kwargs)
            if self.raise_key_error:
                raise KeyNotFoundError(message_id) from None
            return message_id
        return message.render(kwargs)

    def find_locales(self) -> dict[str, dict[str, Template]]:
        translations: dict[str, dict[str, Template]] = {}
        locales = self._extract_locales(self.path)
        for locale, paths in self._find_locales(self.path, locales, ".j2").items():
            translations[locale] = {}
            for file_path in paths:
                with file_path.open(encoding="utf-8") as f:
                    translations[locale][file_path.stem] = self.environment.from_string(f.read())

        return translations
