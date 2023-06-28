from collections import UserString
from typing import Callable, Dict, Any, Awaitable, Optional, Tuple
from json import dumps, JSONEncoder
from aiogram import Dispatcher, BaseMiddleware, Bot
from aiogram.types import TelegramObject
from cores.base import BaseCore
from managers.base import BaseManager
from managers.fsm_manager import FsmManager
from context import I18nContext


def default(default_dump: Callable):
    def serialize_lazy(obj):
        if isinstance(obj, UserString):
            return obj.data
        return default_dump(obj)

    return serialize_lazy


def on_startup(bots: Tuple[Bot]):
    def_enc = JSONEncoder(default=default(dumps))
    for bot in bots:
        if bot.session.json_dumps is dumps:
            bot.session.json_dumps = def_enc.encode
        else:
            bot.session.json_dumps = default(bot.session.json_dumps)


class I18nMiddleware(BaseMiddleware):
    context_key: str
    middleware_key: str = "i18n_middleware"
    locale_key: str
    core: BaseCore
    manager: BaseManager
    default_locale: str

    def __init__(
            self, core: BaseCore,
            manager: Optional[BaseManager] = None,
            context_key: str = "i18n",
            locale_key: str = "locale",
            default_locale: str = "en",
    ):
        self.core = core
        if manager is None:
            manager = FsmManager(default_locale=default_locale, key=locale_key)
        self.manager = manager
        self.context_key = context_key
        self.locale_key = locale_key
        self.default_locale = default_locale

    def setup(self, dispatcher: Dispatcher):
        dispatcher.update.outer_middleware.register(self)
        dispatcher.startup.register(self.core.startup)
        dispatcher.shutdown.register(self.core.shutdown)
        dispatcher.startup.register(on_startup)

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]) -> Any:
        locale = await self.manager.get_locale(event=event, data=data)

        data[self.context_key] = I18nContext(
            locale=locale,
            core=self.core,
            manager=self.manager,
            data=data
        )
        data[self.locale_key] = locale
        data[self.middleware_key] = self

        token = I18nContext.set_current(data[self.context_key])
        try:
            return await handler(event, data)
        finally:
            I18nContext.reset_current(token)
