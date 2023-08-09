from ..utils.magic_proxy import MagicProxy
from .proxy import LazyProxy


class LazyFactory:
    def __init__(self, key_separator: str = "-") -> None:
        self.key_separator = key_separator

    @property
    def key_separator(self) -> str:
        return self._key_separator

    @key_separator.setter
    def key_separator(self, sep: str) -> None:
        if not isinstance(sep, str):
            raise ValueError(f"Key separator should be instance of str not {type(sep).__name__!r}")
        self._key_separator = sep

    def __getattr__(self, item: str) -> MagicProxy[LazyProxy]:
        proxy = MagicProxy(self, key_separator=self._key_separator)
        return proxy.__getattr__(item)

    __call__ = LazyProxy
