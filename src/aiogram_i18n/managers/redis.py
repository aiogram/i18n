from typing import cast

from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.redis import DefaultKeyBuilder, KeyBuilder

from ..exceptions import NoModuleError

try:
    from redis.asyncio.client import Redis
    from redis.asyncio.connection import ConnectionPool
except ImportError as e:
    raise NoModuleError(name="RedisManager", module_name="redis") from e

from .base import BaseManager


class RedisManager(BaseManager):
    def __init__(
        self,
        redis: Redis | ConnectionPool,
        key_builder: KeyBuilder | None = None,
        default_locale: str | None = None,
    ):
        super().__init__(default_locale=default_locale)
        self.key_builder: KeyBuilder = key_builder or DefaultKeyBuilder()
        if isinstance(redis, ConnectionPool):
            redis = Redis(connection_pool=redis)
        self.redis: Redis = redis

    async def get_locale(self, state: FSMContext) -> str:
        redis_key = self.key_builder.build(state.key, "locale")
        value = await self.redis.get(redis_key)
        if isinstance(value, bytes):
            return value.decode("utf-8")
        return value or cast(str, self.default_locale)

    async def set_locale(self, locale: str, state: FSMContext) -> None:
        redis_key = self.key_builder.build(state.key, "locale")
        await self.redis.set(redis_key, locale)
