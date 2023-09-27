from pathlib import Path
from typing import Any, Final

import pytest
from _pytest.legacypath import TempdirFactory
from babel import UnknownLocaleError
from pytest_asyncio import fixture
from pytest_lazyfixture import lazy_fixture

from aiogram_i18n.cores import BaseCore
from aiogram_i18n.utils.fluent_extract import FluentMultipleKeyParser
from tests.check_translations import _check_translations

TEST_CODE_DIR: Final[Path] = Path(__file__).parent.joinpath("data", "test_code").absolute()


@pytest.fixture(scope="function")
def no_locales_output(tmpdir_factory: TempdirFactory) -> Path:
    return Path(*tmpdir_factory.mktemp("no_locales_output").parts())


@pytest.fixture(scope="function")
def multiple_locales_output(tmpdir_factory: TempdirFactory) -> Path:
    return Path(*tmpdir_factory.mktemp("multiple_locales_output").parts())


@pytest.fixture(scope="session")
def code_sample_dir(tmpdir_factory: TempdirFactory) -> Path:
    tmp = Path(*tmpdir_factory.mktemp("code_sample_dir").parts())

    for path in TEST_CODE_DIR.rglob("*.txt"):
        if path.is_file():
            target_path = (tmp / path.relative_to(TEST_CODE_DIR)).with_suffix(".py")
            target_path.write_text(path.read_text(encoding="utf-8"), encoding="utf-8")

    return tmp


@fixture(scope="function")
def fluent_runtime_core_no_locales(no_locales_output: Path) -> BaseCore[Any]:
    from aiogram_i18n.cores import FluentRuntimeCore

    return FluentRuntimeCore(path=no_locales_output, use_isolating=False)


@fixture(scope="function")
def fluent_runtime_core_multiple_locales(multiple_locales_output: Path) -> BaseCore[Any]:
    from aiogram_i18n.cores import FluentRuntimeCore

    return FluentRuntimeCore(path=multiple_locales_output / "{locale}", use_isolating=False)


@fixture(scope="function")
def fluent_compile_core_no_locales(no_locales_output: Path) -> BaseCore[Any]:
    from aiogram_i18n.cores import FluentCompileCore

    return FluentCompileCore(path=no_locales_output, use_isolating=False)


@fixture(scope="function")
def fluent_compile_core_multiple_locales(multiple_locales_output: Path) -> BaseCore[Any]:
    from aiogram_i18n.cores import FluentCompileCore

    return FluentCompileCore(path=multiple_locales_output / "{locale}", use_isolating=False)


@pytest.mark.parametrize(
    "i18n",
    [
        lazy_fixture("fluent_runtime_core_multiple_locales"),
        lazy_fixture("fluent_compile_core_multiple_locales"),
    ],
)
@pytest.mark.asyncio
async def test_multiple_extract(
    i18n: BaseCore[Any], multiple_locales_output: Path, code_sample_dir: Path
) -> None:
    fkp = FluentMultipleKeyParser(
        input_paths=(code_sample_dir,),
        output_dir=multiple_locales_output,
        i18n_keys=["i18n", "L", "I18NFormat"],
        separator="-",
        locales=["en", "uk"],
        exclude_dirs=[],
        exclude_keys=["startup", "shutdown"],
        default_ftl_file="_default.ftl",
    )
    fkp.run(create_missing_dirs=True)

    await i18n.startup()
    assert set(i18n.available_locales) == {"en", "uk"}
    assert multiple_locales_output.joinpath("en").exists()
    assert multiple_locales_output.joinpath("uk").exists()
    _check_translations(i18n)


@pytest.mark.asyncio
@pytest.mark.xfail(raises=FileNotFoundError)
async def test_file_not_found_exception(multiple_locales_output: Path, code_sample_dir: Path):
    fkp = FluentMultipleKeyParser(
        input_paths=(code_sample_dir / "._ERROR_PATH",),
        output_dir=multiple_locales_output,
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
async def test_unknown_locale_error(
    i18n: BaseCore[Any], no_locales_output: Path, code_sample_dir: Path
):
    fkp = FluentMultipleKeyParser(
        input_paths=(code_sample_dir,),
        output_dir=no_locales_output,
        i18n_keys=["i18n", "L", "I18NFormat"],
        separator="-",
        locales=[],
        exclude_dirs=[],
        exclude_keys=["startup", "shutdown"],
        default_ftl_file="_default.ftl",
    )
    fkp.run(create_missing_dirs=True)

    assert i18n.available_locales == ()
    await i18n.startup()
