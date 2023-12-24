from contextlib import contextmanager
from typing import Any, Awaitable, Callable, Dict, Optional, Generator
from warnings import warn

from aiogram import BaseMiddleware, Dispatcher
from aiogram.types import TelegramObject

from aiogram_i18n.context import I18nContext
from aiogram_i18n.cores.base import BaseCore
from aiogram_i18n.lazy.base import BaseLazyFilter
from aiogram_i18n.managers.base import BaseManager
from aiogram_i18n.managers.memory import MemoryManager
from aiogram_i18n.utils.context_instance import ContextInstanceMixin


class I18nMiddleware(BaseMiddleware, ContextInstanceMixin["I18nMiddleware"]):
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
        I18nMiddleware.set_current(self)
        if locale_key:
            warn("parameter locale_key deprecated since version 2.0")

    def setup(self, dispatcher: Dispatcher) -> None:
        dispatcher.update.outer_middleware.register(self)
        dispatcher.startup.register(self.core.startup)
        dispatcher.shutdown.register(self.core.shutdown)
        dispatcher.startup.register(self.manager.startup)
        dispatcher.shutdown.register(self.manager.shutdown)
        dispatcher.startup.register(self.startup)
        dispatcher[self.middleware_key] = self

    async def startup(self, dispatcher: Dispatcher):
        for sub_router in dispatcher.chain_tail:
            for observ in sub_router.observers.values():
                for handler in observ.handlers:
                    if handler.filters:
                        for filter_ in handler.filters:
                            if isinstance(filter_.callback, BaseLazyFilter):
                                await filter_.callback.startup(middleware=self)

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        locale = await self.manager.locale_getter(event=event, **data)
        if self.locale_key is not None:
            data[self.locale_key] = locale

        with self.use_context(locale=locale, data=data):
            return await handler(event, data)

    @contextmanager
    def use_context(
        self,
        locale: Optional[str] = None,
        data: Optional[Dict[str, Any]] = None,
        /,
        **kwargs
    ) -> Generator[I18nContext, None, None]:
        if data:
            kwargs.update(data)

        with I18nContext.with_current(
            self.new_context(
                locale=locale or self.core.default_locale,
                data=kwargs,
            )
        ) as context:
            data[self.context_key] = context
            yield context

    def new_context(self, locale: str, data: Dict[str, Any]) -> I18nContext:
        return I18nContext(
            locale=locale,
            core=self.core,
            manager=self.manager,
            data=data,
            key_separator=self.key_separator,
        )
