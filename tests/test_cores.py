from typing import Any

import pytest
from pytest_lazyfixture import lazy_fixture

from aiogram_i18n.cores.base import BaseCore


@pytest.mark.parametrize("core", [
    lazy_fixture("gnu_text_core"),
    lazy_fixture("fluent_runtime_core"),
    lazy_fixture("fluent_compile_core"),
])
@pytest.mark.asyncio
class Test:
    async def test_startup(self, core: BaseCore[Any]) -> None:
        assert core.available_locales == ()
        await core.startup()
        assert set(core.available_locales) == {"en", "uk"}

    async def test_get(self, core: BaseCore[Any]) -> None:
        assert core.get("hello", locale="en", user="Bob") == "Hello, <b>Bob</b>!"
        assert core.get("cur-lang", locale="uk", language="uk") == "Твоя мова: <i>uk</i>"
