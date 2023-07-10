
from .context import I18nContext
from .lazy import LazyProxy, LazyFactory
from .middleware import I18nMiddleware

L = LazyFactory()

__all__ = (
    "L",
    "LazyProxy",
    "I18nContext",
    "I18nMiddleware"
)

__version__ = "1.0"
