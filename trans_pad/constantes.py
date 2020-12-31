from enum import IntEnum, Enum, unique

APP_NAME = 'TransPad'


@unique
class TranslateChannel(IntEnum):
    MacOSServices = 1
    GoogleAJAX = 2
    GoogleAPI = 3


@unique
class DestLanguage(Enum):
    pass
