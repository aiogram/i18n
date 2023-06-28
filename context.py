from contextlib import asynccontextmanager
from typing import Dict, Any, AsyncIterator

from aiogram.utils.mixins import ContextInstanceMixin

from cores.base import BaseCore
from managers.base import BaseManager


class I18nContext(ContextInstanceMixin["I18nContext"]):
    locale: str
    core: BaseCore
    manager: BaseManager
    data: Dict[str, Any]

    def __init__(self, locale: str, core: BaseCore, manager: BaseManager, data: Dict[str, Any]):
        self.locale = locale
        self.core = core
        self.manager = manager
        self.data = data

    def get(self, key: str, **kwargs):
        return self.core.get(locale=self.locale, key=key, **kwargs)

    async def set_locale(self, locale: str):
        await self.manager.set_locale(
            locale=locale,
            core=self.core,
            manager=self.manager,
            data=self.data
        )
        self.locale = locale
