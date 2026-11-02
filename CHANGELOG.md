# Release and development milestones

These are curated milestones, not a fabricated historical Git commit log.
Development checkpoint numbers are internal, not upstream Knulli versions.
Public release numbering starts at **v1.0.0**.







## v1.0.9 — 2026-11-03

- **Flycast standalone now defaults to Vulkan:** the regular standalone entry launches the Action Pi build based on official Flycast v2.7. Existing RetroArch standard/VL/Xtreme cores remain available.
- **User-reported performance:** in the games tried, the user reports performance on par with or better than the RetroArch cores. This is a hands-on assessment, not a controlled benchmark or a guarantee for every game.
- **Press L3 (click the left analog stick) to open Flycast settings.** Game and menu output use the full-frame rotation correction; HOME returns to ES.
- **Settings persist:** vibration-pack selection and other settings changed in Flycast survive exit and relaunch. Explicit ES settings take priority; the remaining app preferences and controller remaps are retained.
- **GL fallback path retained:** the launcher includes the original GL path when the Vulkan payload is unavailable or explicitly disabled; switching back to GL was not separately tested in this final revision. Test-only Ports entries are excluded.

- **Flycast 스탠드얼론 Vulkan 기본 적용:** 평소 스탠드얼론 항목에서 공식 Flycast v2.7 기반 액션파이용 Vulkan 실행 파일을 사용합니다. 기존 RetroArch 일반·VL·Xtreme 코어도 유지합니다.
- **사용자 실기 체감 기준, RetroArch 코어와 동등하거나 더 나은 성능**을 확인했습니다. 정식 동일 조건 벤치마크 결과나 모든 게임의 성능 보장을 뜻하지 않습니다.
- **L3(왼쪽 아날로그 스틱 클릭)로 Flycast 설정 메뉴에 들어갑니다.** 게임과 자체 메뉴의 전체 화면 회전을 보정하고 HOME으로 ES에 복귀합니다.
- **설정 유지 보완:** Flycast 안에서 고친 진동팩과 각종 설정을 종료·재실행 후에도 유지합니다. ES에서 명시한 옵션은 우선 적용하고, 나머지 앱 설정과 패드 재매핑은 보존합니다.
- **GL 복구 경로 유지:** Vulkan 파일이 없거나 비활성화한 경우의 기존 GL 실행 분기를 유지합니다. 최종 수정판에서 GL로 되돌리는 전환 자체를 별도로 실기 재시험하지는 않았습니다. Ports 시험 항목은 포함하지 않습니다.

## v1.0.8 — 2026-10-31

- **Image refresh r2 — Saturn controller compatibility:** the standalone now honors the ordinary digital/3D analog pad selector. This fixes the confirmed START-button issue in affected games. In ordinary pad mode, the left stick and physical D-pad can both drive digital directions while preserving the ordinary Saturn controller protocol. Held inputs are merged so releasing one source does not release the other; diagonals, a center deadzone and saved axis inversion are supported. True 3D mode retains its analog input.

- **이미지 갱신 r2 — 새턴 패드 호환성:** 스탠드얼론이 일반 패드·3D 아날로그 패드 선택을 올바르게 따르도록 수정해 일부 게임에서 확인된 START 무반응을 해결했습니다. 일반 패드 모드에서도 왼쪽 스틱과 D패드를 모두 방향 이동에 사용할 수 있습니다. 게임에는 일반 새턴 패드로 전달하며, 한쪽 입력만 놓아도 다른 쪽의 눌림을 유지합니다. 대각선·중앙 데드존·저장된 축 반전을 지원하며 실제 3D 모드의 아날로그 입력은 유지합니다.

- **Yaba Sanshiro standalone updated from 1.9.0 to 1.20.51:** the official engine and frontend are adapted for Linux ARM64/GLES, with the ARM64 JIT enabled and Action Pi rotation retained. The RetroArch Saturn core is unchanged.
- **In-game settings: press L3 (click the left analog stick) to open or close the standalone menu.**
- **Audio crackles corrected:** the realtime sound generator now keeps cumulative deadlines instead of accumulating Linux scheduler delays. This fixes the verified BIOS/game crackles without increasing the audio buffer or changing the output backend.
- **Controls and FPS menu fixed:** game buttons, D-pad and sticks are mapped correctly; the Show/Hide FPS setting works without the previous crash. GLES menu drawing and render-thread initialization are corrected.
- **Trial cleanup:** the latest GLES executable has a permanent launch path. Old trial routes and the failed Saturn Vulkan experiment are excluded from this release.
- Existing Mali, PPSSPP Vulkan, Flycast Vulkan/standard core 2.7, Wi-Fi, rotation, Ozone, PortMaster, brightness, rumble, ZRAM and BennuGD are retained. Saturn standalone uses **GLES**, not Vulkan.

- **야바산시로 스탠드얼론 1.9.0 → 1.20.51 업데이트:** 공식 엔진과 프런트엔드를 Linux ARM64/GLES용으로 적용했습니다. ARM64 JIT와 액션파이 회전 보정을 유지하며 RetroArch 새턴 코어는 변경하지 않았습니다.
- **게임 중 설정 메뉴는 L3(왼쪽 아날로그 스틱 클릭)로 열고 닫습니다.**
- **소리 지직·틱틱 잡음 수정:** 소리 생성 시점을 누적 기준으로 계산하여 Linux 스케줄러의 대기 지연이 계속 쌓이는 문제를 고쳤습니다. 오디오 버퍼 확대나 출력 방식 변경 없이 실기에서 확인된 BIOS·게임 잡음을 해결했습니다.
- **조작과 FPS 메뉴 수정:** 게임 버튼·D패드·스틱 매핑을 적용하고 Show/Hide FPS의 표시·숨김과 충돌 문제를 수정했습니다. GLES 설정 메뉴 그리기와 렌더링 스레드의 초기화도 보완했습니다.
- **시험 파일 정리:** 최신 GLES판을 정식 실행 경로로 연결했습니다. 구형 시험 연결과 실패한 새턴 Vulkan 실험은 배포에 포함하지 않습니다.
- 기존 Mali·PPSSPP Vulkan·Flycast Vulkan/일반 코어 2.7·Wi-Fi·회전·Ozone·PortMaster·밝기·진동·ZRAM·BennuGD는 유지합니다. 새턴 스탠드얼론은 Vulkan이 아닌 **GLES**입니다.

## v1.0.7 — 2026-10-28

- **Return to the game list:** after closing PPSSPP or Flycast Vulkan, ES now reopens the saved system’s game list instead of the top-level system selector.
- **Normal startup preserved:** game-list startup is temporary for the return session. The original startup preference is restored when ES closes, or at the next supervisor start after an interrupted session. Other ES settings are retained.
- **Selection limit:** the game list opens at its first entry; the exited game’s cursor position and subfolder are not restored.
- Existing Mali, PPSSPP Vulkan, Flycast Vulkan/standard core 2.7, rotation, Wi-Fi, Ozone, PortMaster, rumble, brightness, ZRAM and BennuGD functionality is retained. Standard Flycast is a good first choice, but VL or Xtreme may perform better in some games; compare the cores for your game.

- **게임 종료 후 목록 복귀:** PPSSPP·Flycast Vulkan을 종료하면 ES 상위 기종 선택 화면 대신 저장된 해당 기종의 게임 목록으로 돌아갑니다.
- **평소 부팅 설정 유지:** 게임 종료 후 복귀할 때만 임시로 게임 목록을 열며, ES 종료 후 원래 시작 설정을 복원합니다. 비정상 종료된 경우 다음 감독자 시작 때 복원하고 다른 ES 설정은 유지합니다.
- **선택 위치 제한:** 목록은 첫 항목부터 표시하며 종료한 게임의 커서·하위 폴더 위치까지 복원하는 기능은 아닙니다.
- 기존 Mali·PPSSPP Vulkan·Flycast Vulkan/일반 코어 2.7·회전·Wi-Fi·Ozone·PortMaster·진동·밝기·ZRAM·BennuGD 기능은 유지합니다. 일반 Flycast를 우선 권장하지만 게임에 따라 VL이나 Xtreme이 더 유리할 수 있으니 비교해서 선택해 주세요.

## v1.0.6 — 2026-10-27

- **Flycast Vulkan:** standard, VL and Xtreme now use Vulkan with correctly oriented gameplay and RetroArch menus, plus normal HOME exit and return to ES without rebooting.
- **Standard Flycast 2.7:** update the standard core to the official v2.7 source release. VL and Xtreme retain their existing source revisions.
- **Strong recommendation:** hands-on testing on the Action Pi showed a significant performance improvement when switching the standard Flycast core from OpenGL to Vulkan, with much smoother gameplay. **We strongly recommend using the standard Flycast core as your first choice.** This observed gain comes from the Vulkan switch; it is not a measured 2.7-versus-2.5 benchmark or a guarantee for every game. (Depending on the game, VL or Xtreme may perform better, so compare the cores and choose the one that works best for your game.)
- **Resolution-change rotation fix:** retain the scoped rotation loader when RetroArch reinitializes Vulkan after an internal-resolution change. The shared fix is installed for all three cores. OpenGL shaders are disabled for these Vulkan sessions; other emulators keep their existing settings.
- Existing Wi-Fi, PPSSPP, Mali menu, Ozone, PortMaster, rumble, brightness, ZRAM and BennuGD improvements are retained.

- **Flycast Vulkan 적용:** 일반·VL·Xtreme을 Vulkan으로 실행하며 게임·RetroArch 메뉴 회전 보정, HOME 종료와 재부팅 없는 ES 메뉴 복귀를 연결했습니다.
- **일반 Flycast 2.7 업데이트:** 일반 코어만 공식 v2.7 소스로 업데이트했습니다. VL·Xtreme의 소스 버전은 유지했습니다.
- **일반 코어 강력 추천:** 액션파이 실기에서 일반 Flycast 코어를 OpenGL에서 Vulkan으로 전환한 뒤 큰 폭의 성능 향상과 훨씬 부드러운 게임 화면을 직접 확인했습니다. **일반 Flycast 코어를 우선 사용하실 것을 강력히 권장합니다.** 확인된 향상은 Vulkan 전환 결과이며 2.7과 2.5의 정량 비교나 모든 게임의 성능 보장은 아닙니다. (게임에 따라 VL이나 Xtreme이 더 유리할 수 있으니 직접 비교해 보고 알맞은 코어를 선택해 주세요.)
- **해상도 변경 시 회전 유지:** 내부 해상도를 바꾸며 RetroArch가 Vulkan을 재초기화할 때 회전 보정 로더가 빠지는 문제를 수정했습니다. 세 코어에 공통 적용했습니다. 해당 Vulkan 실행에서는 GL 셰이더를 끄며 다른 에뮬레이터의 설정은 유지합니다.
- 기존 Wi-Fi·PPSSPP·Mali 메뉴·Ozone·PortMaster·진동·밝기·ZRAM·BennuGD 보완을 유지합니다.

## v1.0.5 — 2026-10-27

- **ZRAM service repaired:** the Services menu now starts/stops runtime-tested modules for this kernel, with the setting retained after reboot. ZRAM is **off by default**. It starts after the menu settles, uses lzo-rle, exposes logical swap of half the detected RAM and caps compressed RAM usage at a quarter of RAM (up to 512 MiB). RAM is allocated on demand. This helps memory-pressure situations; it does not guarantee higher FPS.
- **BennuGD core:** install the supplied ARM64 BennuGD libretro core and reconnect it automatically on each boot without save-overlay. The standard edition keeps its existing FBNeo/MAME cores.
- Existing PPSSPP 1.20.4/Vulkan, Mali menu, Wi-Fi, rotation, Ozone, PortMaster, rumble and brightness improvements are retained.

- **ZRAM 서비스 수정:** 서비스 메뉴에서 현재 커널에 맞춘 모듈을 켜고 끌 수 있으며 재부팅 후에도 선택이 유지됩니다. **기본값은 꺼짐**입니다. 메뉴 준비 후 lzo-rle로 시작하며 논리 스왑은 감지한 RAM의 절반, 실제 압축 RAM 사용 한도는 RAM의 1/4(최대 512MiB)입니다. 필요한 만큼만 RAM을 사용합니다. 메모리 부족 상황을 완화하는 기능이며 FPS 향상을 보장하지는 않습니다.
- **BennuGD 코어 적용:** 제공받은 ARM64 BennuGD libretro 코어를 넣고 재부팅 때 자동 연결되도록 했습니다. save-overlay는 필요 없습니다. 일반판의 FBNeo·MAME 코어는 기존 상태를 유지합니다.
- 기존 PPSSPP 1.20.4·Vulkan, Mali 메뉴, Wi-Fi, 회전, Ozone, PortMaster, 진동·밝기 보완은 유지합니다.

ZRAM block compression/readback, actual 32 MiB swap-out/in, service start/stop and reboot startup were verified on the maintainer device. BennuGD file identity and active core mapping were verified; gameplay and reboot testing of that supplied core were not repeated. Long memory-pressure stress, suspend/resume, all hardware batches and a fresh SD flash of these newly packaged v1.0.5 images have not been tested.

관리자 실기에서 ZRAM 블록 압축·되읽기, 실제 32MiB 스왑 저장·복원, 서비스 켜기·끄기와 재부팅 자동 시작을 확인했습니다. BennuGD는 파일 해시·실제 코어 연결을 확인했으며 해당 제공 코어의 게임 실행·재부팅 시험은 반복하지 않았습니다. 장시간 메모리 압박·절전 복귀·모든 생산분 및 새 v1.0.5 IMG를 SD에 다시 굽는 시험은 하지 않았습니다.

## v1.0.4 — 2026-10-27

- **PPSSPP 1.20.4:** update from 1.19.3 using the official source release and an ARM64 build. PSP games and Emulators → PPSSPP both open the updated Vulkan application.
- **Vulkan/display compatibility:** preserve the existing Mali driver, rotation, output opacity correction and menu return. Add three real Vulkan forwarding exports required by the newer availability check; synchronize both persistent launcher copies.
- **Mixed Korean/English text:** improve fallback font selection for the installed Noto and Nanum families, resolving missing square glyphs in mixed strings.
- Previous Wi-Fi, emulator rotation, Ozone, PortMaster, rumble and brightness shortcut/overlay improvements are retained. No temporary test controllers, captures or personal settings are included.

- **PPSSPP 1.20.4 업데이트:** 공식 소스로 ARM64 빌드해 1.19.3에서 올렸습니다. PSP 게임과 Emulators → PPSSPP 단독 실행 모두 새 Vulkan 버전으로 연결됩니다.
- **Vulkan·화면 호환 보완:** 기존 Mali 드라이버·회전·출력 투명도 보정·메뉴 복귀는 유지하고, 새 버전의 초기 검사에 필요한 Vulkan 함수 전달 3개를 추가했습니다. 부팅용 런처 두 사본도 동기화했습니다.
- **한영 혼합 글꼴 수정:** 설치된 Noto·나눔 글꼴을 올바르게 선택하도록 보완해 혼합 문장의 네모 글자를 해결했습니다.
- 기존 Wi-Fi·에뮬레이터 회전·Ozone·PortMaster·진동·밝기 단축키와 게이지 보정은 유지합니다. 임시 시험 제어 프로그램·캡처·개인 설정은 포함하지 않습니다.

The owner confirmed PPSSPP 1.20.4 still launches correctly after reboot. On-device captures confirmed correct menu orientation and mixed Korean/English text; normal exit and return to ES without reboot were verified. Earlier title-screen rendering was checked remotely. Every game, performance characteristic and hardware batch was not retested. The newly packaged v1.0.4 SD installation images have not been independently reflashed.

사용자가 재부팅 후에도 PPSSPP 1.20.4가 정상 실행되는 것을 확인했습니다. 실기 캡처에서 메뉴 방향·한영 혼합 글꼴을 확인했고, 정상 종료와 재부팅 없는 ES 복귀를 확인했습니다. 앞선 시험에서 게임 타이틀 출력도 원격으로 확인했습니다. 모든 게임의 성능·동작과 모든 생산분을 다시 시험한 것은 아닙니다. 새로 패키징한 v1.0.4 설치 IMG를 별도 SD에 다시 굽는 시험은 반복하지 않았습니다.

## v1.0.3 — 2026-10-26

- **Rumble:** use a 25 kHz motor PWM carrier and compensate low-strength effects. Crazy Taxi 1/2 with Flycast VL/Xtreme now provides noticeable small rumble with reduced high-pitched motor-related noise on the tested device.
- **Brightness shortcut:** hold SELECT, then use Volume +/−. Normal volume and HOME behavior are retained; held adjustment works.
- **Brightness overlay:** show a sun icon, percentage and bar above the menu or game, then hide it about 2.2 seconds after adjustment. It uses an unused display plane and runs only while visible; no idle overlay service is added.
- **Background cleanup:** disable Knulli usage-statistics reporting by default and stop the obsolete repeating boot-log copy on devices carrying it. Omit old diagnostic maps from the image.
- Existing Mali menu/PPSSPP Vulkan, Wi-Fi, screen rotation, Ozone and PortMaster functionality is retained.

- **진동 보정:** 모터 PWM을 25kHz로 바꾸고 작은 진동 신호의 세기를 보정했습니다. 시험 기기의 Flycast VL·Xtreme 크레이지택시 1·2에서 작은 진동이 느껴지고 거슬리던 고주파음이 줄어드는 것을 확인했습니다.
- **밝기 단축키:** SELECT를 먼저 누른 채 볼륨 +/−로 조절합니다. 길게 누름을 지원하며 일반 볼륨과 HOME 동작은 유지합니다.
- **밝기 게이지:** 메뉴와 게임 위에 해 아이콘·밝기 %·막대를 표시하고 조작 후 약 2.2초 뒤 숨깁니다. 비어 있는 출력 레이어를 사용하며 표시할 때만 실행하므로 대기 중 상주 서비스가 추가되지 않습니다.
- **백그라운드 정리:** 기본 통계 전송을 끄고, 예전 부팅 로그 반복 복사 작업이 남은 기기에서는 이를 중지합니다. 옛 진단 maps 파일은 이미지에서 제외했습니다.
- 기존 Mali 메뉴·PPSSPP Vulkan·Wi-Fi·화면 회전·Ozone·PortMaster 기능은 유지했습니다.

On-device tests confirmed rumble strength/noise and persistence after reboot, disabled statistics/repeating logging after reboot, and the brightness shortcut's direction, hold and normal-volume behavior. The owner confirmed the brightness overlay in ES and PPSSPP, automatic hiding, and game exit/menu return; remote inspection confirmed the overlay worker exits. The overlay uses a shared display path, but every emulator and hardware batch was not individually retested. The owner subsequently rebooted the device and confirmed all applied changes still work, including the brightness shortcut and overlay. These newly packaged installation images have not been independently reflashed.

실기에서 진동 세기·소음과 재부팅 후 유지, 재부팅 후 통계 전송·반복 로그 중지, 밝기 단축키의 방향·길게 누름·일반 볼륨 유지를 확인했습니다. 사용자가 ES와 PPSSPP의 밝기 게이지 표시·자동 숨김·게임 종료·메뉴 복귀를 확인했고, 표시 뒤 작업도 종료되는 것을 원격으로 확인했습니다. 공통 화면 경로를 사용하지만 모든 에뮬레이터·생산분을 각각 재시험한 것은 아닙니다. 이후 사용자가 기기를 재부팅하고 밝기 단축키·게이지를 포함한 수정 사항 전체가 정상 작동한다고 확인했습니다. 새로 패키징한 설치 IMG를 별도 SD에 다시 굽는 시험도 반복하지 않았습니다.

## Optional Korean CRC edition: v1.0.2-crc-ko — 2026-10-25

Separate download for the user-supplied FBNeo/MAME2003 Plus CRC-override cores and the reboot-persistent late loader. The clean base and all v1.0.2 fixes are unchanged. Normal v1.0.2 remains the default/latest release. [Korean guide](docs/CRC_KOREAN.ko.md).

한글 패치 아케이드용 CRC 무시 코어와 재부팅 자동 적용을 넣은 별도 다운로드입니다. 클린 기본 설정과 v1.0.2 수정은 같으며, 기본 최신 릴리스는 일반판 v1.0.2로 유지합니다. [한국어 안내](docs/CRC_KOREAN.ko.md).

| Checkpoint | Outcome |
| --- | --- |
| v87 baseline | Known bootable starting point; preserve it while testing Wi-Fi |
| v92–v114 experiments | Boot failures/freezes and incorrect Wi-Fi assumptions; not release recommendations |
| v115 | Personal stable checkpoint with working Wi-Fi, audio and RetroArch |
| v116, 2026-10-22 | Guarded display-client cleanup kernel repair; later Mali/Vulkan and presentation trials |
| 2026-10-23 integration | Correct scanout opacity/rotation, input, persistent settings; Mali menu and same-boot PSP round trips |
| v117 / v118 | Withdrawn because brightness inversion/polarity handling was incomplete |
| v119, 2026-10-24 | Cold boot and suspend/wake brightness correction confirmed; owner confirmed installed stable image |
| v119 Distribution Edition | Public defaults, personal BIOS archive removed, base BIOS retained, private data cleanup; PortMaster rotation added |
| v119 Distribution r2 / personal v120 r2 | ES Emulators/PPSSPP standalone entry routed through the existing Vulkan supervisor; no ROM required; owner confirmed output and menu return |
| Personal v120 | Private successor to personal v119, including BIOS/settings and PortMaster fix; not a public asset |

## First public release: v1.0.0 — 2026-10-24

Public v1.0.0 is the unchanged image previously labeled internally as
v119 Distribution Edition r2. The release title, tag, filenames and documentation
now use v1.0.0; the IMG and XZ bytes and their SHA256 values are unchanged.
The owner downloaded the published image, wrote it to an SD card and confirmed
installation and normal operation. Personal v120 remains unchanged and private.
Historical checkpoint names, runtime paths and packaging tools retain their
original identifiers so they still describe the actual work.

## v1.0.1 — 2026-10-25

- **Wi-Fi after reboot:** retain the existing AIC support and add the stock RTL8723DS path. The active BOOT and the normal/recovery BOOT used by Mali now contain the same Wi-Fi loader and startup code. Their integrity hashes are updated together, preventing the old AIC-only loader from returning on the next boot.
- **Wi-Fi startup:** wait for persistent SHARE settings and a driver-bound radio, then use the current settings. Correct the readiness marker to `/var/run/knulli.share.mounted`. Automatically started workers preserve already active Wi-Fi and existing ConnMan services.
- **Emulator orientation:** extend direction/size correction to standalone RetroArch, N64/Mupen64Plus, Saturn/YabaSanshiro and OpenBOR. The maintainer confirmed all emulator screen directions on hardware. Align the hardware N64/Saturn RetroArch launch paths with their GLES backends rather than the incompatible forced SDL2 route.
- **Other screens:** correct SDLPoP and OD-Commander, and apply scoped rotation to supported SDL/GLES PortMaster games. Compatibility with every individual port is not claimed.
- **PortMaster menus:** fix crashes caused by runtime metadata being a list rather than a single string, including runtime-manager display, port information, requirements and download-size calculation paths. Handle both `pylibs.zip` and already extracted installed sources; apply the correction when PortMaster is launched after installation.
- Keep the existing Mali menu, PPSSPP Vulkan, settings persistence, input, brightness and suspend/resume improvements.

On 2026-10-25, device-test feedback confirmed Wi-Fi still works after reboot with the test8 firmware. This public release promotes the normal test8 image **without changing its IMG bytes**. Emulator orientation was confirmed on hardware by the maintainer. PortMaster runtime-manager and port-management screens were also confirmed; every game, full update, forced update, runtime download and future PortMaster version was not exhaustively retested. See [verification scope](docs/TESTING.md).

- **재부팅 후 Wi-Fi 검색·연결 문제 수정:** 기존 AIC 지원을 유지하면서 순정 RTL8723DS 드라이버 시작 경로를 추가했습니다. 실제 부팅 파일과 Mali가 재부팅·복원에 사용하는 기준 사본을 함께 갱신하고 검증 해시도 맞춰, 다음 부팅에서 옛 AIC 전용 로더로 돌아가던 문제를 고쳤습니다.
- **Wi-Fi 시작 순서 보완:** SHARE 저장 공간과 무선 장치가 준비된 뒤 최신 설정으로 시작하며, 준비 마커 경로를 실제 생성 위치인 `/var/run/knulli.share.mounted`로 바로잡았습니다. 자동 시작 과정은 이미 사용 중인 Wi-Fi와 기존 ConnMan을 강제로 끄거나 재시작하지 않습니다.
- **에뮬레이터 화면 방향·크기 수정:** 스탠드얼론 RetroArch, N64/Mupen64Plus, Saturn/YabaSanshiro, OpenBOR까지 보정 범위를 확장했습니다. 에뮬레이터 화면 방향은 제작자가 실기로 모두 확인했습니다. N64·Saturn의 하드웨어 RetroArch 코어 실행도 강제 SDL2 대신 실제 GLES 백엔드와 맞추도록 보완했습니다.
- **도구·포트 게임 화면 보정:** SDLPoP와 OD-Commander 방향을 수정하고, 지원되는 SDL/GLES 경로의 PortMaster 게임에도 회전 보정을 연결했습니다. 모든 개별 포트 게임의 호환을 보장한다는 뜻은 아닙니다.
- **PortMaster 메뉴 종료 오류 수정:** 런타임 정보가 문자열 대신 목록으로 들어올 때 발생하던 오류를 수정했습니다. 런타임 매니저 표시, 포트 정보·요구 조건, 다운로드 용량 계산 경로를 보완하고, 압축된 `pylibs.zip`과 이미 풀린 설치 소스를 모두 처리합니다. Install PortMaster로 설치한 뒤 실행할 때 보완이 적용됩니다.
- 기존 Mali 메뉴·PPSSPP Vulkan·설정 저장·조작·밝기·절전 복귀 수정은 유지했습니다.

2026년 10월 25일 test8 펌웨어에서 **재부팅 후에도 Wi-Fi가 정상 연결됨을 실기 후기와 사진으로 확인**했습니다. 공개판은 test8 일반판의 **IMG 내용을 바꾸지 않고** 정식 버전으로 승격했습니다. 에뮬레이터 방향은 제작자가 실기로 모두 확인했고, PortMaster 런타임 매니저와 포트 관리 화면도 실기로 확인했습니다. 모든 게임, 전체·강제 업데이트, 런타임 다운로드 및 향후 모든 PortMaster 버전을 전부 재시험한 것은 아닙니다. [검증 범위](docs/TESTING.ko.md)

## v1.0.2 — 2026-10-25

- **RetroArch Ozone restored:** ordinary cores and standalone RetroArch now use GL/gl_sdl rather than forced SDL2 video, with Ozone selected for those sessions.
- **Rotation retained:** a small, scoped GLES3-context helper lets the existing full-frame adapter rotate both gameplay and Ozone. Existing hardware-core output settings and other applications are retained.
- **Menu startup fixed:** synchronize the menu guard's expected normal BOOT hash and its manifest with the Wi-Fi recovery BOOT. This fixes the stale check that could reject menu startup and trigger recovery. The safety check remains enabled.
- Retain the cumulative Wi-Fi reboot/startup fixes, emulator/SDLPoP/OD-Commander orientation, PortMaster runtime-list fixes, Mali menu and PPSSPP Vulkan.

The final runtime changes reached a healthy Mali menu after the home-device SSH update. Wi-Fi reconnected, and ordinary-core/standalone RetroArch checks completed. The owner then confirmed all final changes working on 2026-10-25. This newly packaged public IMG was not independently downloaded and reflashed; not every core, game, port or board variant was retested.

- **RetroArch Ozone 복원:** 일반 코어와 단독 RetroArch를 강제 SDL2 출력 대신 GL/gl_sdl로 실행하고 해당 실행에 Ozone을 지정했습니다.
- **회전 보정 유지:** 해당 RetroArch 실행에만 GLES3 컨텍스트 보조 파일을 연결해 게임과 Ozone 메뉴를 기존 전체 프레임 회전 경로로 표시합니다. 기존 하드웨어 코어 출력 설정과 다른 앱은 유지했습니다.
- **메뉴 시작 오류 수정:** 메뉴 guard의 normal BOOT 기대값과 해당 manifest를 Wi-Fi 복원 BOOT에 맞췄습니다. 옛 검사값 때문에 메뉴 시작을 거부하고 복구 부팅으로 넘어갈 수 있던 문제를 고쳤으며 안전 검사 자체는 유지했습니다.
- 재부팅 후 Wi-Fi·시작 순서, 에뮬레이터·SDLPoP·OD-Commander 방향, PortMaster 런타임 목록 처리, Mali 메뉴·PPSSPP Vulkan 등 누적 수정도 유지했습니다.

집 실기에 SSH로 최종 수정을 적용한 뒤 Mali 메뉴의 정상 시작과 재부팅 후 Wi-Fi 재연결을 확인했습니다. 일반 코어·단독 RetroArch 실행 검사 후, 2026년 10월 25일 사용자가 최종 수정 전체의 정상 작동을 확인했습니다. 새로 패키징한 공개 IMG를 게시 후 다시 내려받아 굽는 시험은 별도로 반복하지 않았으며, 모든 코어·게임·포트·보드 변형을 전부 재시험한 것은 아닙니다.
