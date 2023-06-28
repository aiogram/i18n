# aiogram_i18n

FluentCompileCore:
```pip install fluent_compiler```

FluentRuntimeCore:
```pip install fluent.runtime```

BabelCore:
```pip install Babel```


```python
from cores.fluent_runtime_core import FluentRuntimeCore
from lazy_proxy import LazyProxy
from middleware import I18nMiddleware
from context import I18nContext


mw = I18nMiddleware(
    core=FluentRuntimeCore(
        path="locales/{locale}/LC_MESSAGES"
    )
)


@router.message(CommandStart())
async def cmd_start(message: types.Message, i18n: I18nContext):
    await message.reply(
        text=i18n.get('hello', user=message.from_user.full_name),
        reply_markup=ikb
    )


@router.message(F.text == LazyProxy(key="help"))
async def cmd_help(message: types.Message):
    await message.reply(text=">> " + message.text + " <<")

async def main():
    dp = Dispatcher()
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    dp.include_router(router)
    mw.setup(dispatcher=dp)
    await dp.start_polling(bot)


run(main())

```
