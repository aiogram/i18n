import os
from abc import abstractmethod, ABC
from typing import List, Dict, Optional, Any, Tuple, TypeVar, Generic


Translator = TypeVar("Translator")


class BaseCore(Generic[Translator], ABC):
    default_locale: str
    locales: Dict[str, Translator]

    def __init__(self) -> None:
        self.locales = {}

    @abstractmethod
    def get(self, locale: str, key: str, *args: Any, **kwargs: Any) -> str:
        ...

    def get_translator(self, locale: str) -> Translator:
        if locale not in self.locales:
            locale = self.default_locale
        return self.locales[locale]

    async def startup(self) -> None:
        self.locales.update(self.find_locales())

    async def shutdown(self, *args: Any, **kwargs: Any) -> None:
        ...

    @staticmethod
    def _extract_locales(path: str) -> List[str]:
        if "{locale}" in path:
            path = path.split("{locale}")[0]
        return [p for p in os.listdir(path) if os.path.isdir(os.path.join(path, p))]

    @staticmethod
    def _find_locales(path: str, locales: List[str], ext: Optional[str] = None) -> Dict[str, List[str]]:
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
        return paths

    @abstractmethod
    def find_locales(self) -> Dict[str, Translator]:
        ...

    @property
    def available_locales(self) -> Tuple[str, ...]:
        return tuple(self.locales.keys())
