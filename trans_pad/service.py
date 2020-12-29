from Cocoa import (
    NSObject,
    NSString,
    NSStringPboardType,
    NSLocalizedString,
    NSLog,
)
from AppKit import (  # noqa: E501
    NSPasteboard,
)

import Cocoa
import objc
from objc import typedSelector
import rumps

from trans_pad.config import config
from trans_pad.translate import translate_text

SERVICE_SELECTOR = b'v@:@@o^@'


class MyPastBoard(NSPasteboard):
    pass


def ERROR(s):
    NSLog(u"ERROR: %s", s)
    return s


class TransPadService(NSObject):
    # @service_selector
    @typedSelector(SERVICE_SELECTOR)
    def translateTextService_userData_error_(self, pboard, data, err):
        # NSLog(u"doCapitalizeService_userData_error_(%s, %s)", pboard, data)
        try:
            types = pboard.types()
            pboard_string = None
            if NSStringPboardType in types:
                pboard_string = pboard.stringForType_(NSStringPboardType)
            if pboard_string is None:
                return ERROR(NSLocalizedString(
                    "Error: Pasteboard doesn't contain a string.",
                    "Pasteboard couldn't give string.",
                ))

            new_string = translate_text.translate(pboard_string)
            # rumps.alert(str(config.Common.translate_channel))
            rumps.alert(new_string)

            types = [NSStringPboardType]
            pboard.declareTypes_owner_([NSStringPboardType], None)
            pboard.setString_forType_(new_string, NSStringPboardType)
            return ERROR(None)
        except:  # noqa: E722, B001
            import traceback

            traceback.print_exc()
            return ERROR("Exception, see traceback")
