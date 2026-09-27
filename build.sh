#!/bin/bash
# Build GLFW 3.3.7 static for i386/10.6.
. "$(dirname "$0")/common.sh"
set +o pipefail
VER=3.3.7
URL="https://github.com/glfw/glfw/archive/refs/tags/${VER}.zip"
SRCDIR="$DEPS_BUILD/glfw-${VER}"
mkdir -p "$DEPS_BUILD" "$DEPS_PREFIX"; cd "$DEPS_BUILD"
[ -f "glfw-${VER}.zip" ] || curl -fL -o "glfw-${VER}.zip" "$URL"
[ -d "$SRCDIR" ] || unzip -q "glfw-${VER}.zip"
[ -f "$SRCDIR/.sl_fixed" ] || { /usr/bin/python "$ROOT/glfw_fixups.py" "$SRCDIR" && touch "$SRCDIR/.sl_fixed"; }
cmake -S "$SRCDIR" -B "$DEPS_BUILD/glfw-build" \
  -DCMAKE_TOOLCHAIN_FILE="$TOOLCHAIN" \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_INSTALL_PREFIX="$DEPS_PREFIX" \
  -DCMAKE_PREFIX_PATH="$DEPS_PREFIX;$MP" \
  -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
  -DBUILD_SHARED_LIBS=OFF \
  -DGLFW_BUILD_DOCS=OFF -DGLFW_BUILD_EXAMPLES=OFF -DGLFW_BUILD_TESTS=OFF
cmake --build "$DEPS_BUILD/glfw-build" -j2 && cmake --install "$DEPS_BUILD/glfw-build"
rc=$?; echo "GLFW-DONE rc=$rc"
[ $rc -eq 0 ] && ls "$DEPS_PREFIX"/lib/libglfw3.a 2>/dev/null
