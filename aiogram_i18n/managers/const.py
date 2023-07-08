from typing import Any, Dict

from aiogram.types import TelegramObject

from aiogram_i18n.managers.base import BaseManager


class ConstManager(BaseManager):
    async def get_locale(self, event: TelegramObject, data: Dict[str, Any]) -> str:
        return self.default_locale

    async def set_locale(self, locale: str, *args: Any, **kwargs: Any) -> None:
        ...
