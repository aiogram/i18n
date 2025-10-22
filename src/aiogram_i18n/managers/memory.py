from typing import TYPE_CHECKING, cast

from aiogram.fsm.context import FSMContext

from .base import BaseManager

if TYPE_CHECKING:
    from aiogram.fsm.storage.base import StorageKey


class MemoryManager(BaseManager):
    def __init__(
        self,
        default_locale: str | None = None,
    ):
        super().__init__(default_locale=default_locale)
        self.storage: dict[StorageKey, str] = {}

    async def set_locale(self, locale: str, state: FSMContext) -> None:
        self.storage[state.key] = locale

    async def get_locale(self, state: FSMContext) -> str:
        return cast(str, self.storage.get(state.key, self.default_locale))
