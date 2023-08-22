from typing import Optional, cast

from aiogram import Dispatcher
from aiogram.fsm.context import FSMContext

from aiogram_i18n.managers.base import BaseManager


class FSMManager(BaseManager):
    key: str

    def __init__(self, key: str = "locale", default_locale: Optional[str] = None) -> None:
        super().__init__(default_locale=default_locale)
        self.key = key

    async def startup(self, dispatcher: Dispatcher) -> None:
        try:
            dispatcher.update.outer_middleware._middlewares.index(dispatcher.fsm)  # noqa
        except ValueError as e:
            raise ValueError("dispatcher is not configured to work with fsm") from e

    async def get_locale(self, state: FSMContext) -> str:
        fsm_data = await state.get_data()
        return cast(str, fsm_data.get(self.key, self.default_locale))

    async def set_locale(self, locale: str, state: FSMContext) -> None:
        await state.update_data(data={self.key: locale})
