import logging

from trans_pad.config import config
from trans_pad.constantes import TranslationServices
from trans_pad.translate.service import (
    TranslationServiceMacOSDictionary,
    TranslationServiceGoogleAJAX,

)

__all__ = [
    'translate_text'
]

logger = logging.getLogger(__name__)

TRANSLATION_SERVICE_MAP = {
    TranslationServices.MacOSDictionary: TranslationServiceMacOSDictionary(),
    TranslationServices.GoogleAJAX: TranslationServiceGoogleAJAX(),
    TranslationServices.GoogleAPI: TranslationServiceGoogleAJAX(),  # TODO
}


class TranslateText:
    @staticmethod
    def translate(query: str) -> str:
        logger.debug('query:{} dest_lang:{}'.format(
            query, config.Common.dest_language
        ))

        return TRANSLATION_SERVICE_MAP[
            config.Common.translation_service
        ].translate_text(query=query, dest_lang=config.Common.dest_language)


translate_text = TranslateText()
