from collections import UserString
from typing import Any, Union, Dict, Optional

from aiogram.types import TelegramObject, Message
from magic_filter import MagicFilter

from context import I18nContext


def extract_text(event: TelegramObject) -> Optional[str]:
    if isinstance(event, Message):
        return event.text or event.caption
    return None


class LazyProxy(UserString):
    magic: Optional[MagicFilter]
    key: str
    kwargs: Dict[str, Any]

    def __init__(  # noqa
        self, key: str, magic: Optional[MagicFilter] = None,
        **kwargs: Dict[str, Any]
    ) -> None:
        self.magic = magic
        self.key = key
        self.kwargs = kwargs

    @property
    def data(self) -> str:
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
        return f"{self.__class__.__name__}<'{self.key}'>"
