from __future__ import annotations

from contextlib import contextmanager
from contextvars import ContextVar, Token
from typing import TYPE_CHECKING, Any, Generic, TypeVar, overload

if TYPE_CHECKING:
    from collections.abc import Generator
    from typing import Literal

ContextInstance = TypeVar("ContextInstance")


class ContextInstanceMixin(Generic[ContextInstance]):
    __context_instance: ContextVar[ContextInstance]

    def __init_subclass__(cls, **kwargs: Any) -> None:
        super().__init_subclass__()
        cls.__context_instance = ContextVar(f"instance_{cls.__name__}")

    @overload
    @classmethod
    def get_current(cls) -> ContextInstance | None:  # pragma: no cover
        ...

    @overload
    @classmethod
    def get_current(cls, no_error: Literal[True]) -> ContextInstance | None:  # pragma: no cover
        ...

    @overload
    @classmethod
    def get_current(cls, no_error: Literal[False]) -> ContextInstance:  # pragma: no cover
        ...

    @classmethod
    def get_current(cls, no_error: bool = True) -> ContextInstance | None:  # pragma: no cover
        try:
            current: ContextInstance | None = cls.__context_instance.get()
        except LookupError:
            if no_error:
                current = None
            else:
                raise

        return current

    @classmethod
    def set_current(cls, value: ContextInstance) -> Token[ContextInstance]:
        if not isinstance(value, cls):
            msg = f"Value should be instance of {cls.__name__!r} not {type(value).__name__!r}"
            raise TypeError(msg)
        return cls.__context_instance.set(value)  # type: ignore[arg-type]

    @classmethod
    def reset_current(cls, token: Token[ContextInstance]) -> None:
        cls.__context_instance.reset(token)

    @classmethod
    @contextmanager
    def with_current(cls, value: ContextInstance) -> Generator[ContextInstance, None, None]:
        token = cls.set_current(value=value)
        yield value
        cls.reset_current(token=token)
