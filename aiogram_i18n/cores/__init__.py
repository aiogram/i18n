from importlib import import_module
from typing import Any, cast, TYPE_CHECKING

from .base import BaseCore

if TYPE_CHECKING:
    from .gnu_text_core import GNUTextCore
    from .fluent_compile_core import FluentCompileCore
    from .fluent_runtime_core import FluentRuntimeCore


__cores__ = {
    "GNUTextCore": '.gnu_text_core',
    "FluentRuntimeCore": '.fluent_runtime_core',
    "FluentCompileCore": '.fluent_compile_core'
}

__all__ = (
    "GNUTextCore",
    "FluentRuntimeCore",
    "FluentCompileCore",
    "BaseCore"
)


def __getattr__(name: str) -> BaseCore[Any]:
    if name not in __all__:
        raise AttributeError
    return cast(
        BaseCore[Any],
        getattr(import_module(__cores__[name], "aiogram_i18n.cores"), name)
    )
