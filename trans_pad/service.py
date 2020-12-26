from AppKit import NSPasteboard

import Cocoa
import objc
import rumps


class MyPastBoard(NSPasteboard):
    pass


def serviceSelector(fn):
    # this is the signature of service selectors
    return objc.selector(fn, signature=b"v@:@@o^@")


def ERROR(s):
    # NSLog(u"ERROR: %s", s)
    return s


class ServiceTest(Cocoa.NSObject):
    @serviceSelector
    def translateTextService_userData_error_(self, pboard, data, err):
        # NSLog(u"doCapitalizeService_userData_error_(%s, %s)", pboard, data)
        try:
            types = pboard.types()
            pboardString = None
            if Cocoa.NSStringPboardType in types:
                pboardString = pboard.stringForType_(Cocoa.NSStringPboardType)
            if pboardString is None:
                return ERROR(
                    Cocoa.NSLocalizedString(
                        "Error: Pasteboard doesn't contain a string.",
                        "Pasteboard couldn't give string.",
                    )
                )

            newString = Cocoa.NSString.capitalizedString(pboardString)
            rumps.alert(newString)
            # newString = 'TEST!'

            if not newString:
                return ERROR(
                    Cocoa.NSLocalizedString(
                        "Error: Couldn't capitalize string %s.",
                        "Couldn't perform service operation for string %s.",
                    )
                    % pboardString
                )

            types = [Cocoa.NSStringPboardType]
            pboard.declareTypes_owner_([Cocoa.NSStringPboardType], None)
            pboard.setString_forType_(newString, Cocoa.NSStringPboardType)
            return ERROR(None)
        except:  # noqa: E722, B001
            import traceback

            traceback.print_exc()
            return ERROR("Exception, see traceback")
