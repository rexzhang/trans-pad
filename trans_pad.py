import rumps

from result_pad import ResultPad


class TransPadApp:
    def __init__(self):
        self.result_pad = None
        self.menu_test = rumps.MenuItem(
            title='test',
            callback=lambda _: self.test()
        )

        self.app = rumps.App('TransPad', 'T')
        self.app.menu = [
            self.menu_test,
            None,
        ]

    def run(self):
        self.app.run()

    def test(self):
        if self.result_pad is None:
            self.result_pad = ResultPad()

        self.result_pad.display('')


def main():
    app = TransPadApp()
    app.run()


if __name__ == '__main__':
    main()
