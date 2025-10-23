from typing import Any


class AiogramI18nError(Exception):
    message: str

    def __str__(self) -> str:
        return self.message


class NoModuleError(AiogramI18nError):
    message = (
        "{name} can be used only when {module_name} installed\n"
        "Just install {module_name} (`pip install {module_name}`)"
    )

    def __init__(self, name: str, module_name: str) -> None:
        self.name = name
        self.module_name = module_name

    def __str__(self) -> str:
        return self.message.format(name=self.name, module_name=self.module_name)


class NoTranslateFileExistsError(AiogramI18nError):
    message = "files {ext}in folder ({locale_path}) not found"

    def __init__(self, locale_path: str, ext: str | None = None) -> None:
        self.locale_path = locale_path
        self.ext = ext

    def __str__(self) -> str:
        ext = f"with extension ({self.ext})" if self.ext else ""
        return self.message.format(ext=ext, locale_path=self.locale_path)


class NoLocalesError(AiogramI18nError):
    message = "locales cant be empty"


class NoLocalesFoundError(AiogramI18nError):
    message = "locales ({locales}) in path ({path}) not found"

    def __init__(self, locales: list[str], path: str) -> None:
        self.locales = locales
        self.path = path

    def __str__(self) -> str:
        return self.message.format(locales=", ".join(self.locales), path=self.path)


class KeyNotFoundError(AiogramI18nError):
    message = "Key '{key}' not found."

    def __init__(self, key: str) -> None:
        self.key = key

    def __str__(self) -> str:
        return self.message.format(key=self.key)


class ContextItemError(AiogramI18nError):
    message = "context({context}) has no item '{key}'"

    def __init__(self, key: str, context: dict[str, Any]) -> None:
        self.key = key
        self.context = context

    def __str__(self) -> str:
        return self.message.format(key=self.key, context=self.context)


class UnknownLocaleError(AiogramI18nError):
    message = "Unknown locale: '{locale}'"

    def __init__(self, locale: str) -> None:
        self.locale = locale

    def __str__(self) -> str:
        return self.message.format(locale=self.locale)


class FluentMessageError(AiogramI18nError):
    def __init__(self, message_id: str, errors: list[Exception]) -> None:
        self.message_id = message_id
        self.errors = errors

    def __str__(self) -> str:
        error_word = "error" if len(self.errors) == 1 else "errors"
        lines = [f"\n{len(self.errors)} {error_word} for key '{self.message_id}':"]
        lines.extend(f"  {err} (type={type(err).__name__})" for err in self.errors)
        return "\n".join(lines)
