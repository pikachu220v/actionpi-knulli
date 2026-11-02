# Development history and reasons for the final design

[English](HISTORY.md) · [한국어](HISTORY.ko.md)

## 1. Keep a bootable baseline

The original aim was PPSSPP Vulkan, rather than Vulkan in every emulator. An early
TSPS-style approach was too easily reduced to comparing Mali r32/r42 labels or
changing a PPSSPP option. In practice the kernel module, user-space Mali library,
Vulkan ICD registration, SDL and launch environment all had to agree.

Several experimental images failed before the menu, and adding/removing one
Wi-Fi file from an already changed image did not reconstruct a clean baseline.
The successful method was to restart from the known bootable v87 and preserve
working checkpoints. Stock firmware established that this unit's Wi-Fi hardware
worked. The final working stack used the AIC8800DC files appropriate to that
hardware, rather than treating every Wi-Fi module found in stock firmware as
interchangeable. v115 became the preserved working Wi-Fi/audio/RetroArch baseline.

## 2. Diagnose Mali ABI before installing it

The borrowed TSPS Mali module accessed three inode fields at offsets that did not
match the Action Pi kernel. The observed target offsets were `i_rdev=0x34`,
`i_mapping=0x20`, and `i_private=0x238`; the borrowed module used `0x44`, `0x30`,
and `0x248`. Page, mm_struct and dma_buf accesses were examined separately.

Rather than patching those three instructions and declaring compatibility,
the driver was rebuilt using a pinned public candidate kernel configuration.
The Orange Pi candidate is commit
`5b956b750422abd5e9e9c5523540d2aaf41a7939`; the Mali source is Radxa commit
`2045a3ca2a01f088c0314dc924bda59d154e363e`, r42p0-01eac0, JM/sunxi/devfreq.
Arm GNU 13.3.Rel1 supplied GCC 13.3.1 for AArch64 Linux.

Compilation produced the correct inode accesses. All 301 imported symbol names
were compared with actual target exports. That established name availability,
not complete semantic ABI compatibility. The candidate kernel still lost three
vendor config symbols (`AW_GPU_TYPE`, `ENC_SW2001`, `JOYSTICK_RGP`), so it was never
misrepresented as the exact original vendor tree. Initial compilation also lacked
Module.symvers; a produced `.ko` alone was not treated as dependency validation.

## 3. Avoid switching GPU drivers during each game launch

Removing Panfrost and loading Mali into the same running graphical session
encountered retained GPU power-management state. Starting with Mali as first
owner made initial Vulkan probing possible, but DRM close/restore could still
block. A Vulkan instance being created did not mean PPSSPP could render or exit.

The final route keeps Mali from boot and runs a compatible ES menu on the same
stack. It avoids requiring a Panfrost↔Mali transition for every game. Recovery
still exists for a failed menu startup; the normal path stays on Mali.

## 4. Repair display-client lifetime handling

Diagnostics followed the blocked DRM restore path to the output-poll worker and
its client list. Limited reads distinguished failed reads, wrong layouts and
invalid list entries. Offline code analysis then connected the dangling entry
to early framebuffer setup failure and incomplete cleanup.

The source repair propagates boot-logo connection errors before registration,
rejects zero dimensions, and unwinds registered clients before releasing their
containing allocation. The public candidate already had a meaningful platform
cleanup implementation, while the actual binary had an empty helper; applying
only a core-source diff to unknown vendor source would not restore that helper.

Since the exact vendor source was unavailable, v116 used a bounded ARM64 repair
within three existing function bodies, plus verified branch hooks. Original
bytes and kernel hash were guarded; the kernel was not expanded into guessed
padding. Link capacity, relocations and eight modeled ARM64 execution cases were
checked. Full-image comparison found 298 modified bytes in approved kernel/checksum
ranges. These modeled checks were not substitutes for hardware validation.

## 5. Separate rendering success from panel delivery

Vulkan initialized and PPSSPP ran while the physical display remained black.
Reading the final framebuffer showed recognizable game RGB content, proving
that a running process and a successful present call were insufficient evidence
of visible output. A later capture found alpha zero throughout the ARGB buffer.

The active plane was using premultiplied blending. Changing only its pixel blend
mode to **None**, through the application's existing DRM master, immediately made
the game visible. No DMA coherency or routing change was needed for that test.
The result identified the immediate alpha/blend mismatch, not every possible
source of alpha generation. The persistent opacity helper scopes this correction
to the PPSSPP session and closes its duplicate master descriptor before teardown.

## 6. Correct whole-application rotation and input

The panel's native mode is portrait 720×960. Rotating only the PSP game content
left the PPSSPP interface sideways; correcting orientation without agreeing on
logical dimensions then clipped menus and shrank games. The final wrappers use
landscape 960×720 application dimensions and rotate the complete output. The
owner confirmed game, menu, size, audio and controls, including the corrected D-pad.

The ES menu uses its established screen rotation option. RetroArch's SDL renderer
has a target-texture rotation adapter; GLES Flycast paths have a complete-drawable
adapter. These are separate scoped paths, not a global SDL replacement.

## 7. Keep ES and PPSSPP on one boot

ES can initialize using the vendor EGL/GLES/GBM stack when its loader environment
is kept clean. A supervisor outside ES's process group coordinates normal menu
quit, DRM-master release, PPSSPP startup/quit and a fresh menu. Observing an
unchanged boot ID across round trips distinguished this from hidden reboots.
The owner also selected a game normally and confirmed exit/menu return.

Automatic startup includes a next-boot recovery mechanism. Later the dispatcher
was fixed to avoid restoring historical knulli.conf snapshots over current user
preferences. That resolved language/timezone reverting and preserves PPSSPP choices.

## 8. Other emulator and power fixes

Dreamcast rotation was corrected for normal and standalone Flycast. VL/Xtreme
initially passed the Dreamcast logo but failed entering gameplay; that earlier
logo-only report was not final validation. The original JIT fault context was
being lost through SDL's evdev emergency signal handler. The final fix sets
`SDL_NO_SIGNAL_HANDLERS=1` only for those two old cores. An experimental signal
bridge was abandoned. Both then reached gameplay and were confirmed by the owner.

Suspend immediately woke because active AIC8800 SDIO held a wake lock. The Action
Pi hook remembers enabled Wi-Fi state, disables it before suspend, then restores
the previous ConnMan service after the radio is ready. Token checks cancel stale
reconnect attempts. The owner confirmed wake and automatic reconnection.

RetroArch HOME exit works. PPSSPP HOME exit caused a freeze/recovery reboot and
was disabled; SELECT+START held for about one second remains its exit method.
An early brightness I/O observation hook caused background-music stutter. The
read-path interception was removed; the final held-button supplement is scoped
to real brightness writes and does not inspect every music-file read.

## 9. Resolve brightness recurrence at the actual hardware layer

v117/v118 attempted fixes were withdrawn. Native ascending brightness values are
correct when the physical PWM signal is correct; numerical inversion only hid
the underlying problem temporarily.

First, a DTB edited inside the appended kernel data was not the effective boot
source. The live tree came from the external DTB in the raw TOC1 package at SD
offset `0x1004000`. The FAT copy was also older than that active package. The fix
changes the actual `/backlight0/pwms` polarity flag, refreshes the TOC checksum,
and synchronizes the FAT package without changing bootloader executable code.

Second, even with runtime DT polarity normal, the BSP driver left hardware PCR
bit 8 clear while its cached state said normal. Both cold boot and resume showed
this mismatch. The guarded normalizer validates the board, PWM controller and
runtime arguments, then sets only that physical polarity bit at the late boot
gate and resume hook. Native brightness values and held adjustment stay intact.
The owner confirmed complete shutdown/start and suspend/wake, and register
readback confirmed both transitions from 0 to 256. This became stable v119.

## 10. Public packaging and PortMaster

The public variant sets English and Wi-Fi off, removes personal network settings
from both live defaults and recovery snapshots, omits the additional BIOS archive,
and retains the base system's BIOS. Deleted FAT clusters and file slack were
zeroed, rather than only removing directory entries. Machine IDs, cookies,
histories, pairings and diagnostic captures were excluded from the settings payload.

After installing PortMaster, its Python/PySDL2 interface was rotated left. PySDL2
resolves functions from a named DLL, bypassing the earlier LD_PRELOAD approach.
A private SDL adapter reuses the working renderer correction and forwards other
symbols to the original SDL library. Only PortMaster selects it. The launcher
prepares that setting again if installation/update replaces its shell entry.
The owner confirmed direction and size; this fix is included in the public IMG.

## 11. Unify the standalone PPSSPP entry

ES's Emulators/PPSSPP script contained only a direct `PPSSPP` invocation. It used
the same standalone binary as the working PSP route, but skipped the Vulkan ICD,
output wrappers and opacity/session handling. A separate libretro core exists;
the symptom did not establish two different standalone builds.

The dispatcher now recognizes that specific Emulators entry and requests the
PPSSPP UI through the existing supervisor, without selecting or requiring a ROM.
The session runner omits only the game argument in UI mode. Normal PSP path and
extension validation, Vulkan environment, rotation, opacity, preferences and
SELECT+START handling remain shared. One installation restart reloaded the
resident supervisor. The owner confirmed Vulkan, direction/size and menu return.
The correction is packaged in public v1.0.0 (internal build v119 r2) and personal v120 r2.
Public version numbering starts at v1.0.0; this rename does not change image bytes.

## v1.0.1: Wi-Fi recovery-copy diagnosis and wider rotation

The early test images could connect once and lose Wi-Fi after reboot. A passive failed-boot report identified SDIO 024c:d723 with no bound driver. Its live S06 matched the old AIC-only recovery BOOT and its S08 matched the original rootfs, while the new helper file was present but unused. Mali restore/arm rewrote the active BOOT from that older copy. The preparation marker also existed under /var/run rather than /run. Internal test8 synchronized both BOOT copies and their hashes and corrected the marker; the user then confirmed Wi-Fi after reboot on 2026-10-25. Public v1.0.1 uses the unchanged normal-test8 bytes.

This release also carries the N64/Saturn/OpenBOR/standalone RetroArch launch corrections, SDLPoP and OD-Commander adapters, scoped PortMaster game rotation, and runtime-list metadata fixes. Emulator directions were all verified on hardware by the maintainer. These internal test names remain development history, not public release numbers.

## v1.0.2: Ozone and the menu BOOT guard

- **RetroArch Ozone restored:** ordinary cores and standalone RetroArch now use GL/gl_sdl rather than forced SDL2 video, with Ozone selected for those sessions.
- **Rotation retained:** a small, scoped GLES3-context helper lets the existing full-frame adapter rotate both gameplay and Ozone. Existing hardware-core output settings and other applications are retained.
- **Menu startup fixed:** synchronize the menu guard's expected normal BOOT hash and its manifest with the Wi-Fi recovery BOOT. This fixes the stale check that could reject menu startup and trigger recovery. The safety check remains enabled.
- Retain the cumulative Wi-Fi reboot/startup fixes, emulator/SDLPoP/OD-Commander orientation, PortMaster runtime-list fixes, Mali menu and PPSSPP Vulkan.

The final runtime changes reached a healthy Mali menu after the home-device SSH update. Wi-Fi reconnected, and ordinary-core/standalone RetroArch checks completed. The owner then confirmed all final changes working on 2026-10-25. This newly packaged public IMG was not independently downloaded and reflashed; not every core, game, port or board variant was retested.

## v1.0.3 — 2026-10-26

- **Rumble:** use a 25 kHz motor PWM carrier and compensate low-strength effects. Crazy Taxi 1/2 with Flycast VL/Xtreme now provides noticeable small rumble with reduced high-pitched motor-related noise on the tested device.
- **Brightness shortcut:** hold SELECT, then use Volume +/−. Normal volume and HOME behavior are retained; held adjustment works.
- **Brightness overlay:** show a sun icon, percentage and bar above the menu or game, then hide it about 2.2 seconds after adjustment. It uses an unused display plane and runs only while visible; no idle overlay service is added.
- **Background cleanup:** disable Knulli usage-statistics reporting by default and stop the obsolete repeating boot-log copy on devices carrying it. Omit old diagnostic maps from the image.
- Existing Mali menu/PPSSPP Vulkan, Wi-Fi, screen rotation, Ozone and PortMaster functionality is retained.

## v1.0.4 — 2026-10-27

- **PPSSPP 1.20.4:** update from 1.19.3 using the official source release and an ARM64 build. PSP games and Emulators → PPSSPP both open the updated Vulkan application.
- **Vulkan/display compatibility:** preserve the existing Mali driver, rotation, output opacity correction and menu return. Add three real Vulkan forwarding exports required by the newer availability check; synchronize both persistent launcher copies.
- **Mixed Korean/English text:** improve fallback font selection for the installed Noto and Nanum families, resolving missing square glyphs in mixed strings.
- Previous Wi-Fi, emulator rotation, Ozone, PortMaster, rumble and brightness shortcut/overlay improvements are retained. No temporary test controllers, captures or personal settings are included.

## v1.0.5 — 2026-10-27

- **ZRAM service repaired:** the Services menu now starts/stops runtime-tested modules for this kernel, with the setting retained after reboot. ZRAM is **off by default**. It starts after the menu settles, uses lzo-rle, exposes logical swap of half the detected RAM and caps compressed RAM usage at a quarter of RAM (up to 512 MiB). RAM is allocated on demand. This helps memory-pressure situations; it does not guarantee higher FPS.
- **BennuGD core:** install the supplied ARM64 BennuGD libretro core and reconnect it automatically on each boot without save-overlay. The standard edition keeps its existing FBNeo/MAME cores.
- Existing PPSSPP 1.20.4/Vulkan, Mali menu, Wi-Fi, rotation, Ozone, PortMaster, rumble and brightness improvements are retained.

## v1.0.6 — 2026-10-27

- **Flycast Vulkan:** standard, VL and Xtreme now use Vulkan with correctly oriented gameplay and RetroArch menus, plus normal HOME exit and return to ES without rebooting.
- **Standard Flycast 2.7:** update the standard core to the official v2.7 source release. VL and Xtreme retain their existing source revisions.
- **Strong recommendation:** hands-on testing on the Action Pi showed a significant performance improvement when switching the standard Flycast core from OpenGL to Vulkan, with much smoother gameplay. **We strongly recommend using the standard Flycast core as your first choice.** This observed gain comes from the Vulkan switch; it is not a measured 2.7-versus-2.5 benchmark or a guarantee for every game. (Depending on the game, VL or Xtreme may perform better, so compare the cores and choose the one that works best for your game.)
- **Resolution-change rotation fix:** retain the scoped rotation loader when RetroArch reinitializes Vulkan after an internal-resolution change. The shared fix is installed for all three cores. OpenGL shaders are disabled for these Vulkan sessions; other emulators keep their existing settings.
- Existing Wi-Fi, PPSSPP, Mali menu, Ozone, PortMaster, rumble, brightness, ZRAM and BennuGD improvements are retained.

The maintainer directly played standard/VL/Xtreme Vulkan and reported improved clarity and performance, especially with the standard core. Standard 2.7 was checked remotely for game/demo and menu output, actual Vulkan reinitialization after a resolution increase, preserved orientation and clean return to ES on the same boot. Individual VL/Xtreme resolution changes, physical audio/input on 2.7, a 2.7 performance comparison, a fresh SD flash of these final images and all hardware batches were not retested.

## v1.0.7 — 2026-10-28

- **Return to the game list:** after closing PPSSPP or Flycast Vulkan, ES now reopens the saved system’s game list instead of the top-level system selector.
- **Normal startup preserved:** game-list startup is temporary for the return session. The original startup preference is restored when ES closes, or at the next supervisor start after an interrupted session. Other ES settings are retained.
- **Selection limit:** the game list opens at its first entry; the exited game’s cursor position and subfolder are not restored.
- Existing Mali, PPSSPP Vulkan, Flycast Vulkan/standard core 2.7, rotation, Wi-Fi, Ozone, PortMaster, rumble, brightness, ZRAM and BennuGD functionality is retained. Standard Flycast is a good first choice, but VL or Xtreme may perform better in some games; compare the cores for your game.

On the maintainer device, PSP OutRun 2006 and standard Flycast Crazy Taxi 2 were launched from their ES game lists, exited normally, and returned to the respective PSP/Dreamcast lists without another reboot; captures confirmed both lists. Initial startup remained unchanged after the installation reboot. Preference restoration was checked with both absent and explicit-false settings while preserving other settings. VL/Xtreme use the same supervisor path; their individual launches and a fresh SD flash of these final images were not repeated.

## v1.0.8 — 2026-10-31

- **Yaba Sanshiro standalone updated from 1.9.0 to 1.20.51:** the official engine and frontend are adapted for Linux ARM64/GLES, with the ARM64 JIT enabled and Action Pi rotation retained. The RetroArch Saturn core is unchanged.
- **In-game settings: press L3 (click the left analog stick) to open or close the standalone menu.**
- **Audio crackles corrected:** the realtime sound generator now keeps cumulative deadlines instead of accumulating Linux scheduler delays. This fixes the verified BIOS/game crackles without increasing the audio buffer or changing the output backend.
- **Controls and FPS menu fixed:** game buttons, D-pad and sticks are mapped correctly; the Show/Hide FPS setting works without the previous crash. GLES menu drawing and render-thread initialization are corrected.
- **Trial cleanup:** the latest GLES executable has a permanent launch path. Old trial routes and the failed Saturn Vulkan experiment are excluded from this release.
- Existing Mali, PPSSPP Vulkan, Flycast Vulkan/standard core 2.7, Wi-Fi, rotation, Ozone, PortMaster, brightness, rumble, ZRAM and BennuGD are retained. Saturn standalone uses **GLES**, not Vulkan.

The user confirmed the latest standalone game buttons, D-pad, sticks, L3 menu and FPS toggle, and reported that BIOS/game crackles disappeared after the final sound timing fix. Measured audio generation/delivery returned close to 44.1 kHz without observed empty-ring samples in the short measurement. The final v1.0.8 images have not been freshly flashed or separately reboot-tested. The earlier Magic Knight Rayearth syllable-repetition issue has not been rechecked after this fix; it is not claimed resolved.

## v1.0.8 — image refresh r2 / 2026-10-31

- **Image refresh r2 — Saturn controller compatibility:** the standalone now honors the ordinary digital/3D analog pad selector. This fixes the confirmed START-button issue in affected games. In ordinary pad mode, the left stick and physical D-pad can both drive digital directions while preserving the ordinary Saturn controller protocol. Held inputs are merged so releasing one source does not release the other; diagonals, a center deadzone and saved axis inversion are supported. True 3D mode retains its analog input.

The user confirmed the START compatibility fix, followed by normal operation of the merged stick and D-pad input on the device. A focused host check covered held-source release ordering, diagonals, opposite directions, deadzone, inversion, disconnect, START preservation and bypass in true analog mode. Final r2 images have not been freshly flashed.

## v1.0.9 — 2026-11-03

- **Flycast standalone now defaults to Vulkan:** the regular standalone entry launches the Action Pi build based on official Flycast v2.7. Existing RetroArch standard/VL/Xtreme cores remain available.
- **User-reported performance:** in the games tried, the user reports performance on par with or better than the RetroArch cores. This is a hands-on assessment, not a controlled benchmark or a guarantee for every game.
- **Press L3 (click the left analog stick) to open Flycast settings.** Game and menu output use the full-frame rotation correction; HOME returns to ES.
- **Settings persist:** vibration-pack selection and other settings changed in Flycast survive exit and relaunch. Explicit ES settings take priority; the remaining app preferences and controller remaps are retained.
- **GL fallback path retained:** the launcher includes the original GL path when the Vulkan payload is unavailable or explicitly disabled; switching back to GL was not separately tested in this final revision. Test-only Ports entries are excluded.

the user confirmed Vulkan gameplay, menu orientation, L3, HOME return and final settings persistence. The final Vulkan default/settings revision has not separately been confirmed after reboot, and final distribution images have not yet been flashed to another SD card.
