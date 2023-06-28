from typing import Dict, Callable
from cores.base import BaseCore

from fluent.runtime import FluentBundle, FluentResource


class FluentRuntimeCore(BaseCore):
    locales: Dict[str, FluentBundle]

    def __init__(self, path: str, default_locale: str = "en",
                 use_isolating: bool = True,
                 functions: Dict[str, Callable] = None,
                 pre_compile: bool = True):
        self.path = path
        self.use_isolating = use_isolating
        self.functions = functions
        self.default_locale = default_locale
        self.pre_compile = pre_compile

    def get(self, locale: str, key: str, **kwargs):
        translator: FluentBundle = self.get_translator(locale=locale)
        text, errors = translator.format_pattern(
            pattern=translator.get_message(message_id=key).value,
            args=kwargs
        )
        if errors:
            raise errors[0]
        return text

    async def startup(self, *args, **kwargs):
        self.locales = self.find_locales()

    def find_locales(self) -> Dict[str, FluentBundle]:
        translations: Dict[str, FluentBundle] = {}
        locales = self._extract_locales(self.path)
        for locale, paths in self._find_locales(self.path, locales, ".flt").items():
            translations[locale] = FluentBundle(
                locales=[locale],
                use_isolating=self.use_isolating, functions=self.functions
            )
            for path in paths:
                with open(path, "r", encoding="utf8") as fp:
                    translations[locale].add_resource(FluentResource(fp.read()))
            if self.pre_compile:
                self.__compile_runtime(translations[locale])

        return translations

    @staticmethod
    def __compile_runtime(fb: FluentBundle):
        for key, value in fb._messages.items():  # noqa
            if key not in fb._compiled:  # noqa
                fb._compiled[key] = fb._compiler(value)  # noqa
        for key, value in fb._terms.items():  # noqa
            key = f"-{key}"
            if key not in fb._compiled:  # noqa
                fb._compiled[key] = fb._compiler(value)  # noqa
