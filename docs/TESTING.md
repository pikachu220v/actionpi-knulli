# Verification scope

[English](TESTING.md) · [한국어](TESTING.ko.md)

| Check | Evidence |
| --- | --- |
| v1.0.2 final device runtime | Healthy menu/reboot Wi-Fi after SSH update and guard fix; owner subsequently confirmed all final changes, including Ozone, working |
| Newly packaged v1.0.2 IMG | File readback, complete BOOT references, unaffected bytes and XZ/image hashes checked; a fresh IMG reflash was not independently repeated |
| v1.0.1 source firmware | On 2026-10-25, user feedback confirmed test8 Wi-Fi still works after reboot; public IMG bytes match normal test8 |
| Emulator directions | Maintainer confirmed all emulator screen directions on hardware |
| PortMaster menus | Runtime manager and port-management display confirmed; full update/download/install matrix not exhaustively retested |
| Boot persistence | Actual Mali restore/arm functions preserved updated S06/S08 for three cycles in temporary files; transaction recovery and separate /var/run marker checked offline |
| Core functions | Owner confirmed normal operation after installation |
| Brightness | Owner confirmed complete shutdown/start and suspend/wake; runtime DT/PWM readback agreed |
| ES↔PPSSPP | Automatic and manual launch/exit/menu return confirmed on the same boot |
| PSP display/audio/input | Owner confirmed game and emulator UI, full-size orientation, sound and controls |
| Preferences | PPSSPP exit/relaunch persistence and system language/timezone persistence confirmed |
| RetroArch | Display direction/size and HOME exit confirmed |
| Flycast | Normal/standalone orientation confirmed; VL/Xtreme tested into gameplay, not only startup logo |
| Suspend | Screen remains off; wakes on next press; previously enabled Wi-Fi reconnects |
| PortMaster | Owner relaunched and confirmed direction and size before packaging |
| Emulators/PPSSPP standalone | Owner confirmed Vulkan selection, direction/size and SELECT+START return after the UI-only route fix; no ROM required |
| Public defaults | Offline archive assertions for English, Wi-Fi0, no saved personal network and removed Ports entries |
| Source/base integrity | Source IMG checksum, modified-file readback, unchanged rootfs checksum and final IMG checksum |
| Private data cleanup | Sanitized settings/recovery copies, cleared free clusters/slack, known-credential raw scan |
| Final public variant | On 2026-10-24, owner downloaded the published v1.0.0 image, wrote it to an SD card, installed it on the device and confirmed normal operation |

No claim is made that every game, every PortMaster port, every emulator backend,
all suspend scenarios, all driver ABI behavior or unrelated board variants were
tested. Standalone Flycast HOME exit remains unconfirmed. Shader cache presence,
module load, Vulkan enumeration, a presented framebuffer and a visible game are
different milestones; the history distinguishes them.

The kernel repair's modeled ARM64 tests check selected calls, error paths,
callee-saved state and cleanup ordering. They do not emulate the complete device,
allocator, concurrency, power management or electrical panel.

## v1.0.2

The final runtime changes reached a healthy Mali menu after the home-device SSH update. Wi-Fi reconnected, and ordinary-core/standalone RetroArch checks completed. The owner then confirmed all final changes working on 2026-10-25. This newly packaged public IMG was not independently downloaded and reflashed; not every core, game, port or board variant was retested.

## v1.0.3 — 2026-10-26

- **Rumble:** use a 25 kHz motor PWM carrier and compensate low-strength effects. Crazy Taxi 1/2 with Flycast VL/Xtreme now provides noticeable small rumble with reduced high-pitched motor-related noise on the tested device.
- **Brightness shortcut:** hold SELECT, then use Volume +/−. Normal volume and HOME behavior are retained; held adjustment works.
- **Brightness overlay:** show a sun icon, percentage and bar above the menu or game, then hide it about 2.2 seconds after adjustment. It uses an unused display plane and runs only while visible; no idle overlay service is added.
- **Background cleanup:** disable Knulli usage-statistics reporting by default and stop the obsolete repeating boot-log copy on devices carrying it. Omit old diagnostic maps from the image.
- Existing Mali menu/PPSSPP Vulkan, Wi-Fi, screen rotation, Ozone and PortMaster functionality is retained.

On-device tests confirmed rumble strength/noise and persistence after reboot, disabled statistics/repeating logging after reboot, and the brightness shortcut's direction, hold and normal-volume behavior. The owner confirmed the brightness overlay in ES and PPSSPP, automatic hiding, and game exit/menu return; remote inspection confirmed the overlay worker exits. The overlay uses a shared display path, but every emulator and hardware batch was not individually retested. The owner subsequently rebooted the device and confirmed all applied changes still work, including the brightness shortcut and overlay. These newly packaged installation images have not been independently reflashed.

## v1.0.4 — 2026-10-27

- **PPSSPP 1.20.4:** update from 1.19.3 using the official source release and an ARM64 build. PSP games and Emulators → PPSSPP both open the updated Vulkan application.
- **Vulkan/display compatibility:** preserve the existing Mali driver, rotation, output opacity correction and menu return. Add three real Vulkan forwarding exports required by the newer availability check; synchronize both persistent launcher copies.
- **Mixed Korean/English text:** improve fallback font selection for the installed Noto and Nanum families, resolving missing square glyphs in mixed strings.
- Previous Wi-Fi, emulator rotation, Ozone, PortMaster, rumble and brightness shortcut/overlay improvements are retained. No temporary test controllers, captures or personal settings are included.

The owner confirmed PPSSPP 1.20.4 still launches correctly after reboot. On-device captures confirmed correct menu orientation and mixed Korean/English text; normal exit and return to ES without reboot were verified. Earlier title-screen rendering was checked remotely. Every game, performance characteristic and hardware batch was not retested. The newly packaged v1.0.4 SD installation images have not been independently reflashed.

## v1.0.5 — 2026-10-27

- **ZRAM service repaired:** the Services menu now starts/stops runtime-tested modules for this kernel, with the setting retained after reboot. ZRAM is **off by default**. It starts after the menu settles, uses lzo-rle, exposes logical swap of half the detected RAM and caps compressed RAM usage at a quarter of RAM (up to 512 MiB). RAM is allocated on demand. This helps memory-pressure situations; it does not guarantee higher FPS.
- **BennuGD core:** install the supplied ARM64 BennuGD libretro core and reconnect it automatically on each boot without save-overlay. The standard edition keeps its existing FBNeo/MAME cores.
- Existing PPSSPP 1.20.4/Vulkan, Mali menu, Wi-Fi, rotation, Ozone, PortMaster, rumble and brightness improvements are retained.

ZRAM block compression/readback, actual 32 MiB swap-out/in, service start/stop and reboot startup were verified on the maintainer device. BennuGD file identity and active core mapping were verified; gameplay and reboot testing of that supplied core were not repeated. Long memory-pressure stress, suspend/resume, all hardware batches and a fresh SD flash of these newly packaged v1.0.5 images have not been tested.

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
