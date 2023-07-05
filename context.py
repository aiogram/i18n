from __future__ import annotations

from contextlib import contextmanager
from functools import partial
from typing import Dict, Any, Callable, Generator

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
        separator: str = "-",
    ) -> None:
        self.locale = locale
        self.core = core
        self.manager = manager
        self.data = data
        self.separator = separator

    def get(self, key: str, /, **kwargs: Any) -> str:
        return self.core.get(self.locale, key, **kwargs)

    @contextmanager
    def use_locale(self, locale: str) -> Generator[None, None, None]:
        root_locale = self.locale
        self.locale = locale
        try:
            yield
        finally:
            self.locale = root_locale

    def __getattr__(self, item: str) -> Callable[..., str]:
        return partial(self.get, item.replace("_", self.separator))

    async def set_locale(self, locale: str) -> None:
        await self.manager.set_locale(
            locale=locale,
            core=self.core,
            manager=self.manager,
            data=self.data
        )
        self.locale = locale
