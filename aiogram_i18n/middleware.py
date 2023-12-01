from typing import Any, Awaitable, Callable, Dict, Optional

from aiogram import BaseMiddleware, Dispatcher
from aiogram.types import TelegramObject

from aiogram_i18n.context import I18nContext
from aiogram_i18n.cores.base import BaseCore
from aiogram_i18n.managers.base import BaseManager
from aiogram_i18n.managers.memory import MemoryManager


class I18nMiddleware(BaseMiddleware):
    core: BaseCore[Any]
    manager: BaseManager
    context_key: str
    locale_key: Optional[str]
    middleware_key: str
    key_separator: str
    with_context: bool

    def __init__(
        self,
        core: BaseCore[Any],
        manager: Optional[BaseManager] = None,
        context_key: str = "i18n",
        locale_key: Optional[str] = None,
        middleware_key: str = "i18n_middleware",
        default_locale: str = "en",
        key_separator: str = "-",
    ) -> None:
        self.core = core
        self.manager = manager or MemoryManager()
        self.context_key = context_key
        self.locale_key = locale_key
        self.middleware_key = middleware_key
        self.key_separator = key_separator

        if self.core.default_locale is None:
            self.core.default_locale = default_locale
        if self.manager.default_locale is None:
            self.manager.default_locale = default_locale

    def setup(self, dispatcher: Dispatcher) -> None:
        dispatcher.update.outer_middleware.register(self)
        dispatcher.startup.register(self.core.startup)
        dispatcher.shutdown.register(self.core.shutdown)
        dispatcher.startup.register(self.manager.startup)
        dispatcher.shutdown.register(self.manager.shutdown)

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        locale = await self.manager.locale_getter(event=event, **data)
        data[self.context_key] = context = I18nContext(
            locale=locale,
            core=self.core,
            manager=self.manager,
            data=data,
            key_separator=self.key_separator,
        )
        if self.locale_key is not None:
            data[self.locale_key] = locale
        data[self.middleware_key] = self

        I18nContext.set_current(context)
        return await handler(event, data)
