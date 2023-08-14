from typing import Any, Dict, Optional

from aiogram_i18n.cores.base import BaseCore

from .gnu_translations import SmartGNUTranslations


class GNUTextCore(BaseCore[SmartGNUTranslations]):
    def __init__(
        self,
        *,
        path: str,
        default_locale: Optional[str] = None,
        plural_n_key: Optional[str] = None,
        plural_msg_key: Optional[str] = None,
        plural_context_key: Optional[str] = None,
    ) -> None:
        super().__init__(default_locale=default_locale)
        self.path = path
        self.plural_n_key = plural_n_key
        self.plural_msg_key = plural_msg_key
        self.plural_context_key = plural_context_key

    def find_locales(self) -> Dict[str, SmartGNUTranslations]:
        """
        Load all compiled locales from path

        :return: dict with locales
        """
        translations: Dict[str, SmartGNUTranslations] = {}
        locales = self._extract_locales(self.path)
        for locale, paths in self._find_locales(self.path, locales, ".mo").items():
            trans = translations[locale] = SmartGNUTranslations(
                plural_context_key=self.plural_context_key,
                plural_msg_key=self.plural_msg_key,
                plural_n_key=self.plural_n_key,
            )
            for path in paths:
                with open(path, "rb") as fp:
                    trans.parse(fp=fp)

        return translations

    def get(self, key: str, /, locale: str, **kwargs: Any) -> str:
        translator = self.get_translator(locale=locale)
        return translator.get(key, **kwargs)
