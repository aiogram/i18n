from abc import abstractmethod, ABC
from typing import Dict, Any, TYPE_CHECKING, Awaitable, Callable, Optional

from aiogram.dispatcher.event.handler import CallableMixin
from aiogram.types import TelegramObject


class BaseManager(ABC):
    default_locale: Optional[str]
    set_locale_mixin: CallableMixin

    def __init__(self, default_locale: Optional[str] = None) -> None:
        self.default_locale = default_locale
        self.set_locale_mixin = CallableMixin(self.set_locale)

    @abstractmethod
    async def get_locale(self, event: TelegramObject, data: Dict[str, Any]) -> str:
        ...

    if TYPE_CHECKING:
        set_locale: Callable[..., Awaitable[None]]

    else:
        @abstractmethod
        async def set_locale(self, *args: Any, **kwargs: Any) -> None:
            ...
