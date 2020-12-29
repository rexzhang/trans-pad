from trans_pad.translate.common import Channel
from trans_pad.translate.channel_macos_services import (
    TranslateChannelMacOSServices
)
from trans_pad.translate.channel_googletrans import TranslateChannelGoogleTrans

__all__ = [
    'Channel', 'translate_text'
]

CHANNEL_MAP = {
    Channel.MacOSServices: TranslateChannelMacOSServices,
    Channel.GoogleAJAX: TranslateChannelGoogleTrans,
}


class TranslateText:
    # _channel = Channel.MacOSServices
    _channel = Channel.GoogleAJAX
    _translate = None

    def __init__(self):
        self.set_channel(self._channel)

    def set_channel(self, channel: Channel):
        if channel not in CHANNEL_MAP:
            raise Exception('channel error:{}'.format(channel))

        self._translate = CHANNEL_MAP[channel]()

    def translate(self, query: str) -> str:
        return self._translate.translate_text(query)


translate_text = TranslateText()
