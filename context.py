from __future__ import annotations

from functools import partial
from typing import Dict, Any, Callable

from aiogram.utils.mixins import ContextInstanceMixin

from cores.base import BaseCore
from lazy_proxy import LazyProxy
from managers.base import BaseManager


class I18nMeta(type):
    def __getattr__(self, item: str) -> Callable[..., LazyProxy]:
        return partial(LazyProxy, item)


class I18n(ContextInstanceMixin["I18n"], metaclass=I18nMeta):
    locale: str
    core: BaseCore[Any]
    manager: BaseManager
    data: Dict[str, Any]

    def __init__(
        self,
        locale: str, core: BaseCore[Any],
        manager: BaseManager, data: Dict[str, Any],
    ) -> None:
        self.locale = locale
        self.core = core
        self.manager = manager
        self.data = data

    def get(self, key: str, **kwargs: Any) -> str:
        return self.core.get(self.locale, key, **kwargs)

    def __getattr__(self, item: str) -> Callable[..., str]:
        return partial(self.get, item)

    async def set_locale(self, locale: str) -> None:
        await self.manager.set_locale(
            locale=locale,
            core=self.core,
            manager=self.manager,
            data=self.data
        )
        self.locale = locale
