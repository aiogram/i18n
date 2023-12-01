from typing import Optional, Union, cast

from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.redis import DefaultKeyBuilder, KeyBuilder

from ..exceptions import NoModuleError

try:
    from redis.asyncio.client import Redis
except ImportError as e:
    raise NoModuleError(name="RedisManager", module_name="redis") from e
from redis.asyncio.connection import ConnectionPool

from .base import BaseManager


class RedisManager(BaseManager):
    def __init__(
        self,
        redis: Union[Redis, ConnectionPool],
        key_builder: Optional[KeyBuilder] = None,
        default_locale: Optional[str] = None,
    ):
        super().__init__(default_locale=default_locale)
        self.key_builder: KeyBuilder = key_builder or DefaultKeyBuilder()
        if isinstance(redis, ConnectionPool):
            redis = Redis(connection_pool=redis)
        self.redis: Redis = redis

    async def get_locale(self, state: FSMContext) -> str:
        redis_key = self.key_builder.build(state.key, "locale")  # type: ignore[arg-type]
        redis = cast(Redis, self.redis)
        value = await redis.get(redis_key)
        if isinstance(value, bytes):
            return value.decode("utf-8")
        return value or cast(str, self.default_locale)

    async def set_locale(self, locale: str, state: FSMContext) -> None:
        redis_key = self.key_builder.build(state.key, "locale")  # type: ignore[arg-type]
        redis = cast(Redis, self.redis)
        await redis.set(redis_key, locale)
