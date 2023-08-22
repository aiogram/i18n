from pathlib import Path
from typing import Any, Final

import pytest
from pytest_asyncio import fixture
from pytest_lazyfixture import lazy_fixture

from aiogram_i18n.cores import BaseCore
from aiogram_i18n.utils.fluent_extract import FluentMultipleKeyParser

TEST_LOCALES_DIR: Final[str] = "test_multiple_locales"
LOCALES: Final[str] = str(
    Path(__file__).parent.joinpath("data", TEST_LOCALES_DIR, "{locale}").absolute()
)


@fixture(scope="class")
def fluent_runtime_core_multiple() -> BaseCore[Any]:
    from aiogram_i18n.cores import FluentRuntimeCore

    return FluentRuntimeCore(path=LOCALES, use_isolating=False)


@fixture(scope="class")
def fluent_compile_core_multiple() -> BaseCore[Any]:
    from aiogram_i18n.cores import FluentCompileCore

    return FluentCompileCore(path=LOCALES, use_isolating=False)


@pytest.mark.parametrize(
    "i18n",
    [
        lazy_fixture("fluent_runtime_core_multiple"),
        lazy_fixture("fluent_compile_core_multiple"),
    ],
)
@pytest.mark.asyncio
class Test:
    async def test_multiple_extract(self, i18n: BaseCore[Any]) -> None:
        input_paths = (Path(__file__).absolute(),)
        output_dir = Path(__file__).parent.joinpath("data", TEST_LOCALES_DIR).absolute()

        fkp = FluentMultipleKeyParser(
            input_paths=input_paths,
            output_dir=output_dir,
            i18n_keys=["i18n", "L"],
            separator="-",
            locales=["en", "uk"],
            exclude_dirs=[],
            exclude_keys=["startup", "shutdown"],
        )
        fkp.run(create_missing_dirs=True)

        assert i18n.available_locales == ()
        await i18n.startup()
        assert set(i18n.available_locales) == {"en", "uk"}

    async def test_get(self, i18n: BaseCore[Any]) -> None:
        assert i18n.get("start", "en") == "start"
        assert i18n.get("start", "uk") == "start"

        assert i18n.get("buttons-cancel", "en") == "buttons-cancel"
        assert i18n.get("buttons-cancel", "uk") == "buttons-cancel"

        assert i18n.get("buttons-add-user", "en", user="Bob") == "buttons-add-user Bob"
        assert i18n.get("buttons-add-user", "uk", user="Боб") == "buttons-add-user Боб"

        assert i18n.get("msgs-hello", "en", user="Bob") == "msgs-hello Bob"
        assert i18n.get("msgs-hello", "uk", user="Боб") == "msgs-hello Боб"

        assert i18n.get("msgs-bye", "en", user="Bob") == "msgs-bye Bob"
        assert i18n.get("msgs-bye", "uk", user="Боб") == "msgs-bye Боб"
