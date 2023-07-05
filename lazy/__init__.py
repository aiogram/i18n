
from .proxy import LazyProxy
from .tracer import LazyT

L = LazyT()

__all__ = [
    "LazyProxy", "LazyT", "L"
]
