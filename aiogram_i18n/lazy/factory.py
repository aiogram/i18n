from functools import partial
from typing import Callable, ClassVar

from .proxy import LazyProxy


class LazyFactory:
    _key_separator: ClassVar[str] = "-"

    @classmethod
    def set_key(cls, key_separator: str) -> None:
        cls._key_separator = key_separator

    def __getattr__(self, item: str) -> Callable[..., LazyProxy]:
        return partial(LazyProxy, item.replace("_", self._key_separator))
