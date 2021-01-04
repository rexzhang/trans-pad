from CoreServices.DictionaryServices import (
    DCSGetTermRangeInString,
    DCSCopyTextDefinition,
    # DCSCopyDefinitionMarkup,
)
from googletrans import Translator as GoogleTranslator

from trans_pad.constantes import Languages
from trans_pad.config import config


class TranslateServiceAbstraction:
    def translate_text(self, query: str, dest_lang: Languages) -> str:
        return query


class TranslationServiceMacOSDictionary(TranslateServiceAbstraction):
    def translate_text(self, query: str, dest_lang: Languages) -> str:
        word_range = (0, len(query))
        # dictresult = DCSGetTermRangeInString(None, searchword, 1)
        dict_result = DCSCopyTextDefinition(None, query, word_range)
        return str(dict_result)


class TranslationServiceGoogleAJAX(TranslateServiceAbstraction):
    def __init__(self):
        self._gt = GoogleTranslator()

    def translate_text(self, query: str, dest_lang: Languages) -> str:
        try:
            self._gt.service_urls = (config.Google.service_url,)
            result = self._gt.translate(
                query, src='auto', dest=dest_lang.value
            )

        except TypeError:
            return 'some thing wrong...'

        return result.text
