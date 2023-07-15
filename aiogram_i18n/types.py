"""
All mutable models from aiogram are listed here and LazyProxy is allowed in string fields.
This code is generated automatically.
"""
from __future__ import annotations

from typing import Optional

from aiogram.types import (
    BotCommand as _BotCommand,
    ChatPermissions as _ChatPermissions,
    ErrorEvent as _ErrorEvent,
    ForceReply as _ForceReply,
    InlineKeyboardButton as _InlineKeyboardButton,
    InlineKeyboardMarkup as _InlineKeyboardMarkup,
    InlineQueryResult as _InlineQueryResult,
    InlineQueryResultArticle as _InlineQueryResultArticle,
    InlineQueryResultAudio as _InlineQueryResultAudio,
    InlineQueryResultCachedAudio as _InlineQueryResultCachedAudio,
    InlineQueryResultCachedDocument as _InlineQueryResultCachedDocument,
    InlineQueryResultCachedGif as _InlineQueryResultCachedGif,
    InlineQueryResultCachedMpeg4Gif as _InlineQueryResultCachedMpeg4Gif,
    InlineQueryResultCachedPhoto as _InlineQueryResultCachedPhoto,
    InlineQueryResultCachedSticker as _InlineQueryResultCachedSticker,
    InlineQueryResultCachedVideo as _InlineQueryResultCachedVideo,
    InlineQueryResultCachedVoice as _InlineQueryResultCachedVoice,
    InlineQueryResultContact as _InlineQueryResultContact,
    InlineQueryResultDocument as _InlineQueryResultDocument,
    InlineQueryResultGame as _InlineQueryResultGame,
    InlineQueryResultGif as _InlineQueryResultGif,
    InlineQueryResultLocation as _InlineQueryResultLocation,
    InlineQueryResultMpeg4Gif as _InlineQueryResultMpeg4Gif,
    InlineQueryResultPhoto as _InlineQueryResultPhoto,
    InlineQueryResultVenue as _InlineQueryResultVenue,
    InlineQueryResultVideo as _InlineQueryResultVideo,
    InlineQueryResultVoice as _InlineQueryResultVoice,
    InputContactMessageContent as _InputContactMessageContent,
    InputInvoiceMessageContent as _InputInvoiceMessageContent,
    InputLocationMessageContent as _InputLocationMessageContent,
    InputMedia as _InputMedia,
    InputMediaAnimation as _InputMediaAnimation,
    InputMediaAudio as _InputMediaAudio,
    InputMediaDocument as _InputMediaDocument,
    InputMediaPhoto as _InputMediaPhoto,
    InputMediaVideo as _InputMediaVideo,
    InputMessageContent as _InputMessageContent,
    InputTextMessageContent as _InputTextMessageContent,
    InputVenueMessageContent as _InputVenueMessageContent,
    KeyboardButton as _KeyboardButton,
    KeyboardButtonPollType as _KeyboardButtonPollType,
    LabeledPrice as _LabeledPrice,
    MenuButton as _MenuButton,
    MenuButtonCommands as _MenuButtonCommands,
    MenuButtonDefault as _MenuButtonDefault,
    MenuButtonWebApp as _MenuButtonWebApp,
    MessageEntity as _MessageEntity,
    PassportElementError as _PassportElementError,
    PassportElementErrorDataField as _PassportElementErrorDataField,
    PassportElementErrorFile as _PassportElementErrorFile,
    PassportElementErrorFiles as _PassportElementErrorFiles,
    PassportElementErrorFrontSide as _PassportElementErrorFrontSide,
    PassportElementErrorReverseSide as _PassportElementErrorReverseSide,
    PassportElementErrorSelfie as _PassportElementErrorSelfie,
    PassportElementErrorTranslationFile as _PassportElementErrorTranslationFile,
    PassportElementErrorTranslationFiles as _PassportElementErrorTranslationFiles,
    PassportElementErrorUnspecified as _PassportElementErrorUnspecified,
    ReplyKeyboardMarkup as _ReplyKeyboardMarkup,
    ReplyKeyboardRemove as _ReplyKeyboardRemove,
)

from aiogram_i18n.lazy import LazyProxy


class BotCommand(_BotCommand):
    command: str | LazyProxy  # type: ignore[assignment]
    description: str | LazyProxy  # type: ignore[assignment]


class ChatPermissions(_ChatPermissions):
    ...


class ErrorEvent(_ErrorEvent):
    ...


class ForceReply(_ForceReply):
    input_field_placeholder: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InlineKeyboardButton(_InlineKeyboardButton):
    text: str | LazyProxy  # type: ignore[assignment]
    url: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    callback_data: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    switch_inline_query: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    switch_inline_query_current_chat: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InlineKeyboardMarkup(_InlineKeyboardMarkup):
    ...


class InlineQueryResult(_InlineQueryResult):
    ...


class InlineQueryResultArticle(_InlineQueryResultArticle):
    type: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    id: str | LazyProxy  # type: ignore[assignment]
    title: str | LazyProxy  # type: ignore[assignment]
    url: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    description: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    thumb_url: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InlineQueryResultAudio(_InlineQueryResultAudio):
    type: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    id: str | LazyProxy  # type: ignore[assignment]
    audio_url: str | LazyProxy  # type: ignore[assignment]
    title: str | LazyProxy  # type: ignore[assignment]
    caption: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    parse_mode: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    performer: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InlineQueryResultCachedAudio(_InlineQueryResultCachedAudio):
    type: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    id: str | LazyProxy  # type: ignore[assignment]
    audio_file_id: str | LazyProxy  # type: ignore[assignment]
    caption: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    parse_mode: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InlineQueryResultCachedDocument(_InlineQueryResultCachedDocument):
    type: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    id: str | LazyProxy  # type: ignore[assignment]
    title: str | LazyProxy  # type: ignore[assignment]
    document_file_id: str | LazyProxy  # type: ignore[assignment]
    description: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    caption: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    parse_mode: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InlineQueryResultCachedGif(_InlineQueryResultCachedGif):
    type: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    id: str | LazyProxy  # type: ignore[assignment]
    gif_file_id: str | LazyProxy  # type: ignore[assignment]
    title: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    caption: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    parse_mode: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InlineQueryResultCachedMpeg4Gif(_InlineQueryResultCachedMpeg4Gif):
    type: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    id: str | LazyProxy  # type: ignore[assignment]
    mpeg4_file_id: str | LazyProxy  # type: ignore[assignment]
    title: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    caption: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    parse_mode: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InlineQueryResultCachedPhoto(_InlineQueryResultCachedPhoto):
    type: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    id: str | LazyProxy  # type: ignore[assignment]
    photo_file_id: str | LazyProxy  # type: ignore[assignment]
    title: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    description: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    caption: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    parse_mode: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InlineQueryResultCachedSticker(_InlineQueryResultCachedSticker):
    type: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    id: str | LazyProxy  # type: ignore[assignment]
    sticker_file_id: str | LazyProxy  # type: ignore[assignment]


class InlineQueryResultCachedVideo(_InlineQueryResultCachedVideo):
    type: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    id: str | LazyProxy  # type: ignore[assignment]
    video_file_id: str | LazyProxy  # type: ignore[assignment]
    title: str | LazyProxy  # type: ignore[assignment]
    description: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    caption: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    parse_mode: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InlineQueryResultCachedVoice(_InlineQueryResultCachedVoice):
    type: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    id: str | LazyProxy  # type: ignore[assignment]
    voice_file_id: str | LazyProxy  # type: ignore[assignment]
    title: str | LazyProxy  # type: ignore[assignment]
    caption: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    parse_mode: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InlineQueryResultContact(_InlineQueryResultContact):
    type: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    id: str | LazyProxy  # type: ignore[assignment]
    phone_number: str | LazyProxy  # type: ignore[assignment]
    first_name: str | LazyProxy  # type: ignore[assignment]
    last_name: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    vcard: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    thumb_url: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InlineQueryResultDocument(_InlineQueryResultDocument):
    type: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    id: str | LazyProxy  # type: ignore[assignment]
    title: str | LazyProxy  # type: ignore[assignment]
    document_url: str | LazyProxy  # type: ignore[assignment]
    mime_type: str | LazyProxy  # type: ignore[assignment]
    caption: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    parse_mode: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    description: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    thumb_url: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InlineQueryResultGame(_InlineQueryResultGame):
    type: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    id: str | LazyProxy  # type: ignore[assignment]
    game_short_name: str | LazyProxy  # type: ignore[assignment]


class InlineQueryResultGif(_InlineQueryResultGif):
    type: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    id: str | LazyProxy  # type: ignore[assignment]
    gif_url: str | LazyProxy  # type: ignore[assignment]
    thumb_url: str | LazyProxy  # type: ignore[assignment]
    thumb_mime_type: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    title: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    caption: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    parse_mode: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InlineQueryResultLocation(_InlineQueryResultLocation):
    type: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    id: str | LazyProxy  # type: ignore[assignment]
    title: str | LazyProxy  # type: ignore[assignment]
    thumb_url: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InlineQueryResultMpeg4Gif(_InlineQueryResultMpeg4Gif):
    type: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    id: str | LazyProxy  # type: ignore[assignment]
    mpeg4_url: str | LazyProxy  # type: ignore[assignment]
    thumb_url: str | LazyProxy  # type: ignore[assignment]
    thumb_mime_type: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    title: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    caption: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    parse_mode: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InlineQueryResultPhoto(_InlineQueryResultPhoto):
    type: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    id: str | LazyProxy  # type: ignore[assignment]
    photo_url: str | LazyProxy  # type: ignore[assignment]
    thumb_url: str | LazyProxy  # type: ignore[assignment]
    title: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    description: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    caption: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    parse_mode: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InlineQueryResultVenue(_InlineQueryResultVenue):
    type: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    id: str | LazyProxy  # type: ignore[assignment]
    title: str | LazyProxy  # type: ignore[assignment]
    address: str | LazyProxy  # type: ignore[assignment]
    foursquare_id: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    foursquare_type: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    google_place_id: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    google_place_type: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    thumb_url: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InlineQueryResultVideo(_InlineQueryResultVideo):
    type: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    id: str | LazyProxy  # type: ignore[assignment]
    video_url: str | LazyProxy  # type: ignore[assignment]
    mime_type: str | LazyProxy  # type: ignore[assignment]
    thumb_url: str | LazyProxy  # type: ignore[assignment]
    title: str | LazyProxy  # type: ignore[assignment]
    caption: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    parse_mode: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    description: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InlineQueryResultVoice(_InlineQueryResultVoice):
    type: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    id: str | LazyProxy  # type: ignore[assignment]
    voice_url: str | LazyProxy  # type: ignore[assignment]
    title: str | LazyProxy  # type: ignore[assignment]
    caption: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    parse_mode: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InputContactMessageContent(_InputContactMessageContent):
    phone_number: str | LazyProxy  # type: ignore[assignment]
    first_name: str | LazyProxy  # type: ignore[assignment]
    last_name: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    vcard: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InputInvoiceMessageContent(_InputInvoiceMessageContent):
    title: str | LazyProxy  # type: ignore[assignment]
    description: str | LazyProxy  # type: ignore[assignment]
    payload: str | LazyProxy  # type: ignore[assignment]
    provider_token: str | LazyProxy  # type: ignore[assignment]
    currency: str | LazyProxy  # type: ignore[assignment]
    provider_data: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    photo_url: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InputLocationMessageContent(_InputLocationMessageContent):
    ...


class InputMedia(_InputMedia):
    ...


class InputMediaAnimation(_InputMediaAnimation):
    type: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    caption: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    parse_mode: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InputMediaAudio(_InputMediaAudio):
    type: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    caption: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    parse_mode: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    performer: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    title: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InputMediaDocument(_InputMediaDocument):
    type: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    caption: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    parse_mode: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InputMediaPhoto(_InputMediaPhoto):
    type: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    caption: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    parse_mode: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InputMediaVideo(_InputMediaVideo):
    type: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    caption: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    parse_mode: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InputMessageContent(_InputMessageContent):
    ...


class InputTextMessageContent(_InputTextMessageContent):
    message_text: str | LazyProxy  # type: ignore[assignment]
    parse_mode: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class InputVenueMessageContent(_InputVenueMessageContent):
    title: str | LazyProxy  # type: ignore[assignment]
    address: str | LazyProxy  # type: ignore[assignment]
    foursquare_id: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    foursquare_type: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    google_place_id: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    google_place_type: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class KeyboardButton(_KeyboardButton):
    text: str | LazyProxy  # type: ignore[assignment]


class KeyboardButtonPollType(_KeyboardButtonPollType):
    type: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class LabeledPrice(_LabeledPrice):
    label: str | LazyProxy  # type: ignore[assignment]


class MenuButton(_MenuButton):
    type: str | LazyProxy  # type: ignore[assignment]
    text: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class MenuButtonCommands(_MenuButtonCommands):
    type: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    text: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class MenuButtonDefault(_MenuButtonDefault):
    type: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    text: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class MenuButtonWebApp(_MenuButtonWebApp):
    type: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    text: str | LazyProxy  # type: ignore[assignment]


class MessageEntity(_MessageEntity):
    type: str | LazyProxy  # type: ignore[assignment]
    url: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    language: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    custom_emoji_id: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class PassportElementError(_PassportElementError):
    ...


class PassportElementErrorDataField(_PassportElementErrorDataField):
    source: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    type: str | LazyProxy  # type: ignore[assignment]
    field_name: str | LazyProxy  # type: ignore[assignment]
    data_hash: str | LazyProxy  # type: ignore[assignment]
    message: str | LazyProxy  # type: ignore[assignment]


class PassportElementErrorFile(_PassportElementErrorFile):
    source: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    type: str | LazyProxy  # type: ignore[assignment]
    file_hash: str | LazyProxy  # type: ignore[assignment]
    message: str | LazyProxy  # type: ignore[assignment]


class PassportElementErrorFiles(_PassportElementErrorFiles):
    source: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    type: str | LazyProxy  # type: ignore[assignment]
    file_hashes: str | LazyProxy  # type: ignore[assignment]
    message: str | LazyProxy  # type: ignore[assignment]


class PassportElementErrorFrontSide(_PassportElementErrorFrontSide):
    source: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    type: str | LazyProxy  # type: ignore[assignment]
    file_hash: str | LazyProxy  # type: ignore[assignment]
    message: str | LazyProxy  # type: ignore[assignment]


class PassportElementErrorReverseSide(_PassportElementErrorReverseSide):
    source: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    type: str | LazyProxy  # type: ignore[assignment]
    file_hash: str | LazyProxy  # type: ignore[assignment]
    message: str | LazyProxy  # type: ignore[assignment]


class PassportElementErrorSelfie(_PassportElementErrorSelfie):
    source: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    type: str | LazyProxy  # type: ignore[assignment]
    file_hash: str | LazyProxy  # type: ignore[assignment]
    message: str | LazyProxy  # type: ignore[assignment]


class PassportElementErrorTranslationFile(_PassportElementErrorTranslationFile):
    source: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    type: str | LazyProxy  # type: ignore[assignment]
    file_hash: str | LazyProxy  # type: ignore[assignment]
    message: str | LazyProxy  # type: ignore[assignment]


class PassportElementErrorTranslationFiles(_PassportElementErrorTranslationFiles):
    source: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    type: str | LazyProxy  # type: ignore[assignment]
    file_hashes: str | LazyProxy  # type: ignore[assignment]
    message: str | LazyProxy  # type: ignore[assignment]


class PassportElementErrorUnspecified(_PassportElementErrorUnspecified):
    source: Optional[str | LazyProxy] = None  # type: ignore[assignment]
    type: str | LazyProxy  # type: ignore[assignment]
    element_hash: str | LazyProxy  # type: ignore[assignment]
    message: str | LazyProxy  # type: ignore[assignment]


class ReplyKeyboardMarkup(_ReplyKeyboardMarkup):
    input_field_placeholder: Optional[str | LazyProxy] = None  # type: ignore[assignment]


class ReplyKeyboardRemove(_ReplyKeyboardRemove):
    ...
