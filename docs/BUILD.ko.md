# 빌드와 재현 가능 범위

[English](BUILD.md) · [한국어](BUILD.ko.md)

## 이 저장소에서 다시 빌드할 수 있는 범위

현재 실행 스크립트, 회전 보정 C 소스, 고정한 Mali 드라이버 소스, 복구한 커널 설정,
화면 수정용 어셈블리·링커 스크립트와 과거 이미지 변환 도구를 포함합니다.
완성 바이너리 이미지만 배포하는 대신 수정 내용을 공개하기 위한 구성입니다.

그러나 원본 제조사 커널이나 기존 루트 파일시스템의 모든 프로그램에 대해 완전하고
검증된 대응 소스 트리를 제공하는 것은 **아닙니다**. 이 저장소만으로 펌웨어 전체를
처음부터 빌드할 수는 없습니다. 과거 패키징 도구는 공개 배포 파일에 없는 로컬 이전
이미지를 참조합니다. 작업 기록으로 포함한 것이며, 공개 환경에서 명령 하나로 전체
이미지를 만드는 도구라고 안내하지 않습니다.

## 사용자 공간 보조 기능 빌드

Linux 또는 WSL과 AArch64 Linux 컴파일러를 사용합니다. 작업 때 기록한 도구는
Arm GNU 13.3.Rel1 / GCC 13.3.1이며 대상은 `aarch64-none-linux-gnu`입니다.

```sh
export CROSS_COMPILE=aarch64-none-linux-gnu-
SDL2_LIB=/path/to/target/libSDL2-2.0.so.0.3200.8 sh tools/build-runtime.sh
```

SDL2 입력은 PC의 x86_64 라이브러리가 아니라 대상 기기의 ARM64 라이브러리여야 합니다.
배포 이미지에서 변경하지 않은 `boot/knulli` 루트 파일시스템을 mtools와 unsquashfs로
열어 추출할 수 있습니다. PortMaster 래퍼는 원래 라이브러리의 SONAME에 연결하고,
별도로 감싸지 않은 함수는 원래 라이브러리로 전달합니다. 스크립트는 `build/` 아래에
보조 기능을 만들며 장치에 기록하거나 IMG를 변경하지 않습니다. 컴파일러 버전이 바뀌면
결과 파일의 해시도 달라질 수 있습니다.

커널 보조 코드는 별도로 어셈블·링크할 수 있습니다.

```sh
${CROSS_COMPILE}as -march=armv8.1-a src/display_repair.S -o build/repair.o
${CROSS_COMPILE}ld -T src/display_repair.ld build/repair.o -o build/repair.elf
```

링커 스크립트는 원래 함수가 차지할 수 있는 크기를 강제합니다.
`tools/historical/make_display_test_image.py`에는 원본 바이트·해시 확인 조건,
분기 검증, Unicorn 모의 실행 사례와 Android 체크섬 재생성 과정이 있습니다.
공개 후보 소스에 대한 수정은 `kernel/display-cleanup/`에 있습니다. 해당 플랫폼
소스에는 실제로 동작하는 정리 함수 구현도 있어야 합니다. 두 방식은 같은 수정 의도를
서로 다르게 표현한 것이며, 서로 교환해 넣는 모듈 두 개가 아닙니다.

## Mali 모듈 빌드 입력

고정한 드라이버 소스는 `third_party/mali-valhall/`에 포함되어 있습니다.

```sh
make -C third_party/mali-valhall/drivers/gpu/arm/midgard \
  KDIR=/path/to/reviewed-kernel-build ARCH=arm64 \
  CROSS_COMPILE=aarch64-none-linux-gnu- \
  CONFIG_MALI_MIDGARD=m CONFIG_MALI_PLATFORM_NAME=sunxi \
  CONFIG_MALI_CSF_SUPPORT=n CONFIG_MALI_GATOR_SUPPORT=y CONFIG_MALI_DEVFREQ=y
```

기록한 후보 옵션 전체와 컴파일 명령은 `kernel/`에 있습니다. 이 자료는 당시 실험
구성을 식별하는 것이며, 새로 준비한 임의의 커널 헤더가 기기의 제조사 커널과 일치한다고
보장하지는 않습니다. `Module.symvers`, 생성된 헤더, 공개 심볼 이름, 구조체 배치와
실제 동작이 맞아야 합니다. 강제 로드나 가짜 symvers 파일로 이 검증을 대신하지 마세요.

공개 커널 후보는 다음 커밋입니다.
`orangepi-xunlong/linux-orangepi@5b956b750422abd5e9e9c5523540d2aaf41a7939`.
이것은 기록된 모듈 재빌드에 사용한 헤더·소스 후보이며, 원본 커널의 정확한 소스라고
입증된 것은 아닙니다. 복구 설정과 정규화한 후보 설정은 제조사 심볼에서 차이가 있으므로
`candidate-config-delta.json`도 함께 보존해야 합니다.

## 이미지 패키징 작업 기록

`tools/historical/build_distribution_v119.py`는 실제 공개 배포판 변환 과정을 기록합니다.
설정과 복구 사본에서 개인정보를 정리하고, 추가 BIOS 압축 파일만 제거하고,
PortMaster 훅을 포함하며, 기본 루트 파일시스템을 유지합니다. 이어서 FAT의 비어 있는
클러스터, 파일 끝 여유 공간과 삭제된 디렉터리 항목을 정리합니다. 변경 파일,
알려진 개인 인증 정보의 잔여물과 최종 이미지 체크섬도 확인합니다. 이전 커널·PWM
도구도 포함했습니다. 해시 확인 조건은 의도된 보호 장치이므로, 무관한 펌웨어를
통과시키기 위해 제거하면 안 됩니다.

공개 IMG는 최종 설치된 오버레이 구성을 조사할 때 사용할 수 있는 기준 산출물입니다.
`release/BOOT_COMPONENTS.json`에는 배포한 바이너리 보정 파일과 Mali 모듈의 정확한
해시가 연결되어 있습니다. 이러한 검증 범위는 소스에서 펌웨어 전체를 완전히 재현할 수
있다는 주장보다 제한적입니다.

## 공개 v1.0.1 패키징

공개 IMG는 내부 test8 일반판을 내용 변경 없이 승격한 파일이며 SHA256은 `b5d2193e0b88808c7457d8d714d422f8b927630e06bac432bf8067ea31377c42`입니다. 승격 과정에서 커널·GPU 모듈·BIOS 묶음·개인 CRC 코어를 추가하지 않았습니다. 영어·초기 Wi-Fi 꺼짐, 설정/복구 사본의 저장 네트워크 없음, 개인 코어·게임 ROM 제외와 기존 BIOS 정책을 다시 확인했습니다.

내부 test8에서는 test7 BOOT의 본문과 S06/S08을 유지하고 Mali 가드가 없는 일반 기준 사본을 만든 뒤 실제 manager.modified()로 활성 Mali 번들을 생성했습니다. 복구 매니페스트·BOOT_SHA·BASE_SHA를 함께 맞추고 시작 helper의 SHARE 마커 경로만 수정했습니다. 실제 restore/arm 함수를 임시 파일에서 세 차례 실행했으며 트랜잭션 복원과 /run·/var/run이 분리된 경우를 확인했습니다. 이 검사는 실제 블록 장치나 GPU에 적용한 시험이 아닙니다.

추가된 보정 소스는 src/app_sdl_rotation.c, src/app_gl_rotation.c, src/od_commander_rotation.c이며 실행 스크립트와 유효 S06/S08은 overlay/에 공개했습니다. 두 BOOT와 내장 8723ds 모듈을 포함한 해시는 release/BOOT_COMPONENTS.json에 있습니다. 업로드 전에 XZ 무결성과 압축 전후 체크섬을 확인하며, 펌웨어 전체를 새로 소스 빌드했다는 뜻은 아닙니다.

## v1.0.2 제작

v1.0.1에 Ozone 런처·GLES3 보조 라이브러리·ACTIONPI_FIXES manifest를 반영하고, 메뉴 guard의 BOOT 상수와 MALI_MENU_TRIAL manifest를 normal BOOT에 맞췄습니다. 기존 IMG와 개인 데이터를 바꾸지 않는 사본에서 작업했습니다. 올바른 normal BOOT의 검사 통과, armed BOOT의 거부와 옛 검사값 불일치 재현을 실제 guard 함수에 파일 입출력 대역을 연결해 확인했습니다. 최종 파일 재읽기 및 변경 영역 외 바이트 비교·SHA256을 수행했습니다. 기존 클린 기본값 자료는 변경하지 않았습니다. 새 보조 파일은 tools/build-runtime.sh에 포함됩니다. XZ 무결성·압축/해제 해시는 한 번의 스트리밍 검사로 기록합니다.

## v1.0.3 패키징

config/userdata/system/에 진동·일회성 정리·밝기 OSD 소스를 공개했습니다. config/defaults/multimedia_keys.conf와 양 판의 custom.sh를 초기 설정 압축파일에 병합하고 telemetry=0을 SHARE·부팅 설정에 함께 넣습니다. STABLE_V119는 내부 설치 경로로 유지하고 payload의 설정 압축파일 해시를 갱신합니다. 기존 Wi-Fi·Mali·부팅 사본·회전 코드는 바꾸지 않습니다.

Python 3와 mtools(mcopy), Linux 또는 mtools가 설치된 Ubuntu WSL이 필요합니다. 공개 v1.0.2 일반·CRC 이미지를 압축 해제해 이름을 유지한 뒤 ACTIONPI_IMAGE_DIR 환경 변수에 그 폴더를 지정하고 python3 tools/package-v1.0.3.py를 실행합니다. 두 입력 이미지의 고정 SHA256을 검사하고 새 파일만 생성합니다. 원본 tar 구성·코어 해시와 변경 영역 밖의 전체 바이트를 검사합니다. gzip 메타데이터 시각 때문에 재패키징 결과의 최종 SHA가 항상 동일하다고 주장하지 않습니다. XZ 제작 후 tools/verify-release.py로 압축 무결성과 해제 IMG 해시를 한 번의 스트리밍 읽기로 확인합니다.

## v1.0.4

CRC판은 설정 압축파일 교체 후 FAT에서 비었다고 표시된 옛 파일 클러스터만 0으로 정리합니다. 사용 중인 파일을 변경하지 않고 미할당 영역의 잔여 데이터를 제거해 XZ를 릴리스 용량 제한 안으로 줄입니다. 패키징 도구는 이 정리 뒤 최종 IMG 체크섬을 계산합니다.

build/ppsspp-1.20.4에 실제 빌드 절차·도구 체인·FFmpeg 빌드 스크립트·글꼴 패치를 공개했습니다. 같은 릴리스의 ppsspp-1.20.4.tar.xz는 빌드에 사용한 공식 전체 소스입니다. ARM GNU 13.3.1, CMake 3.31 및 기존 이미지에서 추출한 target-sdk 런타임과 대응 개발 헤더를 사용합니다. ACTIONPI_WORKDIR·ACTIONPI_BUILD_DIR·CMAKE_BIN으로 경로를 지정하고 build.sh, font-fix.sh 순서로 실행합니다. 전달 라이브러리는 src/v116_vulkan_output_rotation.c를 aarch64-none-linux-gnu-gcc -shared -fPIC -O2 -Wall -Wextra -Werror -ldl로 빌드해 rotation/libvulkan.so와 libvulkan.so.1에 같은 파일로 둡니다. 기존 SDL 회전 보조 라이브러리도 함께 둡니다. 자세한 파일 배치는 build/ppsspp-1.20.4/README.md를 참고하세요.

ACTIONPI_IMAGE_DIR에 두 v1.0.3 IMG를, ACTIONPI_PPSSPP_BUNDLE에 빌드한 앱 묶음을 지정한 뒤 tools/package-v1.0.4.py를 실행합니다. 앱·assets·라이선스를 초기 설정 압축파일에 추가하고 /boot 런처 두 사본과 payload 해시를 갱신합니다. 기존 tar 항목·CRC 코어·그 밖의 이미지 영역 바이트가 보존되는지 검사합니다. XZ는 tools/verify-release.py로 한 번 해제하면서 무결성과 IMG 해시를 확인합니다.

## v1.0.5

kernel/zram에 실제 외부 모듈 소스·정규화/실기 추출 설정·소스 식별·빌드 스크립트·용량 API 패치를 공개했습니다. 일반판 릴리스에 SOURCE.json이 가리키는 고정 Orange Pi 전체 소스를 첨부하며 CRC판도 같은 소스를 사용합니다. 제조사 원본 커널의 정확한 대응 트리라는 주장은 아닙니다. tools/package-v1.0.5.py는 두 v1.0.4 IMG와 검증한 ZRAM .ko 묶음·제공 BennuGD 바이너리를 입력으로 사용합니다. 허용한 BOOT 파일과 코어/로더 항목만 추가하고 ZRAM 초기 꺼짐, 기존 tar 항목 및 수정 허용 영역 밖의 이미지 바이트 동일성을 확인합니다. 실기 개인 설정·백업·로그·접속 정보는 입력하지 않습니다.

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
