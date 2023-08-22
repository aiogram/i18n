import os
from abc import ABC, abstractmethod
from typing import Any, Dict, Generic, List, Optional, Tuple, TypeVar, cast

from aiogram_i18n import I18nContext
from aiogram_i18n.exceptions import (
    NoLocalesError,
    NoLocalesFoundError,
    NoTranslateFileExistsError,
)

Translator = TypeVar("Translator")


class BaseCore(Generic[Translator], ABC):
    default_locale: Optional[str]
    locales: Dict[str, Translator]
    locales_map: Dict[str, str]

    def __init__(
        self,
        default_locale: Optional[str] = None,
        locales_map: Optional[Dict[str, str]] = None,
    ) -> None:
        self.default_locale = default_locale
        self.locales = {}
        self.locales_map = locales_map or {}

    @abstractmethod
    def get(self, message: str, locale: Optional[str] = None, /, **kwargs: Any) -> str:
        pass

    def get_translator(self, locale: str) -> Translator:
        return self.locales[locale]

    def get_locale(self, locale: Optional[str] = None) -> str:
        if locale is None:
            locale = I18nContext.get_current(no_error=False).locale
        if locale not in self.locales:
            locale = cast(str, self.default_locale)
        return locale

    async def startup(self) -> None:
        self.locales.update(self.find_locales())

    async def shutdown(self) -> None:
        self.locales.clear()

    @staticmethod
    def _extract_locales(path: str) -> List[str]:
        if "{locale}" in path:
            path = path.split("{locale}")[0]
        locales: List[str] = []
        for file_path in os.listdir(path):
            if os.path.isdir(os.path.join(path, file_path)):
                locales.append(file_path)
        if not locales:
            raise NoLocalesFoundError(locales=[], path=path)
        return locales

    @staticmethod
    def _find_locales(
        path: str, locales: List[str], ext: Optional[str] = None
    ) -> Dict[str, List[str]]:
        if not locales:
            raise NoLocalesError
        paths: Dict[str, List[str]] = {}
        if "{locale}" not in path:
            path = os.path.join(path, "{locale}")
        for locale in locales:
            paths[locale] = []
            locale_path = path.format(locale=locale)
            for obj in os.listdir(locale_path):
                if ext is not None:
                    if not obj.endswith(ext):
                        continue
                obj_path = os.path.join(locale_path, obj)
                if not os.path.isfile(obj_path):
                    continue
                paths[locale].append(obj_path)
            if not paths[locale]:
                raise NoTranslateFileExistsError(ext=ext, locale_path=locale_path)
        if not paths:
            raise NoLocalesFoundError(locales=locales, path=path)
        return paths

    @abstractmethod
    def find_locales(self) -> Dict[str, Translator]:
        pass

    @property
    def available_locales(self) -> Tuple[str, ...]:
        return tuple(self.locales.keys())
