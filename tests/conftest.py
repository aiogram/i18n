from __future__ import annotations

import warnings
from pathlib import Path
from typing import TYPE_CHECKING, Any

import pytest

if TYPE_CHECKING:
    from collections.abc import AsyncGenerator

    from aiogram_i18n.cores import BaseCore

LOCALES = str(
    Path(__file__).parent.joinpath("data", "locales", "{locale}", "LC_MESSAGES").absolute()
)


def is_installed(module_name: str) -> bool:
    try:
        __import__(module_name)
    except ImportError:
        return False
    return True


def pytest_collection_modifyitems(config: pytest.Config, items: list[pytest.Function]) -> None:  # noqa: ARG001
    skip_f: list[str] = []
    if not is_installed("fluent_compiler"):
        skip_f.append("fluent_compile")
        warnings.warn(
            "Just install fluent_compiler (`pip install fluent_compiler`)",
            ImportWarning,
            stacklevel=2,
        )
    if not is_installed("fluent.runtime"):
        skip_f.append("fluent_runtime")
        warnings.warn(
            "Just install fluent_compiler (`pip install fluent_compiler`)",
            ImportWarning,
            stacklevel=2,
        )
    skip_f: tuple[str] = tuple(skip_f)
    to_remove = [item for item in items if any(kw.startswith(skip_f) for kw in item.keywords)]

    for remove in to_remove:
        items.remove(remove)


@pytest.fixture(scope="class")
def gnu_text_core() -> BaseCore[Any]:
    from aiogram_i18n.cores import GNUTextCore

    return GNUTextCore(path=LOCALES)


@pytest.fixture(scope="class")
def fluent_runtime_core() -> BaseCore[Any]:
    from aiogram_i18n.cores import FluentRuntimeCore

    return FluentRuntimeCore(path=LOCALES, use_isolating=False)


@pytest.fixture(scope="class")
def fluent_compile_core() -> BaseCore[Any]:
    from aiogram_i18n.cores import FluentCompileCore

    return FluentCompileCore(path=LOCALES, use_isolating=False)


@pytest.fixture(scope="class")
async def gnu_text_ready(gnu_text: BaseCore[Any]) -> AsyncGenerator[BaseCore[Any], None]:
    await gnu_text.startup()
    yield gnu_text
    await gnu_text.shutdown()


@pytest.fixture(scope="class")
async def fluent_runtime_core_ready(
    fluent_runtime_core: BaseCore[Any],
) -> AsyncGenerator[BaseCore[Any], None]:
    await fluent_runtime_core.startup()
    yield fluent_runtime_core
    await fluent_runtime_core.shutdown()


@pytest.fixture(scope="class")
async def fluent_compile_core_ready(
    fluent_compile_core: BaseCore[Any],
) -> AsyncGenerator[BaseCore[Any], None]:
    await fluent_compile_core.startup()
    yield fluent_compile_core
    await fluent_compile_core.shutdown()
