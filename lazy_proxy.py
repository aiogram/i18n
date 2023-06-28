from collections import UserString
from typing import Any, Union, Dict, Callable, Sequence
from magic_filter import MagicFilter
from aiogram.types import TelegramObject, Message
from string import Template
from context import I18nContext


def extract_text(event: TelegramObject):
    if isinstance(event, Message):
        return event.text or event.caption


class LazyProxy(UserString):
    magic: MagicFilter
    key: str
    kwargs: Dict[str, Any]

    def __init__(self, key: str, magic: MagicFilter = None, **kwargs: Dict[str, Any]):  # noqa
        self.magic = magic
        self.key = key
        self.kwargs = kwargs

    @property
    def data(self):
        context = I18nContext.get_current()
        if context:
            return context.get(key=self.key, **self.kwargs)
        return self.__repr__()

    async def __call__(self, event: TelegramObject) -> Union[bool, Dict[str, Any]]:
        if self.magic is None:
            raise ValueError
        text = self.magic(event)
        return text == self.data

    def __str__(self):
        return self.data

    def __repr__(self):
        return f"{self.__class__.__name__}<{self.data}>"
