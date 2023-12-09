from __future__ import annotations

from typing import Any, Dict, Optional, Tuple, Union

from aiogram.types import Message
from pydantic import BaseModel, model_serializer

from aiogram_i18n.context import I18nContext
from aiogram_i18n.utils.attrdict import AttrDict


class LazyProxy(BaseModel):  # type: ignore[no-redef]
    key: str
    locale: Optional[str]
    kwargs: Dict[str, Any]

    def __init__(self, key: str, locale: Optional[str] = None, /, **kwargs: Any) -> None:
        super().__init__(key=key, locale=locale, kwargs=kwargs)

    @property
    def data(self) -> str:
        i18n = I18nContext.get_current()
        if i18n is None:
            return self.key
        kwargs = {}
        for k, v in self.kwargs.items():
            if hasattr(v, "resolve"):
                v = v.resolve(AttrDict(i18n.context))
            kwargs[k] = v
        return i18n.get(self.key, self.locale, **kwargs)

    def __call__(self, event: Message) -> bool:
        return event.text == self.data

    @model_serializer
    def dump(self) -> str:
        return self.data

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} '{self.key}'>"

    def __int__(self) -> int:
        return int(self.data)

    def __float__(self) -> float:
        return float(self.data)

    def __complex__(self) -> complex:
        return complex(self.data)

    def __hash__(self) -> int:
        return hash(self.data)

    def __getnewargs__(self) -> Tuple[str, ...]:
        return (self.data[:],)

    def __eq__(self, string: object) -> bool:
        if isinstance(string, LazyProxy):
            return self.data == string.data
        return self.data == string

    def __lt__(self, string: Union[str, LazyProxy]) -> bool:
        if isinstance(string, LazyProxy):
            return self.data < string.data
        return self.data < string

    def __le__(self, string: Union[str, LazyProxy]) -> bool:
        if isinstance(string, LazyProxy):
            return self.data <= string.data
        return self.data <= string

    def __gt__(self, string: Union[str, LazyProxy]) -> bool:
        if isinstance(string, LazyProxy):
            return self.data > string.data
        return self.data > string

    def __ge__(self, string: Union[str, LazyProxy]) -> bool:
        if isinstance(string, LazyProxy):
            return self.data >= string.data
        return self.data >= string

    def __contains__(self, char: object) -> bool:
        if isinstance(char, LazyProxy):
            return char.data in self.data
        if isinstance(char, str):
            return char in self.data
        raise TypeError()

    def __len__(self) -> int:
        return len(self.data)
