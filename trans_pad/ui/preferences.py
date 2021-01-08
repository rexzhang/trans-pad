from objc import IBOutlet, IBAction, selectorFor
from AppKit import NSWindowController, NSApp

from trans_pad.constants import (
    Languages,
    TranslationServices,
)
from trans_pad.config import config
from trans_pad.helpers import i18n, PopUpButtonHelper
from trans_pad.translate.service import GOOGLE_SERVICE_URLS


class PreferencesController(NSWindowController):
    # window
    windowObjc = IBOutlet()
    tabViewObjc = IBOutlet()

    # General
    generalTitle = IBOutlet()
    uiLanguageLabel = IBOutlet()
    uiLanguage = IBOutlet()
    destLanguageLabel = IBOutlet()
    destLanguage = IBOutlet()
    translationServiceLabel = IBOutlet()
    translationService = IBOutlet()

    ui_language_helper = None
    dest_language_helper = None
    translation_service_helper = None

    # Google
    googleServiceURLLabel = IBOutlet()
    googleServiceURL = IBOutlet()

    google_service_url_helper = None

    # Support
    sentryDsn = IBOutlet()

    def windowDidLoad(self):
        NSWindowController.windowDidLoad(self)

        # window
        self.windowObjc.setValue_forKey_(_('Preferences'), 'title')

        # tab view
        tab_view_objc = self.tabViewObjc.valueForKey_('tabViewItems')
        print(tab_view_objc.objectAtIndex_(0).valueForKey_('label'))

        # General
        tab_view_objc.objectAtIndex_(0).setValue_forKey_(
            _('General'), 'label'
        )
        self.uiLanguageLabel.setStringValue_(_('UI Language'))
        self.ui_language_helper = PopUpButtonHelper(
            objc_obj=self.uiLanguage,
            values=Languages,
            selected_value=config.Common.ui_language,
            text_map=Languages.text_map(),
        )
        self.destLanguageLabel.setStringValue_(_('Destination Language'))
        self.dest_language_helper = PopUpButtonHelper(
            objc_obj=self.destLanguage,
            values=Languages,
            selected_value=config.Common.dest_language,
            text_map=Languages.text_map(),
        )
        self.translationServiceLabel.setStringValue_(_('Translation Service'))
        self.translation_service_helper = PopUpButtonHelper(
            objc_obj=self.translationService,
            values=TranslationServices,
            selected_value=config.Common.translation_service,
            text_map=TranslationServices.text_map(),
        )

        # Google
        self.googleServiceURLLabel.setStringValue_(_('Service URL'))
        self.google_service_url_helper = PopUpButtonHelper(
            objc_obj=self.googleServiceURL,
            values=GOOGLE_SERVICE_URLS,
            selected_value=config.Google.service_url,
            text_map=None,
        )

        # Support
        self.sentryDsn.setStringValue_(config.Support.sentry_dsn)

    @IBAction
    def uiLanguage_(self, _):
        config.Common.ui_language = self \
            .ui_language_helper.selected_value
        config.dump()

        i18n()

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

    @IBAction
    def googleServiceURL_(self, _):
        config.Google.service_url = self \
            .google_service_url_helper.selected_value
        config.dump()

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
