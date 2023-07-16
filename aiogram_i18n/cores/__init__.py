from importlib import import_module
from .base import BaseCore
from typing import Any

__cores__ = {
    "GNUTextCore": '.gnu_text_core',
    "FluentRuntimeCore": '.fluent_runtime_core',
    "FluentCompileCore": '.fluent_compile_core'
}

__all__ = (
    "GNUTextCore",  # noqa
    "FluentRuntimeCore",  # noqa
    "FluentCompileCore",  # noqa
    "BaseCore"
)


def __getattr__(name: str) -> BaseCore[Any]:
    if name not in __all__:
        raise AttributeError
    return getattr(import_module(__cores__[name], "aiogram_i18n.cores"), name)
