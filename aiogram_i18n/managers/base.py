from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, Awaitable, Callable, Optional

try:
    from aiogram.dispatcher.event.handler import CallableObject as CallableMixin  # type: ignore
except ImportError:
    from aiogram.dispatcher.event.handler import CallableMixin  # type: ignore


class BaseManager(ABC):
    default_locale: Optional[str]

    def __init__(self, default_locale: Optional[str] = None) -> None:
        self.default_locale = default_locale
        self.locale_setter = LocaleSetter(self.set_locale)
        self.locale_getter = LocaleGetter(self.get_locale)

    if TYPE_CHECKING:
        set_locale: Callable[..., Awaitable[None]]
        get_locale: Callable[..., Awaitable[str]]

    else:

        @abstractmethod
        async def set_locale(self, *args: Any, **kwargs: Any) -> None:
            pass

        @abstractmethod
        async def get_locale(self, *args: Any, **kwargs: Any) -> str:
            pass

    async def startup(self, *args: Any, **kwargs: Any) -> None:
        pass

    async def shutdown(self, *args: Any, **kwargs: Any) -> None:
        pass


class LocaleSetter(CallableMixin):
    async def __call__(self, locale: str, /, **kwargs: Any) -> Any:
        return await self.call(locale, **kwargs)


class LocaleGetter(CallableMixin):
    async def __call__(self, **kwargs: Any) -> Any:
        return await self.call(**kwargs)
