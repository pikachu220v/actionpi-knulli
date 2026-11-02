# 소스·라이선스·출처

[English](SOURCES_AND_LICENSES.md) · [한국어](SOURCES_AND_LICENSES.ko.md)

## 소스·라이선스·출처

이 펌웨어는 서로 다른 라이선스를 적용받는 구성 요소들의 모음입니다. 새로 작성한
연결 코드의 저장소 라이선스가 Linux, Arm, SDL, 에뮬레이터, 펌웨어나 BIOS의 조건을
대신하지 않습니다. 포함한 외부 소스의 기존 고지문은 보존했습니다.

| 구성 요소 | 기록한 소스·출처 | 확인 상태 |
| --- | --- | --- |
| 직접 작성한 연결 코드 | `overlay/`, `src/`, `tools/` | 해당 범위를 명시한 MIT 고지 적용. 커널 파생 작업은 GPL 조건 유지 |
| Mali 커널 드라이버 | Radxa allwinner-bsp 커밋 `2045a3ca2a01f088c0314dc924bda59d154e363e`, `modules/gpu/mali-valhall/driver` | 추적되는 상위 소스를 저장소에 포함. license.txt와 파일별 고지 보존. 후보 빌드 입력 기록 |
| 제조사 Linux 5.15.147 | 복구 설정, 바이너리 식별 정보, 보호 조건을 둔 수정 소스 포함 | 정확한 원본 제조사 트리와 빌드 출처는 미확인 |
| 공개 커널 후보 | Orange Pi 커밋 `5b956b750422abd5e9e9c5523540d2aaf41a7939` | 헤더·구조체 배치·소스 비교용. 제조사 바이너리의 정확한 대응 소스라고 주장하지 않음 |
| Knulli 통합 | `knulli-main`의 [Action Pi 보드 설정](https://github.com/knulli-cfw/knulli-linux/tree/knulli-main/board/allwinner/a527/helegany-action-pi), A527 이력 `5a7cb1e8e4dd` | 보드 구성 기반. 기존 이미지 전체의 정확한 소스 대응은 확립되지 않음 |
| SDL2 | [release-2.32.8](https://github.com/libsdl-org/SDL/tree/release-2.32.8) | 대상 SDL 2.32.8 확인. 새 보정 기능은 별도 소스 파일로 제공 |
| Flycast VL 참조 | [libretro/flycast 커밋 4a913e0](https://github.com/libretro/flycast/tree/4a913e063c95d1fae98afc64645831de0bcad57e) | 구형 시그널·JIT 조사에 사용한 소스 참조 |
| PPSSPP/Flycast/RetroArch/ES | 기존 Knulli 프로그램. 이 저장소의 수정 소스가 실행·출력 동작을 감쌈 | 기존 바이너리 각각의 정확한 소스·버전 대응을 모두 확보했다고 주장하지 않음 |
| Mali 사용자 공간 라이브러리 | 기존 제조사 구성. GLES 렌더러에서 r32p0 관찰 | 제조사 독점 바이너리. 커널 드라이버 GPL이 libmali까지 허가하는 것은 아님 |
| AIC8800DC 모듈·펌웨어 | 정상 작동하는 순정 펌웨어의 파일 재사용 | 수정 작업에서 바이너리 출처를 기록했으나, 정확한 대응 모듈 소스·재배포 조건은 완전히 해결되지 않음 |
| 기본 BIOS | 기존 기본 루트 파일시스템의 BIOS를 그대로 유지 | 연결 코드 라이선스 적용 대상이 아님. BIOS가 전혀 없는 배포판은 아님 |
| 추가 개인 BIOS 압축 파일 | 제외 | 공개 배포 파일이 아님 |

## 소스 구분이 필요한 이유

[GNU GPLv2 FAQ](https://www.gnu.org/licenses/old-licenses/gpl-2.0-faq.html)는 GPL
바이너리를 배포할 때의 소스 제공 의무를 설명합니다. 일반적인 상위 프로젝트 주소나
버전 숫자가 비슷한 커널만으로 특정 제조사 바이너리에 사용된 소스라고 할 수는 없습니다.
따라서 공개 후보를 올렸다는 이유만으로 미해결 제조사 소스 문제가 해결되었다고
주장하지 않습니다.

기존 배포판 전체의 소스·출처 목록에는 추가 조사가 필요합니다. 특히 원본 커널 변경분,
순정 Wi-Fi 소스, 제조사 사용자 공간과 유지한 BIOS의 이용 조건을 확인해야 이미지
전체의 완전한 소스 제공이나 재배포 조건 준수를 주장할 수 있습니다. 이 문서는
확인한 근거와 남은 공백을 기록하며, 그 주장을 인증하는 문서가 아닙니다.

## 주요 상위 프로젝트와 원출처

- [Knulli](https://github.com/knulli-cfw/knulli-linux)
- [고정한 Mali 소스](https://github.com/radxa/allwinner-bsp/tree/2045a3ca2a01f088c0314dc924bda59d154e363e/modules/gpu/mali-valhall/driver)
- [고정한 Orange Pi 후보](https://github.com/orangepi-xunlong/linux-orangepi/tree/5b956b750422abd5e9e9c5523540d2aaf41a7939)
- [Arm GNU 13.3.Rel1](https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads)
- [SDL evdev 시그널 처리 경로](https://github.com/libsdl-org/SDL/blob/release-2.32.8/src/core/linux/SDL_evdev_kbd.c)
- [Ultramarine 핸드헬드 제조사 그래픽 구성 작업](https://github.com/Ultramarine-Linux/ultramarine-handheld)

준비 과정에서 기록한 빌드 툴체인 압축 파일의 SHA256:
`322f0b4482fc0d9fa0bb468134841f08d8c554c54ff5aa29a13a7a24bf7e1eb5`.

## v1.0.1 Wi-Fi 출처

AIC 바이너리는 기존에 기록한 순정펌 이식본을 유지했습니다. 8723ds도 5.15.147 대상에서 검토했던 순정 바이너리이며 SDIO 024c:d723 지원 별칭을 포함합니다. 이번 배포는 기존 모듈을 재부팅 후에도 유지되는 부팅 사본에 연결한 것으로, 제조사 소스 전체를 작성하거나 재빌드했다고 주장하지 않습니다. 바이너리 해시는 release/BOOT_COMPONENTS.json에 기록했고 위에 명시한 원본 제조사 커널·소스 출처의 미확인 범위는 그대로입니다.

## v1.0.2 보조 파일

retroarch_gles3_context.c는 이번 적용을 위해 작성한 MIT 보조 소스입니다. SDL의 컨텍스트 주 버전 요청만 해당 프로세스에서 조정하며 SDL/RetroArch 자체를 교체하지 않습니다. 기존 소스·라이선스 미확정 사항은 동일합니다.

## 한국 사용자용 CRC 별도판

FBNeo·MAME2003 Plus는 사용자가 제공한 수정 바이너리이며 IMG를 별도 릴리스로 제공합니다. 정확히 대응하는 소스 버전·CRC 수정 패치는 제공받지 못했습니다. 상위 [FBNeo](https://github.com/finalburnneo/FBNeo)·[MAME2003 Plus](https://github.com/libretro/mame2003-plus-libretro) 링크는 참고 자료입니다. 자동 적용 소스와 해시는 config/crc-ko/ 및 release/crc-ko/에 공개합니다. [한국어 안내](CRC_KOREAN.ko.md). 각 코어의 조건은 일반 MIT 적용 범위와 별개입니다.

CRC 무시 코어 자료 출처: **[dsno님 블로그](https://dsno.tistory.com/m/)**. 사용자가 이 자료를 사용했다고 확인했습니다.

## v1.0.3 자체 보조 코드

config/userdata의 진동·로그 정리·밝기 OSD와 tools/package-v1.0.3.py는 이 프로젝트의 자체 Python·shell 보조 코드이며 기존 원본 glue의 MIT 범위에 포함합니다. 상속한 펌웨어·커널·CRC 코어의 라이선스나 불완전한 대응 소스 상태는 바뀌지 않습니다.

## PPSSPP 1.20.4

PPSSPP는 GPL-2.0-or-later이며 공식 v1.20.4 전체 소스와 그 안의 FFmpeg 소스를 릴리스에 동봉합니다. build/ppsspp-1.20.4/SOURCE.json에 원본 체크섬을 기록하고 글꼴 패치·빌드 스크립트·전달 라이브러리 소스를 공개합니다. LICENSES/ppsspp-1.20.4의 라이선스도 참고하세요. 기존 제조사 커널·바이너리 및 CRC 코어의 대응 소스 제한은 앞서 명시한 상태에서 바뀌지 않습니다.

## v1.0.5

재빌드한 ZRAM·zsmalloc·LZO 모듈은 고정 Orange Pi Linux 트리에서 왔습니다. 전체 원본 소스 압축파일과 실제 외부 모듈 소스·설정·패치·빌드 절차·Linux 고유 라이선스를 kernel/zram 및 LICENSES/zram에 공개합니다. 이번 재빌드 모듈의 소스와 아직 확인되지 않은 제조사 원래 커널 소스는 구분합니다. BennuGD는 config/bennugd/SOURCE.json에 해시를 기록한 제공 바이너리이며 정확한 소스 리비전·빌드 절차는 제공받지 못했습니다. 상위 링크를 정확한 대응 소스로 주장하지 않으며 프로젝트 MIT 연결 코드 라이선스로 이 코어를 재허가하지 않습니다. dsno님 출처는 별도 CRC판의 아케이드 코어에만 해당합니다.

BennuGD 참고 프로젝트: [BennuGD_libretro](https://github.com/diekleinekuh/BennuGD_libretro). 이 링크는 제공 바이너리의 정확한 대응 소스를 확인했다는 의미가 아닙니다.

## v1.0.6 — 2026-10-27

Vulkan 세 코어의 고정 소스·패치·빌드 방법은 src/flycast-vulkan에 공개하며 전체 소스 압축파일 묶음은 일반판 릴리스의 flycast-v1.0.6-sources.tar에 있습니다. config/flycast-vulkan/SOURCES.json에 출처·체크섬을 기록했습니다. 해상도 변경 보정은 전용 로더의 SONAME/NODELETE로 유지합니다. tools/package-v1.0.6.py는 클린 v1.0.5 이미지와 검증된 payload만 입력으로 사용합니다. 새 이미지의 커널·기존 사용자 설정·CRC 코어는 보존합니다.

## v1.0.7

MALI_MENU_TRIAL/mali_session.py는 게임 종료 후 재진입 때만 actionpi_es_menu_return.py를 통해 StartupOnGameList를 임시 적용합니다. LastSystem은 ES의 정상 종료 저장을 이용합니다. 원래 옵션만 작은 복구 기록에 보관하며 ES 종료/다음 시작에 복원합니다. 게임 커서·하위 폴더 복원은 구현하지 않았습니다. tools/package-v1.0.7.py는 v1.0.6 클린 이미지에서 BOOT Python 파일 두 개와 버전 명세만 변경하며 settings.tar.gz·코어·커널은 바꾸지 않습니다. 런타임 복구 기록·개인 설정·시험 캡처는 배포 입력이 아닙니다.

## v1.0.8

야바산시로 1.20.51 GLES는 BOOT의 ACTIONPI_FIXES/saturn에 저장하고 actionpi_app_launcher.py로 실행합니다. 쓰기 가능한 HOME은 /userdata/system/configs/yabasanshiro-1.20.51입니다. 실행기는 ES에서 누락된 입력 매핑을 생성하고 실제 L3 매핑과 기존 회전 보정기를 사용합니다. 내장 ARM64 JIT가 이전 1.9.0 보조 모듈을 대체하며 볼륨 후크는 사용자 볼륨을 유지합니다. 읽기 전용 기본 rootfs 안의 기존 바이너리는 남지만 평소 실행 경로에서는 사용하지 않습니다. tools/package-v1.0.8.py는 클린 v1.0.7에 BOOT 파일 5개와 버전 정보만 추가·수정하며 설정 아카이브·기본 rootfs·Mali·Wi-Fi·PPSSPP·Flycast·ZRAM은 바이트 단위로 유지합니다. 전체 수정 소스·libchdr·라이선스·빌드 자료는 saturn-standalone-1.20.51-v1.0.8-sources.tar.xz로 첨부하며 의존성과 빌드 조건은 src/saturn-standalone에 기록합니다. 상속된 모든 펌웨어 바이너리의 정확한 소스 출처까지 확인됐다는 뜻은 아닙니다.

## v1.0.8 r2

v1.0.8 릴리스 번호를 유지한 r2 이미지에 두 입력 수정을 병합했습니다. player1.pad의 padmode를 따라 일반/3D 패드를 선택하고, 일반 모드에서는 저장된 방향·analogx/analogy 매핑을 함께 샘플링하여 디지털 방향을 합칩니다. 방향 입력만 병합기가 담당하므로 한 입력의 해제가 다른 입력을 취소하지 않습니다. L3·FPS·오디오·GLES 회전은 유지합니다. tools/package-v1.0.8-r2.py는 기존 v1.0.8에서 BOOT의 새턴 실행 파일과 payload.json만 바꾸며, 기본 rootfs·설정 아카이브·다른 에뮬레이터는 유지합니다. 이미지 파일명은 r2로 구분하고, 이전 태그는 이동하지 않습니다. 갱신 릴리스의 기술 문서 링크는 이번 소스 커밋으로 고정합니다. 전체 대응 소스는 saturn-standalone-1.20.51-v1.0.8-r2-sources.tar.xz입니다.

## v1.0.9

야바산시로 1.20.51 GLES는 BOOT의 ACTIONPI_FIXES/saturn에 저장하고 actionpi_app_launcher.py로 실행합니다. 쓰기 가능한 HOME은 /userdata/system/configs/yabasanshiro-1.20.51입니다. 실행기는 ES에서 누락된 입력 매핑을 생성하고 실제 L3 매핑과 기존 회전 보정기를 사용합니다. 내장 ARM64 JIT가 이전 1.9.0 보조 모듈을 대체하며 볼륨 후크는 사용자 볼륨을 유지합니다. 읽기 전용 기본 rootfs 안의 기존 바이너리는 남지만 평소 실행 경로에서는 사용하지 않습니다. tools/package-v1.0.9.py는 클린 v1.0.8에 BOOT 파일 5개와 버전 정보만 추가·수정하며 설정 아카이브·기본 rootfs·Mali·Wi-Fi·PPSSPP·Flycast·ZRAM은 바이트 단위로 유지합니다. 전체 수정 소스·libchdr·라이선스·빌드 자료는 saturn-standalone-1.20.51-v1.0.9-sources.tar.xz로 첨부하며 의존성과 빌드 조건은 src/saturn-standalone에 기록합니다. 상속된 모든 펌웨어 바이너리의 정확한 소스 출처까지 확인됐다는 뜻은 아닙니다.

최종 Flycast 모듈은 configgen 전 install_generator로 앱 설정을 보존하고 Popen 전 prepare로 Vulkan 실행 파일/기존 회전 로더를 선택합니다. 바이너리와 ENABLED는 깨끗한 settings.tar.gz에 추가하고, 개인 emu.cfg·VMU·저장·ROM·BIOS는 가져오지 않습니다. 런처 두 사본과 manifest 해시를 함께 갱신하며 GL 경로를 유지합니다. 이전 r2 새턴 및 기존 코어/다른 앱 파일은 보존합니다. 전체 소스·Zig 빌드 자료는 src/flycast-standalone-vulkan 및 flycast-standalone-v1.0.9-sources.tar.xz를 참조합니다. 최종 바이너리는 검증된 4eca8b... 바이트 그대로이며 test 버전 문자열을 바꾸려고 다시 빌드하지 않았습니다. 추가 quiet_start는 부팅 60초 진단만 차단하고 기존 로그 복사/통계 차단은 유지합니다.
