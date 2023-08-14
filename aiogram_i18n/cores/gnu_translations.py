from gettext import GNUTranslations
from typing import Any, Dict, Optional, Set, Union


class SmartGNUTranslations(GNUTranslations):
    def __init__(
        self,
        plural_n_key: Optional[str],
        plural_msg_key: Optional[str],
        plural_context_key: Optional[str],
    ):
        super().__init__()
        self._is_plural: Set[str] = set()
        self._catalog: Dict[Union[str, tuple[str, int]], str] = {}
        self.plural_n_key = plural_n_key
        self.plural_msg_key = plural_msg_key
        self.plural_context_key = plural_context_key

    def parse(self, fp) -> None:
        super()._parse(fp=fp)  # noqa
        for message in self._catalog:
            if isinstance(message, tuple):
                self._is_plural.add(message[0])

    def get(self, key: str, /, **kwargs: Any) -> str:
        context = kwargs.pop(self.plural_context_key, None)
        if n := kwargs.pop(self.plural_n_key, None) and key in self._is_plural:
            msgid2 = kwargs.pop(self.plural_msg_key, key)
            if context is not None:
                return self.npgettext(context=context, msgid1=key, msgid2=msgid2, n=n).format(
                    **kwargs
                )
            else:
                return self.ngettext(msgid1=key, msgid2=msgid2, n=n).format(**kwargs)
        if context:
            return self.pgettext(context=context, message=key).format(**kwargs)
        else:
            return self.gettext(message=key).format(**kwargs)
