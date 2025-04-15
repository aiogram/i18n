from pathlib import Path
import yaml
from typing import Optional

from aiogram_i18n.cores.base import BaseCore


class I18nYamlCore(BaseCore):
    def __init__(self, path: str, default_locale: str = 'en'):
        """
        :param path: directory with YAML files with translations
        """
        self.path = Path(path)
        super().__init__(path=path, default_locale=default_locale)
        self._cache = {}
        self._load_locales()

    def _load_locales(self):
        for pattern in ("*.yaml", "*.yml"):
            for file in self.path.glob(pattern):
                locale = file.stem
                with file.open(encoding='utf-8') as f:
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
