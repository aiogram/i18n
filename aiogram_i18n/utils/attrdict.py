from typing import Any, Dict

from aiogram_i18n.exceptions import ContextItemError


class AttrDict:
    """
    A wrapper over dict which where element can be accessed as regular attributes
    """

    def __init__(self, data: Dict[str, Any]) -> None:
        self.data: Dict[str, Any] = data

    def __getitem__(self, item: Any) -> Any:
        try:
            return self.data[item]
        except KeyError:
            raise ContextItemError(key=item, context=self.data)

    def __getattr__(self, item: str) -> Any:
        return self.__getitem__(item)
