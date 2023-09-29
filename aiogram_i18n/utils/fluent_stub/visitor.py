from typing import Dict, Generator, Set

from fluent.syntax import ast
from fluent.syntax.visitor import Visitor


class FluentVisitor(Visitor):
    def __init__(self) -> None:
        self.messages: Dict[str, Set[str]] = {}

    def _get_placeholders(self, element: ast.BaseNode) -> Generator[str, None, None]:
        if isinstance(element, ast.VariableReference):
            yield element.id.name
        elif isinstance(element, ast.Placeable):
            yield from self._get_placeholders(element.expression)
        elif isinstance(element, ast.SelectExpression):
            yield from self._get_placeholders(element.selector)
        elif isinstance(element, ast.FunctionReference):
            for pos_arg in element.arguments.positional:
                yield from self._get_placeholders(pos_arg)

    def visit_Message(self, message: ast.Message) -> None:  # noqa: N802
        m = self.messages[message.id.name] = set()

        if not message.value:
            return self.generic_visit(message)

        for element in message.value.elements:
            if isinstance(element, ast.Placeable):
                m.update(self._get_placeholders(element))

        return self.generic_visit(message)
