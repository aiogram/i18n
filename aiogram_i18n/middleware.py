from collections import UserString
from json import dumps, JSONEncoder
from typing import Callable, Dict, Any, Awaitable, Optional, Sequence

from aiogram import Dispatcher, BaseMiddleware, Bot
from aiogram.types import TelegramObject

from aiogram_i18n.context import I18nContext
from aiogram_i18n.cores.base import BaseCore
from aiogram_i18n.managers.base import BaseManager
from aiogram_i18n.managers.fsm import FSMManager


def default(default_dump: Callable[..., str]) -> Callable[..., str]:
    def serialize_lazy(obj: Any) -> str:
        if isinstance(obj, UserString):
            return obj.data
        return default_dump(obj)

    return serialize_lazy


def on_startup(bots: Sequence[Bot]) -> None:
    def_enc = JSONEncoder(default=default(dumps))
    for bot in bots:
        if bot.session.json_dumps is dumps:
            bot.session.json_dumps = def_enc.encode
        else:
            bot.session.json_dumps = default(bot.session.json_dumps)


class I18nMiddleware(BaseMiddleware):
    core: BaseCore[Any]
    manager: BaseManager
    context_key: str
    locale_key: str
    middleware_key: str
    default_locale: str
    key_sep: str

    def __init__(
        self,
        core: BaseCore[Any],
        manager: Optional[BaseManager] = None,
        context_key: str = "i18n",
        locale_key: str = "locale",
        middleware_key: str = "i18n_middleware",
        default_locale: str = "en",
        key_sep: str = "-"
    ) -> None:
        self.core = core
        if manager is None:
            manager = FSMManager(default_locale=default_locale, key=locale_key)
        self.manager = manager
        self.context_key = context_key
        self.locale_key = locale_key
        self.middleware_key = middleware_key
        self.default_locale = default_locale
        self.key_sep = key_sep

    def setup(self, dispatcher: Dispatcher) -> None:
        dispatcher.update.outer_middleware.register(self)
        dispatcher.startup.register(self.core.startup)
        dispatcher.shutdown.register(self.core.shutdown)
        dispatcher.startup.register(on_startup)

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        locale = await self.manager.get_locale(event=event, data=data)

        data[self.context_key] = I18nContext(
            locale=locale,
            core=self.core,
            manager=self.manager,
            data=data,
            key_sep=self.key_sep
        )
        data[self.locale_key] = locale
        data[self.middleware_key] = self

        I18nContext.set_current(data[self.context_key])
        return await handler(event, data)
