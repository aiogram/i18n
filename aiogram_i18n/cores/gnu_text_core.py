from gettext import GNUTranslations
from pathlib import Path
from typing import Any, NoReturn

from aiogram_i18n.cores.base import BaseCore
from aiogram_i18n.exceptions import KeyNotFoundError, UnknownLocaleError


class Fallback:
    def gettext(self, message: str) -> NoReturn:  # noqa: ARG002
        raise KeyError

    def ngettext(self, msgid1: str, msgid2: str | None, n: int) -> NoReturn:  # noqa: ARG002
        raise KeyError


class GNUTextCore(BaseCore[GNUTranslations]):
    def __init__(
        self,
        *,
        path: str | Path,
        default_locale: str | None = None,
        raise_key_error: bool = False,
        locales_map: dict[str, str] | None = None,
    ) -> None:
        super().__init__(path=path, default_locale=default_locale, locales_map=locales_map)
        self.raise_key_error = raise_key_error

    def find_locales(self) -> dict[str, GNUTranslations]:
        """
        Load all compiled locales from path
        :return: dict with locales
        """
        fallback = Fallback()
        translations: dict[str, GNUTranslations] = {}
        locales = self._extract_locales(self.path)
        for locale, paths in self._find_locales(self.path, locales, ".mo").items():
            trans = translations[locale] = GNUTranslations()
            trans._fallback = fallback  # type: ignore[attr-defined]  # noqa: SLF001
            for path in paths:
                with path.open("rb") as fp:
                    trans._parse(fp=fp)  # noqa: SLF001

        for locale, fallback_locale in self.locales_map.items():
            if locale not in translations:
                raise UnknownLocaleError(locale)
            if fallback_locale not in translations:
                raise UnknownLocaleError(fallback_locale)
            translations[locale]._fallback = translations[  # type: ignore[attr-defined]  # noqa: SLF001
                fallback_locale
            ]

        return translations

    def get(self, message: str, locale: str | None = None, /, **kwargs: Any) -> str:
        locale = self.get_locale(locale=locale)
        translator = self.get_translator(locale=locale)
        try:
            return translator.gettext(message=message).format_map(kwargs)
        except KeyError:
            if self.raise_key_error:
                raise KeyNotFoundError(message) from None
            return message.format_map(kwargs)

    def nget(
        self,
        singular: str,
        plural: str | None = None,
        n: int = 1,
        locale: str | None = None,
        /,
        **kwargs: Any,
    ) -> str:
        locale = self.get_locale(locale=locale)
        translator = self.get_translator(locale=locale)
        if plural is None:
            plural = singular
        try:
            return translator.ngettext(msgid1=singular, msgid2=plural, n=n).format_map(kwargs)
        except KeyError:
            if self.raise_key_error:
                raise KeyNotFoundError(singular) from None
            if n == 1:
                return singular
            return plural
