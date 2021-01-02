import rumps

from trans_pad.constantes import APP_NAME
from trans_pad.translate import translate_text
from trans_pad.result_pad import ResultPad
from trans_pad.service import register_service
from trans_pad.ui.preferences import PreferencesWindow


class TransPadApp:
    result_pad = None
    preferences_window = None

    def __init__(self):
        menu = [
            rumps.MenuItem(
                title='Preferences...', key=',',
                callback=lambda sender: self.window_preferences(sender),
            ),
            rumps.MenuItem(
                title='About TransPad',
                callback=lambda _: self.window_about(),
            ),
            rumps.separator,
        ]

        self.app = rumps.App(
            APP_NAME, icon='icon.icns', template=True, menu=menu
        )

        register_service('TransPadService')
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

    def window_preferences(self, sender):
        if self.preferences_window is None:
            self.preferences_window = PreferencesWindow()

        self.preferences_window.display(sender)


def main():
    rumps.debug_mode(True)

    app = TransPadApp()
    app.run()


if __name__ == '__main__':
    main()
