from abc import abstractmethod
from typing import Any

from aiogram.filters.base import Filter

from aiogram_i18n.managers.base import CallableMixin


class BaseLazyFilter(Filter):
    async def call(self, context_key: str, **kwargs: Any):
        return await CallableMixin(callback=self.startup).call(kwargs.pop(context_key), **kwargs)

    @abstractmethod
    async def startup(self, *args: Any, **kwargs: Any) -> None:
        pass
