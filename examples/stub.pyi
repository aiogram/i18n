from typing import Any

from aiogram_i18n import I18nContext as _I18nContext
from aiogram_i18n.lazy import LazyFactory as _LazyFactory


class I18nStubs:
    def hello(self, *, user: Any) -> str: ...
    def cur_lang(self, *, language: Any) -> str: ...
    def help(self) -> str: ...


class I18nContext(I18nStubs, _I18nContext):
    ...
    

class LazyFactory(I18nStubs, _LazyFactory):
    ...
    

L: LazyFactory    
