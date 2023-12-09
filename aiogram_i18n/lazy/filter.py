from typing import Any, Union, Dict, Optional, Tuple, TYPE_CHECKING

from aiogram.types import Message

from aiogram_i18n.lazy.base import BaseLazyFilter

if TYPE_CHECKING:
    from aiogram_i18n import I18nMiddleware


class LazyFilter(BaseLazyFilter):
    keys: Tuple[str, ...]
    all_keys: Optional[Tuple[str]]

    def __init__(self, *keys: str):
        self.keys = keys
        self.all_keys = None

    async def startup(self, middleware: "I18nMiddleware"):
        self.all_keys = tuple(
            middleware.core.get(key, locale)
            for locale in middleware.core.available_locales
            for key in self.keys
        )

    async def __call__(self, message: Message) -> Union[bool, Dict[str, Any]]:
        return message.text in self.all_keys
