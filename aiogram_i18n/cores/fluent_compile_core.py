from typing import Dict, Callable, Optional, Any, cast

try:
    from fluent_compiler.bundle import FluentBundle  # type: ignore[import]
except ImportError:
    raise ImportError(
        "FluentCompileCore can be used only when fluent_compiler installed\n"
        "Just install fluent_compiler (`pip install fluent_compiler`)"
    )

from aiogram_i18n.cores.base import BaseCore


class FluentCompileCore(BaseCore[FluentBundle]):
    def __init__(
        self,
        path: str,
        default_locale: str = "en",
        use_isolating: bool = True,
        functions: Optional[Dict[str, Callable[..., Any]]] = None
    ) -> None:
        super().__init__()
        self.path = path
        self.use_isolating = use_isolating
        self.functions = functions
        self.default_locale = default_locale

    def get(self, locale: str, key: str, **kwargs: Any) -> str:  # type: ignore[override]
        translator: FluentBundle = self.get_translator(locale=locale)
        text, errors = translator.format(message_id=key, args=kwargs)
        if errors:
            raise ValueError("\n".join(errors))
        return cast(str, text)  # 'cause fluent_compiler type-ignored

    def find_locales(self) -> Dict[str, FluentBundle]:
        """
        Load all compiled locales from path

        :return: dict with locales
        """
        translations: Dict[str, FluentBundle] = {}
        locales = self._extract_locales(self.path)
        for locale, paths in self._find_locales(self.path, locales, ".flt").items():
            texts = []
            for path in paths:
                with open(path, "r", encoding="utf8") as fp:
                    texts.append(fp.read())
            translations[locale] = FluentBundle.from_string(
                text="\n".join(texts), locale=locale,
                use_isolating=self.use_isolating,
                functions=self.functions
            )

        return translations
