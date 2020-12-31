from objc import IBOutlet, IBAction
from AppKit import NSWindowController, NSApp


class PreferencesController(NSWindowController):
    count = 0
    counterTextField = IBOutlet()
    channelListDataSource = IBOutlet()
    channelList = IBOutlet()

    # def windowDidLoad(self):
    #     NSWindowController.windowDidLoad(self)
    #
    #     # Start the counter
    #     self.count = 0

    @IBAction
    def increment_(self, sender):
        self.count += 1
        self.updateDisplay()

    @IBAction
    def displayInfo_(self, sender):
        # print(self)
        # print(sender)

        self.channelList.removeAllItems()
        print(self.channelList.numberOfItems())
        self.channelList.addItemWithTitle_('test1')
        self.channelList.addItemWithTitle_('test2')
        print(self.channelList.numberOfItems())
        print(self.channelList.indexOfSelectedItem())
        self.channelList.selectItemAtIndex_(1)
        print(self.channelList.indexOfSelectedItem())

    def updateDisplay(self):
        self.counterTextField.setStringValue_(self.count)


class PreferencesWindow:
    def __init__(self):
        self._controller = None

    def display(self, sender):
        # Initiate the contrller with a XIB
        self._controller = PreferencesController.alloc() \
            .initWithWindowNibName_('preferences')
        # self._controller.loadWindow()

        # Show the window
        self._controller.showWindow_(sender)

        # Bring app to top
        NSApp.activateIgnoringOtherApps_(True)
