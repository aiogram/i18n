from typing import Optional, List


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

    def __init__(
        self,
        locale_path: str, ext: Optional[str] = None
    ) -> None:
        self.locale_path = locale_path
        self.ext = ext

    def __str__(self) -> str:
        ext = f"with extension ({self.ext})" if self.ext else ""
        return self.message.format(ext=ext, locale_path=self.locale_path)


class NoLocalesError(AiogramI18nError):
    message = "locales cant be empty"


class NoLocalesFoundError(AiogramI18nError):
    message = "locales ({locales}) in path ({path}) not found"

    def __init__(self, locales: List[str], path: str) -> None:
        self.locales = locales
        self.path = path

    def __str__(self) -> str:
        return self.message.format(locales=", ".join(self.locales), path=self.path)


class KeyNotFound(AiogramI18nError):
    message = "Key '{key}' not found."

    def __init__(self, key: str) -> None:
        self.key = key

    def __str__(self) -> str:
        return self.message.format(key=self.key)
