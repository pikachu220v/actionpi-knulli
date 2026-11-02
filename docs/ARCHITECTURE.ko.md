# 작동 구조와 연결 방식

[English](ARCHITECTURE.md) · [한국어](ARCHITECTURE.ko.md)

## 대상과 보호 조건

`/boot/boot/knulli.board`가 `helegany-action-pi`여야 하며, 커널은 원본 확인 조건을
통과하고 화면 정리 수정을 적용한 특정 5.15.147 바이너리를 사용합니다. 버전 문자열이
같다는 것만으로 호환성을 확인할 수는 없습니다. 이 문서는 임의의 A527/TSPS 기기에
해당 모듈을 설치하라는 안내가 아닙니다.

## 부팅 과정

1. 기존 파티션 초기화 기능이 새 카드의 SHARE를 확장하고 재부팅합니다.
2. SHARE가 마운트되면 S12가 `/boot/postshare.sh`를 호출합니다.
   `STABLE_V119/firstboot.py`는 설치 자료의 해시를 확인하고, 개인정보를 정리한 설정만
   풀어 넣은 뒤 완료 표시를 기록합니다. 이후 저장 내용을 동기화하고 재부팅합니다.
   개인 BIOS 압축 파일은 복원하지 않습니다.
3. `boot-custom.sh`가 Action Pi용 사용자 공간 수정을 준비합니다. Mali 시작 제어와
   부팅 인자가 Panfrost의 선점을 막고, 후보 Mali 모듈과 제조사 라이브러리를 사용합니다.
4. 부팅 후반의 제어 단계에서 실제 PWM 극성을 맞춥니다. 보드, 컨트롤러 레지스터 정보,
   실행 중인 장치 트리의 PWM 인자를 확인한 뒤 비트 8을 변경합니다.
5. 관리 프로그램이 제조사 EGL/GLES/GBM 로더 환경과 올바른 화면 방향·입력·오디오 설정으로
   ES를 실행합니다. 복구 및 시도 표시를 통해 시작 실패 시 다음 부팅에서 대체 경로로
   돌아갈 수 있도록 합니다.

## PSP 실행과 메뉴 복귀

실행 분배기는 PSP 요청을 `mali_session.py`로 전달합니다. 관리 프로그램은 ES의
Emulators/PPSSPP에서 보내는 UI 단독 실행 요청도 처리합니다. 이 경우 ROM 인자만 생략하며,
일반 게임 실행에는 경로 검증을 유지합니다.

관리 프로그램은 ES에 정상 종료를 요청하고 화면 자원이 닫힐 때까지 기다립니다.
이후 해당 세션에만 Vulkan/SDL 출력 보정과 불투명도 보정을 적용하여 PPSSPP를 실행합니다.
종료 시 보조 파일 디스크립터를 해제한 뒤 메뉴를 다시 띄웁니다. GPU는 계속 Mali가
담당하며, 일반 실행 경로에서는 GPU 드라이버를 해제하거나 다시 연결하지 않습니다.

자동 세션은 이전 `knulli.conf`를 현재 사용자 설정 위에 복원하지 않습니다.
PPSSPP 설정 디렉터리도 저장된 선택을 버리지 않도록 처리합니다. 과거 일회성 진단
관리 도구는 정상 실행 경로와 분리되어 있으며, 예전 실험 명령을 직접 실행할 필요가 없습니다.

## 출력 보정 구성

| 프로그램·경로 | 보정 방식 |
| --- | --- |
| ES | 자체 screenrotate 옵션과 메뉴에만 적용하는 감사·입력 보조 기능 |
| PPSSPP Vulkan | Vulkan 출력 변환, 이에 맞춘 SDL 논리 해상도, 세션 한정 불투명도 보정 |
| RetroArch SDL2 | 960×720 대상 텍스처를 시계 방향 90도로 회전해 720×960으로 출력 |
| RetroArch GL / Flycast 스탠드얼론 | GLES 전체 출력용 FBO 회전 |
| PortMaster/PySDL2 | 원래 SDL로 나머지 함수를 전달하는 전용 이름의 SDL DLL |

회전 라이브러리는 시스템 전체의 `/usr/lib/libSDL2`를 교체하지 않습니다.
PortMaster 보조 기능은 `ACTIONPI_MALI_SESSION=1`일 때 해당 프로그램의
`PYSDL2_DLL_PATH` 선택만 수정합니다. 설치나 업데이트로 실행 스크립트가 교체되면
실행 준비 단계에서 다시 적용합니다.

## 전원·밝기·오디오

절전 훅은 Wi-Fi 전원이 켜져 있었는지 기록하고, SDIO의 절전 방지 잠금을 해제하기 위해
Wi-Fi를 끕니다. 복귀 후에는 기억한 서비스에 다시 연결하도록 예약합니다. 원래 꺼져 있던
Wi-Fi를 단순히 절전에서 깨어났다는 이유로 켜지는 않습니다.

같은 복귀 경로에서 PWM 극성도 정상화합니다. 밝기 값은 기기 본래의 증가 방향 값을
사용하며, 소프트웨어로 최댓값에서 현재 값을 빼는 반전 방식이 아닙니다. 스피커 LINEOUT
게인은 23에서 25로 올렸으며, 헤드폰 게인은 바꾸지 않습니다.

## 복구

빈 `/boot/DISABLE_MALI.txt` 파일을 만들면 대체 메뉴 경로를 요청할 수 있습니다.
이 경로에서는 정상 PPSSPP Vulkan 기능을 제공하지 않습니다. 카드 자체의 복구 사본을
보관해 주세요. 체크섬으로 보호되어 있으며 다른 이미지의 백업과 서로 바꿔 쓸 수 없습니다.
새 엄격한 정상화 기능을 유지한 채 예전 PWM 장치 트리 플래그만 복원하지 마세요.
과거 실험의 일부를 섞기보다는 전체 이미지로 복원하는 편이 적절합니다.

## v1.0.1 Wi-Fi와 부팅 사본 연결

활성 번들은 `/boot/partitions/BOOT.IMG`입니다. Mali의 restore_boot·arm_boot는 `/boot/PPSSPP_VULKAN/autostart-backup/BOOT.IMG`를 기준으로 이를 다시 쓰며 트랜잭션 복원도 같은 기준을 사용합니다. Wi-Fi 수정을 두 사본에 넣고 복구 매니페스트의 BOOT 해시, manager의 BOOT_SHA, autostart의 BASE_SHA를 함께 맞춥니다. Mali 부팅 인자는 바꾸지 않았습니다.

S06은 AIC 경로를 유지하면서 순정 8723ds도 등록합니다. S08은 준비 작업을 예약하고, 실제 SHARE·/var/run/knulli.share.mounted·설치 완료와 필요한 무선 인터페이스를 기다린 뒤 최신 userdata 설정을 읽습니다. 기존에 켜진 무선 장치·서비스는 보존합니다. 앞 단계 전원 보완은 별개이며 상태 표시만으로 실제 네트워크 접속 성공을 뜻하지는 않습니다.

SDL Renderer·GLES 코어·OD-Commander 소프트웨어 Surface 경로를 구분해 보정합니다. PortMaster는 전용 SDL과 포트 게임용 제한적 preload를 사용하며, 설치 소스의 알려진 런타임 목록 처리 구문만 보완합니다.

## v1.0.2 Ozone과 전체 BOOT 검증 연결

일반 코어/단독 RetroArch는 gl/gl_sdl/ozone을 마지막 추가 설정으로 받습니다. 해당 프로세스에만 retroarch_gles3_context.so → app_output_rotation.so 순으로 연결해 SDL 주 버전 요청을 최소 3으로 맞춥니다. 기존 하드웨어 코어의 영상 설정은 유지합니다. 메뉴 guard의 BOOT 상수는 normal 복원 BOOT의 SHA256과 같아야 하며, 활성 armed BOOT를 요구하는 검사가 아닙니다. manager BOOT_SHA·autostart BASE_SHA·복원 manifest·메뉴 guard/manifest를 함께 갱신해야 합니다.

## v1.0.3 사용자 설정과 OSD

custom.sh는 일회성 로그 정리와 진동 보정을 실행하고 끝납니다. 진동 보정은 절전 후크를 부팅마다 다시 설치합니다. S50triggerhappy가 userdata의 multimedia_keys.conf를 우선 읽어 밝기 wrapper를 실행합니다. wrapper는 원래 밝기 계산·길게 누름·release를 유지하고 OSD만 요청합니다. OSD는 자체 non-master DRM 클라이언트의 dumb framebuffer와 비어 있는 plane을 사용합니다. 앱 master fd는 설정 호출 때만 복제하고 즉시 닫으며 대기 중 유지하지 않습니다. 표시 종료 때 자체 framebuffer와 비어 있는 plane 속성을 정리합니다. 통계는 system.telemetry=0으로 비활성화합니다.

## PPSSPP 1.20.4

앱·assets·전달 라이브러리는 /userdata/system/ppsspp-1.20.4에 설치됩니다. 두 /boot 런처 사본은 같은 앱을 실행하며 기존 Mali 세션·사용자 설정·종료 처리를 유지합니다. 원래 1.19.3 바이너리는 읽기 전용 시스템에 복구용으로 남지만 일반 실행에는 사용하지 않습니다.

## v1.0.5

S00bootcustom에서 BOOT의 zramswap wrapper 한 파일만 기존 서비스에 bind mount합니다. /var/run은 S04populate에서 나중에 생성되므로 이른 연결 로그는 BOOT에 둡니다. 기존 S99 사용자 서비스는 같은 설정값을 따르며 메뉴가 안정된 뒤 검증 모듈 5개를 올립니다. 시작 도중 중단된 기록이 있으면 다음 부팅에서 재시도를 차단하고 ACTIONPI_ZRAM/DISABLED로 복구할 수 있습니다. 기존 모듈과 modprobe 인덱스는 덮어쓰지 않습니다. BennuGD는 SHARE의 custom.sh/S99에서 연결하며 일반판은 BennuGD만, CRC판은 기존 아케이드 두 코어·MAME 별칭도 유지합니다.

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
