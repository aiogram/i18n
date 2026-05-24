# aiogram_i18n

[![PyPI version](https://img.shields.io/pypi/v/aiogram-i18n.svg)](https://pypi.org/project/aiogram-i18n/)
[![Python versions](https://img.shields.io/pypi/pyversions/aiogram-i18n.svg)](https://pypi.org/project/aiogram-i18n/)
[![License](https://img.shields.io/pypi/l/aiogram-i18n.svg)](https://pypi.org/project/aiogram-i18n/)
[![Downloads](https://img.shields.io/pypi/dm/aiogram-i18n.svg)](https://pypi.org/project/aiogram-i18n/)
[![Documentation](https://readthedocs.org/projects/aiogram-i18n/badge/?version=latest)](https://aiogram-i18n.readthedocs.io/)

Internationalization middleware for [aiogram](https://github.com/aiogram/aiogram).

`aiogram_i18n` adds locale-aware translation contexts to handlers, supports lazy translated
values in filters and keyboards, and lets you choose between Fluent and GNU gettext backends.

## Features

- Middleware for aiogram 3 routers and dispatchers.
- Fluent backends powered by `fluent.runtime` or `fluent-compiler`.
- GNU gettext backend for compiled `.mo` catalogs.
- Lazy translation proxies for buttons, filters, and other delayed values.
- Locale managers for memory, FSM, Redis, constants, and custom storage.
- Stub generation for gettext catalogs (`.po`, `.pot`, `.mo`).

## Installation

Install the base package:

```bash
pip install aiogram-i18n
```

Choose a backend:

```bash
# Fluent with fluent-compiler
pip install "aiogram-i18n[compiler]"

# Fluent with fluent.runtime
pip install "aiogram-i18n[runtime]"

# GNU gettext uses Python's stdlib gettext module
pip install aiogram-i18n
```

## Quick Start

Create Fluent locale files:

```text
locales/
  en/
    LC_MESSAGES/
      bot.ftl
  uk/
    LC_MESSAGES/
      bot.ftl
```

Example `locales/en/LC_MESSAGES/bot.ftl`:

```ftl
hello = Hello, <b>{ $user }</b>!
help = Help
```

Use the middleware in your bot:

```python
import asyncio
from contextlib import suppress
from logging import INFO, basicConfig
from typing import Any

from aiogram import Bot, Dispatcher, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from aiogram_i18n import I18nContext, I18nMiddleware, LazyProxy
from aiogram_i18n.cores import FluentRuntimeCore
from aiogram_i18n.lazy.filter import LazyFilter
from aiogram_i18n.types import KeyboardButton, ReplyKeyboardMarkup

router = Router(name=__name__)

keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text=LazyProxy("help"))]],
    resize_keyboard=True,
)


@router.message(CommandStart())
async def cmd_start(message: Message, i18n: I18nContext) -> Any:
    name = message.from_user.mention_html()
    return message.answer(
        text=i18n.get("hello", user=name),
        reply_markup=keyboard,
    )


@router.message(LazyFilter("help"))
async def cmd_help(message: Message) -> Any:
    return message.answer(text=message.text)


async def main() -> None:
    basicConfig(level=INFO)

    bot = Bot("42:ABC", default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.include_router(router)

    i18n = I18nMiddleware(
        core=FluentRuntimeCore(path="locales/{locale}/LC_MESSAGES"),
        default_locale="en",
    )
    i18n.setup(dispatcher=dp)

    await dp.start_polling(bot)


if __name__ == "__main__":
    with suppress(KeyboardInterrupt):
        asyncio.run(main())
```

## Translation Access

Handlers can receive `I18nContext` through aiogram dependency injection:

```python
@router.message(CommandStart())
async def handler(message: Message, i18n: I18nContext) -> None:
    await message.answer(i18n.get("hello", user=message.from_user.full_name))
```

You can also use attribute-style keys. The default separator is `-`, so
`i18n.profile.title()` resolves `profile-title`.

```python
text = i18n.profile.title(user="Andrew")
```

For lazy values, use `LazyProxy` or the built-in factory:

```python
from aiogram_i18n import L, LazyProxy

LazyProxy("help")
L.profile.title(user="Andrew")
```

Lazy values are useful in filters, keyboards, and objects that are rendered after the locale is
known. Import mutable aiogram types from `aiogram_i18n.types` when they contain lazy values.

## Backends

### FluentRuntimeCore

Runtime Fluent backend based on `fluent.runtime`.

```python
from aiogram_i18n.cores import FluentRuntimeCore

core = FluentRuntimeCore(path="locales/{locale}/LC_MESSAGES")
```

Install it with:

```bash
pip install "aiogram-i18n[runtime]"
```

### FluentCompileCore

Compiled Fluent backend based on `fluent-compiler`.

```python
from aiogram_i18n.cores import FluentCompileCore

core = FluentCompileCore(path="locales/{locale}/LC_MESSAGES")
```

Install it with:

```bash
pip install "aiogram-i18n[compiler]"
```

### GNUTextCore

GNU gettext backend for `.mo` files.

```python
from aiogram_i18n.cores import GNUTextCore

core = GNUTextCore(path="locales/{locale}/LC_MESSAGES")
```

Expected layout:

```text
locales/
  en/
    LC_MESSAGES/
      bot.mo
```

## Locale Management

The middleware stores and reads the current locale through a manager. By default it uses
`MemoryManager`.

```python
i18n = I18nMiddleware(
    core=FluentRuntimeCore(path="locales/{locale}/LC_MESSAGES"),
    default_locale="en",
)
```

To persist locales elsewhere, pass another manager:

```python
from aiogram_i18n.managers import FSMManager

i18n = I18nMiddleware(
    core=FluentRuntimeCore(path="locales/{locale}/LC_MESSAGES"),
    manager=FSMManager(),
)
```

## CLI

The package exposes an `i18n` command.

Generate Python stubs from gettext catalogs:

```bash
i18n stub -i locales/en/LC_MESSAGES/bot.po -o stubs/i18n.pyi
```

Supported stub inputs are `.po`, `.pot`, and `.mo`. The parser uses `polib`, so install it if your
environment does not already provide it:

```bash
pip install polib
```

FTL extraction and FTL stub generation are handled by
[FTL-Extract](https://pypi.org/project/FTL-Extract/):

```bash
pip install ftl-extract
```

## Documentation

Full documentation is available at
[aiogram-i18n.readthedocs.io](https://aiogram-i18n.readthedocs.io/).

## License

`aiogram_i18n` is distributed under the MIT license.
