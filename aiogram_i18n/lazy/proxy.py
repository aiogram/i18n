from __future__ import annotations

from typing import Any, Dict, Tuple, Union

from pydantic import BaseModel

from aiogram_i18n.context import I18nContext


class LazyProxy(BaseModel):  # type: ignore[no-redef]
    key: str
    kwargs: Dict[str, Any]

    def __init__(self, key: str, /, **kwargs: Any) -> None:
        super().__init__(key=key, kwargs=kwargs)

    @property
    def data(self) -> str:
        context = I18nContext.get_current()
        if context:
            return context.get(self.key, **self.kwargs)
        return self.key

    def model_dump(self, **kwargs: Any) -> str:  # type: ignore[override]
        return self.data

    def model_dump_json(self, **kwargs: Any) -> str:
        return self.data

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}<'{self.key}'>"

    def __int__(self) -> int:
        return int(self.data)

    def __float__(self) -> float:
        return float(self.data)

    def __complex__(self) -> complex:
        return complex(self.data)

    def __hash__(self) -> int:
        return hash(self.data)

    def __getnewargs__(self) -> Tuple[str, ...]:
        return self.data[:],

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
