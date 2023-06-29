from typing import Any, Optional

from magic_filter import MagicFilter


class LazyProxy(str):
    def __init__(self, key: str, magic: Optional[MagicFilter] = None, **kwargs: Any) -> None:
        ...
