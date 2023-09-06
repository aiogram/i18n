from pathlib import Path
from typing import Any, Final

import pytest
from pytest_asyncio import fixture
from pytest_lazyfixture import lazy_fixture

from aiogram_i18n.cores import BaseCore
from aiogram_i18n.exceptions import NoLocalesFoundError
from aiogram_i18n.utils.fluent_extract import FluentKeyParser
from tests.check_translations import _check_translations

TEST_CODE_DIR: Final[Path] = Path(__file__).parent.joinpath("data", "test_code").absolute()
LOCALES_OUTPUT_DIR: Final[Path] = Path(__file__).parent.joinpath("locales_output").absolute()
LOCALES_OUTPUT_FILE = "locales_output.ftl"
LOCALES: Final[str] = str(LOCALES_OUTPUT_DIR / "{locale}")


@fixture(scope="function")
def fluent_runtime_core_multiple() -> BaseCore[Any]:
    from aiogram_i18n.cores import FluentRuntimeCore

    return FluentRuntimeCore(path=LOCALES, use_isolating=False)


@fixture(scope="function")
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
async def test_extract_(i18n: BaseCore[Any]) -> None:
    fkp = FluentKeyParser(
        input_dirs=(TEST_CODE_DIR,),
        output_file=LOCALES_OUTPUT_DIR / LOCALES_OUTPUT_FILE,
        i18n_keys=["i18n", "L", "I18NFormat"],
        separator="-",
        locales=["en", "uk"],
        exclude_dirs=[],
        exclude_keys=["startup", "shutdown"],
    )
    fkp.run(create_missing_dirs=True)

    assert i18n.available_locales == ()
    await i18n.startup()
    assert set(i18n.available_locales) == {"en", "uk"}
    assert LOCALES_OUTPUT_DIR.joinpath("en", LOCALES_OUTPUT_FILE).exists()
    assert LOCALES_OUTPUT_DIR.joinpath("uk", LOCALES_OUTPUT_FILE).exists()

    try:
        await i18n.startup()
        _check_translations(i18n)
    finally:
        __import__("shutil").rmtree(LOCALES_OUTPUT_DIR)


@pytest.mark.asyncio
@pytest.mark.xfail(raises=FileNotFoundError)
async def test_file_not_found_exception():
    fkp = FluentKeyParser(
        input_dirs=(TEST_CODE_DIR / "._ERROR_PATH",),
        output_file=LOCALES_OUTPUT_DIR / LOCALES_OUTPUT_FILE,
        i18n_keys=["i18n", "L", "I18NFormat"],
        separator="-",
        locales=["en", "uk"],
        exclude_dirs=[],
        exclude_keys=["startup", "shutdown"],
    )
    fkp.run(create_missing_dirs=True)


@pytest.mark.parametrize(
    "i18n",
    [
        lazy_fixture("fluent_runtime_core_multiple"),
        lazy_fixture("fluent_compile_core_multiple"),
    ],
)
@pytest.mark.asyncio
@pytest.mark.xfail(raises=NoLocalesFoundError)
async def test_no_locales_found_error(i18n: BaseCore[Any]):
    fkp = FluentKeyParser(
        input_dirs=(TEST_CODE_DIR,),
        output_file=LOCALES_OUTPUT_DIR / LOCALES_OUTPUT_FILE,
        i18n_keys=["i18n", "L", "I18NFormat"],
        separator="-",
        locales=[],
        exclude_dirs=[],
        exclude_keys=["startup", "shutdown"],
    )
    fkp.run(create_missing_dirs=True)

    assert i18n.available_locales == ()
    try:
        await i18n.startup()

    finally:
        __import__("shutil").rmtree(LOCALES_OUTPUT_DIR)
