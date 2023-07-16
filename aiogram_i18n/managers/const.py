from typing import Any, Dict, NoReturn, cast

from aiogram.types import TelegramObject

from aiogram_i18n.managers.base import BaseManager


class ConstManager(BaseManager):
    async def get_locale(self, event: TelegramObject, data: Dict[str, Any]) -> str:
        return cast(str, self.default_locale)

    async def set_locale(self, locale: str) -> NoReturn:
        raise RuntimeError(
            f"'{type(self).__name__}' doesn't support this method."
        )
