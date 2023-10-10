from typing import Union


def fix_fluent_named_arguments(fix: bool):
    if not fix:
        return
    from fluent.syntax import FluentParserStream, ParseError, ast
    from fluent.syntax.parser import FluentParser, with_span

    @with_span
    def get_literal(
        self, ps: FluentParserStream
    ) -> Union[ast.NumberLiteral, ast.StringLiteral, ast.VariableReference]:
        if ps.is_number_start():
            return self.get_number(ps)
        if ps.current_char == '"':
            return self.get_string(ps)
        if ps.current_char == "$":
            ps.next()
            return ast.VariableReference(self.get_identifier(ps))
        raise ParseError("E0014")

    FluentParser.get_literal = get_literal


def fix_fluent_number_grouping(fix: bool):
    from fluent.runtime.types import FluentNumber

    FluentNumber.default_number_format_options.useGrouping = fix
