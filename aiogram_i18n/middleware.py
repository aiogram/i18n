from typing import Callable, Dict, Any, Awaitable, Optional

from aiogram import Dispatcher, BaseMiddleware
from aiogram.types import TelegramObject

from aiogram_i18n.context import I18nContext
from aiogram_i18n.cores.base import BaseCore
from aiogram_i18n.managers.base import BaseManager
from aiogram_i18n.managers.fsm import FSMManager


class I18nMiddleware(BaseMiddleware):
    core: BaseCore[Any]
    manager: BaseManager
    context_key: str
    locale_key: str
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
        with_context: bool = True
    ) -> None:
        self.core = core
        self.manager = manager or FSMManager(key=locale_key)
        self.context_key = context_key
        self.locale_key = locale_key
        self.middleware_key = middleware_key
        self.key_separator = key_separator
        self.with_context = with_context

        if self.core.default_locale is None:
            self.core.default_locale = default_locale
        if self.manager.default_locale is None:
            self.manager.default_locale = default_locale

    def setup(self, dispatcher: Dispatcher) -> None:
        dispatcher.update.outer_middleware.register(self)
        dispatcher.startup.register(self.core.startup)
        dispatcher.shutdown.register(self.core.shutdown)

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        locale = await self.manager.get_locale(event=event, data=data)
        data[self.context_key] = context = I18nContext(
            locale=locale,
            core=self.core,
            manager=self.manager,
            data=data,
            key_separator=self.key_separator
        )
        if self.locale_key is not None:
            data[self.locale_key] = locale
        data[self.middleware_key] = self

        if self.with_context:
            I18nContext.set_current(context)
        return await handler(event, data)
