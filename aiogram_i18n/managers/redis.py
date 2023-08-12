from typing import Optional, Union, cast

from aiogram import Dispatcher
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.redis import DefaultKeyBuilder, KeyBuilder, RedisStorage

from ..exceptions import NoModuleError

try:
    from redis.asyncio.client import Redis
except ImportError:
    raise NoModuleError(name="RedisManager", module_name="redis")
from redis.asyncio.connection import ConnectionPool

from .base import BaseManager


class RedisManager(BaseManager):
    def __init__(
        self,
        redis: Optional[Union[Redis[bytes], ConnectionPool]] = None,
        key_builder: Optional[KeyBuilder] = None,
        default_locale: Optional[str] = None,
    ):
        super().__init__(default_locale=default_locale)
        self.key_builder: KeyBuilder = key_builder or DefaultKeyBuilder()
        if isinstance(redis, ConnectionPool):
            redis = Redis(connection_pool=redis)
        self.redis: Optional[Redis[bytes]] = redis

    async def startup(self, dispatcher: Dispatcher) -> None:
        if self.redis is not None:
            return
        if not isinstance(dispatcher.fsm.storage, RedisStorage):
            raise ValueError("no source specified with Redis")
        self.redis = dispatcher.fsm.storage.redis

    async def get_locale(self, state: FSMContext) -> str:
        redis_key = self.key_builder.build(state.key, "locale")  # type: ignore[arg-type]
        redis = cast(Redis[bytes], self.redis)
        value = await redis.get(redis_key)
        if isinstance(value, bytes):
            return value.decode("utf-8")
        return value or cast(str, self.default_locale)

    async def set_locale(self, locale: str, state: FSMContext) -> None:
        redis_key = self.key_builder.build(state.key, "locale")  # type: ignore[arg-type]
        redis = cast(Redis[bytes], self.redis)
        await redis.set(redis_key, locale)
