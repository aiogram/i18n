from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Optional

STUB_TEMPLATE = """from contextlib import contextmanager
from typing import Any, Generator, Union

from aiogram_i18n import LazyProxy


{classes}

class I18nStubs:
    {body}

class I18nContext(I18nStubs):
    def get(self, key: str, /, **kwargs: Any) -> str: ...
    async def set_locale(self, locale: str, **kwargs: Any) -> None: ...
    @contextmanager
    def use_locale(self, locale: str) -> Generator[I18nContext, None, None]: ...
    @contextmanager
    def use_context(self, **kwargs: Any) -> Generator[I18nContext, None, None]: ...
    def set_context(self, **kwargs: Any) -> None: ...

class LazyFactory(I18nStubs):
    key_separator: str
    def set_separator(self, key_separator: str) -> None: ...
    def __call__(self, key: str, /, **kwargs: dict[str, Any]) -> LazyProxy: ...

L: LazyFactory
"""


class BaseNode(ABC):
    name: str

    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def __str__(self) -> str:
        ...


class BaseClass(BaseNode, ABC):
    attrs: list[BaseNode]
    stub: BaseClass
    classes: list[BaseClass]
    number: int

    def add_class(self, class_node: BaseClass) -> BaseClass:
        self.attrs.append(class_node)
        while class_node in class_node.stub.classes:
            class_node.number += 1
        class_node.stub.classes.append(class_node)
        return class_node

    def create_class(self, name: str) -> BaseClass:
        return self.add_class(ClassNode(name=name, stub=self.stub))

    def create_call(self, params: Optional[list[str]] = None) -> MethodNode:
        return self.create_method(name="__call__", params=params)

    def add_method(self, method: MethodNode) -> MethodNode:
        self.attrs.append(method)
        return method

    def create_method(self, name: str, params: Optional[list[str]] = None) -> MethodNode:
        return self.add_method(method=MethodNode(name=name, params=params))

    @abstractmethod
    def __repr__(self) -> str:
        ...


class MethodNode(BaseNode):
    params: list[str]

    def __init__(
        self, name: str, params: Optional[list[str]] = None, kw_only: bool = True
    ) -> None:
        super().__init__(name)
        self.params = params or []
        self.kw_only = kw_only

    def __str__(self) -> str:
        params = [f"{x}: Any" for x in self.params]
        if params and self.kw_only:
            params.insert(0, "*")
        params.insert(0, "self")
        return f"def {self.name.replace('-', '_')}({', '.join(params)}) -> str: ..."

    __repr__ = __str__


class ClassNode(BaseClass):
    def __init__(
        self,
        name: str,
        stub: BaseClass,
        mro: Optional[list[str]] = None,
        number: int = 0,
    ) -> None:
        super().__init__(name)
        self.number = number
        self.attrs = []
        self.stub = stub
        self.mro = mro

    def __repr__(self) -> str:
        body = "\n    ".join(str(i) for i in self.attrs)
        mro = "" if self.mro is None else f"{', '.join(self.mro)}"
        return f"class {self.class_name}{mro}:\n    {body}"

    def __str__(self) -> str:
        return f"{self.name} = {self.class_name}()"

    @property
    def class_name(self) -> str:
        return f"{self.name.title()}{self.number or ''}"

    def __hash__(self) -> int:
        return self.class_name.__hash__()

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, ClassNode):
            return hash(other) == hash(self)
        raise ValueError(f"unknown type {type(other)}")


class Stub(BaseClass):
    def __init__(self) -> None:
        super().__init__("I18nContext")
        self.attrs = []
        self.stub = self
        self.classes = []

    def __repr__(self) -> str:
        return "\n\n".join(repr(i) for i in reversed(self.classes))

    def __str__(self) -> str:
        return "\n    ".join(str(i) for i in self.attrs)

    def render(self) -> str:
        return STUB_TEMPLATE.format(classes=repr(self), body=str(self))


class Attr:
    def __init__(self, name: str) -> None:
        self.attrs: list[Attr] = []
        self.params: Optional[list[str]] = None
        self.name = name

    def render(self, node: BaseClass) -> None:
        if self.attrs:
            me = node.create_class(self.name)
            for attr in self.attrs:
                attr.render(me)
            if self.params is not None:
                me.create_call(self.params)
        else:
            node.create_method(name=self.name, params=self.params)

    def add(self, name: str) -> Attr:
        if name not in self.attrs:
            self.attrs.append(Attr(name=name))
        return self.attrs[self.attrs.index(name)]  # type: ignore[arg-type]

    def __hash__(self) -> int:
        return self.name.__hash__()

    def __eq__(self, other: object) -> bool:
        return hash(other) == self.__hash__()

    def __str__(self) -> str:
        text = f"<Attr{{{self.name}}}"
        if self.attrs:
            attrs = "\n    ".join(str(i) for i in self.attrs)
            text += f" attrs: \n    {attrs}"

        if self.params:
            text += f" params: {', '.join(self.params)}"

        return text + ">"

    __repr__ = __str__


class Key(Attr):
    def __init__(self) -> None:
        super().__init__("stub")

    def run(self, messages: dict[str, list[str]]) -> str:
        for mk, mv in messages.items():
            attr: Attr = self
            for smk in mk.split("-"):
                attr = attr.add(smk)
            attr.params = mv
        stub = Stub()
        for attr_ in self.attrs:
            attr_.render(node=stub)
        return stub.render()

    def __str__(self) -> str:
        return "\n".join(str(i) for i in self.attrs)
