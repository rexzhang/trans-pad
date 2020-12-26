from CoreServices.DictionaryServices import (
    DCSGetTermRangeInString,
    DCSCopyTextDefinition,
    # DCSCopyDefinitionMarkup,
)

from trans_pad.translate.common import TranslateChannelAbstraction


class TranslateChannelMacOSServices(TranslateChannelAbstraction):
    def translate_text(self, query: str) -> str:
        wordrange = (0, len(query))
        # dictresult = DCSGetTermRangeInString(None, searchword, 1)
        dictresult = DCSCopyTextDefinition(None, query, wordrange)
        return str(dictresult)
