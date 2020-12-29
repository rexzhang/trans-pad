from enum import IntEnum

from tree_struct_config import (
    Root,
    Branch,
)
from tree_struct_config.exceptiones import ConfigFileException


class TranslateChannel(IntEnum):
    MacOSServices = 1
    GoogleAJAX = 2


class Config(Root):
    class Common(Branch):
        translate_channel = TranslateChannel.GoogleAJAX

    class GoogleAJAX(Branch):
        service_url = 'translate.google.cn'


config = Config(file='')
try:
    config.load()

except ConfigFileException:
    pass
