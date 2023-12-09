from contextlib import contextmanager
from contextvars import ContextVar, Token
from typing import Any, Generic, Literal, Optional, TypeVar, cast, overload, Generator

ContextInstance = TypeVar("ContextInstance")


class ContextInstanceMixin(Generic[ContextInstance]):
    __context_instance: ContextVar[ContextInstance]

    def __init_subclass__(cls, **kwargs: Any) -> None:
        super().__init_subclass__()
        cls.__context_instance = ContextVar(f"instance_{cls.__name__}")

    @overload  # noqa: F811
    @classmethod
    def get_current(cls) -> Optional[ContextInstance]:  # pragma: no cover  # noqa: F811
        ...

    @overload  # noqa: F811
    @classmethod
    def get_current(  # noqa: F811
        cls, no_error: Literal[True]
    ) -> Optional[ContextInstance]:  # pragma: no cover  # noqa: F811
        ...

    @overload  # noqa: F811
    @classmethod
    def get_current(  # noqa: F811
        cls, no_error: Literal[False]
    ) -> ContextInstance:  # pragma: no cover  # noqa: F811
        ...

    @classmethod  # noqa: F811
    def get_current(  # noqa: F811
        cls, no_error: bool = True
    ) -> Optional[ContextInstance]:  # pragma: no cover  # noqa: F811
        # on mypy 0.770 I catch that contextvars.ContextVar always contextvars.ContextVar[Any]
        cls.__context_instance = cast(ContextVar[ContextInstance], cls.__context_instance)

        try:
            current: Optional[ContextInstance] = cls.__context_instance.get()
        except LookupError:
            if no_error:
                current = None
            else:
                raise

        return current

    @classmethod
    def set_current(cls, value: ContextInstance) -> Token[ContextInstance]:
        if not isinstance(value, cls):
            raise TypeError(
                f"Value should be instance of {cls.__name__!r} not {type(value).__name__!r}"
            )
        return cls.__context_instance.set(value)

    @classmethod
    def reset_current(cls, token: Token[ContextInstance]) -> None:
        cls.__context_instance.reset(token)

    @classmethod
    @contextmanager
    def with_current(cls, value: ContextInstance) -> Generator[ContextInstance, None, None]:
        token = cls.set_current(value=value)
        yield value
        cls.reset_current(token=token)
