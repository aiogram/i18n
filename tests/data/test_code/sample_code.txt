"""
This is a code file for testing multiple-extract.
This code should not be executed or linted!
"""


async def methods() -> None:
    await i18n.startup()
    await i18n.shutdown()


def no_separator() -> None:
    client.answer(i18n.get("greeting-text"))  # _default.ftl
    client.answer(i18n.get("help-text"))  # _default.ftl


@on(L("cmds-question--start"))  # cmds/question.ftl
def ask_name() -> None:
    client.answer(i18n.get("dialog-questions-simple--name"))  # dialog/questions/simple.ftl
    client.answer(i18n.get("dialog-questions-simple--surname"))  # dialog/question/simple.ftl
    client.answer(i18n.get("dialog-questions-simple--age"))  # dialog/questions/simple.ftl

    client.answer(i18n.get("dialog-questions-harder--pi-digit"))  # dialog/questions/harder.ftl
    client.answer(i18n.get("dialog-questions-harder--e-digit"))  # dialog/questions/harder.ftl
    client.answer(i18n.get("dialog-questions-harder--phi-digit"))  # dialog/questions/harder.ftl


@on(L("cmds--fast-start"))  # cmds.ftl
@on(L("cmds--slow-start"))  # cmds.ftl
@on(L.cmds.start())  # _default.ftl
def start(name: str) -> None:
    client.answer(i18n.get("dialog-start--text", name=name))  # dialog/start.ftl
    client.answer(i18n.get("dialog-start--choose", name=name))  # dialog/start.ftl


dialog = Window(
    title=I18NFormat("dialog-window--title"),  # dialog/window.ftl
    text=I18NFormat("dialog-window--description"),  # dialog/window.ftl
    meta=I18NFormat("dialog-window--meta"),  # dialog/window.ftl
    buttons=[
        Button(I18NFormat("dialog-buttons--add-user")),  # dialog/buttons.ftl
        Button(I18NFormat("dialog-buttons--del-user")),  # dialog/buttons.ftl
        Button(I18NFormat("dialog-buttons--cancel")),  # dialog/buttons.ftl
    ],
)
