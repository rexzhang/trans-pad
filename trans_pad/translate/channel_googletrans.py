from googletrans import Translator as GoogleTranslator

from trans_pad.translate.common import TranslateChannelAbstraction


class TranslateChannelGoogleTrans(TranslateChannelAbstraction):
    def __init__(self):
        self.t = GoogleTranslator(service_urls=['translate.google.cn', ])

    def translate_text(self, query: str) -> str:
        result = self.t.translate(query, src='auto', dest='zh-cn')
        return result.text
