from __future__ import annotations

from abc import abstractmethod, ABC
from typing import Any, Awaitable, Callable, Dict, Optional, TYPE_CHECKING

from aiogram.dispatcher.event.handler import CallableMixin
from aiogram.types import TelegramObject


class BaseManager(ABC):
    default_locale: Optional[str]
    locale_setter: LocaleSetter

    def __init__(self, default_locale: Optional[str] = None) -> None:
        self.default_locale = default_locale
        self.locale_setter = LocaleSetter(self)

    @abstractmethod
    async def get_locale(self, event: TelegramObject, data: Dict[str, Any]) -> str:
        ...

    if TYPE_CHECKING:
        set_locale: Callable[..., Awaitable[None]]

    else:
        @abstractmethod
        async def set_locale(self, *args: Any, **kwargs: Any) -> None:
            ...


class LocaleSetter(CallableMixin):
    def __init__(self, manager: BaseManager) -> None:
        super().__init__(callback=manager.set_locale)

    async def __call__(self, locale: str, /, **kwargs: Any) -> Any:
        return await self.call(locale, **kwargs)
