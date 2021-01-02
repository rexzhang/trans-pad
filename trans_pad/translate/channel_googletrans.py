from googletrans import Translator as GoogleTranslator

from trans_pad.constantes import Languages
from trans_pad.translate.common import TranslateChannelAbstraction


class TranslationServiceGoogleTrans(TranslateChannelAbstraction):
    def __init__(self):
        self.t = GoogleTranslator(service_urls=['translate.google.cn', ])

    def translate_text(self, query: str, dest_lang: Languages) -> str:
        try:
            result = self.t.translate(query, src='auto', dest=dest_lang.value)
        except TypeError:
            return 'some thing wrong...'

        return result.text
