from aiogram import MagicFilter


class LazyProxy(str):
    def __init__(self, key: str, magic: MagicFilter = None, **kwargs): pass