from typing import Any, Union

from aiogram_i18n import I18nContext as _I18nContext
from aiogram_i18n.lazy import LazyProxy, LazyFactory as _LazyFactory


class I18nStubs:
    def hello(self, *, user: Any) -> Union[str, LazyProxy]: ...
    def cur_lang(self, *, language: Any) -> Union[str, LazyProxy]: ...
    def help(self) -> Union[str, LazyProxy]: ...


class I18nContext(I18nStubs, _I18nContext):
    ...
    

class LazyFactory(I18nStubs, _LazyFactory):
    ...
    

L: LazyFactory    
