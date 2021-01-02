from trans_pad.config import config
from trans_pad.constantes import TranslationService
from trans_pad.translate.channel_macos_services import (
    TranslationServiceMacOSDictionary
)
from trans_pad.translate.channel_googletrans import (
    TranslationServiceGoogleTrans,
)

__all__ = [
    'translate_text'
]

CHANNEL_MAP = {
    TranslationService.MacOSDictionary: TranslationServiceMacOSDictionary(),
    TranslationService.GoogleAJAX: TranslationServiceGoogleTrans(),
    TranslationService.GoogleAPI: TranslationServiceGoogleTrans(),
}


class TranslateText:
    def translate(self, query: str) -> str:
        # return self._translate.translate_text(query)
        return CHANNEL_MAP[
            config.Common.translation_service
        ].translate_text(query)


translate_text = TranslateText()
