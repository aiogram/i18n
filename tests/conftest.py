from pathlib import Path

import pytest
from pytest_asyncio import fixture
from aiogram_i18n.cores.base import BaseCore

LOCALES = str(Path(__file__).parent.joinpath("data", "locales", "{locale}", "LC_MESSAGES").absolute())


def is_install(module_name: str):
    try:
        __import__(module_name)
    except ImportError:
        return False
    else:
        return True


def pytest_collection_modifyitems(config, items: list[pytest.Function]):
    skip_f = []
    if not is_install("fluent_compiler"):
        skip_f.append("fluent_compile")
        print(f"\nJust install fluent_compiler (`pip install fluent_compiler`)")
    if not is_install("fluent.runtime"):
        skip_f.append("fluent_runtime")
        print(f"\nJust install fluent.runtime (`pip install fluent.runtime`)")
    skip_f = tuple(skip_f)
    to_remove = []
    for item in items:
        for kw in item.keywords:
            if kw.startswith(skip_f):
                to_remove.append(item)
    for remove in to_remove:
        items.remove(remove)


@fixture(scope="class")
def gnu_text_core():
    from aiogram_i18n.cores.gnu_text_core import GNUTextCore
    return GNUTextCore(path=LOCALES)


@fixture(scope="class")
def fluent_runtime_core():
    from aiogram_i18n.cores.fluent_runtime_core import FluentRuntimeCore
    return FluentRuntimeCore(path=LOCALES, use_isolating=False)


@fixture(scope="class")
def fluent_compile_core():
    from aiogram_i18n.cores.fluent_compile_core import FluentCompileCore
    return FluentCompileCore(path=LOCALES, use_isolating=False)


@fixture(scope="class")
async def gnu_text_ready(gnu_text: BaseCore):
    await gnu_text.startup()
    yield gnu_text
    await gnu_text.shutdown()


@fixture(scope="class")
async def fluent_runtime_core_ready(fluent_runtime_core: BaseCore):
    await fluent_runtime_core.startup()
    yield fluent_runtime_core
    await fluent_runtime_core.shutdown()


@fixture(scope="class")
async def fluent_compile_core_ready(fluent_compile_core: BaseCore):
    await fluent_compile_core.startup()
    yield fluent_compile_core
    await fluent_compile_core.shutdown()
