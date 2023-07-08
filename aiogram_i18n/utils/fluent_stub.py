from os import makedirs, path
from typing import Dict, List

try:
    from fluent.syntax import FluentParser
except ImportError:
    raise ImportError(
        "fluent stub generator can be used only when fluent.syntax installed\n"
        "Just install fluent.syntax (`pip install fluent.syntax`)"
    )
from fluent.syntax.ast import Placeable, FunctionReference, VariableReference, SelectExpression, Junk


def parse(text: str) -> Dict[str, List[str]]:
    messages = {}
    resource = FluentParser().parse(text)
    if not resource.body:
        raise ValueError("no body")
    for message in resource.body:
        if isinstance(message, Junk):
            raise ValueError(message.annotations, "from ", message.content)
        m = messages[message.id.name] = []
        for element in message.value.elements:
            if isinstance(element, Placeable):
                if isinstance(element.expression, FunctionReference):
                    for pos_arg in element.expression.arguments.positional:
                        m.append(pos_arg.id.name)
                elif isinstance(element.expression, VariableReference):
                    m.append(element.expression.id.name)
                elif isinstance(element.expression, SelectExpression):
                    m.append(element.expression.selector.id.name)
    return messages


def parse_file(file: str) -> Dict[str, List[str]]:
    with open(file=file, mode="r", encoding="utf8") as r:
        text = r.read()
    return parse(text=text)


def stub_from_messages(messages: Dict[str, List[str]], kw_only: bool = True) -> str:
    stub_text = """from aiogram_i18n import I18nContext as _I18nContext\nclass I18nContext(_I18nContext):\n\n\n"""
    for name, params in messages.items():
        if params and kw_only:
            params.insert(0, "*")
        params.insert(0, "self")
        stub_text += f"    def {name.replace('-', '_')}({', '.join(params)}) -> str: ...\n"
    return stub_text


def stub_from_file(file: str, kw_only: bool = True) -> str:
    return stub_from_messages(messages=parse_file(file=file), kw_only=kw_only)


def stub_from_string(text: str, kw_only: bool = True) -> str:
    return stub_from_messages(messages=parse(text=text), kw_only=kw_only)


def from_file_to_file(from_file: str, to_file: str, kw_only: bool = True) -> None:
    makedirs(path.dirname(to_file), exist_ok=True)
    with open(file=to_file, mode="w", encoding="utf8") as w:
        w.write(stub_from_file(file=from_file, kw_only=kw_only))


def from_string_to_file(string: str, to_file: str, kw_only: bool = True) -> None:
    makedirs(path.dirname(to_file), exist_ok=True)
    with open(file=to_file, mode="w", encoding="utf8") as w:
        w.write(stub_from_string(text=string, kw_only=kw_only))


def from_files_to_file(files: List[str], to_file: str, kw_only: bool = True):
    makedirs(path.dirname(to_file), exist_ok=True)
    with open(file=to_file, mode="w", encoding="utf8") as w:
        w.write(stub_from_messages(
            messages={k: v for file in files for k, v in parse_file(file).items()}
        ))



