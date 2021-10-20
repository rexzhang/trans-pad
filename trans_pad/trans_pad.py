import logging

import rumps

from trans_pad.constants import APP_NAME
from trans_pad.path import (
    get_path_for_file_config,
    get_path_for__file__,
)
from trans_pad.translate import translate_text
from trans_pad.result_pad import ResultPad
from trans_pad.service import register_service
from trans_pad.ui.preferences import PreferencesWindow

logger = logging.Logger(__name__)


class TransPadApp:
    result_pad = None
    preferences_window = None

    def __init__(self):
        menu = [
            rumps.MenuItem(
                title="{}...".format(_("Preferences")),
                key=",",
                callback=lambda sender: self.window_preferences(sender),
            ),
            rumps.MenuItem(
                title=_("About TransPad"),
                callback=lambda _: self.window_about(),
            ),
            rumps.separator,
        ]

        self.app = rumps.App(
            APP_NAME, icon="icon.icns", template=True, menu=menu, quit_button=_("Quit")
        )

        register_service("TransPadService")
        return

    def run(self):
        self.app.run()

    @staticmethod
    def window_about():
        rumps.alert(
            title=_("About TransPad"),
            message="ProjectURL:https://github.com/rexzhang/trans-pad \nConfigPath:{} \n{}".format(
                get_path_for_file_config(), get_path_for__file__()
            ),
            icon_path="icon.icns",
        )
        # rumps.Window('message').run()

    def test(self):
        if self.result_pad is None:
            self.result_pad = ResultPad()

        self.result_pad.result = translate_text.translate("This is a test!")
        self.result_pad.display()

    def window_preferences(self, sender):
        if self.preferences_window is None:
            self.preferences_window = PreferencesWindow()

        self.preferences_window.display(sender)


def main():
    app = TransPadApp()
    app.run()
