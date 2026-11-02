# Flycast standalone Vulkan / Action Pi v1.0.9

The release asset `flycast-standalone-v1.0.9-sources.tar.xz` contains the full
modified Flycast v2.7 source tree and pinned dependency sources, upstream licenses,
the Zig 0.13.0 cross-build recipes, display-surface patch, final BOOT integration
and build records. Upstream commit: 5aa091fde632fb332c8d8c34e280d62dc951954c.

The shipped binary is the exact hardware-tested file, SHA256
4eca8bb183ed44d3c171581f72f5c7dbf692559ae2a20ca081a0681f9cefb4d2;
it identifies itself as `v2.7-actionpi-vulkan-test`. It was not rebuilt or relabeled
for publication. Vulkan-only rendering, ARM64 JIT and SDL2 input/audio are enabled;
DreamLink, Lua, separate ALSA/AO/Pulse backends and Breakpad are excluded.

The app-specific VK_KHR_display surface patch selects the rotation loader's logical
960x720 mode instead of rejecting it using SDL's physical portrait window size.
The existing loader rotates the whole game/menu into physical 720x960 output.
System SDL2, the kernel and Mali libraries are unchanged.

For a rebuild, use the complete source asset and adapt the recorded absolute build
paths to your checkout. Supply the matching target SDK and Zig/compiler/CMake
tools documented by the archived scripts. Inherited proprietary Mali/SDK runtime
libraries are not redistributed in this source asset. No byte-identical rebuild
is promised for different SDKs. The final BOOT module must run install_generator
before configgen, then prepare before Popen, to preserve saved settings and L3.

The user confirmed Vulkan game/menu output, L3, HOME return and final settings
persistence across exit/relaunch. Performance comparison is the user's hands-on
assessment, not a controlled benchmark. Final Vulkan-default reboot, GL rollback
transition and fresh final-image flashing were not separately tested.

No ROM, BIOS, VMU/save, SSH credentials, personal device configuration or recovery
tar is included. Existing source/component provenance limitations remain in the
firmware's SOURCES_AND_LICENSES documentation.
