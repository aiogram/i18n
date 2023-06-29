from abc import abstractmethod, ABC
from typing import Dict, Any

from aiogram.types import TelegramObject


class BaseManager(ABC):
    default_locale: str

    def __init__(self, default_locale: str = "en") -> None:
        self.default_locale = default_locale

    @abstractmethod
    async def get_locale(self, event: TelegramObject, data: Dict[str, Any]) -> str:
        ...

    @abstractmethod
    async def set_locale(self, locale: str, *args: Any, **kwargs: Any) -> None:
        ...
