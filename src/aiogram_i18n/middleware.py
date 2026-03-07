from __future__ import annotations

from contextlib import contextmanager
from typing import TYPE_CHECKING, Any, cast
from warnings import warn

from aiogram import BaseMiddleware, Dispatcher

from aiogram_i18n.context import I18nContext
from aiogram_i18n.lazy.base import BaseLazyFilter
from aiogram_i18n.managers.base import BaseManager, CallableMixin  # type: ignore[attr-defined]
from aiogram_i18n.managers.memory import MemoryManager
from aiogram_i18n.utils.context_instance import ContextInstanceMixin

if TYPE_CHECKING:
    from collections.abc import Awaitable, Callable, Generator

    from aiogram.types import TelegramObject

    from aiogram_i18n.cores.base import BaseCore
    from aiogram_i18n.types import StartupFunction


class I18nMiddleware(BaseMiddleware, ContextInstanceMixin["I18nMiddleware"]):
    core: BaseCore[Any]
    manager: BaseManager
    context_key: str
    locale_key: str | None
    middleware_key: str
    key_separator: str
    with_context: bool
    enabled_startup: bool

    def __init__(
        self,
        core: BaseCore[Any],
        manager: BaseManager | None = None,
        context_key: str = "i18n",
        locale_key: str | None = None,
        middleware_key: str = "i18n_middleware",
        default_locale: str = "en",
        key_separator: str = "-",
        enabled_startup: bool = True,
    ) -> None:
        self.core = core
        self.manager = manager or MemoryManager()
        self.context_key = context_key
        self.locale_key = locale_key
        self.middleware_key = middleware_key
        self.key_separator = key_separator
        self.enabled_startup = enabled_startup

        if self.core.default_locale is None:
            self.core.default_locale = default_locale
        if self.manager.default_locale is None:
            self.manager.default_locale = default_locale
        I18nMiddleware.set_current(self)
        if locale_key:
            warn("parameter locale_key deprecated since version 2.0", stacklevel=2)
        self._startup: list[CallableMixin] = []

    def on_startup(self, func: StartupFunction) -> StartupFunction:
        self._startup.append(CallableMixin(callback=func))
        return func

    def setup(self, dispatcher: Dispatcher) -> None:
        dispatcher.update.outer_middleware.register(self)
        dispatcher.startup.register(self.core.startup)
        dispatcher.shutdown.register(self.core.shutdown)
        dispatcher.startup.register(self.manager.startup)
        dispatcher.shutdown.register(self.manager.shutdown)
        if self.enabled_startup:
            dispatcher.startup.register(self.startup)
        dispatcher[self.middleware_key] = self

    async def startup(self, dispatcher: Dispatcher, **kwargs) -> None:  # type: ignore[no-untyped-def]
        kwargs["dispatcher"] = dispatcher
        with self.use_context(data=kwargs):
            for startup_func in self._startup:
                await startup_func.call(**kwargs)
            for sub_router in dispatcher.chain_tail:
                for observer in sub_router.observers.values():
                    for handler in observer.handlers:
                        if not handler.filters:
                            continue
                        for filter_ in handler.filters:
                            if not isinstance(filter_.callback, BaseLazyFilter):
                                continue
                            await filter_.callback.call(self.context_key, **kwargs)

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        locale = await self.manager.locale_getter(event=event, **data)
        if self.locale_key is not None:
            data[self.locale_key] = locale

        with self.use_context(locale=locale, data=data):
            return await handler(event, data)

    @contextmanager
    def use_context(
        self,
        locale: str | None = None,
        data: dict[str, Any] | None = None,
    ) -> Generator[I18nContext, None, None]:
        if data is None:
            data = dict()  # noqa: C408

        with I18nContext.with_current(
            self.new_context(
                locale=cast(str, locale or self.core.default_locale),
                data=data,
            )
        ) as context:
            data[self.context_key] = context
            yield context

    def new_context(self, locale: str, data: dict[str, Any]) -> I18nContext:
        return I18nContext(
            locale=locale,
            core=self.core,
            manager=self.manager,
            data=data,
            key_separator=self.key_separator,
        )
