from CoreServices.DictionaryServices import (
    DCSGetTermRangeInString,
    DCSCopyTextDefinition,
    # DCSCopyDefinitionMarkup,
)
from googletrans import Translator as GoogleTranslator
from googletrans.constants import DEFAULT_SERVICE_URLS

from trans_pad.constantes import Languages
from trans_pad.config import config
from trans_pad.helpers import MacOSInfo


class TranslateServiceAbstraction:
    def translate_text(self, query: str, dest_lang: Languages) -> str:
        return query


class TranslationServiceMacOSDictionary(TranslateServiceAbstraction):
    def translate_text(self, query: str, dest_lang: Languages) -> str:
        word_range = (0, len(query))
        # dictresult = DCSGetTermRangeInString(None, searchword, 1)
        dict_result = DCSCopyTextDefinition(None, query, word_range)
        return str(dict_result)


# Google service
GOOGLE_LANGUAGE_ID_MAP = {
    Languages.en: 'en',
    Languages.fr: 'fr',
    Languages.zh_CN: 'zh-cn',
}

GOOGLE_LANGUAGES = GOOGLE_LANGUAGE_ID_MAP.keys()
GOOGLE_SERVICE_URLS = DEFAULT_SERVICE_URLS


class TranslationServiceGoogleAJAX(TranslateServiceAbstraction):
    def __init__(self):
        self._gt = GoogleTranslator()

    @staticmethod
    def _get_dest_lang_id(dest_lang: Languages) -> str:
        if dest_lang == Languages.AUTO:
            return MacOSInfo().system_language.value

        if dest_lang.value in GOOGLE_LANGUAGE_ID_MAP:
            return dest_lang.value

        raise ValueError('dest_lang not in support:{}'.format(dest_lang))

    def translate_text(self, query: str, dest_lang: Languages) -> str:
        try:
            self._gt.service_urls = (config.Google.service_url,)
            result = self._gt.translate(
                query, src='auto', dest=GOOGLE_LANGUAGE_ID_MAP[
                    self._get_dest_lang_id(dest_lang)
                ]
            )

        except (TypeError, ValueError) as e:
            return 'some thing wrong...{}'.format(e)

        return result.text
