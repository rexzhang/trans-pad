from trans_pad.config import config
from trans_pad.constantes import TranslateChannel
from trans_pad.translate.channel_macos_services import (
    TranslateChannelMacOSServices
)
from trans_pad.translate.channel_googletrans import TranslateChannelGoogleTrans

__all__ = [
    'translate_text'
]

CHANNEL_MAP = {
    TranslateChannel.MacOSServices: TranslateChannelMacOSServices(),
    TranslateChannel.GoogleAJAX: TranslateChannelGoogleTrans(),
}


class TranslateText:
    def translate(self, query: str) -> str:
        # return self._translate.translate_text(query)
        return CHANNEL_MAP[config.Common.translate_channel].translate_text(
            query
        )


translate_text = TranslateText()
