from AppKit import (
    NSApplication, NSRegisterServicesProvider
)
import rumps

from trans_pad.constantes import APP_NAME
from trans_pad.config import config
from trans_pad.constantes import TranslateChannel
from trans_pad.translate import translate_text
from trans_pad.result_pad import ResultPad
from trans_pad.service import TransPadService
from trans_pad.xib.preferences import PreferencesWindow


class TransPadApp:
    result_pad = None
    preferences_window = None

    def __init__(self):
        self.menu_translate_channel_google_ajax = rumps.MenuItem(
            title='from Google AJAX',
            callback=lambda sender: self.toggle_translate_channel(sender)
        )
        if config.Common.translate_channel == TranslateChannel.GoogleAJAX:
            self.menu_translate_channel_google_ajax.state = True
        else:
            self.menu_translate_channel_google_ajax.state = False

        menu = [
            rumps.MenuItem(
                title='xib',
                callback=lambda sender: self.test_xib(sender),
            ),
            rumps.MenuItem(
                title='About TransPad',
                callback=lambda _: self.window_about(),
            ),
            rumps.separator,

            rumps.MenuItem('Translation provider: macOS Dictionary or Google'),
            self.menu_translate_channel_google_ajax,

            rumps.separator,
        ]

        self.app = rumps.App(
            APP_NAME, icon='icon.icns', template=True, menu=menu
        )

        # self.app._nsapp.setServicesProvider(test)
        # NSApplication.sharedApplication().setServicesProvider_(test)
        service_provider = TransPadService.alloc().init()
        NSRegisterServicesProvider(service_provider, "TransPadService")
        return

    @staticmethod
    def toggle_translate_channel(sender):
        sender.state = not sender.state
        if sender.state:
            config.Common.translate_channel = TranslateChannel.GoogleAJAX
        else:
            config.Common.translate_channel = TranslateChannel.MacOSServices

        config.dump()
        return

    def run(self):
        self.app.run()

    @staticmethod
    def window_about():
        rumps.alert(
            title='About TransPad',
            message='https://github.com/rexzhang/trans-pad',
            icon_path='icon.icns'
        )
        # rumps.Window('message').run()

    def test(self):
        if self.result_pad is None:
            self.result_pad = ResultPad()

        self.result_pad.result = translate_text.translate('This is a test!')
        self.result_pad.display()

    def test_xib(self, sender):
        if self.preferences_window is None:
            self.preferences_window = PreferencesWindow()

        self.preferences_window.display(sender)


def main():
    rumps.debug_mode(True)

    app = TransPadApp()
    app.run()


if __name__ == '__main__':
    main()
