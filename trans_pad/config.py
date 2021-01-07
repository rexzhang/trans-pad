import os.path

from tree_struct_config import (
    Root,
    Branch,
)
from tree_struct_config.exceptiones import ConfigFileException
from rumps import application_support

from trans_pad.constants import (
    APP_NAME,
    Languages,
    TranslationServices,
)


class Config(Root):
    class Common(Branch):
        auto_launch_on_login: bool = False
        ui_language: Languages = Languages.AUTO

        dest_language: Languages = Languages.AUTO
        translation_service: TranslationServices = TranslationServices.GoogleAJAX

    class Support(Branch):
        sentry_dsn: str = ''

    class Google(Branch):
        service_url: str = 'translate.google.cn'


config = Config(
    file=os.path.join(application_support(APP_NAME), 'config.json')
)
try:
    config.load()

    # TODO, fix it in tree_struct_config
    try:
        config.Common.ui_language = Languages(config.Common.ui_language)
    except ValueError:
        config.Common.ui_language = Languages.AUTO
    try:
        config.Common.dest_language = Languages(config.Common.dest_language)
    except ValueError:
        config.Common.dest_language = Languages.AUTO

    config.Common.translation_service = TranslationServices(
        config.Common.translation_service
    )

except (ConfigFileException, TypeError):
    pass
