from typing import Dict, Optional, cast

from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.base import StorageKey

from .base import BaseManager


class MemoryManager(BaseManager):
    def __init__(
        self,
        default_locale: Optional[str] = None,
    ):
        super().__init__(default_locale=default_locale)
        self.storage: Dict[StorageKey, str] = {}

    async def set_locale(self, locale: str, state: FSMContext) -> None:
        self.storage[state.key] = locale

    async def get_locale(self, state: FSMContext) -> str:
        return cast(str, self.storage.get(state.key, self.default_locale))
