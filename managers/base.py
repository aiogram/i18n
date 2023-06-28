from abc import abstractmethod
from typing import Dict, Any

from aiogram.types import TelegramObject


class BaseManager:
    default_locale: str

    def __init__(self, default_locale: str = "en"):
        self.default_locale = default_locale

    @abstractmethod
    async def get_locale(self, event: TelegramObject, data: Dict[str, Any]) -> str:
        return self.default_locale

    @abstractmethod
    async def set_locale(self, locale: str, *args, **kwargs) -> None:
        raise NotImplementedError
