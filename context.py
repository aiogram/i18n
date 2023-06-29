from __future__ import annotations

from typing import Dict, Any

from aiogram.utils.mixins import ContextInstanceMixin

from cores.base import BaseCore
from managers.base import BaseManager


class I18nContext(ContextInstanceMixin["I18nContext"]):
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

    async def set_locale(self, locale: str) -> None:
        await self.manager.set_locale(
            locale=locale,
            core=self.core,
            manager=self.manager,
            data=self.data
        )
        self.locale = locale
