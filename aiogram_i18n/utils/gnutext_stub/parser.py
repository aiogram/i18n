import re
from collections.abc import Sequence
from typing import Final, cast

from aiogram_i18n.exceptions import NoModuleError
from aiogram_i18n.utils.cli.echo import red

try:
    from polib import MOEntry, POEntry, mofile, pofile
except ImportError:
    raise NoModuleError(name="GNUText stub generator", module_name="polib") from None

msg_id: Final[re.Pattern[str]] = re.compile(r"^[a-zA-Z_-][a-zA-Z0-9_-]*$")
msg_kwarg: Final[re.Pattern[str]] = re.compile(r"\{(.+)}")
Messages = dict[str, list[str]]


def parse(files: Sequence[POEntry | MOEntry]) -> Messages:
    if not files:
        msg = "no have messages"
        raise ValueError(msg)
    messages: Messages = {}
    for message in files:
        if not msg_id.match(message.msgid):
            msg = f"{message.msgid} is invalid name"
            raise ValueError(msg)
        if not message.msgstr:
            msg = "message is empty"
            raise ValueError(msg)
        kwargs = msg_kwarg.search(message.msgstr)
        messages[message.msgid] = list(kwargs.groups()) if kwargs else []
    return messages


def parse_po_file(file: str) -> Messages:
    try:
        return parse(cast(list[POEntry], pofile(file)))
    except ValueError as e:
        red(f"file {file} {e.args[0]}")
        raise


def parse_mo_file(file: str) -> Messages:
    try:
        return parse(cast(list[MOEntry], mofile(file)))
    except ValueError as e:
        red(f"file {file} {e.args[0]}")
        raise
