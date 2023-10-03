from __future__ import annotations

from contextlib import contextmanager
from typing import TYPE_CHECKING, Any, Dict, Generator, Optional

from aiogram_i18n.managers.base import BaseManager
from aiogram_i18n.utils.context_instance import ContextInstanceMixin
from aiogram_i18n.utils.magic_proxy import MagicProxy

if TYPE_CHECKING:
    from aiogram_i18n.cores.base import BaseCore


class I18nContext(ContextInstanceMixin["I18nContext"]):
    locale: str
    core: BaseCore[Any]
    manager: BaseManager
    data: Dict[str, Any]
    key_separator: str
    context: Dict[str, Any]

    def __init__(
        self,
        locale: str,
        core: BaseCore[Any],
        manager: BaseManager,
        data: Dict[str, Any],
        key_separator: str = "-",
    ) -> None:
        self.locale = locale
        self.core = core
        self.manager = manager
        self.data = data
        self.key_separator = key_separator
        self.context = {}

    def get(self, key: str, locale: Optional[str] = None, /, **kwargs: Any) -> str:
        return self.core.get(key, locale or self.locale, **kwargs)

    __call__ = get

    def __getattr__(self, item: str) -> MagicProxy[str]:
        proxy = MagicProxy(self, key_separator=self.key_separator)
        return proxy.__getattr__(item)

    async def set_locale(self, locale: str, **kwargs: Any) -> None:
        kwargs.update(self.data, core=self.core)
        await self.manager.locale_setter(locale, **kwargs)
        self.locale = locale

    @contextmanager
    def use_locale(self, locale: str) -> Generator[I18nContext, None, None]:
        old_locale = self.locale
        self.locale = locale
        try:
            yield self
        finally:
            self.locale = old_locale

    @contextmanager
    def use_context(self, **kwargs: Any) -> Generator[I18nContext, None, None]:
        old_context = self.context
        self.context = kwargs
        try:
            yield self
        finally:
            self.context = old_context

    def set_context(self, **kwargs: Any) -> None:
        self.context = kwargs
