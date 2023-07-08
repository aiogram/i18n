from collections import UserString
from typing import Any, Dict

from aiogram_i18n.context import I18nContext


class LazyProxy(UserString):
    key: str
    kwargs: Dict[str, Any]

    def __init__(  # noqa
        self, key: str, **kwargs: Dict[str, Any]
    ) -> None:
        self.key = key
        self.kwargs = kwargs

    @property
    def data(self) -> str:  # type: ignore[override]
        context = I18nContext.get_current()
        if context:
            return context.get(key=self.key, **self.kwargs)
        return self.key

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}<'{self.key}'>"
