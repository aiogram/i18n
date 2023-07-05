from functools import partial
from typing import Callable

from lazy.proxy import LazyProxy


class LazyT:
    def __init__(self, separator: str = "-") -> None:
        self.separator = separator

    def __getattr__(self, item: str) -> Callable[..., LazyProxy]:
        return partial(LazyProxy, item.replace("_", self.separator))
