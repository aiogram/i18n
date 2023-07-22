
from typing import Any, Dict, Self, Optional, Callable, TypeVar


T = TypeVar("T", bound=Callable[..., Any])


class MagicProxy:
    def __init__(self, call: T, key_separator: str = "-") -> None:
        self.key_separator = key_separator
        self._call = call
        self._query = []

    def __getattr__(self, item: str) -> Self:
        self._query.append(item)
        return self

    def __call__(
        self, key: Optional[str] = None, /, **kwargs: Dict[str, Any]
    ) -> T:
        if key is not None:
            self._query.append(key)

        key = self.key_separator.join(self._query)
        self._query.clear()

        return self._call(key, **kwargs)
