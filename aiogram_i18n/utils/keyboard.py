from typing import Union

from aiogram.types import (
    KeyboardButton as _KeyboardButton,
    InlineKeyboardButton as _InlineKeyboardButton
)

from aiogram_i18n import LazyProxy


class KeyboardButton(_KeyboardButton):
    text: Union[str, LazyProxy]  # type: ignore[assignment]

    class Config:
        arbitrary_types_allowed = True


class InlineKeyboardButton(_InlineKeyboardButton):
    text: Union[str, LazyProxy]  # type: ignore[assignment]

    class Config:
        arbitrary_types_allowed = True
