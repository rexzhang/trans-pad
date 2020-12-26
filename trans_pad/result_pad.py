from threading import Timer

from AppKit import (
    NSZeroRect,
    NSBorderlessWindowMask,

    NSPanel,
    NSScreen,
)
from WebKit import (
    WKWebView,
    WKWebViewConfiguration,
)


class ResultPad:
    def __init__(self):
        self._panel = None
        self._web_view = None

        self.rect = ((0.0, 0.0), (0.0, 0.0))
        self.buf = 2
        self.flag = 0

        self.timer = None
        self.result = None

    def display(self):
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

            self._web_view = WKWebView.new()
            self._web_view.initWithFrame_configuration_(
                NSZeroRect, WKWebViewConfiguration.new()
            )
            self._web_view.setFrameSize_(
                self._panel.contentView().frame().size
            )
            self._web_view.loadHTMLString_baseURL_(
                '<html><body><p>{}</p></body></html>'.format(self.result),
                None
            )
            self._panel.contentView().addSubview_(self._web_view)

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
