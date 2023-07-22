from __future__ import annotations

from typing import Any, Callable, TypeVar, List, Generic


T = TypeVar("T", bound=Any)


class MagicProxy(Generic[T]):
    def __init__(
        self, call: Callable[..., T], key_separator: str = "-"
    ) -> None:
        self.key_separator = key_separator
        self._call = call
        self._query: List[str] = []

    def __getattr__(self, item: str) -> MagicProxy:
        self._query.append(item)
        return self

    def __call__(self, /, **kwargs: Any) -> T:
        key = self.key_separator.join(self._query)
        return self._call(key, **kwargs)
