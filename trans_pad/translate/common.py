from enum import Enum, auto


class Channel(Enum):
    MacOSServices = auto()
    GoogleAJAX = auto()


class TranslateChannelAbstraction:
    def translate_text(self, query: str) -> str:
        return query
