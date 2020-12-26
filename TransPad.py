import rumps

from AppKit import NSApplication, NSRegisterServicesProvider, NSApp
from Cocoa import NSRegisterServicesProvider

from trans_pad.dictionary_api import DictionaryGoogleTrans
from trans_pad.result_pad import ResultPad
from trans_pad.service import ServiceTest

rumps.debug_mode(True)


def test():
    print('tttttt')


class TransPadApp:
    def __init__(self):
        self.result_pad = None
        self.translate = DictionaryGoogleTrans()

        self.menu_test = rumps.MenuItem(
            title='test',
            callback=lambda _: self.test()
        )

        self.app = rumps.App('TransPad', 'T')
        # self.app._nsapp.setServicesProvider(test)
        # NSApplication.sharedApplication().setServicesProvider_(test)
        serviceProvider = ServiceTest.alloc().init()
        NSRegisterServicesProvider(serviceProvider, "TransPadService")
        self.app.menu = [
            self.menu_test,
            None,
        ]

    def run(self):
        self.app.run()

    def test(self):
        if self.result_pad is None:
            self.result_pad = ResultPad()

        self.result_pad.result = self.translate.translate('test')

        self.result_pad.display()


def main():
    app = TransPadApp()
    app.run()


if __name__ == '__main__':
    main()
