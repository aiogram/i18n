from pathlib import Path
from typing import Any, Final

import pytest
from babel import UnknownLocaleError
from pytest_asyncio import fixture
from pytest_lazyfixture import lazy_fixture

from aiogram_i18n.cores import BaseCore
from aiogram_i18n.utils.fluent_extract import FluentMultipleKeyParser
from tests.check_translations import _check_translations

TEST_CODE_DIR: Final[Path] = Path(__file__).parent.joinpath("data", "test_code").absolute()
NO_LOCALES_OUTPUT_DIR: Final[Path] = Path(__file__).parent.joinpath("no_locales_output").absolute()
MULTIPLE_LOCALES_OUTPUT_DIR: Final[Path] = (
    Path(__file__).parent.joinpath("multiple_locales_output").absolute()
)


@fixture(scope="function")
def fluent_runtime_core_no_locales() -> BaseCore[Any]:
    from aiogram_i18n.cores import FluentRuntimeCore

    return FluentRuntimeCore(path=NO_LOCALES_OUTPUT_DIR, use_isolating=False)


@fixture(scope="function")
def fluent_runtime_core_multiple_locales() -> BaseCore[Any]:
    from aiogram_i18n.cores import FluentRuntimeCore

    return FluentRuntimeCore(path=MULTIPLE_LOCALES_OUTPUT_DIR / "{locale}", use_isolating=False)


@fixture(scope="function")
def fluent_compile_core_no_locales() -> BaseCore[Any]:
    from aiogram_i18n.cores import FluentCompileCore

    return FluentCompileCore(path=NO_LOCALES_OUTPUT_DIR, use_isolating=False)


@fixture(scope="function")
def fluent_compile_core_multiple_locales() -> BaseCore[Any]:
    from aiogram_i18n.cores import FluentCompileCore

    return FluentCompileCore(path=MULTIPLE_LOCALES_OUTPUT_DIR / "{locale}", use_isolating=False)


@pytest.mark.parametrize(
    "i18n",
    [
        lazy_fixture("fluent_runtime_core_multiple_locales"),
        lazy_fixture("fluent_compile_core_multiple_locales"),
    ],
)
@pytest.mark.asyncio
async def test_multiple_extract(i18n: BaseCore[Any]) -> None:
    fkp = FluentMultipleKeyParser(
        input_paths=(TEST_CODE_DIR,),
        output_dir=MULTIPLE_LOCALES_OUTPUT_DIR,
        i18n_keys=["i18n", "L", "I18NFormat"],
        separator="-",
        locales=["en", "uk"],
        exclude_dirs=[],
        exclude_keys=["startup", "shutdown"],
        default_ftl_file="_default.ftl",
    )
    fkp.run(create_missing_dirs=True)

    try:
        await i18n.startup()
        assert set(i18n.available_locales) == {"en", "uk"}
        assert MULTIPLE_LOCALES_OUTPUT_DIR.joinpath("en").exists()
        assert MULTIPLE_LOCALES_OUTPUT_DIR.joinpath("uk").exists()
        _check_translations(i18n)
    finally:
        __import__("shutil").rmtree(MULTIPLE_LOCALES_OUTPUT_DIR)


@pytest.mark.asyncio
@pytest.mark.xfail(raises=FileNotFoundError)
async def test_file_not_found_exception():
    fkp = FluentMultipleKeyParser(
        input_paths=(TEST_CODE_DIR / "._ERROR_PATH",),
        output_dir=MULTIPLE_LOCALES_OUTPUT_DIR,
        i18n_keys=["i18n", "L", "I18NFormat"],
        separator="-",
        locales=["en", "uk"],
        exclude_dirs=[],
        exclude_keys=["startup", "shutdown"],
        default_ftl_file="_default.ftl",
    )
    fkp.run(create_missing_dirs=True)


@pytest.mark.parametrize(
    "i18n",
    [
        lazy_fixture("fluent_runtime_core_no_locales"),
        lazy_fixture("fluent_compile_core_no_locales"),
    ],
)
@pytest.mark.asyncio
@pytest.mark.xfail(raises=(UnknownLocaleError, TypeError))
async def test_unknown_locale_error(i18n: BaseCore[Any]):
    fkp = FluentMultipleKeyParser(
        input_paths=(TEST_CODE_DIR,),
        output_dir=NO_LOCALES_OUTPUT_DIR,
        i18n_keys=["i18n", "L", "I18NFormat"],
        separator="-",
        locales=[],
        exclude_dirs=[],
        exclude_keys=["startup", "shutdown"],
        default_ftl_file="_default.ftl",
    )
    fkp.run(create_missing_dirs=True)

    assert i18n.available_locales == ()
    try:
        await i18n.startup()

    finally:
        __import__("shutil").rmtree(NO_LOCALES_OUTPUT_DIR)
        pass
