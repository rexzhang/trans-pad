from CoreServices.DictionaryServices import (
    DCSGetTermRangeInString,
    DCSCopyTextDefinition,
    # DCSCopyDefinitionMarkup,
)

from trans_pad.constantes import Languages
from trans_pad.translate.common import TranslateChannelAbstraction


class TranslationServiceMacOSDictionary(TranslateChannelAbstraction):
    def translate_text(self, query: str, dest_lang: Languages) -> str:
        word_range = (0, len(query))
        # dictresult = DCSGetTermRangeInString(None, searchword, 1)
        dict_result = DCSCopyTextDefinition(None, query, word_range)
        return str(dict_result)
