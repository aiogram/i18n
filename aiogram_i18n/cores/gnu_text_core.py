from gettext import GNUTranslations
from typing import Any, Dict, Optional

from aiogram_i18n.cores.base import BaseCore


class GNUTextCore(BaseCore[GNUTranslations]):
    def __init__(
        self,
        *,
        path: str,
        default_locale: Optional[str] = None,
    ) -> None:
        super().__init__(default_locale=default_locale)
        self.path = path

    def find_locales(self) -> Dict[str, GNUTranslations]:
        """
        Load all compiled locales from path

        :return: dict with locales
        """
        translations: Dict[str, GNUTranslations] = {}
        locales = self._extract_locales(self.path)
        for locale, paths in self._find_locales(self.path, locales, ".mo").items():
            trans = translations[locale] = GNUTranslations()
            for path in paths:
                with open(path, "rb") as fp:
                    trans._parse(fp=fp)  # noqa

        return translations

    def get(self, message: str, locale: Optional[str] = None, /, **kwargs: Any) -> str:
        translator = self.get_translator(locale=locale)
        return translator.gettext(message=message).format(**kwargs)

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
        return translator.ngettext(msgid1=singular, msgid2=plural or singular, n=n).format(
            **kwargs
        )
