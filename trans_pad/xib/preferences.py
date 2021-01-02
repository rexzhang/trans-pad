from objc import IBOutlet, IBAction
from AppKit import NSWindowController, NSApp

from trans_pad.constantes import (
    TranslationService,
    TRANSLATION_SERVICE_TEXT_MAP,
)
from trans_pad.config import config
from trans_pad.helpers import PopUpButtonHelper


class PreferencesController(NSWindowController):
    uiLanguage = IBOutlet()
    destLanguage = IBOutlet()
    translationService = IBOutlet()

    translation_service_helper = None

    def windowDidLoad(self):
        NSWindowController.windowDidLoad(self)
        self.translation_service_helper = PopUpButtonHelper(
            objc_obj=self.translationService,
            values=TranslationService,
            selected_value=config.Common.translation_service,
            text_map=TRANSLATION_SERVICE_TEXT_MAP,
        )

    @IBAction
    def translationService_(self, _):
        config.Common.translation_service = self \
            .translation_service_helper.selected_value
        config.dump()

    @IBAction
    def destLanguage_(self, _):
        pass

    # def updateDisplay(self):
    #     self.counterTextField.setStringValue_(self.count)


class PreferencesWindow:
    def __init__(self):
        self._controller = None

    def display(self, sender):
        # Initiate the controller with a XIB
        self._controller = PreferencesController.alloc() \
            .initWithWindowNibName_('preferences')
        # self._controller.loadWindow()

        # Show the window
        self._controller.showWindow_(sender)

        # Bring app to top
        NSApp.activateIgnoringOtherApps_(True)
