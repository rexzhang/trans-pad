from threading import Timer

from AppKit import (
    NSBorderlessWindowMask,

    NSPanel,
    NSScreen,
)


# from NSScreen import mainScreen


class ResultPad:
    def __init__(self):
        self._panel = None
        self.rect = ((0.0, 0.0), (0.0, 0.0))
        self.buf = 2
        self.flag = 0

        self.timer = None

    def display(self, content):
        if self._panel is None:
            screen_size = NSScreen.mainScreen().frame().size
            center_point = screen_size.width / 2, screen_size.height / 2
            self.rect = (
                (center_point[0] - 100, center_point[1] - 100), (400, 200)
            )

            self._panel = NSPanel.alloc()
            # self._panel.init()
            self._panel.initWithContentRect_styleMask_backing_defer_(
                self.rect, NSBorderlessWindowMask, self.buf, self.flag
            )
            self._panel.setTitle_("HelloWorld")
            self._panel.setFloatingPanel_(True)
            self._panel.setWorksWhenModal_(True)
            self._panel.setHidesOnDeactivate_(True)

        else:
            self._panel.setHidesOnDeactivate_(False)
            # self._panel.update()
            self.timer = Timer(2, self.hide)
            self.timer.start()

        self._panel.setFrame_display_(self.rect, True)

        self._panel.update()
        self._panel.orderFrontRegardless()

    def hide(self):
        # self.timer.stop()
        self._panel.setHidesOnDeactivate_(True)
