from pathlib import Path
from typing import Any, Final

import pytest
from _pytest.legacypath import TempdirFactory
from pytest_asyncio import fixture
from pytest_lazyfixture import lazy_fixture

from aiogram_i18n.cores import BaseCore
from aiogram_i18n.exceptions import NoLocalesFoundError
from aiogram_i18n.utils.fluent_extract import FluentKeyParser
from tests.check_translations import _check_translations

TEST_CODE_DIR: Final[Path] = Path(__file__).parent.joinpath("data", "test_code").absolute()
LOCALES_OUTPUT_FILE = "locales_output.ftl"


@pytest.fixture(scope="function")
def locales_output(tmpdir_factory: TempdirFactory) -> Path:
    return Path(*tmpdir_factory.mktemp("locales_output").parts())


@pytest.fixture(scope="session")
def code_sample_dir(tmpdir_factory: TempdirFactory) -> Path:
    tmp = Path(*tmpdir_factory.mktemp("code_sample_dir").parts())

    for path in TEST_CODE_DIR.rglob("*.txt"):
        if path.is_file():
            target_path = (tmp / path.relative_to(TEST_CODE_DIR)).with_suffix(".py")
            target_path.write_text(path.read_text(encoding="utf-8"), encoding="utf-8")

    return tmp


@fixture(scope="function")
def fluent_runtime_core(locales_output: Path) -> BaseCore[Any]:
    from aiogram_i18n.cores import FluentRuntimeCore

    return FluentRuntimeCore(path=locales_output / "{locale}", use_isolating=False)


@fixture(scope="function")
def fluent_compile_core(locales_output: Path) -> BaseCore[Any]:
    from aiogram_i18n.cores import FluentCompileCore

    return FluentCompileCore(path=locales_output / "{locale}", use_isolating=False)


@pytest.mark.parametrize(
    "i18n",
    [
        lazy_fixture("fluent_runtime_core"),
        lazy_fixture("fluent_compile_core"),
    ],
)
@pytest.mark.asyncio
async def test_extract(i18n: BaseCore[Any], code_sample_dir: Path, locales_output: Path):
    fkp = FluentKeyParser(
        input_dirs=(code_sample_dir,),
        output_file=locales_output / LOCALES_OUTPUT_FILE,
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
    assert locales_output.joinpath("en", LOCALES_OUTPUT_FILE).exists()
    assert locales_output.joinpath("uk", LOCALES_OUTPUT_FILE).exists()

    await i18n.startup()
    _check_translations(i18n)


@pytest.mark.asyncio
@pytest.mark.xfail(raises=FileNotFoundError)
async def test_file_not_found_exception(
    locales_output: Path,
    code_sample_dir: Path,
):
    fkp = FluentKeyParser(
        input_dirs=(code_sample_dir / "._ERROR_PATH",),
        output_file=locales_output / LOCALES_OUTPUT_FILE,
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
        lazy_fixture("fluent_runtime_core"),
        lazy_fixture("fluent_compile_core"),
    ],
)
@pytest.mark.asyncio
@pytest.mark.xfail(raises=NoLocalesFoundError)
async def test_no_locales_found_error(
    i18n: BaseCore[Any], locales_output: Path, code_sample_dir: Path
):
    fkp = FluentKeyParser(
        input_dirs=(code_sample_dir,),
        output_file=locales_output / LOCALES_OUTPUT_FILE,
        i18n_keys=["i18n", "L", "I18NFormat"],
        separator="-",
        locales=[],
        exclude_dirs=[],
        exclude_keys=["startup", "shutdown"],
    )
    fkp.run(create_missing_dirs=True)

    assert i18n.available_locales == ()
    await i18n.startup()
