from typing import Any, Dict, Tuple, Union

from aiogram.types import Message

from aiogram_i18n import I18nContext
from aiogram_i18n.lazy.base import BaseLazyFilter


class LazyFilter(BaseLazyFilter):
    keys: Tuple[str, ...]
    all_keys: Tuple[str, ...]

    def __init__(self, *keys: str):
        self.keys = keys
        self.all_keys = ()

    async def startup(self, i18n: I18nContext) -> None:
        self.all_keys = tuple(
            i18n.core.get(key, locale)
            for locale in i18n.core.available_locales
            for key in self.keys
        )

    async def __call__(self, message: Message) -> Union[bool, Dict[str, Any]]:
        return message.text in self.all_keys
