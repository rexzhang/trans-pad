from enum import Enum, auto

from CoreServices.DictionaryServices import (
    DCSGetTermRangeInString,
    DCSCopyTextDefinition,
    # DCSCopyDefinitionMarkup,
)

from googletrans import Translator as GoogleTranslator


class Language(Enum):
    AUTO = auto
    CHINESE = auto
    ENGLISH = auto


class DictionaryAbstract:
    def __init__(self, in_lang=Language.ENGLISH, out_lang=Language.CHINESE):
        self.in_lang = in_lang
        self.out_lang = out_lang

    def translate(self, query):
        return ''


class DictionaryMacOS(DictionaryAbstract):
    def translate(self, query):
        wordrange = (0, len(query))
        # dictresult = DCSGetTermRangeInString(None, searchword, 1)
        dictresult = DCSCopyTextDefinition(None, query, wordrange)
        return str(dictresult)


class DictionaryGoogleTrans(DictionaryAbstract):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self._t = GoogleTranslator(service_urls=['translate.google.cn', ])
        self._t = GoogleTranslator(service_urls=['translate.google.com', ])

    def translate(self, query):
        result = self._t.translate(query, src='auto', dest='zh-cn')
        return result.text
