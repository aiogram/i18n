# aiogram_i18n

FluentCompileCore:
```pip install fluent_compiler```

FluentRuntimeCore:
```pip install fluent.runtime```

BabelCore:
```pip install Babel```

```python
import asyncio
from contextlib import suppress
from logging import basicConfig, INFO
from typing import Any

from aiogram import Router, Dispatcher, F, Bot
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, Message

from context import I18n
from cores.fluent_runtime_core import FluentRuntimeCore
from lazy_proxy import LazyProxy
from middleware import I18nMiddleware
from utils.keyboard import KeyboardButton  # you should import the keyboard from here if you want to use LazyProxy

router = Router(name=__name__)
rkb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=LazyProxy(key="help"))]  # or I18n.help()
    ], resize_keyboard=True
)


@router.message(CommandStart())
async def cmd_start(message: Message, i18n: I18n) -> Any:
    name = message.from_user.mention_html()
    return message.reply(
        text=i18n.hello(user=name),  # aka i18n.get("hello", user=name)
        reply_markup=rkb
    )


@router.message(F.text == I18n.help())
async def cmd_help(message: Message) -> Any:
    return message.reply(text="-- " + message.text + " --")


async def main() -> None:
    basicConfig(level=INFO)
    bot = Bot("42:ABC", parse_mode=ParseMode.HTML)
    i18n = I18nMiddleware(
        core=FluentRuntimeCore(
            path="locales/{locale}/LC_MESSAGES"
        )
    )

    dp = Dispatcher()
    dp.include_router(router)
    i18n.setup(dispatcher=dp)

    await dp.start_polling(bot)


if __name__ == "__main__":
    with suppress(KeyboardInterrupt):
        asyncio.run(main())
```
