"""
All mutable models from aiogram are listed here and LazyProxy is allowed in string fields.
This code is generated automatically.
"""
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Awaitable, Callable, List, Literal, Optional, Union

from aiogram import types

from aiogram_i18n.lazy import LazyProxy

StrOrLazy = Union[str, LazyProxy]
StartupFunction = Callable[..., Awaitable[None]]  # Callable[[I18nContext, ...], Awaitable[None]]


class BotCommand(types.BotCommand):
    command: StrOrLazy
    description: StrOrLazy

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            command: StrOrLazy,
            description: StrOrLazy,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(command=command, description=description, **__pydantic_kwargs)


class ChatPermissions(types.ChatPermissions):
    pass


class ForceReply(types.ForceReply):
    input_field_placeholder: Optional[StrOrLazy] = None

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            input_field_placeholder: Optional[StrOrLazy] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(input_field_placeholder=input_field_placeholder, **__pydantic_kwargs)


class InlineKeyboardButton(types.InlineKeyboardButton):
    text: StrOrLazy
    url: Optional[StrOrLazy] = None
    callback_data: Optional[StrOrLazy] = None
    switch_inline_query: Optional[StrOrLazy] = None
    switch_inline_query_current_chat: Optional[StrOrLazy] = None

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            text: StrOrLazy,
            url: Optional[StrOrLazy] = None,
            callback_data: Optional[StrOrLazy] = None,
            switch_inline_query: Optional[StrOrLazy] = None,
            switch_inline_query_current_chat: Optional[StrOrLazy] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(
                text=text,
                url=url,
                callback_data=callback_data,
                switch_inline_query=switch_inline_query,
                switch_inline_query_current_chat=switch_inline_query_current_chat,
                **__pydantic_kwargs,
            )


class InlineKeyboardMarkup(types.InlineKeyboardMarkup):
    pass


class InlineQueryResult(types.InlineQueryResult):
    pass


class InlineQueryResultArticle(types.InlineQueryResultArticle):
    id: StrOrLazy
    title: StrOrLazy
    url: Optional[StrOrLazy] = None
    description: Optional[StrOrLazy] = None
    thumbnail_url: Optional[StrOrLazy] = None

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            id: StrOrLazy,
            title: StrOrLazy,
            url: Optional[StrOrLazy] = None,
            description: Optional[StrOrLazy] = None,
            thumbnail_url: Optional[StrOrLazy] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(
                id=id,
                title=title,
                url=url,
                description=description,
                thumbnail_url=thumbnail_url,
                **__pydantic_kwargs,
            )


class InlineQueryResultAudio(types.InlineQueryResultAudio):
    id: StrOrLazy
    audio_url: StrOrLazy
    title: StrOrLazy
    caption: Optional[StrOrLazy] = None
    parse_mode: Optional[StrOrLazy] = None
    performer: Optional[StrOrLazy] = None

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            id: StrOrLazy,
            audio_url: StrOrLazy,
            title: StrOrLazy,
            caption: Optional[StrOrLazy] = None,
            parse_mode: Optional[StrOrLazy] = None,
            performer: Optional[StrOrLazy] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(
                id=id,
                audio_url=audio_url,
                title=title,
                caption=caption,
                parse_mode=parse_mode,
                performer=performer,
                **__pydantic_kwargs,
            )


class InlineQueryResultCachedAudio(types.InlineQueryResultCachedAudio):
    id: StrOrLazy
    audio_file_id: StrOrLazy
    caption: Optional[StrOrLazy] = None
    parse_mode: Optional[StrOrLazy] = None

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            id: StrOrLazy,
            audio_file_id: StrOrLazy,
            caption: Optional[StrOrLazy] = None,
            parse_mode: Optional[StrOrLazy] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(
                id=id,
                audio_file_id=audio_file_id,
                caption=caption,
                parse_mode=parse_mode,
                **__pydantic_kwargs,
            )


class InlineQueryResultCachedDocument(types.InlineQueryResultCachedDocument):
    id: StrOrLazy
    title: StrOrLazy
    document_file_id: StrOrLazy
    description: Optional[StrOrLazy] = None
    caption: Optional[StrOrLazy] = None
    parse_mode: Optional[StrOrLazy] = None

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            id: StrOrLazy,
            title: StrOrLazy,
            document_file_id: StrOrLazy,
            description: Optional[StrOrLazy] = None,
            caption: Optional[StrOrLazy] = None,
            parse_mode: Optional[StrOrLazy] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(
                id=id,
                title=title,
                document_file_id=document_file_id,
                description=description,
                caption=caption,
                parse_mode=parse_mode,
                **__pydantic_kwargs,
            )


class InlineQueryResultCachedGif(types.InlineQueryResultCachedGif):
    id: StrOrLazy
    gif_file_id: StrOrLazy
    title: Optional[StrOrLazy] = None
    caption: Optional[StrOrLazy] = None
    parse_mode: Optional[StrOrLazy] = None

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            id: StrOrLazy,
            gif_file_id: StrOrLazy,
            title: Optional[StrOrLazy] = None,
            caption: Optional[StrOrLazy] = None,
            parse_mode: Optional[StrOrLazy] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(
                id=id,
                gif_file_id=gif_file_id,
                title=title,
                caption=caption,
                parse_mode=parse_mode,
                **__pydantic_kwargs,
            )


class InlineQueryResultCachedMpeg4Gif(types.InlineQueryResultCachedMpeg4Gif):
    id: StrOrLazy
    mpeg4_file_id: StrOrLazy
    title: Optional[StrOrLazy] = None
    caption: Optional[StrOrLazy] = None
    parse_mode: Optional[StrOrLazy] = None

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            id: StrOrLazy,
            mpeg4_file_id: StrOrLazy,
            title: Optional[StrOrLazy] = None,
            caption: Optional[StrOrLazy] = None,
            parse_mode: Optional[StrOrLazy] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(
                id=id,
                mpeg4_file_id=mpeg4_file_id,
                title=title,
                caption=caption,
                parse_mode=parse_mode,
                **__pydantic_kwargs,
            )


class InlineQueryResultCachedPhoto(types.InlineQueryResultCachedPhoto):
    id: StrOrLazy
    photo_file_id: StrOrLazy
    title: Optional[StrOrLazy] = None
    description: Optional[StrOrLazy] = None
    caption: Optional[StrOrLazy] = None
    parse_mode: Optional[StrOrLazy] = None

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            id: StrOrLazy,
            photo_file_id: StrOrLazy,
            title: Optional[StrOrLazy] = None,
            description: Optional[StrOrLazy] = None,
            caption: Optional[StrOrLazy] = None,
            parse_mode: Optional[StrOrLazy] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(
                id=id,
                photo_file_id=photo_file_id,
                title=title,
                description=description,
                caption=caption,
                parse_mode=parse_mode,
                **__pydantic_kwargs,
            )


class InlineQueryResultCachedSticker(types.InlineQueryResultCachedSticker):
    id: StrOrLazy
    sticker_file_id: StrOrLazy

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            id: StrOrLazy,
            sticker_file_id: StrOrLazy,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(id=id, sticker_file_id=sticker_file_id, **__pydantic_kwargs)


class InlineQueryResultCachedVideo(types.InlineQueryResultCachedVideo):
    id: StrOrLazy
    video_file_id: StrOrLazy
    title: StrOrLazy
    description: Optional[StrOrLazy] = None
    caption: Optional[StrOrLazy] = None
    parse_mode: Optional[StrOrLazy] = None

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            id: StrOrLazy,
            video_file_id: StrOrLazy,
            title: StrOrLazy,
            description: Optional[StrOrLazy] = None,
            caption: Optional[StrOrLazy] = None,
            parse_mode: Optional[StrOrLazy] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(
                id=id,
                video_file_id=video_file_id,
                title=title,
                description=description,
                caption=caption,
                parse_mode=parse_mode,
                **__pydantic_kwargs,
            )


class InlineQueryResultCachedVoice(types.InlineQueryResultCachedVoice):
    id: StrOrLazy
    voice_file_id: StrOrLazy
    title: StrOrLazy
    caption: Optional[StrOrLazy] = None
    parse_mode: Optional[StrOrLazy] = None

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            id: StrOrLazy,
            voice_file_id: StrOrLazy,
            title: StrOrLazy,
            caption: Optional[StrOrLazy] = None,
            parse_mode: Optional[StrOrLazy] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(
                id=id,
                voice_file_id=voice_file_id,
                title=title,
                caption=caption,
                parse_mode=parse_mode,
                **__pydantic_kwargs,
            )


class InlineQueryResultContact(types.InlineQueryResultContact):
    id: StrOrLazy
    phone_number: StrOrLazy
    first_name: StrOrLazy
    last_name: Optional[StrOrLazy] = None
    vcard: Optional[StrOrLazy] = None
    thumbnail_url: Optional[StrOrLazy] = None

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            id: StrOrLazy,
            phone_number: StrOrLazy,
            first_name: StrOrLazy,
            last_name: Optional[StrOrLazy] = None,
            vcard: Optional[StrOrLazy] = None,
            thumbnail_url: Optional[StrOrLazy] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(
                id=id,
                phone_number=phone_number,
                first_name=first_name,
                last_name=last_name,
                vcard=vcard,
                thumbnail_url=thumbnail_url,
                **__pydantic_kwargs,
            )


class InlineQueryResultDocument(types.InlineQueryResultDocument):
    id: StrOrLazy
    title: StrOrLazy
    document_url: StrOrLazy
    mime_type: StrOrLazy
    caption: Optional[StrOrLazy] = None
    parse_mode: Optional[StrOrLazy] = None
    description: Optional[StrOrLazy] = None
    thumbnail_url: Optional[StrOrLazy] = None

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            id: StrOrLazy,
            title: StrOrLazy,
            document_url: StrOrLazy,
            mime_type: StrOrLazy,
            caption: Optional[StrOrLazy] = None,
            parse_mode: Optional[StrOrLazy] = None,
            description: Optional[StrOrLazy] = None,
            thumbnail_url: Optional[StrOrLazy] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(
                id=id,
                title=title,
                document_url=document_url,
                mime_type=mime_type,
                caption=caption,
                parse_mode=parse_mode,
                description=description,
                thumbnail_url=thumbnail_url,
                **__pydantic_kwargs,
            )


class InlineQueryResultGame(types.InlineQueryResultGame):
    id: StrOrLazy
    game_short_name: StrOrLazy

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            id: StrOrLazy,
            game_short_name: StrOrLazy,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(id=id, game_short_name=game_short_name, **__pydantic_kwargs)


class InlineQueryResultGif(types.InlineQueryResultGif):
    id: StrOrLazy
    gif_url: StrOrLazy
    thumbnail_url: StrOrLazy
    thumbnail_mime_type: Optional[StrOrLazy] = None
    title: Optional[StrOrLazy] = None
    caption: Optional[StrOrLazy] = None
    parse_mode: Optional[StrOrLazy] = None

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            id: StrOrLazy,
            gif_url: StrOrLazy,
            thumbnail_url: StrOrLazy,
            thumbnail_mime_type: Optional[StrOrLazy] = None,
            title: Optional[StrOrLazy] = None,
            caption: Optional[StrOrLazy] = None,
            parse_mode: Optional[StrOrLazy] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(
                id=id,
                gif_url=gif_url,
                thumbnail_url=thumbnail_url,
                thumbnail_mime_type=thumbnail_mime_type,
                title=title,
                caption=caption,
                parse_mode=parse_mode,
                **__pydantic_kwargs,
            )


class InlineQueryResultLocation(types.InlineQueryResultLocation):
    id: StrOrLazy
    title: StrOrLazy
    thumbnail_url: Optional[StrOrLazy] = None

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            id: StrOrLazy,
            title: StrOrLazy,
            thumbnail_url: Optional[StrOrLazy] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(id=id, title=title, thumbnail_url=thumbnail_url, **__pydantic_kwargs)


class InlineQueryResultMpeg4Gif(types.InlineQueryResultMpeg4Gif):
    id: StrOrLazy
    mpeg4_url: StrOrLazy
    thumbnail_url: StrOrLazy
    thumbnail_mime_type: Optional[StrOrLazy] = None
    title: Optional[StrOrLazy] = None
    caption: Optional[StrOrLazy] = None
    parse_mode: Optional[StrOrLazy] = None

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            id: StrOrLazy,
            mpeg4_url: StrOrLazy,
            thumbnail_url: StrOrLazy,
            thumbnail_mime_type: Optional[StrOrLazy] = None,
            title: Optional[StrOrLazy] = None,
            caption: Optional[StrOrLazy] = None,
            parse_mode: Optional[StrOrLazy] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(
                id=id,
                mpeg4_url=mpeg4_url,
                thumbnail_url=thumbnail_url,
                thumbnail_mime_type=thumbnail_mime_type,
                title=title,
                caption=caption,
                parse_mode=parse_mode,
                **__pydantic_kwargs,
            )


class InlineQueryResultPhoto(types.InlineQueryResultPhoto):
    id: StrOrLazy
    photo_url: StrOrLazy
    thumbnail_url: StrOrLazy
    title: Optional[StrOrLazy] = None
    description: Optional[StrOrLazy] = None
    caption: Optional[StrOrLazy] = None
    parse_mode: Optional[StrOrLazy] = None

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            id: StrOrLazy,
            photo_url: StrOrLazy,
            thumbnail_url: StrOrLazy,
            title: Optional[StrOrLazy] = None,
            description: Optional[StrOrLazy] = None,
            caption: Optional[StrOrLazy] = None,
            parse_mode: Optional[StrOrLazy] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(
                id=id,
                photo_url=photo_url,
                thumbnail_url=thumbnail_url,
                title=title,
                description=description,
                caption=caption,
                parse_mode=parse_mode,
                **__pydantic_kwargs,
            )


class InlineQueryResultVenue(types.InlineQueryResultVenue):
    id: StrOrLazy
    title: StrOrLazy
    address: StrOrLazy
    foursquare_id: Optional[StrOrLazy] = None
    foursquare_type: Optional[StrOrLazy] = None
    google_place_id: Optional[StrOrLazy] = None
    google_place_type: Optional[StrOrLazy] = None
    thumbnail_url: Optional[StrOrLazy] = None

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            id: StrOrLazy,
            title: StrOrLazy,
            address: StrOrLazy,
            foursquare_id: Optional[StrOrLazy] = None,
            foursquare_type: Optional[StrOrLazy] = None,
            google_place_id: Optional[StrOrLazy] = None,
            google_place_type: Optional[StrOrLazy] = None,
            thumbnail_url: Optional[StrOrLazy] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(
                id=id,
                title=title,
                address=address,
                foursquare_id=foursquare_id,
                foursquare_type=foursquare_type,
                google_place_id=google_place_id,
                google_place_type=google_place_type,
                thumbnail_url=thumbnail_url,
                **__pydantic_kwargs,
            )


class InlineQueryResultVideo(types.InlineQueryResultVideo):
    id: StrOrLazy
    video_url: StrOrLazy
    mime_type: StrOrLazy
    thumbnail_url: StrOrLazy
    title: StrOrLazy
    caption: Optional[StrOrLazy] = None
    parse_mode: Optional[StrOrLazy] = None
    description: Optional[StrOrLazy] = None

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            id: StrOrLazy,
            video_url: StrOrLazy,
            mime_type: StrOrLazy,
            thumbnail_url: StrOrLazy,
            title: StrOrLazy,
            caption: Optional[StrOrLazy] = None,
            parse_mode: Optional[StrOrLazy] = None,
            description: Optional[StrOrLazy] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(
                id=id,
                video_url=video_url,
                mime_type=mime_type,
                thumbnail_url=thumbnail_url,
                title=title,
                caption=caption,
                parse_mode=parse_mode,
                description=description,
                **__pydantic_kwargs,
            )


class InlineQueryResultVoice(types.InlineQueryResultVoice):
    id: StrOrLazy
    voice_url: StrOrLazy
    title: StrOrLazy
    caption: Optional[StrOrLazy] = None
    parse_mode: Optional[StrOrLazy] = None

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            id: StrOrLazy,
            voice_url: StrOrLazy,
            title: StrOrLazy,
            caption: Optional[StrOrLazy] = None,
            parse_mode: Optional[StrOrLazy] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(
                id=id,
                voice_url=voice_url,
                title=title,
                caption=caption,
                parse_mode=parse_mode,
                **__pydantic_kwargs,
            )


class InputContactMessageContent(types.InputContactMessageContent):
    phone_number: StrOrLazy
    first_name: StrOrLazy
    last_name: Optional[StrOrLazy] = None
    vcard: Optional[StrOrLazy] = None

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            phone_number: StrOrLazy,
            first_name: StrOrLazy,
            last_name: Optional[StrOrLazy] = None,
            vcard: Optional[StrOrLazy] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(
                phone_number=phone_number,
                first_name=first_name,
                last_name=last_name,
                vcard=vcard,
                **__pydantic_kwargs,
            )


class InputInvoiceMessageContent(types.InputInvoiceMessageContent):
    title: StrOrLazy
    description: StrOrLazy
    payload: StrOrLazy
    provider_token: StrOrLazy
    currency: StrOrLazy
    provider_data: Optional[StrOrLazy] = None
    photo_url: Optional[StrOrLazy] = None

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            title: StrOrLazy,
            description: StrOrLazy,
            payload: StrOrLazy,
            provider_token: StrOrLazy,
            currency: StrOrLazy,
            provider_data: Optional[StrOrLazy] = None,
            photo_url: Optional[StrOrLazy] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(
                title=title,
                description=description,
                payload=payload,
                provider_token=provider_token,
                currency=currency,
                provider_data=provider_data,
                photo_url=photo_url,
                **__pydantic_kwargs,
            )


class InputLocationMessageContent(types.InputLocationMessageContent):
    pass


class InputMedia(types.InputMedia):
    pass


class InputMediaAnimation(types.InputMediaAnimation):
    caption: Optional[StrOrLazy] = None
    parse_mode: Optional[StrOrLazy] = None

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            caption: Optional[StrOrLazy] = None,
            parse_mode: Optional[StrOrLazy] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(caption=caption, parse_mode=parse_mode, **__pydantic_kwargs)


class InputMediaAudio(types.InputMediaAudio):
    caption: Optional[StrOrLazy] = None
    parse_mode: Optional[StrOrLazy] = None
    performer: Optional[StrOrLazy] = None
    title: Optional[StrOrLazy] = None

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            caption: Optional[StrOrLazy] = None,
            parse_mode: Optional[StrOrLazy] = None,
            performer: Optional[StrOrLazy] = None,
            title: Optional[StrOrLazy] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(
                caption=caption,
                parse_mode=parse_mode,
                performer=performer,
                title=title,
                **__pydantic_kwargs,
            )


class InputMediaDocument(types.InputMediaDocument):
    caption: Optional[StrOrLazy] = None
    parse_mode: Optional[StrOrLazy] = None

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            caption: Optional[StrOrLazy] = None,
            parse_mode: Optional[StrOrLazy] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(caption=caption, parse_mode=parse_mode, **__pydantic_kwargs)


class InputMediaPhoto(types.InputMediaPhoto):
    caption: Optional[StrOrLazy] = None
    parse_mode: Optional[StrOrLazy] = None

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            caption: Optional[StrOrLazy] = None,
            parse_mode: Optional[StrOrLazy] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(caption=caption, parse_mode=parse_mode, **__pydantic_kwargs)


class InputMediaVideo(types.InputMediaVideo):
    caption: Optional[StrOrLazy] = None
    parse_mode: Optional[StrOrLazy] = None

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            caption: Optional[StrOrLazy] = None,
            parse_mode: Optional[StrOrLazy] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(caption=caption, parse_mode=parse_mode, **__pydantic_kwargs)


class InputMessageContent(types.InputMessageContent):
    pass


class InputTextMessageContent(types.InputTextMessageContent):
    message_text: StrOrLazy
    parse_mode: Optional[StrOrLazy] = None

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            message_text: StrOrLazy,
            parse_mode: Optional[StrOrLazy] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(message_text=message_text, parse_mode=parse_mode, **__pydantic_kwargs)


class InputVenueMessageContent(types.InputVenueMessageContent):
    title: StrOrLazy
    address: StrOrLazy
    foursquare_id: Optional[StrOrLazy] = None
    foursquare_type: Optional[StrOrLazy] = None
    google_place_id: Optional[StrOrLazy] = None
    google_place_type: Optional[StrOrLazy] = None

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            title: StrOrLazy,
            address: StrOrLazy,
            foursquare_id: Optional[StrOrLazy] = None,
            foursquare_type: Optional[StrOrLazy] = None,
            google_place_id: Optional[StrOrLazy] = None,
            google_place_type: Optional[StrOrLazy] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(
                title=title,
                address=address,
                foursquare_id=foursquare_id,
                foursquare_type=foursquare_type,
                google_place_id=google_place_id,
                google_place_type=google_place_type,
                **__pydantic_kwargs,
            )


class KeyboardButton(types.KeyboardButton):
    text: StrOrLazy

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            text: StrOrLazy,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(text=text, **__pydantic_kwargs)


class KeyboardButtonPollType(types.KeyboardButtonPollType):
    type: Optional[StrOrLazy] = None

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            type: Optional[StrOrLazy] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(type=type, **__pydantic_kwargs)


class LabeledPrice(types.LabeledPrice):
    label: StrOrLazy

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            label: StrOrLazy,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(label=label, **__pydantic_kwargs)


class MenuButton(types.MenuButton):
    type: StrOrLazy
    text: Optional[StrOrLazy] = None

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            type: StrOrLazy,
            text: Optional[StrOrLazy] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(type=type, text=text, **__pydantic_kwargs)


class MenuButtonCommands(types.MenuButtonCommands):
    text: Optional[StrOrLazy] = None

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            text: Optional[StrOrLazy] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(text=text, **__pydantic_kwargs)


class MenuButtonDefault(types.MenuButtonDefault):
    text: Optional[StrOrLazy] = None

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            text: Optional[StrOrLazy] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(text=text, **__pydantic_kwargs)


class MenuButtonWebApp(types.MenuButtonWebApp):
    text: StrOrLazy

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            text: StrOrLazy,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(text=text, **__pydantic_kwargs)


class MessageEntity(types.MessageEntity):
    type: StrOrLazy
    url: Optional[StrOrLazy] = None
    language: Optional[StrOrLazy] = None
    custom_emoji_id: Optional[StrOrLazy] = None

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            type: StrOrLazy,
            url: Optional[StrOrLazy] = None,
            language: Optional[StrOrLazy] = None,
            custom_emoji_id: Optional[StrOrLazy] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(
                type=type,
                url=url,
                language=language,
                custom_emoji_id=custom_emoji_id,
                **__pydantic_kwargs,
            )


class PassportElementError(types.PassportElementError):
    pass


class PassportElementErrorDataField(types.PassportElementErrorDataField):
    type: StrOrLazy
    field_name: StrOrLazy
    data_hash: StrOrLazy
    message: StrOrLazy

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            type: StrOrLazy,
            field_name: StrOrLazy,
            data_hash: StrOrLazy,
            message: StrOrLazy,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(
                type=type,
                field_name=field_name,
                data_hash=data_hash,
                message=message,
                **__pydantic_kwargs,
            )


class PassportElementErrorFile(types.PassportElementErrorFile):
    type: StrOrLazy
    file_hash: StrOrLazy
    message: StrOrLazy

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            type: StrOrLazy,
            file_hash: StrOrLazy,
            message: StrOrLazy,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(type=type, file_hash=file_hash, message=message, **__pydantic_kwargs)


class PassportElementErrorFiles(types.PassportElementErrorFiles):
    type: StrOrLazy
    message: StrOrLazy

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            type: StrOrLazy,
            message: StrOrLazy,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(type=type, message=message, **__pydantic_kwargs)


class PassportElementErrorFrontSide(types.PassportElementErrorFrontSide):
    type: StrOrLazy
    file_hash: StrOrLazy
    message: StrOrLazy

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            type: StrOrLazy,
            file_hash: StrOrLazy,
            message: StrOrLazy,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(type=type, file_hash=file_hash, message=message, **__pydantic_kwargs)


class PassportElementErrorReverseSide(types.PassportElementErrorReverseSide):
    type: StrOrLazy
    file_hash: StrOrLazy
    message: StrOrLazy

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            type: StrOrLazy,
            file_hash: StrOrLazy,
            message: StrOrLazy,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(type=type, file_hash=file_hash, message=message, **__pydantic_kwargs)


class PassportElementErrorSelfie(types.PassportElementErrorSelfie):
    type: StrOrLazy
    file_hash: StrOrLazy
    message: StrOrLazy

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            type: StrOrLazy,
            file_hash: StrOrLazy,
            message: StrOrLazy,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(type=type, file_hash=file_hash, message=message, **__pydantic_kwargs)


class PassportElementErrorTranslationFile(types.PassportElementErrorTranslationFile):
    type: StrOrLazy
    file_hash: StrOrLazy
    message: StrOrLazy

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            type: StrOrLazy,
            file_hash: StrOrLazy,
            message: StrOrLazy,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(type=type, file_hash=file_hash, message=message, **__pydantic_kwargs)


class PassportElementErrorTranslationFiles(types.PassportElementErrorTranslationFiles):
    type: StrOrLazy
    message: StrOrLazy

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            type: StrOrLazy,
            message: StrOrLazy,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(type=type, message=message, **__pydantic_kwargs)


class PassportElementErrorUnspecified(types.PassportElementErrorUnspecified):
    type: StrOrLazy
    element_hash: StrOrLazy
    message: StrOrLazy

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            type: StrOrLazy,
            element_hash: StrOrLazy,
            message: StrOrLazy,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(
                type=type, element_hash=element_hash, message=message, **__pydantic_kwargs
            )


class ReplyKeyboardMarkup(types.ReplyKeyboardMarkup):
    input_field_placeholder: Optional[StrOrLazy] = None

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            input_field_placeholder: Optional[StrOrLazy] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(input_field_placeholder=input_field_placeholder, **__pydantic_kwargs)


class ReplyKeyboardRemove(types.ReplyKeyboardRemove):
    pass


__all__ = (
    "BotCommand",
    "ChatPermissions",
    "ForceReply",
    "InlineKeyboardButton",
    "InlineKeyboardMarkup",
    "InlineQueryResult",
    "InlineQueryResultArticle",
    "InlineQueryResultAudio",
    "InlineQueryResultCachedAudio",
    "InlineQueryResultCachedDocument",
    "InlineQueryResultCachedGif",
    "InlineQueryResultCachedMpeg4Gif",
    "InlineQueryResultCachedPhoto",
    "InlineQueryResultCachedSticker",
    "InlineQueryResultCachedVideo",
    "InlineQueryResultCachedVoice",
    "InlineQueryResultContact",
    "InlineQueryResultDocument",
    "InlineQueryResultGame",
    "InlineQueryResultGif",
    "InlineQueryResultLocation",
    "InlineQueryResultMpeg4Gif",
    "InlineQueryResultPhoto",
    "InlineQueryResultVenue",
    "InlineQueryResultVideo",
    "InlineQueryResultVoice",
    "InputContactMessageContent",
    "InputInvoiceMessageContent",
    "InputLocationMessageContent",
    "InputMedia",
    "InputMediaAnimation",
    "InputMediaAudio",
    "InputMediaDocument",
    "InputMediaPhoto",
    "InputMediaVideo",
    "InputMessageContent",
    "InputTextMessageContent",
    "InputVenueMessageContent",
    "KeyboardButton",
    "KeyboardButtonPollType",
    "LabeledPrice",
    "MenuButton",
    "MenuButtonCommands",
    "MenuButtonDefault",
    "MenuButtonWebApp",
    "MessageEntity",
    "PassportElementError",
    "PassportElementErrorDataField",
    "PassportElementErrorFile",
    "PassportElementErrorFiles",
    "PassportElementErrorFrontSide",
    "PassportElementErrorReverseSide",
    "PassportElementErrorSelfie",
    "PassportElementErrorTranslationFile",
    "PassportElementErrorTranslationFiles",
    "PassportElementErrorUnspecified",
    "ReplyKeyboardMarkup",
    "ReplyKeyboardRemove",
    "StartupFunction",
)

for _entity_name in __all__:
    _entity = globals()[_entity_name]
    if not hasattr(_entity, "model_rebuild"):
        continue
    _entity.model_rebuild(
        _types_namespace={
            "List": List,
            "Optional": Optional,
            "Union": Union,
            "Literal": Literal,
            **{k: v for k, v in vars(types).items() if k in types.__all__},
        }
    )

del _entity
del _entity_name
