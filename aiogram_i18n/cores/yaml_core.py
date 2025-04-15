import os
import yaml
from typing import Optional

from aiogram_i18n.cores.base import BaseCore


class I18nYamlCore(BaseCore):
    def __init__(self, path: str, default_locale: str = 'en'):
        """
        :param path: directory with YAML files with translations
        """
        super().__init__(path=path, default_locale=default_locale)
        self._cache = {} 
        self._load_locales()

    def _load_locales(self):
        for filename in os.listdir(self.path):
            if filename.endswith('.yaml') or filename.endswith('.yml'):
                locale = os.path.splitext(filename)[0]
                file_path = os.path.join(self.path, filename)
                with open(file_path, encoding='utf-8') as f:
                    self._cache[locale] = yaml.safe_load(f)

    def find_locales(self):
        return list(self._cache.keys())

    def get(self, key: str, locale: Optional[str] = None, /, **kwargs) -> str:
        effective_locale = locale or self.default_locale
        translations = self._cache.get(effective_locale)
        if translations is None:
            # if no locale is specified, we use translations from the default locale
            translations = self._cache.get(self.default_locale, {})

        text = translations.get(key, key)
        try:
            text = text.format(**kwargs)
        except Exception:
            pass
        return text

# full project in: https://github.com/klaymov/aiogram_i18n-yaml_core
