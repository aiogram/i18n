from typing import Any

from aiogram_i18n.cores import BaseCore


def _check_translations(i18n: BaseCore[Any]) -> None:
    assert i18n.get("cmds-question--start", "en") == "cmds-question--start"
    assert i18n.get("cmds-question--start", "uk") == "cmds-question--start"
    assert (
        i18n.get("dialog-questions-harder--pi-digit", "en") == "dialog-questions-harder--pi-digit"
    )
    assert (
        i18n.get("dialog-questions-harder--pi-digit", "uk") == "dialog-questions-harder--pi-digit"
    )
    assert i18n.get("dialog-questions-harder--e-digit", "en") == "dialog-questions-harder--e-digit"
    assert i18n.get("dialog-questions-harder--e-digit", "uk") == "dialog-questions-harder--e-digit"
    assert (
        i18n.get("dialog-questions-harder--phi-digit", "en")
        == "dialog-questions-harder--phi-digit"
    )
    assert (
        i18n.get("dialog-questions-harder--phi-digit", "uk")
        == "dialog-questions-harder--phi-digit"
    )
    assert i18n.get("dialog-questions-simple--name", "en") == "dialog-questions-simple--name"
    assert i18n.get("dialog-questions-simple--name", "uk") == "dialog-questions-simple--name"
    assert i18n.get("dialog-questions-simple--surname", "en") == "dialog-questions-simple--surname"
    assert i18n.get("dialog-questions-simple--surname", "uk") == "dialog-questions-simple--surname"
    assert i18n.get("dialog-questions-simple--age", "en") == "dialog-questions-simple--age"
    assert i18n.get("dialog-questions-simple--age", "uk") == "dialog-questions-simple--age"
    assert i18n.get("dialog-buttons--add-user", "en") == "dialog-buttons--add-user"
    assert i18n.get("dialog-buttons--add-user", "uk") == "dialog-buttons--add-user"
    assert i18n.get("dialog-buttons--del-user", "en") == "dialog-buttons--del-user"
    assert i18n.get("dialog-buttons--del-user", "uk") == "dialog-buttons--del-user"
    assert i18n.get("dialog-buttons--cancel", "en") == "dialog-buttons--cancel"
    assert i18n.get("dialog-buttons--cancel", "uk") == "dialog-buttons--cancel"
    assert i18n.get("dialog-start--text", "en", name="Bob") == "dialog-start--text Bob"
    assert i18n.get("dialog-start--text", "uk", name="Боб") == "dialog-start--text Боб"
    assert i18n.get("dialog-start--choose", "en", name="Bob") == "dialog-start--choose Bob"
    assert i18n.get("dialog-start--choose", "uk", name="Боб") == "dialog-start--choose Боб"
    assert i18n.get("dialog-window--title", "en") == "dialog-window--title"
    assert i18n.get("dialog-window--title", "uk") == "dialog-window--title"
    assert i18n.get("dialog-window--description", "en") == "dialog-window--description"
    assert i18n.get("dialog-window--description", "uk") == "dialog-window--description"
    assert i18n.get("dialog-window--meta", "en") == "dialog-window--meta"
    assert i18n.get("dialog-window--meta", "uk") == "dialog-window--meta"
    assert i18n.get("greeting-text", "en") == "greeting-text"
    assert i18n.get("greeting-text", "uk") == "greeting-text"
    assert i18n.get("help-text", "en") == "help-text"
    assert i18n.get("help-text", "uk") == "help-text"
    assert i18n.get("cmds-start", "en") == "cmds-start"
    assert i18n.get("cmds-start", "uk") == "cmds-start"
    assert i18n.get("cmds--fast-start", "en") == "cmds--fast-start"
    assert i18n.get("cmds--fast-start", "uk") == "cmds--fast-start"
    assert i18n.get("cmds--slow-start", "en") == "cmds--slow-start"
    assert i18n.get("cmds--slow-start", "uk") == "cmds--slow-start"
