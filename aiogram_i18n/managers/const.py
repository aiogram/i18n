from typing import NoReturn, cast

from aiogram_i18n.managers.base import BaseManager


class ConstManager(BaseManager):
    async def get_locale(self) -> str:
        return cast(str, self.default_locale)

    async def set_locale(self, locale: str) -> NoReturn:
        raise RuntimeError(f"'{type(self).__name__}' doesn't support this method.")
