from __future__ import annotations

from typing import Any

from context import I18nContext
from lazy_proxy import LazyProxy


class AttribTracer:
    def __init__(self, sep: str = "-") -> None:
        self.separator = sep
        self._query = ""

    def __getattr__(self, item: str) -> AttribTracer:
        self._query += f"{item}{self.separator}"
        return self

    def __call__(self, **kwargs: Any) -> str:
        i18n = I18nContext.get_current(False)
        text = i18n.get(self._query[:-1], **kwargs)
        self._query = ""
        return text

    def lazy(self, **kwargs: Any) -> LazyProxy:
        proxy = LazyProxy(self._query, **kwargs)
        self._query = ""
        return proxy


T = AttribTracer()
