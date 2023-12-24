from pathlib import Path
from typing import Any, Callable, Dict, Optional, Union, cast

from aiogram_i18n.exceptions import KeyNotFoundError, NoModuleError
from aiogram_i18n.utils.text_decorator import td

try:
    from fluent.runtime import FluentBundle, FluentResource
except ImportError as e:
    raise NoModuleError(name="FluentRuntimeCore", module_name="fluent.runtime") from e

from aiogram_i18n.cores.base import BaseCore


class FluentRuntimeCore(BaseCore[FluentBundle]):
    def __init__(
        self,
        path: Union[str, Path],
        default_locale: Optional[str] = None,
        use_isolating: bool = False,
        functions: Optional[Dict[str, Callable[..., Any]]] = None,
        pre_compile: bool = True,
        raise_key_error: bool = True,
        use_td: bool = True,
        locales_map: Optional[Dict[str, str]] = None,
    ) -> None:
        super().__init__(path=path, default_locale=default_locale, locales_map=locales_map)
        self.use_isolating = use_isolating
        self.functions = functions or {}
        if use_td:
            self.functions.update(td.functions)
        self.pre_compile = pre_compile
        self.raise_key_error = raise_key_error

    def get(self, message_id: str, locale: Optional[str] = None, /, **kwargs: Any) -> str:
        locale = self.get_locale(locale=locale)
        translator: FluentBundle = self.get_translator(locale=locale)
        try:
            message = translator.get_message(message_id=message_id)
            if message.value is None:
                raise KeyError(message)
        except KeyError:
            if locale := self.locales_map.get(locale):
                return self.get(message_id, locale, **kwargs)
            if self.raise_key_error:
                raise KeyNotFoundError(message_id) from None
            return message_id
        text, errors = translator.format_pattern(pattern=message.value, args=kwargs)
        if errors:
            raise errors[0]
        return cast(str, text)

    def find_locales(self) -> Dict[str, FluentBundle]:
        translations: Dict[str, FluentBundle] = {}
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
        for key, value in fb._messages.items():  # noqa
            if key not in fb._compiled:  # noqa
                fb._compiled[key] = fb._compiler(value)  # noqa
        for key, value in fb._terms.items():  # noqa
            key = f"-{key}"
            if key not in fb._compiled:  # noqa
                fb._compiled[key] = fb._compiler(value)  # noqa
