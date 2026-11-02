# Public file boundaries

[English](PUBLIC_FILES.md) · [한국어](PUBLIC_FILES.ko.md)

Published code is staged using an explicit allowlist from the **public distribution**.
The original private working directory and complete conversation are not uploaded.

## Included

- Curated development history with confirmed outcomes and failed approaches.
- Current startup/session/opacity/rotation/input/power helpers.
- Exact upstream Mali driver source at the pinned commit, with original notices.
- Recovered kernel config and candidate config/options, source cleanup patch,
  guarded assembly repair and verification summary.
- Historical image conversion and PWM tools, identified as historical where they
  require unpublished earlier input images.
- Sanitized public defaults, PortMaster installer entry, release manifest,
  component hashes, final image/checksum and a compressed release asset.
- Build, installation, recovery, test-coverage and source/provenance documentation.

## Excluded

- Personal images, the private BIOS archive and private captures.
- Saved personal Wi-Fi SSIDs/passwords and recovery copies containing them.
- GitHub credentials, browser session material, authentication screenshots,
  known-hosts files and SSH private/host keys.
- Raw user conversations, private network logs, machine IDs, cookies, histories,
  Bluetooth pairing records, game captures, diagnostic memory dumps and game ROMs.
- Compiler installations, Git databases and untracked build artifacts from the
  driver working tree.

The source image's base rootfs and its original BIOS were deliberately retained
unchanged. This is distinct from excluding the additional personal BIOS archive.
The public packaging zeroed 3,289,493,504 free FAT bytes and scrubbed 122 file
tails plus 26 deleted records, so removing a filename was not the only cleanup.

The downloadable IMG belongs in GitHub **Releases**, not the Git source history.
The source tree is small enough to inspect and clone without downloading firmware.

## Added or refreshed for v1.0.1

- overlay/etc/init.d/S06modprobe and S08connman: effective boot startup code.
- overlay/usr/bin/emulatorlauncher: renderer-aware application routing.
- overlay/boot/ACTIONPI_FIXES/: current common app, PortMaster runtime, OD-Commander and Wi-Fi helpers.
- overlay/boot/PPSSPP_VULKAN/: updated active manager/autostart integrity link.
- src/app_sdl_rotation.c, app_gl_rotation.c and od_commander_rotation.c: adapter source; no compiled userspace adapter is needed in Git.
- tools/ActionPi-WiFi-Diagnostic.sh and wifi-diagnostic.py: passive report collector, compatible with this release.
- release/distribution-v1.0.1.manifest.json and current component/source inventories and asset hashes.

At the v1.0.1 release, personal CRC-core images were excluded. Game ROMs, screenshots containing network details and prior personal stable images remain excluded. The separate clean CRC edition is described below.

## Added or refreshed for v1.0.2

- src/retroarch_gles3_context.c and its ARM64 command in tools/build-runtime.sh.
- overlay/boot/ACTIONPI_FIXES/actionpi_app_launcher.py and MALI_MENU_TRIAL/mali_menu_trial.py.
- release/distribution-v1.0.2.manifest.json, FIELD_VALIDATION-v1.0.2.json and current image/asset/source hashes.
- Normal v1.0.2 excludes user CRC cores; prior personal BIOS/settings remain unpublished.

## Separate Korean CRC edition

The CRC-core IMG is offered in a separate release. config/crc-ko/ contains the actual startup sources; release/crc-ko/ contains dedicated manifests/checksums. See the [Korean guide](CRC_KOREAN.ko.md).

## v1.0.3 additions

Publish config/userdata/system/rumble-fix, background-quiet and brightness-osd, shared multimedia_keys.conf, edition-specific custom.sh, tools/package-v1.0.3.py and its FAT helper. Inventories record their hashes. No live private configuration, logs or network credentials are copied.

## v1.0.4

Publish build/ppsspp-1.20.4, LICENSES/ppsspp-1.20.4, tools/package-v1.0.4.py, updated runners/Vulkan forwarding source and release manifests. Private device settings, screenshots and diagnostic logs are excluded.

## v1.0.5

Added kernel/zram, LICENSES/zram, overlay/boot/ACTIONPI_ZRAM, standard/CRC core loader sources, config/bennugd/SOURCE.json, packaging script and v1.0.5 manifests. Binaries are in the IMG and source archives are release assets; private backups are not public.

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
