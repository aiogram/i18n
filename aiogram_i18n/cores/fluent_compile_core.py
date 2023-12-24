from pathlib import Path
from typing import Any, Callable, Dict, Optional, Union, cast

from aiogram_i18n.exceptions import KeyNotFoundError, NoModuleError
from aiogram_i18n.utils.text_decorator import td

try:
    from fluent_compiler.bundle import FluentBundle
except ImportError as e:
    raise NoModuleError(name="FluentCompileCore", module_name="fluent_compiler") from e

from aiogram_i18n.cores.base import BaseCore


class FluentCompileCore(BaseCore[FluentBundle]):
    def __init__(
        self,
        path: Union[str, Path],
        default_locale: Optional[str] = None,
        use_isolating: bool = False,
        functions: Optional[Dict[str, Callable[..., Any]]] = None,
        raise_key_error: bool = True,
        use_td: bool = True,
        locales_map: Optional[Dict[str, str]] = None,
    ) -> None:
        super().__init__(path=path, default_locale=default_locale, locales_map=locales_map)
        self.use_isolating = use_isolating
        self.functions = functions or {}
        if use_td:
            self.functions.update(td.functions)
        self.raise_key_error = raise_key_error

    def get(self, message: str, locale: Optional[str] = None, /, **kwargs: Any) -> str:
        locale = self.get_locale(locale=locale)
        translator: FluentBundle = self.get_translator(locale=locale)
        try:
            text, errors = translator.format(message_id=message, args=kwargs)
        except KeyError:
            if locale := self.locales_map.get(locale):
                return self.get(message, locale, **kwargs)
            if self.raise_key_error:
                raise KeyNotFoundError(message) from None
            return message
        if errors:
            raise errors[0]
        return cast(str, text)  # 'cause fluent_compiler type-ignored

    def find_locales(self) -> Dict[str, FluentBundle]:
        """
        Load all compiled locales from path

        :return: dict with locales
        """
        translations: Dict[str, FluentBundle] = {}
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
