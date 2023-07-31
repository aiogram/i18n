from aiogram_i18n.exceptions import NoModuleError

try:
    from .base import BaseFluentKeyParser
    from .parser import FluentKeyParser, FluentMultipleKeyParser
    from .models import FluentKeywords, FluentMatch, FluentTemplate, FluentTemplateDir
except ImportError:
    raise NoModuleError(name="Fluent key extractor", module_name="libcst")

__all__ = [
    "BaseFluentKeyParser",
    "FluentKeyParser",
    "FluentKeywords",
    "FluentMatch",
    "FluentMultipleKeyParser",
    "FluentTemplate",
    "FluentTemplateDir",
]
