# 공개 파일 범위

[English](PUBLIC_FILES.md) · [한국어](PUBLIC_FILES.ko.md)

## 공개 범위

공개 코드는 **배포판**에서 명시적인 허용 목록을 사용해 선별했습니다.
원래 개인 작업 디렉터리나 대화 전체를 업로드하지 않았습니다.

## 포함한 항목

- 확인된 결과와 실패한 접근을 정리한 개발 이력.
- 현재 사용하는 시작·세션·불투명도·회전·입력·전원 보조 기능.
- 고정한 커밋의 정확한 상위 Mali 드라이버 소스와 원래 고지문.
- 복구한 커널 설정, 후보 커널 설정과 옵션, 소스 정리 패치,
  원본 확인 조건이 있는 어셈블리 수정 및 검증 요약.
- 과거 이미지 변환·PWM 도구. 공개되지 않은 이전 입력 이미지를 필요로 하는 경우
  과거 작업용 도구임을 명시했습니다.
- 개인정보를 정리한 배포판 기본 설정, PortMaster 설치 항목, 릴리스 구성 명세,
  구성 파일 해시, 최종 이미지·체크섬 및 압축 배포 파일.
- 빌드·설치·복구·검증 범위·소스와 출처에 관한 문서.

## 제외한 항목

- 개인용 이미지, 개인 BIOS 압축 파일 및 개인 캡처.
- 저장된 개인 Wi-Fi SSID·비밀번호와 이를 포함하는 복구 사본.
- GitHub 인증 정보, 브라우저 세션 자료, 인증 화면 캡처,
  known-hosts 파일 및 SSH 개인 키·호스트 키.
- 원본 사용자 대화, 비공개 네트워크 로그, 기기 식별자, 쿠키, 사용 기록,
  Bluetooth 페어링 기록, 게임 화면 캡처, 진단 메모리 덤프 및 게임 ROM.
- 컴파일러 설치 파일, Git 데이터베이스와 드라이버 작업 폴더의 추적되지 않는 빌드 산출물.

원본 이미지의 기본 루트 파일시스템과 그 안의 원래 BIOS는 의도적으로 그대로 유지했습니다.
별도로 추가한 개인 BIOS 압축 파일을 제외한 것과는 구분됩니다. 공개 이미지 제작 시
FAT 여유 공간 3,289,493,504바이트를 0으로 채우고, 파일 끝 여유 영역 122개와 삭제된
항목 26개를 정리했습니다. 파일 이름만 지우는 방식으로 끝내지 않았습니다.

다운로드할 IMG는 Git 소스 이력 대신 GitHub **Releases**에 둡니다.
소스 저장소는 펌웨어 전체를 내려받지 않고도 살펴보고 복제할 수 있는 크기로 유지합니다.

## v1.0.1 추가·갱신 파일

- overlay/etc/init.d/S06modprobe·S08connman: 실제 부팅 시작 코드.
- overlay/usr/bin/emulatorlauncher: 렌더러에 맞춘 실행 경로.
- overlay/boot/ACTIONPI_FIXES/: 공통 앱·PortMaster 런타임·OD-Commander·Wi-Fi helper 최신본.
- overlay/boot/PPSSPP_VULKAN/: 활성 manager/autostart의 갱신된 해시 연결.
- src/app_sdl_rotation.c·app_gl_rotation.c·od_commander_rotation.c: 보정 소스. 컴파일된 사용자 공간 라이브러리를 Git에 넣지는 않습니다.
- tools/ActionPi-WiFi-Diagnostic.sh·wifi-diagnostic.py: 이번 공개판에서도 쓸 수 있는 읽기 전용 진단.
- release/distribution-v1.0.1.manifest.json과 현재 구성/소스 목록·자산 체크섬.

v1.0.1 공개 당시 CRC 코어판은 제외했습니다. 게임 ROM·네트워크 정보가 보이는 사진·이전 개인용 안정판은 공개하지 않습니다.

## v1.0.2 추가·갱신

- src/retroarch_gles3_context.c 및 tools/build-runtime.sh의 ARM64 빌드 명령.
- overlay/boot/ACTIONPI_FIXES/actionpi_app_launcher.py와 MALI_MENU_TRIAL/mali_menu_trial.py.
- release/distribution-v1.0.2.manifest.json, FIELD_VALIDATION-v1.0.2.json 및 최신 이미지/자산/소스 해시.
- 일반판에는 CRC 코어를 넣지 않습니다. 이전 개인 BIOS·설정은 공개하지 않습니다.

## 한국 사용자용 CRC 별도판

일반판과 분리된 릴리스에 CRC 적용 IMG를 제공합니다. config/crc-ko/는 실제 자동 적용 소스, release/crc-ko/는 전용 구성/체크섬입니다. [상세 안내](CRC_KOREAN.ko.md).

## v1.0.3 추가 파일

config/userdata/system/rumble-fix, background-quiet, brightness-osd와 config/defaults/multimedia_keys.conf, 일반·CRC custom.sh, tools/package-v1.0.3.py 및 FAT 도구를 공개합니다. source inventory와 release manifest에 해시를 기록합니다. 라이브 기기의 개인 설정·로그·SSID·비밀번호는 복사하지 않았습니다.

## v1.0.4

build/ppsspp-1.20.4、LICENSES/ppsspp-1.20.4、tools/package-v1.0.4.py、갱신된 런처·Vulkan 전달 소스 및 release manifest를 공개합니다. 원격 실기의 개인 설정·스크린샷·진단 로그는 포함하지 않습니다.

## v1.0.5

kernel/zram·LICENSES/zram·overlay/boot/ACTIONPI_ZRAM·일반/CRC 코어 로더 소스·config/bennugd/SOURCE.json·패키징 스크립트·v1.0.5 명세를 추가했습니다. 바이너리는 IMG에, 전체 소스는 릴리스 자산에 포함하며 개인 백업은 공개하지 않습니다.

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
