from re import compile, match, search
from typing import Union

from aiogram_i18n.exceptions import NoModuleError
from aiogram_i18n.utils.cli.echo import red

try:
    from polib import MOEntry, POEntry, mofile, pofile
except ImportError:
    raise NoModuleError(name="GnuText stub generator", module_name="polib")


msg_id = compile(r"^[a-zA-Z_-][a-zA-Z0-9_-]*$")
msg_kwarg = compile(r"\{(.+)\}")
MESSAGES = dict[str, list[str]]


def parse(files: list[Union[POEntry, MOEntry]]) -> MESSAGES:
    messages: MESSAGES = {}
    for message in files:
        if not match(msg_id, message.msgid):
            red(f"{message.msgid} is invalid name")
        if not message.msgstr:
            red("Message is empty")
        kwargs = search(msg_kwarg, message.msgstr)
        messages[message.msgid] = list(kwargs.groups()) if kwargs else []
    return messages


def parse_po_file(file: str) -> MESSAGES:
    return parse(pofile(file))


def parse_mo_file(file: str) -> MESSAGES:
    return parse(mofile(file))
