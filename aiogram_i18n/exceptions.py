from typing import Optional, List


class AiogramI18nError(Exception):
    msg: str

    def __str__(self):
        return self.msg


class NoModuleError(AiogramI18nError):
    msg = "{core_name} can be used only when {module_name} installed\n" \
          "Just install {module_name} (`pip install {module_name}`)"

    def __init__(self, core_name: str, module_name: str):
        self.core_name = core_name
        self.module_name = module_name

    def __str__(self):
        return self.msg.format(core_name=self.core_name, module_name=self.module_name)


class NoTranslateFileExistsError(AiogramI18nError):
    msg = "files {ext}in folder ({locale_path}) not found"

    def __init__(self, locale_path: str, ext: Optional[str] = None):
        self.locale_path = locale_path
        self.ext = ext

    def __str__(self):
        if self.ext:
            ext = f"with extension ({self.ext})"
        else:
            ext = ''
        return self.msg.format(ext=ext, locale_path=self.locale_path)


class NoLocalesError(AiogramI18nError):
    msg = "locales cant be empty"


class NoFindLocalesError(AiogramI18nError):
    msg = "locales ({locales}) in path ({path}) not found"
    def __init__(self, locales: List[str], path: str):
        self.locales = locales
        self.path = path

    def __str__(self):
        return self.msg.format(locales=", ".join(self.locales), path=self.path)
