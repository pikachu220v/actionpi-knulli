# Action Pi Knulli v1.0.9

## English

Unofficial Knulli adaptation for the Helegaly Action Pi. Mali runs the menu and PPSSPP Vulkan in the same boot.

### What changed

- **Flycast standalone now defaults to Vulkan:** the regular standalone entry launches the Action Pi build based on official Flycast v2.7. Existing RetroArch standard/VL/Xtreme cores remain available.
- **User-reported performance:** in the games tried, the user reports performance on par with or better than the RetroArch cores. This is a hands-on assessment, not a controlled benchmark or a guarantee for every game.
- **Press L3 (click the left analog stick) to open Flycast settings.** Game and menu output use the full-frame rotation correction; HOME returns to ES.
- **Settings persist:** vibration-pack selection and other settings changed in Flycast survive exit and relaunch. Explicit ES settings take priority; the remaining app preferences and controller remaps are retained.
- **GL fallback path retained:** the launcher includes the original GL path when the Vulkan payload is unavailable or explicitly disabled; switching back to GL was not separately tested in this final revision. Test-only Ports entries are excluded.

### Installation

Download this release's .img.xz and SHA256SUMS, verify the checksum and flash the whole SD card. Extract XZ first if required by your flashing tool. Flashing erases the selected card.

**On first installation, a black screen after the boot image is normal. Allow about 5 minutes: SHARE expansion and settings installation may restart the device once or twice before the menu appears. Keep power on until setup finishes.**

Saturn standalone settings: **L3 (click the left analog stick)**.

Brightness: **hold SELECT + Volume +/−**. Exit PPSSPP: **hold SELECT+START for about one second**. Emulator exit with the top HOME key works in RetroArch and remains disabled in PPSSPP. No game ROMs are included. ZRAM recovery: create an empty `ACTIONPI_ZRAM/DISABLED` file on BOOT to skip its startup.

### Verification and technical documentation

The user confirmed Vulkan gameplay, menu orientation, L3, HOME return and final settings persistence. The final Vulkan default/settings revision has not separately been confirmed after reboot, and final distribution images have not yet been flashed to another SD card.

- [History](https://github.com/pikachu220v/actionpi-knulli/blob/v1.0.9/docs/HISTORY.md)
- [Architecture](https://github.com/pikachu220v/actionpi-knulli/blob/v1.0.9/docs/ARCHITECTURE.md)
- [Build and packaging](https://github.com/pikachu220v/actionpi-knulli/blob/v1.0.9/docs/BUILD.md)
- [Published files](https://github.com/pikachu220v/actionpi-knulli/blob/v1.0.9/docs/PUBLIC_FILES.md)
- [Sources and licenses](https://github.com/pikachu220v/actionpi-knulli/blob/v1.0.9/docs/SOURCES_AND_LICENSES.md)
- [Installation](https://github.com/pikachu220v/actionpi-knulli/blob/v1.0.9/docs/RELEASE.md)
- [Verification scope](https://github.com/pikachu220v/actionpi-knulli/blob/v1.0.9/docs/TESTING.md)

Board integration is based on [upstream Knulli's Action Pi board configuration](https://github.com/knulli-cfw/knulli-linux/tree/knulli-main/board/allwinner/a527/helegany-action-pi). This is an adaptation of an inherited image, not a complete from-source firmware build.

Raw IMG: 6,069,178,368 bytes. SHA256: cef5a6a24dc71286cbf77698a7e0b86bbe096244b714c7a1a50cc075b581202b.

Yaba Sanshiro application source and build notes: [src/saturn-standalone](https://github.com/pikachu220v/actionpi-knulli/tree/v1.0.9/src/saturn-standalone); the matching full source archive is attached to this release.

---

## 한국어

Helegaly Action Pi용 비공식 Knulli 수정 배포판입니다. 같은 부팅에서 Mali 메뉴와 PPSSPP Vulkan을 사용합니다.

### 수정 내역

- **Flycast 스탠드얼론 Vulkan 기본 적용:** 평소 스탠드얼론 항목에서 공식 Flycast v2.7 기반 액션파이용 Vulkan 실행 파일을 사용합니다. 기존 RetroArch 일반·VL·Xtreme 코어도 유지합니다.
- **사용자 실기 체감 기준, RetroArch 코어와 동등하거나 더 나은 성능**을 확인했습니다. 정식 동일 조건 벤치마크 결과나 모든 게임의 성능 보장을 뜻하지 않습니다.
- **L3(왼쪽 아날로그 스틱 클릭)로 Flycast 설정 메뉴에 들어갑니다.** 게임과 자체 메뉴의 전체 화면 회전을 보정하고 HOME으로 ES에 복귀합니다.
- **설정 유지 보완:** Flycast 안에서 고친 진동팩과 각종 설정을 종료·재실행 후에도 유지합니다. ES에서 명시한 옵션은 우선 적용하고, 나머지 앱 설정과 패드 재매핑은 보존합니다.
- **GL 복구 경로 유지:** Vulkan 파일이 없거나 비활성화한 경우의 기존 GL 실행 분기를 유지합니다. 최종 수정판에서 GL로 되돌리는 전환 자체를 별도로 실기 재시험하지는 않았습니다. Ports 시험 항목은 포함하지 않습니다.

### 설치

이 릴리스의 .img.xz와 SHA256SUMS를 내려받아 체크섬을 확인하고 SD 전체에 굽습니다. 기록 프로그램이 XZ를 지원하지 않으면 먼저 압축을 풀어 주세요. 기록 대상 SD의 기존 내용은 지워집니다.

**첫 설치는 부팅 이미지 뒤 검정화면이 보여도 정상입니다. 약 5분 기다리면 SHARE 자동 확장·설정 설치 중 한두 번 재부팅한 뒤 메뉴가 표시됩니다. 전원을 유지한 채 완료될 때까지 기다려 주세요.**

새턴 스탠드얼론 설정 메뉴: **L3(왼쪽 아날로그 스틱 클릭)**.

밝기는 **SELECT를 누른 채 볼륨 +/−**, PPSSPP 종료는 **SELECT+START 약 1초**입니다. 상단의 HOME키를 이용한 에뮬레이터 종료는 RetroArch에서 작동하며 PPSSPP에서는 비활성화되어 있습니다. 게임 ROM은 포함하지 않습니다. ZRAM 복구는 BOOT의 `ACTIONPI_ZRAM` 안에 이름이 `DISABLED`인 빈 파일을 만들면 됩니다.

### 검증 범위와 기술 문서

사용자가 Vulkan 게임 실행·메뉴 방향·L3·HOME 복귀·최종 설정 지속성을 확인했습니다. 최종 Vulkan 기본/설정 보존 단계의 별도 재부팅 및 최종 배포 이미지의 새 SD 설치 확인은 아직 하지 않았습니다.

- [작업 이력](https://github.com/pikachu220v/actionpi-knulli/blob/v1.0.9/docs/HISTORY.ko.md)
- [작동 구조](https://github.com/pikachu220v/actionpi-knulli/blob/v1.0.9/docs/ARCHITECTURE.ko.md)
- [빌드·이미지 제작](https://github.com/pikachu220v/actionpi-knulli/blob/v1.0.9/docs/BUILD.ko.md)
- [공개 파일](https://github.com/pikachu220v/actionpi-knulli/blob/v1.0.9/docs/PUBLIC_FILES.ko.md)
- [출처·라이선스](https://github.com/pikachu220v/actionpi-knulli/blob/v1.0.9/docs/SOURCES_AND_LICENSES.ko.md)
- [설치 안내](https://github.com/pikachu220v/actionpi-knulli/blob/v1.0.9/docs/RELEASE.ko.md)
- [검증 범위](https://github.com/pikachu220v/actionpi-knulli/blob/v1.0.9/docs/TESTING.ko.md)

보드 구성은 상위 Knulli의 [Action Pi 보드 설정](https://github.com/knulli-cfw/knulli-linux/tree/knulli-main/board/allwinner/a527/helegany-action-pi)을 기반으로 했습니다. 기존 이미지를 수정한 배포판이며 모든 구성요소를 소스에서 완전히 재빌드한 펌웨어는 아닙니다.

압축 해제 IMG: 6,069,178,368바이트. SHA256: cef5a6a24dc71286cbf77698a7e0b86bbe096244b714c7a1a50cc075b581202b.

야바산시로 소스·빌드 자료: [src/saturn-standalone](https://github.com/pikachu220v/actionpi-knulli/tree/v1.0.9/src/saturn-standalone). 정확히 대응하는 전체 수정 소스 묶음을 릴리스에 첨부했습니다.

Flycast standalone full source and build notes: [src/flycast-standalone-vulkan](https://github.com/pikachu220v/actionpi-knulli/tree/v1.0.9/src/flycast-standalone-vulkan). The corresponding full source asset is attached to this release.
