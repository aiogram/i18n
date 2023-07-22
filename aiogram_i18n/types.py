"""
All mutable models from aiogram are listed here and LazyProxy is allowed in string fields.
This code is generated automatically.
"""
from __future__ import annotations

from typing import Optional, List, Union, Literal

from aiogram import types

from aiogram_i18n.lazy import LazyProxy


class BotCommand(types.BotCommand):
    command: str | LazyProxy  # type: ignore[assignment]
    description: str | LazyProxy  # type: ignore[assignment]


class ChatPermissions(types.ChatPermissions):
    ...


class ForceReply(types.ForceReply):
    input_field_placeholder: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InlineKeyboardButton(types.InlineKeyboardButton):
    text: str | LazyProxy  # type: ignore[assignment]
    url: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    callback_data: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    switch_inline_query: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    switch_inline_query_current_chat: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InlineKeyboardMarkup(types.InlineKeyboardMarkup):
    ...


class InlineQueryResult(types.InlineQueryResult):
    ...


class InlineQueryResultArticle(types.InlineQueryResultArticle):
    id: str | LazyProxy  # type: ignore[assignment]
    title: str | LazyProxy  # type: ignore[assignment]
    url: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    description: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    thumbnail_url: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InlineQueryResultAudio(types.InlineQueryResultAudio):
    id: str | LazyProxy  # type: ignore[assignment]
    audio_url: str | LazyProxy  # type: ignore[assignment]
    title: str | LazyProxy  # type: ignore[assignment]
    caption: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    parse_mode: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    performer: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InlineQueryResultCachedAudio(types.InlineQueryResultCachedAudio):
    id: str | LazyProxy  # type: ignore[assignment]
    audio_file_id: str | LazyProxy  # type: ignore[assignment]
    caption: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    parse_mode: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InlineQueryResultCachedDocument(types.InlineQueryResultCachedDocument):
    id: str | LazyProxy  # type: ignore[assignment]
    title: str | LazyProxy  # type: ignore[assignment]
    document_file_id: str | LazyProxy  # type: ignore[assignment]
    description: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    caption: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    parse_mode: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InlineQueryResultCachedGif(types.InlineQueryResultCachedGif):
    id: str | LazyProxy  # type: ignore[assignment]
    gif_file_id: str | LazyProxy  # type: ignore[assignment]
    title: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    caption: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    parse_mode: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InlineQueryResultCachedMpeg4Gif(types.InlineQueryResultCachedMpeg4Gif):
    id: str | LazyProxy  # type: ignore[assignment]
    mpeg4_file_id: str | LazyProxy  # type: ignore[assignment]
    title: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    caption: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    parse_mode: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InlineQueryResultCachedPhoto(types.InlineQueryResultCachedPhoto):
    id: str | LazyProxy  # type: ignore[assignment]
    photo_file_id: str | LazyProxy  # type: ignore[assignment]
    title: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    description: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    caption: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    parse_mode: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InlineQueryResultCachedSticker(types.InlineQueryResultCachedSticker):
    id: str | LazyProxy  # type: ignore[assignment]
    sticker_file_id: str | LazyProxy  # type: ignore[assignment]


class InlineQueryResultCachedVideo(types.InlineQueryResultCachedVideo):
    id: str | LazyProxy  # type: ignore[assignment]
    video_file_id: str | LazyProxy  # type: ignore[assignment]
    title: str | LazyProxy  # type: ignore[assignment]
    description: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    caption: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    parse_mode: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InlineQueryResultCachedVoice(types.InlineQueryResultCachedVoice):
    id: str | LazyProxy  # type: ignore[assignment]
    voice_file_id: str | LazyProxy  # type: ignore[assignment]
    title: str | LazyProxy  # type: ignore[assignment]
    caption: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    parse_mode: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InlineQueryResultContact(types.InlineQueryResultContact):
    id: str | LazyProxy  # type: ignore[assignment]
    phone_number: str | LazyProxy  # type: ignore[assignment]
    first_name: str | LazyProxy  # type: ignore[assignment]
    last_name: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    vcard: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    thumbnail_url: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InlineQueryResultDocument(types.InlineQueryResultDocument):
    id: str | LazyProxy  # type: ignore[assignment]
    title: str | LazyProxy  # type: ignore[assignment]
    document_url: str | LazyProxy  # type: ignore[assignment]
    mime_type: str | LazyProxy  # type: ignore[assignment]
    caption: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    parse_mode: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    description: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    thumbnail_url: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InlineQueryResultGame(types.InlineQueryResultGame):
    id: str | LazyProxy  # type: ignore[assignment]
    game_short_name: str | LazyProxy  # type: ignore[assignment]


class InlineQueryResultGif(types.InlineQueryResultGif):
    id: str | LazyProxy  # type: ignore[assignment]
    gif_url: str | LazyProxy  # type: ignore[assignment]
    thumbnail_url: str | LazyProxy  # type: ignore[assignment]
    thumbnail_mime_type: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    title: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    caption: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    parse_mode: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InlineQueryResultLocation(types.InlineQueryResultLocation):
    id: str | LazyProxy  # type: ignore[assignment]
    title: str | LazyProxy  # type: ignore[assignment]
    thumbnail_url: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InlineQueryResultMpeg4Gif(types.InlineQueryResultMpeg4Gif):
    id: str | LazyProxy  # type: ignore[assignment]
    mpeg4_url: str | LazyProxy  # type: ignore[assignment]
    thumbnail_url: str | LazyProxy  # type: ignore[assignment]
    thumbnail_mime_type: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    title: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    caption: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    parse_mode: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InlineQueryResultPhoto(types.InlineQueryResultPhoto):
    id: str | LazyProxy  # type: ignore[assignment]
    photo_url: str | LazyProxy  # type: ignore[assignment]
    thumbnail_url: str | LazyProxy  # type: ignore[assignment]
    title: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    description: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    caption: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    parse_mode: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InlineQueryResultVenue(types.InlineQueryResultVenue):
    id: str | LazyProxy  # type: ignore[assignment]
    title: str | LazyProxy  # type: ignore[assignment]
    address: str | LazyProxy  # type: ignore[assignment]
    foursquare_id: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    foursquare_type: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    google_place_id: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    google_place_type: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    thumbnail_url: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InlineQueryResultVideo(types.InlineQueryResultVideo):
    id: str | LazyProxy  # type: ignore[assignment]
    video_url: str | LazyProxy  # type: ignore[assignment]
    mime_type: str | LazyProxy  # type: ignore[assignment]
    thumbnail_url: str | LazyProxy  # type: ignore[assignment]
    title: str | LazyProxy  # type: ignore[assignment]
    caption: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    parse_mode: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    description: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InlineQueryResultVoice(types.InlineQueryResultVoice):
    id: str | LazyProxy  # type: ignore[assignment]
    voice_url: str | LazyProxy  # type: ignore[assignment]
    title: str | LazyProxy  # type: ignore[assignment]
    caption: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    parse_mode: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InputContactMessageContent(types.InputContactMessageContent):
    phone_number: str | LazyProxy  # type: ignore[assignment]
    first_name: str | LazyProxy  # type: ignore[assignment]
    last_name: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    vcard: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InputInvoiceMessageContent(types.InputInvoiceMessageContent):
    title: str | LazyProxy  # type: ignore[assignment]
    description: str | LazyProxy  # type: ignore[assignment]
    payload: str | LazyProxy  # type: ignore[assignment]
    provider_token: str | LazyProxy  # type: ignore[assignment]
    currency: str | LazyProxy  # type: ignore[assignment]
    provider_data: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    photo_url: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InputLocationMessageContent(types.InputLocationMessageContent):
    ...


class InputMedia(types.InputMedia):
    ...


class InputMediaAnimation(types.InputMediaAnimation):
    caption: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    parse_mode: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InputMediaAudio(types.InputMediaAudio):
    caption: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    parse_mode: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    performer: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    title: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InputMediaDocument(types.InputMediaDocument):
    caption: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    parse_mode: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InputMediaPhoto(types.InputMediaPhoto):
    caption: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    parse_mode: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InputMediaVideo(types.InputMediaVideo):
    caption: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    parse_mode: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InputMessageContent(types.InputMessageContent):
    ...


class InputTextMessageContent(types.InputTextMessageContent):
    message_text: str | LazyProxy  # type: ignore[assignment]
    parse_mode: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InputVenueMessageContent(types.InputVenueMessageContent):
    title: str | LazyProxy  # type: ignore[assignment]
    address: str | LazyProxy  # type: ignore[assignment]
    foursquare_id: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    foursquare_type: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    google_place_id: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    google_place_type: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class KeyboardButton(types.KeyboardButton):
    text: str | LazyProxy  # type: ignore[assignment]


class KeyboardButtonPollType(types.KeyboardButtonPollType):
    type: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class LabeledPrice(types.LabeledPrice):
    label: str | LazyProxy  # type: ignore[assignment]


class MenuButton(types.MenuButton):
    type: str | LazyProxy  # type: ignore[assignment]
    text: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class MenuButtonCommands(types.MenuButtonCommands):
    text: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class MenuButtonDefault(types.MenuButtonDefault):
    text: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class MenuButtonWebApp(types.MenuButtonWebApp):
    text: str | LazyProxy  # type: ignore[assignment]


class MessageEntity(types.MessageEntity):
    type: str | LazyProxy  # type: ignore[assignment]
    url: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    language: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    custom_emoji_id: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class PassportElementError(types.PassportElementError):
    ...


class PassportElementErrorDataField(types.PassportElementErrorDataField):
    type: str | LazyProxy  # type: ignore[assignment]
    field_name: str | LazyProxy  # type: ignore[assignment]
    data_hash: str | LazyProxy  # type: ignore[assignment]
    message: str | LazyProxy  # type: ignore[assignment]


class PassportElementErrorFile(types.PassportElementErrorFile):
    type: str | LazyProxy  # type: ignore[assignment]
    file_hash: str | LazyProxy  # type: ignore[assignment]
    message: str | LazyProxy  # type: ignore[assignment]


class PassportElementErrorFiles(types.PassportElementErrorFiles):
    type: str | LazyProxy  # type: ignore[assignment]
    message: str | LazyProxy  # type: ignore[assignment]


class PassportElementErrorFrontSide(types.PassportElementErrorFrontSide):
    type: str | LazyProxy  # type: ignore[assignment]
    file_hash: str | LazyProxy  # type: ignore[assignment]
    message: str | LazyProxy  # type: ignore[assignment]


class PassportElementErrorReverseSide(types.PassportElementErrorReverseSide):
    type: str | LazyProxy  # type: ignore[assignment]
    file_hash: str | LazyProxy  # type: ignore[assignment]
    message: str | LazyProxy  # type: ignore[assignment]


class PassportElementErrorSelfie(types.PassportElementErrorSelfie):
    type: str | LazyProxy  # type: ignore[assignment]
    file_hash: str | LazyProxy  # type: ignore[assignment]
    message: str | LazyProxy  # type: ignore[assignment]


class PassportElementErrorTranslationFile(types.PassportElementErrorTranslationFile):
    type: str | LazyProxy  # type: ignore[assignment]
    file_hash: str | LazyProxy  # type: ignore[assignment]
    message: str | LazyProxy  # type: ignore[assignment]


class PassportElementErrorTranslationFiles(types.PassportElementErrorTranslationFiles):
    type: str | LazyProxy  # type: ignore[assignment]
    message: str | LazyProxy  # type: ignore[assignment]


class PassportElementErrorUnspecified(types.PassportElementErrorUnspecified):
    type: str | LazyProxy  # type: ignore[assignment]
    element_hash: str | LazyProxy  # type: ignore[assignment]
    message: str | LazyProxy  # type: ignore[assignment]


class ReplyKeyboardMarkup(types.ReplyKeyboardMarkup):
    input_field_placeholder: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class ReplyKeyboardRemove(types.ReplyKeyboardRemove):
    ...


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
)


# Load typing forward refs for every TelegramObject
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
