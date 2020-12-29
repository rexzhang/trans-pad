import os.path

from tree_struct_config import (
    Root,
    Branch,
)
from tree_struct_config.exceptiones import ConfigFileException
from rumps import application_support

from trans_pad.constantes import APP_NAME, TranslateChannel


class Config(Root):
    class Common(Branch):
        translate_channel = TranslateChannel.GoogleAJAX

    class GoogleAJAX(Branch):
        service_url = 'translate.google.cn'


config = Config(
    file=os.path.join(application_support(APP_NAME), 'config.json')
)
try:
    config.load()

except (ConfigFileException, TypeError):
    pass
