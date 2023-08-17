from gettext import GNUTranslations
from typing import Any, Dict, Optional

from aiogram_i18n.cores.base import BaseCore
from aiogram_i18n.exceptions import KeyNotFoundError


class Fallback:
    def gettext(self, message):
        raise KeyError

    def ngettext(self, msgid1, msgid2, n):
        raise KeyError


class GNUTextCore(BaseCore[GNUTranslations]):
    def __init__(
        self,
        *,
        path: str,
        default_locale: Optional[str] = None,
        raise_key_error: bool = False,
        locales_map: Optional[Dict[str, str]] = None,
    ) -> None:
        super().__init__(default_locale=default_locale, locales_map=locales_map)
        self.path = path
        self.raise_key_error = raise_key_error

    def find_locales(self) -> Dict[str, GNUTranslations]:
        """
        Load all compiled locales from path

        :return: dict with locales
        """
        fallback = Fallback()
        translations: Dict[str, GNUTranslations] = {}
        locales = self._extract_locales(self.path)
        for locale, paths in self._find_locales(self.path, locales, ".mo").items():
            trans = translations[locale] = GNUTranslations()
            trans._fallback = fallback
            for path in paths:
                with open(path, "rb") as fp:
                    trans._parse(fp=fp)  # noqa

        for locale, fallback_locale in self.locales_map.items():
            if locale not in translations:
                raise ValueError
            if fallback_locale not in translations:
                raise ValueError
            translations[locale]._fallback = translations[fallback_locale]  # noqa

        return translations

    def get(self, message: str, locale: Optional[str] = None, /, **kwargs: Any) -> str:
        translator = self.get_translator(locale=locale)
        try:
            return translator.gettext(message=message).format(**kwargs)
        except KeyError:
            if self.raise_key_error:
                raise KeyNotFoundError(message) from None
            return message

    def nget(
        self,
        singular: str,
        plural: Optional[str] = None,
        n: int = 1,
        locale: Optional[str] = None,
        /,
        **kwargs: Any,
    ) -> str:
        translator = self.get_translator(locale=locale)
        try:
            return translator.ngettext(
                msgid1=singular,
                msgid2=plural or singular,
                n=n
            ).format(**kwargs)
        except KeyError:
            if self.raise_key_error:
                raise KeyNotFoundError(singular) from None
            if n == 1:
                return singular
            else:
                return plural
