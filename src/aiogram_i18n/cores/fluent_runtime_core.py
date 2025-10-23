from collections.abc import Callable
from pathlib import Path
from typing import Any, cast

from aiogram_i18n.exceptions import FluentMessageError, KeyNotFoundError, NoModuleError
from aiogram_i18n.utils.text_decorator import td

try:
    from fluent.runtime import FluentBundle, FluentResource
except ImportError as e:
    raise NoModuleError(name="FluentRuntimeCore", module_name="fluent.runtime") from e

from aiogram_i18n.cores.base import BaseCore


class FluentRuntimeCore(BaseCore[FluentBundle]):
    def __init__(
        self,
        path: str | Path,
        default_locale: str | None = None,
        use_isolating: bool = False,
        functions: dict[str, Callable[..., Any]] | None = None,
        pre_compile: bool = True,
        raise_key_error: bool = True,
        use_td: bool = True,
        locales_map: dict[str, str] | None = None,
    ) -> None:
        super().__init__(path=path, default_locale=default_locale, locales_map=locales_map)
        self.use_isolating = use_isolating
        self.functions = functions or {}
        if use_td:
            self.functions.update(td.functions)
        self.pre_compile = pre_compile
        self.raise_key_error = raise_key_error

    def get(self, message_id: str, locale: str | None = None, /, **kwargs: Any) -> str:
        locale = self.get_locale(locale=locale)
        translator: FluentBundle = self.get_translator(locale=locale)
        try:
            message = translator.get_message(message_id=message_id)
            if message.value is None:
                raise KeyError(message)  # noqa: TRY301
        except KeyError:
            locale: str | None = self.locales_map.get(locale)
            if locale is not None:
                return self.get(message_id, locale, **kwargs)
            if self.raise_key_error:
                raise KeyNotFoundError(message_id) from None
            return message_id
        text, errors = translator.format_pattern(pattern=message.value, args=kwargs)
        if errors:
            raise FluentMessageError(message_id=message_id, errors=errors)
        return cast(str, text)

    def find_locales(self) -> dict[str, FluentBundle]:
        translations: dict[str, FluentBundle] = {}
        locales = self._extract_locales(self.path)

        for locale, paths in self._find_locales(self.path, locales, ".ftl").items():
            translations[locale] = FluentBundle(
                locales=[locale], use_isolating=self.use_isolating, functions=self.functions
            )

            for path in paths:
                with path.open("r", encoding="utf8") as fp:
                    translations[locale].add_resource(FluentResource(fp.read()))

            if self.pre_compile:
                self.__compile_runtime(translations[locale])

        return translations

    @staticmethod
    def __compile_runtime(fb: FluentBundle) -> None:
        for key, value in fb._messages.items():  # noqa: SLF001
            if key not in fb._compiled:  # noqa: SLF001
                fb._compiled[key] = fb._compiler(value)  # noqa: SLF001
        for key, value in fb._terms.items():  # noqa: SLF001
            key = f"-{key}"
            if key not in fb._compiled:  # noqa: SLF001
                fb._compiled[key] = fb._compiler(value)  # noqa: SLF001
