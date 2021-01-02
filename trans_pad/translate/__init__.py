from trans_pad.config import config
from trans_pad.constantes import TranslationServices
from trans_pad.helpers import Logger
from trans_pad.translate.channel_macos_services import (
    TranslationServiceMacOSDictionary
)
from trans_pad.translate.channel_googletrans import (
    TranslationServiceGoogleTrans,
)

__all__ = [
    'translate_text'
]

logger = Logger()

TRANSLATION_SOURCE_MAP = {
    TranslationServices.MacOSDictionary: TranslationServiceMacOSDictionary(),
    TranslationServices.GoogleAJAX: TranslationServiceGoogleTrans(),
    TranslationServices.GoogleAPI: TranslationServiceGoogleTrans(),  # TODO
}


class TranslateText:
    @staticmethod
    def translate(query: str) -> str:
        logger.debug(query, config.Common.dest_language)
        return TRANSLATION_SOURCE_MAP[
            config.Common.translation_service
        ].translate_text(query=query, dest_lang=config.Common.dest_language)


translate_text = TranslateText()
