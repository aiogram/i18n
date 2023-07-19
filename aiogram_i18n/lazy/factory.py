from functools import partial
from typing import Callable, Dict, Any

from .proxy import LazyProxy


class LazyFactory:
    def __init__(self, key_separator: str = "-") -> None:
        self.key_separator = key_separator

    def set_separator(self, key_separator: str) -> None:
        if not isinstance(key_separator, str):
            raise ValueError(
                f"Key separator should be instance of str not {type(key_separator).__name__!r}"
            )
        self.key_separator = key_separator

    def __getattr__(self, item: str) -> Callable[..., LazyProxy]:
        return partial(LazyProxy, item.replace("_", self.key_separator))

    def __call__(self, key: str, /, **kwargs: Dict[str, Any]) -> LazyProxy:
        return LazyProxy(key, **kwargs)
