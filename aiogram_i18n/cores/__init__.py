from .base import BaseCore
from typing import Any

__cores__ = {
    "GNUTextCore": 'gnu_text_core',
    "FluentRuntimeCore": 'fluent_runtime_core',
    "FluentCompileCore": 'fluent_compile_core'
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
    return getattr(__import__(__cores__[name], globals(), locals(), [name], 0), name)
