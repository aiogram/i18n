from typing import Optional


STUB_TEMPLATE = """from contextlib import contextmanager
from typing import Any, Union, Generator, Dict
from aiogram_i18n import LazyProxy

{classes}

class I18nStubs:
    {body}

class I18nContext(I18nStubs):
    def get(self, key: str, /, **kwargs: Any) -> str: ...
    async def set_locale(self, locale: str, **kwargs: Any) -> None: ...
    @contextmanager
    def use_locale(self, locale: str) -> Generator["I18nContext", None, None]: ...

class LazyFactory(I18nStubs):
    key_separator: str
    def set_separator(self, key_separator: str) -> None: ...
    def __call__(self, key: str, /, **kwargs: Dict[str, Any]) -> LazyProxy: ...

L: LazyFactory
"""


class BaseNode:
    name: str

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        raise NotImplementedError


class BaseClass(BaseNode):
    attrs: list[BaseNode]
    stub: "BaseClass"
    classes: list

    def add_class(self, class_node: "BaseClass") -> "BaseClass":
        self.attrs.append(class_node)
        class_node.stub.classes.append(class_node)
        return class_node

    def create_class(self, name: str):
        return self.add_class(ClassNode(name=name, stub=self.stub))

    def create_call(self, params: Optional[list[str]] = None):
        return self.create_method(name="__call__", params=params)

    def add_method(self, method: "MethodNode") -> "MethodNode":
        self.attrs.append(method)
        return method

    def create_method(self, name: str, params: Optional[list[str]] = None):
        return self.add_method(method=MethodNode(name=name, params=params))

    def __repr__(self):
        pass


class MethodNode(BaseNode):
    params: list[str]

    def __init__(self, name: str, params: Optional[list[str]] = None, kw_only: bool = True):
        super().__init__(name)
        self.params = params or []
        self.kw_only = kw_only

    def __str__(self):
        params = list(map(lambda x: f'{x}: Any', self.params))
        if params and self.kw_only:
            params.insert(0, "*")
        params.insert(0, "self")
        return f"def {self.name.replace('-', '_')}({', '.join(params)}) -> Union[str, LazyProxy]: ..."

    __repr__ = __str__


class ClassNode(BaseClass):

    def __init__(self, name: str, stub: BaseClass, mro: Optional[list[str]] = None):
        super().__init__(name)
        self.attrs = []
        self.stub = stub
        self.mro = mro

    def __repr__(self):
        body = "\n   ".join(str(i) for i in self.attrs)
        mro = "" if self.mro is None else f"{', '.join(self.mro)}"
        return f"class __{self.name}{mro}:\n   {body}"

    def __str__(self):
        return f"{self.name} = __{self.name}()"


class Stub(BaseClass):

    def __init__(self):
        super().__init__("I18nContext")
        self.attrs = []
        self.stub = self
        self.classes = []

    def __repr__(self):
        return "\n\n".join(repr(i) for i in reversed(self.classes))

    def __str__(self):
        return "\n    ".join(str(i) for i in self.attrs)

    def render(self):
        return STUB_TEMPLATE.format(classes=repr(self), body=str(self))


class Attr:
    def __init__(self, name: str):
        self.attrs: list["Attr"] = []
        self.params = None
        self.name = name

    def render(self, stub: Stub):
        if self.attrs:
            me = stub.create_class(self.name)
            for attr in self.attrs:
                attr.render(me)
            if self.params:
                me.create_call(self.params)
        else:
            stub.create_method(name=self.name, params=self.params)

    def add(self, name: str) -> "Attr":
        if name not in self.attrs:
            self.attrs.append(Attr(name=name))
        return self.attrs[self.attrs.index(name)]  # noqa

    def __hash__(self):
        return self.name.__hash__()

    def __eq__(self, other):
        return hash(other) == self.__hash__()

    def __str__(self):
        text = f"<Attr{{{self.name}}}"
        if self.attrs:
            attrs = '\n    '.join(str(i) for i in self.attrs)
            text += f" attrs: \n    {attrs}"

        if self.params:
            text += f" params: {', '.join(self.params)}"

        return text + ">"

    __repr__ = __str__


class Key(Attr):
    def __init__(self):
        super().__init__("stub")

    def run(self, messages: dict[str, list[str]]):
        for mk, mv in messages.items():
            attr = self
            for smk in mk.split("-"):
                attr = attr.add(smk)
            attr.params = mv
        stub = Stub()
        for attr in self.attrs:
            attr.render(stub=stub)
        return stub.render()

    def __str__(self):
        return "\n".join(str(i) for i in self.attrs)
