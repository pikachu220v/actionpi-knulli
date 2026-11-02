# Sources, licenses and provenance

[English](SOURCES_AND_LICENSES.md) · [한국어](SOURCES_AND_LICENSES.ko.md)

This firmware is a collection of separately licensed components. A repository
license for original glue does not replace Linux, Arm, SDL, emulator, firmware
or BIOS terms. Existing notices in vendored files are preserved.

| Component | Recorded source/provenance | Status |
| --- | --- | --- |
| Original adaptation glue | `overlay/`, `src/`, `tools/` | Original glue uses the scoped MIT notice; kernel-derived work retains GPL terms |
| Mali kernel driver | Radxa allwinner-bsp commit `2045a3ca2a01f088c0314dc924bda59d154e363e`, `modules/gpu/mali-valhall/driver` | Tracked upstream source vendored here; license.txt and file notices retained; candidate build inputs recorded |
| Vendor Linux5.15.147 | Recovered config, binary identity and guarded repair source included | Exact original vendor tree/build provenance remains unidentified |
| Public kernel candidate | Orange Pi commit `5b956b750422abd5e9e9c5523540d2aaf41a7939` | Used for header/layout/source comparison; not a substitute claim for exact vendor corresponding source |
| Knulli integration | [Action Pi board configuration](https://github.com/knulli-cfw/knulli-linux/tree/knulli-main/board/allwinner/a527/helegany-action-pi) on `knulli-main`; A527 history at `5a7cb1e8e4dd` | Board-integration base; complete exact source closure of inherited image not established |
| SDL2 | [release-2.32.8](https://github.com/libsdl-org/SDL/tree/release-2.32.8) | Target SDL2.32.8 identified; new adapters are separate source files |
| Flycast VL reference | [libretro/flycast commit4a913e0](https://github.com/libretro/flycast/tree/4a913e063c95d1fae98afc64645831de0bcad57e) | Recorded source reference for old signal/JIT investigation |
| PPSSPP/Flycast/RetroArch/ES | Inherited Knulli programs; adaptation source here wraps their launch/output behavior | Exact source/version closure for every inherited binary is not claimed |
| Mali userspace libraries | Inherited vendor stack; observed r32p0 GLES renderer | Proprietary/vendor binaries; the kernel-driver GPL license does not license libmali |
| AIC8800DC module/firmware | Files reused from working stock firmware | Binary provenance recorded by adaptation; exact corresponding module source/redistribution terms not fully resolved |
| Base BIOS | Inherited base-rootfs BIOS retained unchanged | Not covered by this project's glue license; this is not a BIOS-free distribution |
| Added personal BIOS archive | Excluded | Not a public release asset |

## Why the source distinction matters

The [GNU GPLv2 FAQ](https://www.gnu.org/licenses/old-licenses/gpl-2.0-faq.html)
explains source obligations when distributing GPL binaries. A generic upstream
URL or similarly numbered kernel is not, by itself, the source used for a given
vendor binary. This repository therefore does not claim that the unresolved
vendor source questions have been solved merely by publishing a public candidate.

The full source/provenance inventory of the inherited distribution still needs
work. In particular, exact original kernel changes, stock Wi-Fi source and
vendor userspace/retained BIOS terms should be resolved before claiming complete
source or redistribution compliance for the entire image. This document records
the actual evidence and gaps; it is not a certification of that claim.

## Primary upstream references

- [Knulli](https://github.com/knulli-cfw/knulli-linux)
- [Pinned Mali source](https://github.com/radxa/allwinner-bsp/tree/2045a3ca2a01f088c0314dc924bda59d154e363e/modules/gpu/mali-valhall/driver)
- [Pinned Orange Pi candidate](https://github.com/orangepi-xunlong/linux-orangepi/tree/5b956b750422abd5e9e9c5523540d2aaf41a7939)
- [Arm GNU13.3.Rel1](https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads)
- [SDL evdev signal path](https://github.com/libsdl-org/SDL/blob/release-2.32.8/src/core/linux/SDL_evdev_kbd.c)
- [Ultramarine handheld vendor-stack work](https://github.com/Ultramarine-Linux/ultramarine-handheld)

Build toolchain archive SHA256 recorded during preparation:
`322f0b4482fc0d9fa0bb468134841f08d8c554c54ff5aa29a13a7a24bf7e1eb5`.

## v1.0.1 Wi-Fi provenance

The AIC binaries are retained from the recorded stock-firmware integration. The 8723ds module is the stock-firmware binary already reviewed for the 5.15.147 target; its alias includes SDIO vendor 024c/device d723. This release wires those existing modules into persistent boot copies rather than claiming to have authored or rebuilt their complete vendor sources. Binary hashes are recorded in release/BOOT_COMPONENTS.json. The unresolved original vendor-kernel/source provenance described above still applies.

## v1.0.2 helper

retroarch_gles3_context.c is an MIT-licensed adaptation helper written for this integration. It adjusts the scoped SDL context-major request without replacing SDL or RetroArch. Existing unresolved provenance/licensing items remain unchanged.

## Separate Korean CRC edition

The FBNeo/MAME2003 Plus binaries were supplied by the user and are packaged in a separate IMG release. Exact corresponding source versions and CRC modification patches were not supplied. Upstream [FBNeo](https://github.com/finalburnneo/FBNeo) and [MAME2003 Plus](https://github.com/libretro/mame2003-plus-libretro) links are references, not proof of a matching binary source. Actual startup sources and binary hashes are in config/crc-ko/ and release/crc-ko/. Component terms are separate from this repository's scoped MIT adaptation license.

CRC-override core materials: **[dsno](https://dsno.tistory.com/m/)**, as identified by the user.

## v1.0.3 original helpers

The new userdata rumble, cleanup and brightness OSD helpers and packaging logic are original project Python/shell glue under the existing scoped MIT terms. Inherited firmware/kernel/CRC-core licenses and corresponding-source limitations remain unchanged.

## PPSSPP 1.20.4

PPSSPP is GPL-2.0-or-later. The release includes the exact official v1.20.4 full source archive, including bundled FFmpeg. build/ppsspp-1.20.4/SOURCE.json records its checksum; font patches, build scripts and forwarding-library source are published. See LICENSES/ppsspp-1.20.4. Previously documented corresponding-source limitations for inherited vendor kernel/binaries and modified CRC cores remain unchanged.

## v1.0.5

The rebuilt ZRAM/zsmalloc/LZO modules derive from the pinned Orange Pi Linux tree. Full source archive, actual external translation units, configurations, patches, build recipe and retained Linux notices are published in kernel/zram and LICENSES/zram. The source used for these rebuilt modules is documented separately from the still-unresolved original vendor kernel provenance. BennuGD is the user-supplied binary identified in config/bennugd/SOURCE.json. Its exact source revision/build recipe was not supplied; the upstream reference is not proof of corresponding source and the project MIT glue license does not relicense that core. dsno credit applies only to the separately packaged CRC arcade cores.

BennuGD reference project: [BennuGD_libretro](https://github.com/diekleinekuh/BennuGD_libretro). This link is not evidence of the supplied binary’s exact corresponding source.

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
