from objc import IBOutlet, IBAction
from AppKit import NSWindowController, NSApp

from trans_pad.constantes import (
    Languages,
    LANGUAGES_TEXT_MAP,
    TranslationServices,
    TRANSLATION_SERVICES_TEXT_MAP,
)
from trans_pad.config import config
from trans_pad.helpers import PopUpButtonHelper


class PreferencesController(NSWindowController):
    # General
    uiLanguage = IBOutlet()
    destLanguage = IBOutlet()
    translationService = IBOutlet()

    dest_language_helper = None
    translation_service_helper = None

    # Support
    sentryDsn = IBOutlet()

    def windowDidLoad(self):
        NSWindowController.windowDidLoad(self)

        # General
        self.dest_language_helper = PopUpButtonHelper(
            objc_obj=self.destLanguage,
            values=Languages,
            selected_value=config.Common.dest_language,
            text_map=LANGUAGES_TEXT_MAP,
        )
        self.translation_service_helper = PopUpButtonHelper(
            objc_obj=self.translationService,
            values=TranslationServices,
            selected_value=config.Common.translation_service,
            text_map=TRANSLATION_SERVICES_TEXT_MAP,
        )

        # Support
        self.sentryDsn.setStringValue_(config.Support.sentry_dsn)

    @IBAction
    def destLanguage_(self, _):
        config.Common.dest_language = self \
            .dest_language_helper.selected_value
        config.dump()

    @IBAction
    def translationService_(self, _):
        config.Common.translation_service = self \
            .translation_service_helper.selected_value
        config.dump()

    # def updateDisplay(self):
    #     self.counterTextField.setStringValue_(self.count)

    @IBAction
    def sentryDsn_(self, _):
        config.Support.sentry_dsn = self.sentryDsn.stringValue()
        config.dump()


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
