from __future__ import annotations

import sys
from typing import (
    Any, Dict, Tuple, Union, Iterable,
    Optional, Mapping, Self, List
)

from pydantic import BaseModel

from aiogram_i18n.context import I18nContext


class LazyProxy(BaseModel):
    key: str
    kwargs: Dict[str, Any]

    class Config:
        arbitrary_types_allowed = True

    def __init__(
        self, key: str, /, **kwargs: Dict[str, Any]
    ) -> None:
        super().__init__(key=key, kwargs=kwargs)

    @property
    def data(self) -> str:
        context = I18nContext.get_current()
        if context:
            return context.get(self.key, **self.kwargs)
        return self.key

    def dict(self, **kwargs: Any) -> str:  # type: ignore[override]
        return self.data

    def json(self, **kwargs: Any) -> str:
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

    def __getitem__(self, index: int) -> Self:
        return self.__class__(self.data[index])

    def __add__(self, other: object) -> Self:
        if isinstance(other, LazyProxy):
            return self.__class__(self.data + other.data)
        elif isinstance(other, str):
            return self.__class__(self.data + other)
        return self.__class__(self.data + str(other))

    def __radd__(self, other: object) -> Self:
        if isinstance(other, str):
            return self.__class__(other + self.data)
        return self.__class__(str(other) + self.data)

    def __mul__(self, n: int) -> Self:
        return self.__class__(self.data * n)

    __rmul__ = __mul__

    def __mod__(self, args: Any) -> Self:
        return self.__class__(self.data % args)

    def __rmod__(self, template: object) -> Self:
        return self.__class__(str(template) % self)

    # the following methods are defined in alphabetical order:
    def capitalize(self) -> Self:
        return self.__class__(self.data.capitalize())

    def casefold(self) -> Self:
        return self.__class__(self.data.casefold())

    def center(self, width: int, *args: Any) -> Self:
        return self.__class__(self.data.center(width, *args))

    def count(
        self,
        sub: Union[str, LazyProxy],
        start: int = 0,
        end: int = sys.maxsize
    ) -> int:
        if isinstance(sub, LazyProxy):
            sub = sub.data
        return self.data.count(sub, start, end)

    def removeprefix(self, prefix: Union[str, LazyProxy], /) -> Self:
        if isinstance(prefix, LazyProxy):
            prefix = prefix.data
        return self.__class__(self.data.removeprefix(prefix))

    def removesuffix(self, suffix: Union[str, LazyProxy], /) -> Self:
        if isinstance(suffix, LazyProxy):
            suffix = suffix.data
        return self.__class__(self.data.removesuffix(suffix))

    def encode(self, encoding: str = "utf-8", errors: str = "strict") -> bytes:
        encoding = "utf-8" if encoding is None else encoding
        errors = "strict" if errors is None else errors
        return self.data.encode(encoding, errors)

    def endswith(
        self, suffix: str | Tuple[str, ...], start: int = 0, end: int = sys.maxsize
    ) -> bool:
        return self.data.endswith(suffix, start, end)

    def expandtabs(self, tabsize: int = 8) -> Self:
        return self.__class__(self.data.expandtabs(tabsize))

    def find(
        self, sub: Union[str, LazyProxy],
        start: int = 0, end: int = sys.maxsize
    ) -> int:
        if isinstance(sub, LazyProxy):
            sub = sub.data
        return self.data.find(sub, start, end)

    def format(self, /, *args: Any, **kwds: Any) -> str:
        return self.data.format(*args, **kwds)

    def format_map(self, mapping: Mapping[str, Any]) -> str:
        return self.data.format_map(mapping)

    def index(self, sub: str, start: int = 0, end: int = sys.maxsize) -> int:
        return self.data.index(sub, start, end)

    def isalpha(self) -> bool:
        return self.data.isalpha()

    def isalnum(self) -> bool:
        return self.data.isalnum()

    def isascii(self) -> bool:
        return self.data.isascii()

    def isdecimal(self) -> bool:
        return self.data.isdecimal()

    def isdigit(self) -> bool:
        return self.data.isdigit()

    def isidentifier(self) -> bool:
        return self.data.isidentifier()

    def islower(self) -> bool:
        return self.data.islower()

    def isnumeric(self) -> bool:
        return self.data.isnumeric()

    def isprintable(self) -> bool:
        return self.data.isprintable()

    def isspace(self) -> bool:
        return self.data.isspace()

    def istitle(self) -> bool:
        return self.data.istitle()

    def isupper(self) -> bool:
        return self.data.isupper()

    def join(self, seq: Iterable[str]) -> str:
        return self.data.join(seq)

    def ljust(self, width: int, *args: Any) -> Self:
        return self.__class__(self.data.ljust(width, *args))

    def lower(self) -> Self:
        return self.__class__(self.data.lower())

    def lstrip(self, chars: Optional[str] = None) -> Self:
        return self.__class__(self.data.lstrip(chars))

    maketrans = str.maketrans

    def partition(self, sep: str) -> Tuple[str, str, str]:
        return self.data.partition(sep)

    def replace(
        self,
        old: Union[str, LazyProxy],
        new: Union[str, LazyProxy],
        maxsplit: int = -1
    ) -> Self:
        if isinstance(old, LazyProxy):
            old = old.data
        if isinstance(new, LazyProxy):
            new = new.data
        return self.__class__(self.data.replace(old, new, maxsplit))

    def rfind(self, sub: Union[str, LazyProxy], start: int = 0, end: int = sys.maxsize) -> int:
        if isinstance(sub, LazyProxy):
            sub = sub.data
        return self.data.rfind(sub, start, end)

    def rindex(self, sub: str, start: int = 0, end: int = sys.maxsize) -> int:
        return self.data.rindex(sub, start, end)

    def rjust(self, width: int, *args: Any) -> Self:
        return self.__class__(self.data.rjust(width, *args))

    def rpartition(self, sep: str) -> Tuple[str, str, str]:
        return self.data.rpartition(sep)

    def rstrip(self, chars: Optional[str] = None) -> Self:
        return self.__class__(self.data.rstrip(chars))

    def split(self, sep: Optional[str] = None, maxsplit: int = -1) -> List[str]:
        return self.data.split(sep, maxsplit)

    def rsplit(self, sep: Optional[str] = None, maxsplit: int = -1) -> List[str]:
        return self.data.rsplit(sep, maxsplit)

    def splitlines(self, keepends: bool = False) -> List[str]:
        return self.data.splitlines(keepends)

    def startswith(self, prefix: str, start: int = 0, end: int = sys.maxsize) -> bool:
        return self.data.startswith(prefix, start, end)

    def strip(self, chars: Optional[str] = None) -> Self:
        return self.__class__(self.data.strip(chars))

    def swapcase(self) -> Self:
        return self.__class__(self.data.swapcase())

    def title(self) -> Self:
        return self.__class__(self.data.title())

    def translate(self, *args: Any) -> Self:
        return self.__class__(self.data.translate(*args))

    def upper(self) -> Self:
        return self.__class__(self.data.upper())

    def zfill(self, width: int) -> Self:
        return self.__class__(self.data.zfill(width))
