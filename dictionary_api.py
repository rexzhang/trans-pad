from enum import Enum, auto

from CoreServices.DictionaryServices import (
    DCSGetTermRangeInString,
    DCSCopyTextDefinition,
    # DCSCopyDefinitionMarkup,
)


class Language(Enum):
    AUTO_DETECT = auto
    CHINESE = auto
    ENGLISH = auto


class DictionaryAbstract:
    def __init__(self, in_lang=Language.ENGLISH, out_lang=Language.CHINESE):
        self.in_lang = in_lang
        self.out_lang = out_lang

    def translate(self, key):
        return ''


class DictionaryMacOS(DictionaryAbstract):
    def translate(self, key):
        wordrange = (0, len(key))
        # dictresult = DCSGetTermRangeInString(None, searchword, 1)
        dictresult = DCSCopyTextDefinition(None, key, wordrange)
        return str(dictresult)
