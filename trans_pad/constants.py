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

    @staticmethod
    def fallback_language():
        return Languages.en

    @staticmethod
    def text_map() -> dict:
        return {
            Languages.AUTO: _('System Language'),

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
    MacOSDictionary: str = 'macos-dictionary'  # macOS 系统自带字典软件
    GoogleAJAX: str = 'google-ajax'
    GoogleAPI: str = 'google-api'

    @staticmethod
    def text_map():
        return {
            TranslationServices.MacOSDictionary: _('macOS System Dictionary'),
            TranslationServices.GoogleAJAX: _('Google Translate'),
            TranslationServices.GoogleAPI: _('Google Translate API'),
        }
