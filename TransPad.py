from AppKit import (
    NSApplication, NSRegisterServicesProvider, NSApp
)
import rumps

from trans_pad.translate import translate_text
from trans_pad.result_pad import ResultPad
from trans_pad.service import TransPadService


class TransPadApp:
    result_pad = None

    def __init__(self):
        self.menu_test = rumps.MenuItem(
            title='test',
            callback=lambda _: self.test()
        )

        self.app = rumps.App('TransPad', icon='icon.icns')
        # self.app._nsapp.setServicesProvider(test)
        # NSApplication.sharedApplication().setServicesProvider_(test)
        service_provider = TransPadService.alloc().init()
        NSRegisterServicesProvider(service_provider, "TransPadService")

        self.app.menu = [
            self.menu_test,
            None,
        ]

    def run(self):
        self.app.run()

    def test(self):
        if self.result_pad is None:
            self.result_pad = ResultPad()

        self.result_pad.result = translate_text.translate('This is a test!')
        self.result_pad.display()


def main():
    rumps.debug_mode(True)

    app = TransPadApp()
    app.run()


if __name__ == '__main__':
    main()
