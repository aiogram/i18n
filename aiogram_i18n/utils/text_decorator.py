from aiogram import Bot
from aiogram.utils.text_decorations import TextDecoration as TextD, html_decoration, markdown_decoration
from aiogram_i18n.context import I18nContext
from typing import Optional, Dict, Callable, Any, Literal


class Null:
    def __getattr__(self, item) -> Callable[[str], str]:
        return self.__call__

    def __call__(self, value: str, *args, **kwargs) -> str:
        return value


class TextDecoration:
    def __init__(self):
        self.decorations = {
            "html": html_decoration,
            "markdown": markdown_decoration,
            None: Null()
        }

    @property
    def functions(self) -> Dict[str, Callable[..., Any]]:
        return {
            "LINK": self.link,
            "BOLD": self.bold,
            "ITALIC": self.italic,
            "CODE": self.code,
            "PRE": self.pre,
            "PRE_LANGUAGE": self.pre_language,
            "UNDERLINE": self.underline,
            "STRIKETHROUGH": self.strikethrough,
            "SPOILER": self.spoiler,
            "QUOTE": self.quote,
            "CUSTOM_EMOJI": self.custom_emoji,
        }

    @property
    def i18n(self) -> I18nContext:
        context = I18nContext.get_current()
        if context:
            return context
        raise Exception

    @property
    def bot(self) -> Bot:
        return self.i18n.data["bot"]

    def get_decoration(self, parse_mode: Optional[str] = None) -> TextD:
        parse_mode = parse_mode or self.i18n.context.get("parse_mode") or self.bot.parse_mode
        return self.decorations[parse_mode.lower().strip()]

    def link(self, value: str, link: str, parse_mode: Optional[str] = None) -> str:
        return self.get_decoration(parse_mode=parse_mode).link(value, link)

    def bold(self, value: str, parse_mode: Optional[str] = None) -> str:
        return self.get_decoration(parse_mode=parse_mode).bold(value)

    def italic(self, value: str, parse_mode: Optional[str] = None) -> str:
        return self.get_decoration(parse_mode=parse_mode).italic(value)

    def code(self, value: str, parse_mode: Optional[str] = None) -> str:
        return self.get_decoration(parse_mode=parse_mode).code(value)

    def pre(self, value: str, parse_mode: Optional[str] = None) -> str:
        return self.get_decoration(parse_mode=parse_mode).pre(value)

    def pre_language(self, value: str, language: str, parse_mode: Optional[str] = None) -> str:
        return self.get_decoration(parse_mode=parse_mode).pre_language(value, language)

    def underline(self, value: str, parse_mode: Optional[str] = None) -> str:
        return self.get_decoration(parse_mode=parse_mode).underline(value)

    def strikethrough(self, value: str, parse_mode: Optional[str] = None) -> str:
        return self.get_decoration(parse_mode=parse_mode).strikethrough(value)

    def spoiler(self, value: str, parse_mode: Optional[str] = None) -> str:
        return self.get_decoration(parse_mode=parse_mode).spoiler(value)

    def quote(self, value: str, parse_mode: Optional[str] = None) -> str:
        return self.get_decoration(parse_mode=parse_mode).quote(value)

    def custom_emoji(self, value: str, custom_emoji_id: str, parse_mode: Optional[str] = None) -> str:
        return self.get_decoration(parse_mode=parse_mode).custom_emoji(value, custom_emoji_id)


td = TextDecoration()
