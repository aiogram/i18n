from abc import abstractmethod
from typing import TYPE_CHECKING, Any, Dict, Union

if TYPE_CHECKING:
    from aiogram_i18n import I18nMiddleware


class BaseLazyFilter:

    async def startup(self, middleware: "I18nMiddleware") -> None:
        pass

    @abstractmethod
    async def __call__(self, *args: Any, **kwargs: Any) -> Union[bool, Dict[str, Any]]:
        pass

    def __await__(self):  # type: ignore # pragma: no cover
        # Is needed only for inspection and this method is never be called
        return self.__call__
