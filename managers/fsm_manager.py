from typing import Dict, Any, Optional
from aiogram.fsm.context import FSMContext
from aiogram.types import TelegramObject

from managers.base import BaseManager


class FsmManager(BaseManager):
    key: str

    def __init__(self, key: str = "locale", default_locale: str = "en"):
        super().__init__(default_locale=default_locale)
        self.key = key

    async def get_locale(self, event: TelegramObject, data: Dict[str, Any]) -> str:
        state: Optional[FSMContext] = data.get("state")
        locale: Optional[str] = None
        if state:
            fsm_data = await state.get_data()
            locale = fsm_data.get(self.key, None)
        if locale is None:
            locale = self.default_locale
            if state:
                await state.update_data(data={self.key: locale})
        return locale

    async def set_locale(self, locale: str, *args: Any, **kwargs: Any) -> None:
        state: FSMContext = kwargs["data"].get("state")
        await state.update_data(data={self.key: locale})
