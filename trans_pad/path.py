from pathlib import Path

from rumps import application_support

from trans_pad.constants import APP_NAME


def get_path_for__file__() -> str:
    return __file__


def get_path_for_file_config() -> Path:
    return Path(application_support(APP_NAME)).joinpath("config.json")


def get_path_for_i18n() -> Path:
    path = Path(__file__).parent.parent
    # if path.name == 'python38.zip':
    if path.name.startswith("python3."):
        # in app Bundle
        path = path.parent.parent

    return path.joinpath("po")
