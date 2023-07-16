from contextlib import contextmanager
from functools import partial
from typing import Dict, Any, Generator, Callable

from aiogram.utils.mixins import ContextInstanceMixin

from aiogram_i18n.cores.base import BaseCore
from aiogram_i18n.managers.base import BaseManager


class I18nContext(ContextInstanceMixin["I18nContext"]):
    locale: str
    core: BaseCore[Any]
    manager: BaseManager
    data: Dict[str, Any]
    key_separator: str

    def __init__(
        self,
        locale: str, core: BaseCore[Any],
        manager: BaseManager, data: Dict[str, Any],
        key_separator: str = "-"
    ) -> None:
        self.locale = locale
        self.core = core
        self.manager = manager
        self.data = data
        self.key_separator = key_separator

    def get(self, key: str, /, **kwargs: Any) -> str:
        return self.core.get(key, locale=self.locale, **kwargs)

    async def set_locale(self, locale: str, **kwargs: Any) -> None:
        await self.manager.set_locale_mixin.call(
            locale,
            core=self.core,
            manager=self.manager,
            **self.data, **kwargs
        )
        self.locale = locale

    def __getattr__(self, item: str) -> Callable[..., str]:
        return partial(self.get, item.replace("_", self.key_separator))

    @contextmanager
    def use_locale(self, locale: str) -> Generator["I18nContext", None, None]:
        old_locale = self.locale
        self.locale = locale
        try:
            yield self
        finally:
            self.locale = old_locale
