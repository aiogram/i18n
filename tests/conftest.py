from __future__ import annotations
from aiogram_i18n.cores import BaseCore
from pathlib import Path
from typing import Any, AsyncGenerator, List

import pytest
from pytest_asyncio import fixture


LOCALES = str(
    Path(__file__).parent.joinpath("data", "locales", "{locale}", "LC_MESSAGES").absolute()
)


def is_installed(module_name: str) -> bool:
    try:
        __import__(module_name)
    except ImportError:
        return False
    return True


def pytest_collection_modifyitems(
    config: Any, items: list[pytest.Function]  # noqa
) -> None:
    _skip_f: List[str] = []
    if not is_installed("fluent_compiler"):
        _skip_f.append("fluent_compile")
        print(f"\nJust install fluent_compiler (`pip install fluent_compiler`)")
    if not is_installed("fluent.runtime"):
        _skip_f.append("fluent_runtime")
        print(f"\nJust install fluent.runtime (`pip install fluent.runtime`)")
    skip_f = tuple(_skip_f)
    to_remove = []
    for item in items:
        for kw in item.keywords:
            if kw.startswith(skip_f):
                to_remove.append(item)
    for remove in to_remove:
        items.remove(remove)


@fixture(scope="class")
def gnu_text_core() -> BaseCore[Any]:
    from aiogram_i18n.cores import GNUTextCore
    return GNUTextCore(path=LOCALES)


@fixture(scope="class")
def fluent_runtime_core() -> BaseCore[Any]:
    from aiogram_i18n.cores import FluentRuntimeCore
    return FluentRuntimeCore(path=LOCALES, use_isolating=False)


@fixture(scope="class")
def fluent_compile_core() -> BaseCore[Any]:
    from aiogram_i18n.cores import FluentCompileCore
    return FluentCompileCore(path=LOCALES, use_isolating=False)


@fixture(scope="class")
async def gnu_text_ready(
    gnu_text: BaseCore[Any]
) -> AsyncGenerator[BaseCore[Any], None]:
    await gnu_text.startup()
    yield gnu_text
    await gnu_text.shutdown()


@fixture(scope="class")
async def fluent_runtime_core_ready(
    fluent_runtime_core: BaseCore[Any]
) -> AsyncGenerator[BaseCore[Any], None]:
    await fluent_runtime_core.startup()
    yield fluent_runtime_core
    await fluent_runtime_core.shutdown()


@fixture(scope="class")
async def fluent_compile_core_ready(
    fluent_compile_core: BaseCore[Any]
) -> AsyncGenerator[BaseCore[Any], None]:
    await fluent_compile_core.startup()
    yield fluent_compile_core
    await fluent_compile_core.shutdown()
