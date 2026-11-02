# Runtime architecture

[English](ARCHITECTURE.md) · [한국어](ARCHITECTURE.ko.md)

Target guard: `/boot/boot/knulli.board` must be `helegany-action-pi`; kernel is
the specifically guarded, repaired 5.15.147 binary. Equal version strings alone
are not a compatibility test. These files are not instructions to install the
module on arbitrary A527/TSPS devices.

## Startup

1. Original partition initialization expands SHARE on a new card and reboots.
2. S12 invokes `/boot/postshare.sh` after SHARE is mounted. `STABLE_V119/firstboot.py`
   verifies payload hashes, extracts only sanitized settings, writes a completion
   marker, syncs and reboots. It does not restore the personal BIOS archive.
3. `boot-custom.sh` prepares the Action Pi userspace fixes. The Mali startup gate
   and boot arguments prevent Panfrost from taking the GPU first, then use the
   candidate Mali module and vendor libraries.
4. The late gate reconciles the hardware PWM polarity. It validates the board,
   controller register description and live DT PWM arguments before changing bit8.
5. A supervisor starts ES with the vendor EGL/GLES/GBM loader environment, correct
   screen rotation, input and audio settings. Its recovery/attempt markers allow
   the next boot to fall back if startup fails.

## PSP handoff

The dispatcher routes PSP launch requests to `mali_session.py`. The supervisor
also handles an explicit UI-only request from ES Emulators/PPSSPP. It omits the
ROM argument for that mode; normal game requests retain their path validation.
The supervisor
asks ES to quit normally and waits for its display resources to close. It starts
PPSSPP with the scoped Vulkan/SDL output wrappers and opacity correction. On exit
it releases helper descriptors before bringing the menu back. GPU ownership
remains Mali; the ordinary route does not unload/rebind GPU drivers.

Automatic sessions do not restore a historical knulli.conf over current choices.
PPSSPP's configuration tree is handled without discarding saved preferences.
The old one-shot diagnostic managers remain separate from this normal session
route; manually running their original experiment commands is not required.

## Output adapters

| Process/path | Correction |
| --- | --- |
| ES | Native screenrotate option and menu-only audit/input supplement |
| PPSSPP Vulkan | Vulkan output transform, matching SDL logical dimensions, scoped opacity helper |
| RetroArch SDL2 | 960×720 target texture, clockwise90 presentation to 720×960 |
| RetroArch GL / standalone Flycast | Whole GLES drawable FBO rotation |
| PortMaster/PySDL2 | Private named SDL DLL with forwarding dependency on original SDL |

No rotation library replaces `/usr/lib/libSDL2` globally. The PortMaster helper
patches only its `PYSDL2_DLL_PATH` selection under `ACTIONPI_MALI_SESSION=1`;
launch preparation repeats if its shell entry has been replaced.

## Power, brightness and audio

The suspend hook records whether Wi-Fi is powered, disables it to release the
SDIO wake lock, then schedules reconnect to the remembered service after wake.
If Wi-Fi was off, the hook does not enable it merely because the unit woke.
The same resume entry normalizes PWM polarity. Brightness numbers are native
ascending values, not a software `max-value` inversion. Speaker LINEOUT gain is
25 instead of23; this does not change the headphone gain.

## Recovery

An empty `/boot/DISABLE_MALI.txt` requests the fallback menu. That fallback does
not provide the normal PPSSPP Vulkan path. Keep the card's own recovery snapshots:
they are checksum guarded and are not interchangeable with a different image's
backups. Do not restore just the old PWM DT flag while retaining the new strict
normalizer. Whole-image recovery is preferable to mixing historical experiments.

## v1.0.1 Wi-Fi and boot-copy integration

`/boot/partitions/BOOT.IMG` is the active bundle. Mali `restore_boot()` and `arm_boot()` regenerate it from `/boot/PPSSPP_VULKAN/autostart-backup/BOOT.IMG`; transaction recovery also uses that baseline. Wi-Fi changes therefore belong in both copies. The recovery manifest BOOT hash, manager `BOOT_SHA`, and autostart `BASE_SHA` form a linked integrity chain. The active Mali boot arguments remain unchanged.

S06 preserves the AIC path and registers stock 8723ds. S08 queues the deferred startup helper. It waits for persistent SHARE, the `/var/run/knulli.share.mounted` marker, installation completion and a bound interface as applicable, reads current userdata settings, and preserves existing radio/service use. The earlier power helper remains separate. Status files report requested operations rather than proving network access.

App wrappers distinguish SDL renderers, GLES-backed cores and OD-Commander software window surfaces. PortMaster gets its own SDL adapter and scoped game preload; installed Python sources are patched only at known runtime-list patterns.

## v1.0.2 Ozone and the complete BOOT reference chain

Ordinary-core/standalone RetroArch receives final gl/gl_sdl/ozone overrides. Only these processes preload retroarch_gles3_context.so before app_output_rotation.so, requesting at least GLES3 while preserving other SDL attributes. Existing hardware-core output settings remain. The menu guard expects the normal recovery BOOT hash, not the armed active BOOT. Keep manager BOOT_SHA, autostart BASE_SHA, recovery manifests and the menu guard/manifest synchronized.

## v1.0.3 userdata and brightness OSD

custom.sh runs one-shot background cleanup and rumble calibration, then exits; the latter recreates its suspend/resume hook each boot. Native S50triggerhappy prefers the userdata multimedia_keys.conf. Its brightness wrapper preserves original calculations, hold and release behavior while requesting the OSD. The OSD owns a dumb framebuffer through its own non-master DRM client and uses an unused plane. It borrows the active application master fd only for configuration calls and immediately closes it, never keeping it across a wait. On completion it removes its own framebuffer and restores unused plane properties. system.telemetry=0 disables default statistics.

## PPSSPP 1.20.4

Install the application, assets and forwarding libraries in /userdata/system/ppsspp-1.20.4. Both /boot session-runner copies reference the same app and retain existing Mali ownership, user configuration and exit handling. The old 1.19.3 executable remains in the read-only system for recovery but is not used by normal launches.

## v1.0.5

S00bootcustom bind-mounts only the zramswap service wrapper from BOOT; its log must be on BOOT because /var/run is created later at S04populate. S99user services still obey the existing setting. Early boot startup waits for a stable menu before loading the five checked modules. A durable pending marker blocks a repeated incomplete startup, and ACTIONPI_ZRAM/DISABLED is a recovery switch. No original module or modprobe index is overwritten. The BennuGD override uses SHARE custom.sh at S99; standard loads only BennuGD while CRC retains the two existing arcade overrides and the MAME alias.

## v1.0.6 — 2026-10-27

Pinned sources, patches and build recipes for the three Vulkan cores are in src/flycast-vulkan; the standard release includes flycast-v1.0.6-sources.tar containing the full source archives. config/flycast-vulkan/SOURCES.json records identities and checksums. The scoped loader retains rotation through Vulkan reinitialization using SONAME/NODELETE. tools/package-v1.0.6.py consumes only the clean v1.0.5 images and checked payload; the kernel, existing archive settings and CRC cores are preserved.

## v1.0.7

MALI_MENU_TRIAL/mali_session.py uses actionpi_es_menu_return.py to temporarily enable StartupOnGameList only when ES returns after a game. LastSystem is saved by normal ES shutdown. Only the original startup option is journaled and restored on ES exit or the next supervisor start. Game cursor/subfolder restoration is not implemented. tools/package-v1.0.7.py changes only two BOOT Python files and version metadata on the clean v1.0.6 images, preserving settings.tar.gz, cores and kernel. Runtime recovery journals, personal settings and test captures are not packaging inputs.

## v1.0.8

Yaba Sanshiro 1.20.51 GLES is stored in BOOT ACTIONPI_FIXES/saturn and launched by actionpi_app_launcher.py. Its writable HOME is /userdata/system/configs/yabasanshiro-1.20.51. The runner initializes missing input mappings from ES, copies the real L3 binding and uses the existing output rotation helper. The native ARM64 JIT replaces the former 1.9.0 shim. The volume hook preserves the user volume. The original inherited binary remains inside the read-only base rootfs but is not the normal execution route. tools/package-v1.0.8.py adds five BOOT files and version metadata to the clean v1.0.7 image; the settings archive, base rootfs, Mali, Wi-Fi, PPSSPP, Flycast and ZRAM remain byte-identical. Full modified application source, libchdr, notices and build references are attached as saturn-standalone-1.20.51-v1.0.8-sources.tar.xz; see src/saturn-standalone for dependencies and rebuild requirements. This does not establish exact source provenance for all inherited firmware binaries.

## v1.0.8 r2

Image refresh r2 merges both input fixes without increasing the v1.0.8 release version. The player1.pad path honors padmode; in ordinary mode a sampler merges saved physical direction/analogx/analogy bindings into digital directions, with exclusive ownership of those four buttons to avoid cross-source releases. L3, FPS, audio and GLES rotation remain intact. tools/package-v1.0.8-r2.py changes only the Saturn executable and payload.json in the existing v1.0.8 image, retaining the base rootfs, settings archive and other emulators. Filenames identify r2; original tags are not moved. Updated Release documentation links are pinned to this source commit. The full source asset is saturn-standalone-1.20.51-v1.0.8-r2-sources.tar.xz.

## v1.0.9

Yaba Sanshiro 1.20.51 GLES is stored in BOOT ACTIONPI_FIXES/saturn and launched by actionpi_app_launcher.py. Its writable HOME is /userdata/system/configs/yabasanshiro-1.20.51. The runner initializes missing input mappings from ES, copies the real L3 binding and uses the existing output rotation helper. The native ARM64 JIT replaces the former 1.9.0 shim. The volume hook preserves the user volume. The original inherited binary remains inside the read-only base rootfs but is not the normal execution route. tools/package-v1.0.9.py adds five BOOT files and version metadata to the clean v1.0.8 image; the settings archive, base rootfs, Mali, Wi-Fi, PPSSPP, Flycast and ZRAM remain byte-identical. Full modified application source, libchdr, notices and build references are attached as saturn-standalone-1.20.51-v1.0.9-sources.tar.xz; see src/saturn-standalone for dependencies and rebuild requirements. This does not establish exact source provenance for all inherited firmware binaries.

The final Flycast module installs its settings-preserving generator hook before configgen, then selects the Vulkan executable and existing rotation loader before Popen. Only the executable and ENABLED enter the clean settings archive; no personal emu.cfg, VMU/save, ROM or BIOS is copied. Both launchers and their existing manifest hash references are updated; the GL fallback path is retained. Saturn r2 and existing cores/other app payloads are preserved. Full source and Zig build references are in src/flycast-standalone-vulkan and flycast-standalone-v1.0.9-sources.tar.xz. The exact tested executable bytes are shipped, retaining its test version string. The quiet-start addition targets only the old 60-second boot diagnostic while retaining prior progress-copy and statistics suppression.
