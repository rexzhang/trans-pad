import os.path
from tree_struct_config import (
    Root,
    Branch,
)
from tree_struct_config.exceptiones import ConfigFileException


from trans_pad.constants import (
    Languages,
    TranslationServices,
)
from trans_pad.path import get_path_for_file_config


class Config(Root):
    class Common(Branch):
        auto_launch_on_login: bool = False
        ui_language: Languages = Languages.AUTO

        dest_language: Languages = Languages.AUTO
        translation_service: TranslationServices = TranslationServices.GoogleAJAX

    class Support(Branch):
        sentry_dsn: str = ""

    class Google(Branch):
        service_url: str = "translate.google.cn"


config = Config(file=get_path_for_file_config())
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
