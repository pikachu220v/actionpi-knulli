# Action Pi Knulli adaptation

Unofficial Knulli adaptation for **Helegaly Action Pi**, documenting the work needed
to run a Mali-based EmulationStation menu and PPSSPP Vulkan on the same boot.
This is a community adaptation, not an official Knulli release or a universal
TrimUI Smart Pro S firmware.

[한국어 안내](README.ko.md) · [Development history](docs/HISTORY.md) ·
[Architecture](docs/ARCHITECTURE.md) · [Build/source status](docs/BUILD.md) ·
[Troubleshooting](docs/TROUBLESHOOTING.md)

## Download and install

Choose your edition:

| Edition | Release download |
| --- | --- |
| Standard / 일반판 | [Action Pi Knulli v1.0.9](https://github.com/pikachu220v/actionpi-knulli/releases/tag/v1.0.9) |
| 한국 사용자용 CRC 무시 코어 적용판 | [CRC 적용판 v1.0.9 다운로드](https://github.com/pikachu220v/actionpi-knulli/releases/tag/v1.0.9-crc-ko) |

Use the `.img.xz` asset and matching SHA256 file. Extract the image if your flashing
application does not accept XZ, then write the image to the **whole SD card**.
Writing an image replaces the selected card's contents.

**On first installation, a black screen after the boot image is normal. Please
allow about 5 minutes: the device will automatically restart once or twice while
expanding SHARE and installing settings, then show the menu. There is no need to
worry; leave the power on and wait for setup to finish.** Subsequent PSP launches
do not require a reboot. See [installation and release details](docs/RELEASE.md).

## Distribution defaults

| Item | Public distribution |
| --- | --- |
| Language | English, including PPSSPP |
| Wi-Fi | Off initially; no personal saved SSID/password |
| Additional BIOS collection | Excluded |
| Original base-system BIOS | Retained unchanged |
| Game ROMs | Not included |
| Ports restore-original-menu shortcut | Removed |
| Old hardcoded PPSSPP Vulkan test shortcut | Removed; launch games from PSP |
| PortMaster | Installer retained; direction/size fix applied when launched |

The distribution is **not BIOS-free**: it retains the base system's original
BIOS files at the maintainer's explicit choice. Add any additional BIOS you need
to SHARE's `bios` directory. This repository does not upload the separate
personal images or their Wi-Fi configuration.

## Working features

- Mali owns the GPU from startup; ES → PPSSPP Vulkan → ES works without a reboot
  between games.
- Correct menu, PSP, RetroArch, Flycast and PortMaster direction/size on the
  physically portrait 720×960 panel; application layout is landscape 960×720.
- PPSSPP game/menu output, audio, analog sticks, buttons and D-pad; preferences
  persist between launches.
- The ES **Emulators → PPSSPP** entry opens the same Vulkan application menu,
  without needing a game file, using the same display correction and exit path.
- Normal/standalone Flycast, plus VL/Xtreme gameplay after scoped signal handling.
- Brightness direction and held adjustment, including cold boot and suspend resume.
- Suspend/wake and Wi-Fi reconnect when Wi-Fi was enabled before sleep.
- Korean/Seoul preferences remain selectable and persistent, although this public
  edition starts in English. Speaker LINEOUT gain is adjusted from 23 to 25.

Hold **SELECT+START for about one second** to exit PPSSPP. Emulator exit using
the top HOME key works in RetroArch and is disabled in PPSSPP after a quit regression.
Flycast standalone HOME exit is not separately confirmed.

## Evidence and limits

The core functions were confirmed working on hardware by the device owner. PortMaster
direction/size was separately confirmed on hardware before packaging. Public
distribution defaults and file integrity were checked offline. On 2026-10-24,
the owner downloaded the published v1.0.0 image, wrote it to an SD card,
installed it on the device and confirmed normal operation. See [test coverage](docs/TESTING.md).

The Knulli board-integration base is the upstream [Action Pi board configuration](https://github.com/knulli-cfw/knulli-linux/tree/knulli-main/board/allwinner/a527/helegany-action-pi)
on `knulli-main` (`board/allwinner/a527/helegany-action-pi`).

The exact vendor source of the original 5.15.147 kernel has **not** been identified.
The pinned public candidate is not described as that exact source. This repository
contains the adaptation code, guarded repair source, recovered config, and pinned
Mali source, but is **not a complete from-source rebuild of every firmware
component**. [Sources, licenses and unresolved provenance](docs/SOURCES_AND_LICENSES.md)
distinguish these cases explicitly.

## Repository contents

| Directory | Purpose |
| --- | --- |
| `overlay/boot/` | Actual runtime scripts/source extracted from the public IMG |
| `src/` | Rotation adapters and guarded display/PWM repair source |
| `kernel/` | Recovered kernel config, candidate options, repair patch/evidence |
| `third_party/mali-valhall/` | Pinned upstream driver source, with its license |
| `config/` | Public defaults and PortMaster installation entry |
| `tools/` | Portable helper build script and historical packaging scripts |
| `release/` | Public image manifest, hashes and component inventory; no IMG in Git |
| `docs/` | History, architecture, testing, troubleshooting and provenance |

Original project glue is provided under the scoped MIT terms in `LICENSE`;
kernel-derived and third-party files retain their own terms. No blanket MIT
license is applied to the firmware. Credits: Knulli/Batocera, Linux/Allwinner/
Orange Pi/Radxa, Arm, SDL, PPSSPP, Libretro/Flycast, PortMaster and the
[Ultramarine handheld work](https://github.com/Ultramarine-Linux/ultramarine-handheld)
that helped establish the vendor-stack direction.

## Release history

### v1.0.9 changes

- **Flycast standalone now defaults to Vulkan:** the regular standalone entry launches the Action Pi build based on official Flycast v2.7. Existing RetroArch standard/VL/Xtreme cores remain available.
- **User-reported performance:** in the games tried, the user reports performance on par with or better than the RetroArch cores. This is a hands-on assessment, not a controlled benchmark or a guarantee for every game.
- **Press L3 (click the left analog stick) to open Flycast settings.** Game and menu output use the full-frame rotation correction; HOME returns to ES.
- **Settings persist:** vibration-pack selection and other settings changed in Flycast survive exit and relaunch. Explicit ES settings take priority; the remaining app preferences and controller remaps are retained.
- **GL fallback path retained:** the launcher includes the original GL path when the Vulkan payload is unavailable or explicitly disabled; switching back to GL was not separately tested in this final revision. Test-only Ports entries are excluded.

the user confirmed Vulkan gameplay, menu orientation, L3, HOME return and final settings persistence. The final Vulkan default/settings revision has not separately been confirmed after reboot, and final distribution images have not yet been flashed to another SD card.

### v1.0.8 changes

- **Image refresh r2 — Saturn controller compatibility:** the standalone now honors the ordinary digital/3D analog pad selector. This fixes the confirmed START-button issue in affected games. In ordinary pad mode, the left stick and physical D-pad can both drive digital directions while preserving the ordinary Saturn controller protocol. Held inputs are merged so releasing one source does not release the other; diagonals, a center deadzone and saved axis inversion are supported. True 3D mode retains its analog input.

The user confirmed the START compatibility fix, followed by normal operation of the merged stick and D-pad input on the device. A focused host check covered held-source release ordering, diagonals, opposite directions, deadzone, inversion, disconnect, START preservation and bypass in true analog mode. Final r2 images have not been freshly flashed.

- **Yaba Sanshiro standalone updated from 1.9.0 to 1.20.51:** the official engine and frontend are adapted for Linux ARM64/GLES, with the ARM64 JIT enabled and Action Pi rotation retained. The RetroArch Saturn core is unchanged.
- **In-game settings: press L3 (click the left analog stick) to open or close the standalone menu.**
- **Audio crackles corrected:** the realtime sound generator now keeps cumulative deadlines instead of accumulating Linux scheduler delays. This fixes the verified BIOS/game crackles without increasing the audio buffer or changing the output backend.
- **Controls and FPS menu fixed:** game buttons, D-pad and sticks are mapped correctly; the Show/Hide FPS setting works without the previous crash. GLES menu drawing and render-thread initialization are corrected.
- **Trial cleanup:** the latest GLES executable has a permanent launch path. Old trial routes and the failed Saturn Vulkan experiment are excluded from this release.
- Existing Mali, PPSSPP Vulkan, Flycast Vulkan/standard core 2.7, Wi-Fi, rotation, Ozone, PortMaster, brightness, rumble, ZRAM and BennuGD are retained. Saturn standalone uses **GLES**, not Vulkan.

The user confirmed the latest standalone game buttons, D-pad, sticks, L3 menu and FPS toggle, and reported that BIOS/game crackles disappeared after the final sound timing fix. Measured audio generation/delivery returned close to 44.1 kHz without observed empty-ring samples in the short measurement. The final v1.0.8 images have not been freshly flashed or separately reboot-tested. The earlier Magic Knight Rayearth syllable-repetition issue has not been rechecked after this fix; it is not claimed resolved.

### v1.0.7 changes

- **Return to the game list:** after closing PPSSPP or Flycast Vulkan, ES now reopens the saved system’s game list instead of the top-level system selector.
- **Normal startup preserved:** game-list startup is temporary for the return session. The original startup preference is restored when ES closes, or at the next supervisor start after an interrupted session. Other ES settings are retained.
- **Selection limit:** the game list opens at its first entry; the exited game’s cursor position and subfolder are not restored.
- Existing Mali, PPSSPP Vulkan, Flycast Vulkan/standard core 2.7, rotation, Wi-Fi, Ozone, PortMaster, rumble, brightness, ZRAM and BennuGD functionality is retained. Standard Flycast is a good first choice, but VL or Xtreme may perform better in some games; compare the cores for your game.

On the maintainer device, PSP OutRun 2006 and standard Flycast Crazy Taxi 2 were launched from their ES game lists, exited normally, and returned to the respective PSP/Dreamcast lists without another reboot; captures confirmed both lists. Initial startup remained unchanged after the installation reboot. Preference restoration was checked with both absent and explicit-false settings while preserving other settings. VL/Xtreme use the same supervisor path; their individual launches and a fresh SD flash of these final images were not repeated.

### v1.0.6 changes

- **Flycast Vulkan:** standard, VL and Xtreme now use Vulkan with correctly oriented gameplay and RetroArch menus, plus normal HOME exit and return to ES without rebooting.
- **Standard Flycast 2.7:** update the standard core to the official v2.7 source release. VL and Xtreme retain their existing source revisions.
- **Strong recommendation:** hands-on testing on the Action Pi showed a significant performance improvement when switching the standard Flycast core from OpenGL to Vulkan, with much smoother gameplay. **We strongly recommend using the standard Flycast core as your first choice.** This observed gain comes from the Vulkan switch; it is not a measured 2.7-versus-2.5 benchmark or a guarantee for every game. (Depending on the game, VL or Xtreme may perform better, so compare the cores and choose the one that works best for your game.)
- **Resolution-change rotation fix:** retain the scoped rotation loader when RetroArch reinitializes Vulkan after an internal-resolution change. The shared fix is installed for all three cores. OpenGL shaders are disabled for these Vulkan sessions; other emulators keep their existing settings.
- Existing Wi-Fi, PPSSPP, Mali menu, Ozone, PortMaster, rumble, brightness, ZRAM and BennuGD improvements are retained.

The maintainer directly played standard/VL/Xtreme Vulkan and reported improved clarity and performance, especially with the standard core. Standard 2.7 was checked remotely for game/demo and menu output, actual Vulkan reinitialization after a resolution increase, preserved orientation and clean return to ES on the same boot. Individual VL/Xtreme resolution changes, physical audio/input on 2.7, a 2.7 performance comparison, a fresh SD flash of these final images and all hardware batches were not retested.

### v1.0.5 changes

- **ZRAM service repaired:** the Services menu now starts/stops runtime-tested modules for this kernel, with the setting retained after reboot. ZRAM is **off by default**. It starts after the menu settles, uses lzo-rle, exposes logical swap of half the detected RAM and caps compressed RAM usage at a quarter of RAM (up to 512 MiB). RAM is allocated on demand. This helps memory-pressure situations; it does not guarantee higher FPS.
- **BennuGD core:** install the supplied ARM64 BennuGD libretro core and reconnect it automatically on each boot without save-overlay. The standard edition keeps its existing FBNeo/MAME cores.
- Existing PPSSPP 1.20.4/Vulkan, Mali menu, Wi-Fi, rotation, Ozone, PortMaster, rumble and brightness improvements are retained.

ZRAM block compression/readback, actual 32 MiB swap-out/in, service start/stop and reboot startup were verified on the maintainer device. BennuGD file identity and active core mapping were verified; gameplay and reboot testing of that supplied core were not repeated. Long memory-pressure stress, suspend/resume, all hardware batches and a fresh SD flash of these newly packaged v1.0.5 images have not been tested.

### v1.0.4 changes

- **PPSSPP 1.20.4:** update from 1.19.3 using the official source release and an ARM64 build. PSP games and Emulators → PPSSPP both open the updated Vulkan application.
- **Vulkan/display compatibility:** preserve the existing Mali driver, rotation, output opacity correction and menu return. Add three real Vulkan forwarding exports required by the newer availability check; synchronize both persistent launcher copies.
- **Mixed Korean/English text:** improve fallback font selection for the installed Noto and Nanum families, resolving missing square glyphs in mixed strings.
- Previous Wi-Fi, emulator rotation, Ozone, PortMaster, rumble and brightness shortcut/overlay improvements are retained. No temporary test controllers, captures or personal settings are included.

The owner confirmed PPSSPP 1.20.4 still launches correctly after reboot. On-device captures confirmed correct menu orientation and mixed Korean/English text; normal exit and return to ES without reboot were verified. Earlier title-screen rendering was checked remotely. Every game, performance characteristic and hardware batch was not retested. The newly packaged v1.0.4 SD installation images have not been independently reflashed.

### v1.0.3 changes

- **Rumble:** use a 25 kHz motor PWM carrier and compensate low-strength effects. Crazy Taxi 1/2 with Flycast VL/Xtreme now provides noticeable small rumble with reduced high-pitched motor-related noise on the tested device.
- **Brightness shortcut:** hold SELECT, then use Volume +/−. Normal volume and HOME behavior are retained; held adjustment works.
- **Brightness overlay:** show a sun icon, percentage and bar above the menu or game, then hide it about 2.2 seconds after adjustment. It uses an unused display plane and runs only while visible; no idle overlay service is added.
- **Background cleanup:** disable Knulli usage-statistics reporting by default and stop the obsolete repeating boot-log copy on devices carrying it. Omit old diagnostic maps from the image.
- Existing Mali menu/PPSSPP Vulkan, Wi-Fi, screen rotation, Ozone and PortMaster functionality is retained.

On-device tests confirmed rumble strength/noise and persistence after reboot, disabled statistics/repeating logging after reboot, and the brightness shortcut's direction, hold and normal-volume behavior. The owner confirmed the brightness overlay in ES and PPSSPP, automatic hiding, and game exit/menu return; remote inspection confirmed the overlay worker exits. The overlay uses a shared display path, but every emulator and hardware batch was not individually retested. The owner subsequently rebooted the device and confirmed all applied changes still work, including the brightness shortcut and overlay. These newly packaged installation images have not been independently reflashed.

### v1.0.2 changes

- **RetroArch Ozone restored:** ordinary cores and standalone RetroArch now use GL/gl_sdl rather than forced SDL2 video, with Ozone selected for those sessions.
- **Rotation retained:** a small, scoped GLES3-context helper lets the existing full-frame adapter rotate both gameplay and Ozone. Existing hardware-core output settings and other applications are retained.
- **Menu startup fixed:** synchronize the menu guard's expected normal BOOT hash and its manifest with the Wi-Fi recovery BOOT. This fixes the stale check that could reject menu startup and trigger recovery. The safety check remains enabled.
- Retain the cumulative Wi-Fi reboot/startup fixes, emulator/SDLPoP/OD-Commander orientation, PortMaster runtime-list fixes, Mali menu and PPSSPP Vulkan.

The final runtime changes reached a healthy Mali menu after the home-device SSH update. Wi-Fi reconnected, and ordinary-core/standalone RetroArch checks completed. The owner then confirmed all final changes working on 2026-10-25. This newly packaged public IMG was not independently downloaded and reflashed; not every core, game, port or board variant was retested. [Release notes](release/NOTES.md).

### v1.0.1 update

Wi-Fi reboot persistence, AIC/RTL8723DS support, emulator/tool/game rotation and PortMaster runtime-menu fixes are included. Emulator directions were all confirmed on hardware by the maintainer; test8 Wi-Fi after reboot was confirmed in device feedback. The public IMG is unchanged from normal test8. [Full changes](CHANGELOG.md).

## Downloads / 다운로드

### [일반판 v1.0.9 / Standard edition](https://github.com/pikachu220v/actionpi-knulli/releases/tag/v1.0.9)

### [한국 사용자용 — CRC 무시 코어 적용판 v1.0.9](https://github.com/pikachu220v/actionpi-knulli/releases/tag/v1.0.9-crc-ko)

CRC 무시 코어: [dsno님 자료](https://dsno.tistory.com/m/). [CRC판 한국어 안내](docs/CRC_KOREAN.ko.md).
