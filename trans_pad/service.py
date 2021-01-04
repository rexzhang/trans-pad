import logging

from Cocoa import (
    NSObject,
    NSString,
    NSStringPboardType,
    NSLocalizedString,
)
from AppKit import (  # noqa
    NSApplication,
    NSRegisterServicesProvider,
    NSPasteboard,
)

from objc import typedSelector
import rumps

from trans_pad.sentry import capture_exception
from trans_pad.translate import translate_text

logger = logging.getLogger(__name__)

SERVICE_SELECTOR = b'v@:@@o^@'


class MyPastBoard(NSPasteboard):
    pass


def error(s):
    logger.error(s)
    return s


class TransPadService(NSObject):
    # @service_selector
    @typedSelector(SERVICE_SELECTOR)
    def translateTextService_userData_error_(self, pboard, data, err):
        logger.debug('received some request from service:{} {}'.format(
            pboard, data
        ))
        try:
            types = pboard.types()
            pboard_string = None
            if NSStringPboardType in types:
                pboard_string = pboard.stringForType_(NSStringPboardType)
            if pboard_string is None:
                return error(NSLocalizedString(
                    "Error: Pasteboard doesn't contain a string.",
                    "Pasteboard couldn't give string.",
                ))

            new_string = translate_text.translate(pboard_string)
            rumps.alert(new_string)

            types = [NSStringPboardType]
            pboard.declareTypes_owner_([NSStringPboardType], None)
            pboard.setString_forType_(new_string, NSStringPboardType)
            return ''

        except Exception as e:  # noqa: E722, B001
            capture_exception(e)
            # import traceback
            # traceback.print_exc()
            return error("Exception, see traceback")


def register_service(name: str):
    # self.app._nsapp.setServicesProvider(test)
    # NSApplication.sharedApplication().setServicesProvider_(test)
    service_provider = TransPadService.alloc().init()
    NSRegisterServicesProvider(service_provider, name)
