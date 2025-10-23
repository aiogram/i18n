from collections.abc import Callable
from pathlib import Path
from typing import Any, cast

from aiogram_i18n.exceptions import FluentMessageError, KeyNotFoundError, NoModuleError
from aiogram_i18n.utils.text_decorator import td

try:
    from fluent_compiler.bundle import FluentBundle
except ImportError as e:
    raise NoModuleError(name="FluentCompileCore", module_name="fluent_compiler") from e

from aiogram_i18n.cores.base import BaseCore


class FluentCompileCore(BaseCore[FluentBundle]):
    def __init__(
        self,
        path: str | Path,
        default_locale: str | None = None,
        use_isolating: bool = False,
        functions: dict[str, Callable[..., Any]] | None = None,
        raise_key_error: bool = True,
        use_td: bool = True,
        locales_map: dict[str, str] | None = None,
    ) -> None:
        super().__init__(path=path, default_locale=default_locale, locales_map=locales_map)
        self.use_isolating = use_isolating
        self.functions = functions or {}
        if use_td:
            self.functions.update(td.functions)
        self.raise_key_error = raise_key_error

    def get(self, message: str, locale: str | None = None, /, **kwargs: Any) -> str:
        locale = self.get_locale(locale=locale)
        translator: FluentBundle = self.get_translator(locale=locale)
        try:
            text, errors = translator.format(message_id=message, args=kwargs)
        except KeyError:
            locale: str | None = self.locales_map.get(locale)
            if locale is not None:
                return self.get(message, locale, **kwargs)
            if self.raise_key_error:
                raise KeyNotFoundError(message) from None
            return message
        if errors:
            raise FluentMessageError(message_id=message, errors=errors)
        return cast(str, text)  # 'cause fluent_compiler type-ignored

    def find_locales(self) -> dict[str, FluentBundle]:
        """
        Load all compiled locales from path

        :return: dict with locales
        """
        translations: dict[str, FluentBundle] = {}
        locales = self._extract_locales(self.path)
        for locale, paths in self._find_locales(self.path, locales, ".ftl").items():
            texts = []
            for path in paths:
                with path.open("r", encoding="utf8") as fp:
                    texts.append(fp.read())
            translations[locale] = FluentBundle.from_string(
                text="\n".join(texts),
                locale=locale,
                use_isolating=self.use_isolating,
                functions=self.functions,
            )

        return translations
