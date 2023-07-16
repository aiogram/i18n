import os
from abc import abstractmethod, ABC
from typing import List, Dict, Optional, Any, Tuple, TypeVar, Generic, cast
from aiogram_i18n.exceptions import NoTranslateFileExistsError, NoLocalesFoundError, NoLocalesError


Translator = TypeVar("Translator")


class BaseCore(Generic[Translator], ABC):
    default_locale: Optional[str]
    locales: Dict[str, Translator]

    def __init__(self, default_locale: Optional[str] = None) -> None:
        self.default_locale = default_locale
        self.locales = {}

    @abstractmethod
    def get(self, key: str, /, locale: str, **kwargs: Any) -> str:
        ...

    def get_translator(self, locale: str) -> Translator:
        if locale not in self.locales:
            locale = cast(str, self.default_locale)
        return self.locales[locale]

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
            raise NoLocalesFoundError(locales=["..."], path=path)
        return locales

    @staticmethod
    def _find_locales(path: str, locales: List[str], ext: Optional[str] = None) -> Dict[str, List[str]]:
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
        ...

    @property
    def available_locales(self) -> Tuple[str, ...]:
        return tuple(self.locales.keys())
