from contextlib import contextmanager
from functools import partial
from typing import Dict, Any, Generator

from aiogram.utils.mixins import ContextInstanceMixin

from aiogram_i18n.cores.base import BaseCore
from aiogram_i18n.managers.base import BaseManager


class I18nContext(ContextInstanceMixin["I18nContext"]):
    locale: str
    core: BaseCore[Any]
    manager: BaseManager
    data: Dict[str, Any]
    key_sep: str

    def __init__(
            self,
            locale: str, core: BaseCore[Any],
            manager: BaseManager, data: Dict[str, Any],
            key_sep: str = "-"
    ) -> None:
        self.locale = locale
        self.core = core
        self.manager = manager
        self.data = data
        self.key_sep = key_sep

    def get(self, key: str, **kwargs: Any) -> str:
        return self.core.get(locale=self.locale, key=key, **kwargs)

    async def set_locale(self, locale: str) -> None:
        await self.manager.set_locale(
            locale=locale,
            core=self.core,
            manager=self.manager,
            data=self.data
        )
        self.locale = locale

    def __getattr__(self, item: str) -> partial:
        return partial(self.get, key=item.replace("_", self.key_sep))

    @contextmanager
    def with_locale(self, locale: str) -> Generator["I18nContext", None, None]:
        old_locale = self.locale
        self.locale = locale
        try:
            yield self
        finally:
            self.locale = old_locale
