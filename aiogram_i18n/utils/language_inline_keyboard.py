from typing import Any

from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from aiogram_i18n import I18nContext
from aiogram_i18n.lazy.base import BaseLazyFilter

INLINE_MARKUP = list[list[InlineKeyboardButton]]


class LanguageCallbackFilter(BaseLazyFilter):
    keyboard: "LanguageInlineMarkup"
    slice: slice

    def __init__(self, keyboard: "LanguageInlineMarkup"):
        self.keyboard = keyboard
        self.slice = slice(len(keyboard.prefix), None)

    async def startup(self, i18n: I18nContext) -> None:
        await self.keyboard.startup(i18n=i18n)

    async def __call__(self, callback: CallbackQuery) -> bool | dict[str, Any]:
        if not callback.data or not callback.data.startswith(self.keyboard.prefix):
            return False
        return {self.keyboard.param: callback.data[self.slice]}


class LanguageInlineMarkup:
    def __init__(
        self,
        key: str,
        row: int = 3,
        hide_current: bool = False,
        prefix: str = "__lang__",
        param: str = "lang",
        keyboard: INLINE_MARKUP | None = None,
    ):
        self.key = key
        self.row = row
        self.hide_current = hide_current
        self.prefix = prefix
        self.param = param
        self.filter = LanguageCallbackFilter(keyboard=self)
        self.keyboards: dict[str, INLINE_MARKUP] = {}
        self.keyboard: INLINE_MARKUP | None = keyboard or []

    def reply_markup(self, locale: str | None = None) -> InlineKeyboardMarkup:
        if locale is None:
            locale = I18nContext.get_current(no_error=False).locale
        return InlineKeyboardMarkup(inline_keyboard=self.keyboards.get(locale) or [])

    async def startup(self, i18n: I18nContext) -> None:
        if self.keyboards:
            self.keyboards.clear()
        for locale in i18n.core.available_locales:
            button = InlineKeyboardButton(
                text=i18n.core.get(self.key, locale),
                callback_data=f"{self.prefix}{locale}",
            )
            for _locale in i18n.core.available_locales:
                if self.hide_current and locale == _locale:
                    continue

                if _locale not in self.keyboards:
                    self.keyboards[_locale] = [[]]

                if len(self.keyboards[_locale][-1]) == self.row:
                    self.keyboards[_locale].append([])

                self.keyboards[_locale][-1].append(button)
        if not self.keyboard:
            return
        for keyboard in self.keyboards.values():
            keyboard.extend(self.keyboard)
