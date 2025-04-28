from typing import Any

import pytest

from aiogram_i18n.cores.base import BaseCore


@pytest.mark.parametrize(
    "core",
    [
        "gnu_text_core",
        "fluent_runtime_core",
        "fluent_compile_core",
    ],
)
@pytest.mark.asyncio
class Test:
    async def test_startup(self, core: BaseCore[Any], request) -> None:
        core = request.getfixturevalue(core)

        assert core.available_locales == ()
        await core.startup()
        assert set(core.available_locales) == {"en", "uk"}

    async def test_get(self, core: BaseCore[Any], request) -> None:
        core = request.getfixturevalue(core)

        assert core.get("hello", "en", user="Bob") == "Hello, <b>Bob</b>!"
        assert core.get("cur-lang", "uk", language="uk") == "Твоя мова: <i>uk</i>"
