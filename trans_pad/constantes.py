from enum import Enum, unique

APP_NAME = 'TransPad'


@unique
class Languages(str, Enum):
    """
    key: '{}_{}.format(ISO 639-3, ISO 3166-1 Alpha-2)
    value : key
    """
    AUTO = 'auto'

    en: str = 'en'
    fr: str = 'fr'
    zh_CN: str = 'zh_CN'

    # def fallback_language(self): # TODO
    #     return self.en


LANGUAGES_TEXT_MAP = {
    Languages.AUTO: '自动',

    Languages.en: 'English',
    Languages.fr: 'Français',
    Languages.zh_CN: '简体中文',
}

UI_LANGUAGES = (
    Languages.en,
    # Languages.fr,
    Languages.zh_CN,
)


# Translation Service

@unique
class TranslationServices(str, Enum):
    MacOSDictionary: str = 'macos-dictionary'
    GoogleAJAX: str = 'google-ajax'
    GoogleAPI: str = 'Google-api'


TRANSLATION_SERVICES_TEXT_MAP = {
    TranslationServices.MacOSDictionary: 'macOS 系统自带字典软件',
    TranslationServices.GoogleAJAX: 'Google 翻译服务',
    TranslationServices.GoogleAPI: 'Google 翻译商业 API',
}


@unique
class DestLanguage(Enum):
    pass


DEST_LANGUAGES = ()
