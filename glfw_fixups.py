#!/usr/bin/env python
# Idempotent GLFW 3.3.7 fixups for the Mac OS X 10.6 SDK (i386).
# GLFW 3.3 uses the 10.12-era AppKit enum names, absent from the 10.6 SDK.
# Inject a compatibility header mapping them to the pre-10.12 names into
# cocoa_platform.h (included by every GLFW Cocoa source before use).
import sys, os

root = sys.argv[1]
p = os.path.join(root, "src", "cocoa_platform.h")

SHIM = """
// --- Snow Leopard (10.6 SDK) AppKit name compatibility (injected) ---
#ifndef SL_COCOA_COMPAT
#define SL_COCOA_COMPAT
#define NSEventTypeApplicationDefined NSApplicationDefined
#define NSEventMaskAny NSAnyEventMask
#define NSEventMaskKeyUp NSKeyUpMask
#define NSWindowStyleMaskBorderless NSBorderlessWindowMask
#define NSWindowStyleMaskClosable NSClosableWindowMask
#define NSWindowStyleMaskMiniaturizable NSMiniaturizableWindowMask
#define NSWindowStyleMaskResizable NSResizableWindowMask
#define NSWindowStyleMaskTitled NSTitledWindowMask
#define NSEventModifierFlagCapsLock NSAlphaShiftKeyMask
#define NSEventModifierFlagCommand NSCommandKeyMask
#define NSEventModifierFlagControl NSControlKeyMask
#define NSEventModifierFlagDeviceIndependentFlagsMask NSDeviceIndependentModifierFlagsMask
#define NSEventModifierFlagOption NSAlternateKeyMask
#define NSEventModifierFlagShift NSShiftKeyMask
#define NSBitmapFormatAlphaNonpremultiplied NSAlphaNonpremultipliedBitmapFormat
#ifndef NSWindowCollectionBehaviorFullScreenPrimary
#define NSWindowCollectionBehaviorFullScreenPrimary (1 << 7)
#endif
#endif // SL_COCOA_COMPAT
"""

s = open(p).read()
if "SL_COCOA_COMPAT" in s:
    print("skip cocoa_platform.h (already shimmed)")
else:
    anchor = "#include <Carbon/Carbon.h>\n"
    if anchor not in s:
        print("MISS cocoa_platform.h (anchor not found)")
    else:
        s = s.replace(anchor, anchor + SHIM, 1)
        open(p, "w").write(s)
        print("fix  cocoa_platform.h (AppKit 10.6 shim injected)")
