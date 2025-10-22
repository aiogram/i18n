from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Generic, TypeVar, cast

from aiogram_i18n import I18nContext
from aiogram_i18n.exceptions import NoLocalesError, NoLocalesFoundError, NoTranslateFileExistsError

Translator = TypeVar("Translator")


class BaseCore(ABC, Generic[Translator]):
    """
    Is an abstract base class for implementing core functionality for translation.
    """

    default_locale: str | None
    locales: dict[str, Translator]
    locales_map: dict[str, str]

    def __init__(
        self,
        path: str | Path,
        default_locale: str | None = None,
        locales_map: dict[str, str] | None = None,
    ) -> None:
        """

        :param default_locale: The default locale to be used for translations.
            If not provided, it will default to None.
        """
        self.path = path if isinstance(path, Path) else Path(path)
        self.default_locale = default_locale
        self.locales = {}
        self.locales_map = locales_map or {}

    @abstractmethod
    def get(self, message: str, locale: str | None = None, /, **kwargs: Any) -> str:
        pass

    def nget(
        self,
        singular: str,
        plural: str | None = None,  # noqa: ARG002
        n: int = 1,  # noqa: ARG002
        locale: str | None = None,
        /,
        **kwargs: Any,
    ) -> str:
        return self.get(singular, locale, **kwargs)

    def get_translator(self, locale: str) -> Translator:
        return self.locales[locale]

    def get_locale(self, locale: str | None = None) -> str:
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
    def _extract_locales(path: Path) -> list[str]:
        if "{locale}" in path.parts:
            path = Path(*path.parts[: path.parts.index("{locale}")])

        locales: list[str] = [file_path.name for file_path in path.iterdir() if file_path.is_dir()]

        if not locales:
            raise NoLocalesFoundError(locales=[], path=path.as_posix())

        return locales

    @staticmethod
    def _find_locales(
        path: Path, locales: list[str], ext: str | None = None
    ) -> dict[str, list[Path]]:
        if not locales:
            raise NoLocalesError

        paths: dict[str, list[Path]] = {}

        if "{locale}" not in path.as_posix():
            path = path.joinpath("{locale}")

        for locale in locales:
            locale_path = Path(path.as_posix().format(locale=locale))
            recursive_paths = locale_path.rglob(f"*{ext}")  # Will recursively search for files
            paths.setdefault(locale, []).extend(recursive_paths)

            if not paths[locale]:
                raise NoTranslateFileExistsError(ext=ext, locale_path=locale_path.as_posix())
        if not paths:
            raise NoLocalesFoundError(locales=locales, path=path.as_posix())

        return paths

    @abstractmethod
    def find_locales(self) -> dict[str, Translator]:
        pass

    @property
    def available_locales(self) -> tuple[str, ...]:
        return tuple(self.locales.keys())
