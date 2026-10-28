from __future__ import annotations

from datetime import datetime, timezone

import pytest
from aiogram import Dispatcher, Router
from aiogram.enums import ChatType
from aiogram.filters import Command, and_f, invert_f, or_f
from aiogram.types import Chat, Message, User

from aiogram_i18n import I18nMiddleware
from aiogram_i18n.cores import GNUTextCore
from aiogram_i18n.lazy.filter import LazyFilter
from tests.conftest import LOCALES


def make_message(text: str) -> Message:
    return Message(
        message_id=1,
        date=datetime.now(timezone.utc),
        chat=Chat(id=1, type=ChatType.PRIVATE),
        from_user=User(id=1, is_bot=False, first_name="TestUser"),
        text=text,
    )


@pytest.mark.asyncio
async def test_lazy_filter_direct() -> None:
    core = GNUTextCore(path=LOCALES)
    middleware = I18nMiddleware(core=core, default_locale="en")
    dp = Dispatcher()
    router = Router()
    dp.include_router(router)
    middleware.setup(dp)

    lazy = LazyFilter("hello")

    @router.message(lazy)
    async def handler(_msg: Message) -> bool:
        return True

    await dp.emit_startup()
    try:
        assert len(lazy.all_keys) > 0
        assert await lazy(make_message("hello")) is True
        assert await lazy(make_message("unknown")) is False
    finally:
        await dp.emit_shutdown()


@pytest.mark.asyncio
async def test_lazy_filter_in_or_f() -> None:
    core = GNUTextCore(path=LOCALES)
    middleware = I18nMiddleware(core=core, default_locale="en")
    dp = Dispatcher()
    router = Router()
    dp.include_router(router)
    middleware.setup(dp)

    lazy = LazyFilter("hello")

    @router.message(or_f(Command("start"), lazy))
    async def handler(_msg: Message) -> bool:
        return True

    await dp.emit_startup()
    try:
        assert len(lazy.all_keys) > 0, "LazyFilter inside or_f did not have startup called!"
        assert await lazy(make_message("hello")) is True
        assert await lazy(make_message("unknown")) is False
    finally:
        await dp.emit_shutdown()


@pytest.mark.asyncio
async def test_lazy_filter_in_and_f_and_invert_f() -> None:
    core = GNUTextCore(path=LOCALES)
    middleware = I18nMiddleware(core=core, default_locale="en")
    dp = Dispatcher()
    router = Router()
    dp.include_router(router)
    middleware.setup(dp)

    lazy_and = LazyFilter("hello")
    lazy_inv = LazyFilter("cur-lang")

    @router.message(and_f(lazy_and, invert_f(lazy_inv)))
    async def handler(_msg: Message) -> bool:
        return True

    await dp.emit_startup()
    try:
        assert len(lazy_and.all_keys) > 0
        assert len(lazy_inv.all_keys) > 0
        assert await lazy_and(make_message("hello")) is True
        assert await lazy_inv(make_message("cur-lang")) is True
    finally:
        await dp.emit_shutdown()
