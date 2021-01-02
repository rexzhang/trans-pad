from enum import Enum, unique

APP_NAME = 'TransPad'


@unique
class TranslationService(Enum):
    MacOSDictionary = 1
    GoogleAJAX = 2
    GoogleAPI = 3


TRANSLATION_SERVICE_TEXT_MAP = {
    TranslationService.MacOSDictionary: 'macOS 系统自带字典软件',
    TranslationService.GoogleAJAX: 'Google 翻译服务',
    TranslationService.GoogleAPI: 'Google 翻译商业 API',
}


@unique
class DestLanguage(Enum):
    pass
