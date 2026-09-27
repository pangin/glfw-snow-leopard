# glfw-snow-leopard

Build **GLFW 3.3.7** static for **Mac OS X 10.6.8 / i386**.

```sh
./build.sh      # -> prefix/lib/libglfw3.a (i386)
```

Key 10.6 fix — `glfw_fixups.py` injects a compatibility header into
`cocoa_platform.h` mapping the 10.12-era AppKit names GLFW 3.3 uses back to the
pre-10.12 names present in the 10.6 SDK (e.g. `NSWindowStyleMaskTitled` ->
`NSTitledWindowMask`, `NSEventModifierFlagCommand` -> `NSCommandKeyMask`,
`NSEventMaskKeyUp` -> `NSKeyUpMask`, plus `NSWindowCollectionBehaviorFullScreenPrimary`).
Uses the clang/`ld64-274` toolchain.
