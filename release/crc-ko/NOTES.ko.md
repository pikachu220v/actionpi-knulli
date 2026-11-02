# 한국 사용자용 · CRC 무시 코어 적용판 v1.0.9

한글 패치 아케이드 게임용 FBNeo·MAME2003 Plus CRC 무시 코어가 필요한 분을 위한 별도 배포판입니다. 기본 배포판과 이미지·체크섬을 분리했습니다.

CRC 무시 코어는 **[dsno님 자료](https://dsno.tistory.com/m/)**를 사용했습니다. 이번 버전에서 두 코어 바이너리는 변경하지 않았습니다.

## v1.0.9 수정 내역

- **Flycast 스탠드얼론 Vulkan 기본 적용:** 평소 스탠드얼론 항목에서 공식 Flycast v2.7 기반 액션파이용 Vulkan 실행 파일을 사용합니다. 기존 RetroArch 일반·VL·Xtreme 코어도 유지합니다.
- **사용자 실기 체감 기준, RetroArch 코어와 동등하거나 더 나은 성능**을 확인했습니다. 정식 동일 조건 벤치마크 결과나 모든 게임의 성능 보장을 뜻하지 않습니다.
- **L3(왼쪽 아날로그 스틱 클릭)로 Flycast 설정 메뉴에 들어갑니다.** 게임과 자체 메뉴의 전체 화면 회전을 보정하고 HOME으로 ES에 복귀합니다.
- **설정 유지 보완:** Flycast 안에서 고친 진동팩과 각종 설정을 종료·재실행 후에도 유지합니다. ES에서 명시한 옵션은 우선 적용하고, 나머지 앱 설정과 패드 재매핑은 보존합니다.
- **GL 복구 경로 유지:** Vulkan 파일이 없거나 비활성화한 경우의 기존 GL 실행 분기를 유지합니다. 최종 수정판에서 GL로 되돌리는 전환 자체를 별도로 실기 재시험하지는 않았습니다. Ports 시험 항목은 포함하지 않습니다.

코어는 재부팅할 때마다 자동 연결되며 save-overlay는 필요 없습니다. MAME2003 Plus의 mame078plus 이름도 처리합니다.

## 설치와 사용

이 릴리스의 .img.xz와 SHA256SUMS를 내려받아 체크섬을 확인하고 SD 전체에 기록합니다. 필요하면 XZ를 먼저 풀어 주세요. 대상 SD의 기존 내용은 지워집니다.

**첫 설치 시 부팅 이미지 이후 검정화면이 보여도 약 5분 기다려 주세요. 자동 확장·설정 적용으로 한두 번 재부팅한 뒤 메뉴가 표시됩니다. 완료될 때까지 전원을 유지하세요.**

새턴 스탠드얼론 메뉴: **L3(왼쪽 스틱 클릭)**.

새턴 스탠드얼론 메뉴: **L3(왼쪽 스틱 클릭)**.

밝기: SELECT+볼륨 +/−. PPSSPP 종료: SELECT+START 약 1초. 상단의 HOME키를 이용한 에뮬레이터 종료는 RetroArch에서 작동하고 PPSSPP에서는 비활성화되어 있습니다. 게임 ROM은 포함하지 않습니다. ZRAM 복구는 BOOT의 `ACTIONPI_ZRAM` 폴더에 `DISABLED`라는 빈 파일을 만들면 됩니다.

## 확인 범위와 출처

사용자가 Vulkan 게임 실행·메뉴 방향·L3·HOME 복귀·최종 설정 지속성을 확인했습니다. 최종 Vulkan 기본/설정 보존 단계의 별도 재부팅 및 최종 배포 이미지의 새 SD 설치 확인은 아직 하지 않았습니다.

제공된 두 코어와 자동 연결은 기존 확인 결과를 유지하며 새 이미지에서 코어 해시 동일성을 확인했습니다. 정확히 일치하는 수정 코어 소스와 CRC 패치는 제공받지 못했으며 상위 소스 링크를 정확한 대응 소스로 주장하지 않습니다.

- [CRC판 상세 안내](https://github.com/pikachu220v/actionpi-knulli/blob/v1.0.9/docs/CRC_KOREAN.ko.md)
- [작업 이력](https://github.com/pikachu220v/actionpi-knulli/blob/v1.0.9/docs/HISTORY.ko.md)
- [작동 구조](https://github.com/pikachu220v/actionpi-knulli/blob/v1.0.9/docs/ARCHITECTURE.ko.md)
- [빌드·이미지 제작](https://github.com/pikachu220v/actionpi-knulli/blob/v1.0.9/docs/BUILD.ko.md)
- [공개 파일](https://github.com/pikachu220v/actionpi-knulli/blob/v1.0.9/docs/PUBLIC_FILES.ko.md)
- [출처·라이선스](https://github.com/pikachu220v/actionpi-knulli/blob/v1.0.9/docs/SOURCES_AND_LICENSES.ko.md)
- [설치 안내](https://github.com/pikachu220v/actionpi-knulli/blob/v1.0.9/docs/RELEASE.ko.md)
- [검증 범위](https://github.com/pikachu220v/actionpi-knulli/blob/v1.0.9/docs/TESTING.ko.md)

압축 해제 IMG: 6,069,178,368바이트. SHA256: 0702b8b3734c97d5b4b3223f0a121a75c7a5802cef594bef1c958fdcb609b304. CRC판 전용 체크섬을 사용하세요.

BennuGD는 별도로 제공받은 코어이며 dsno님 출처 표기는 FBNeo·MAME CRC 무시 코어에만 해당합니다. BennuGD의 정확한 대응 소스·빌드 정보는 제공받지 못했습니다.

Flycast 대응 소스: [일반판의 flycast-v1.0.6-sources.tar](https://github.com/pikachu220v/actionpi-knulli/releases/download/v1.0.9/flycast-v1.0.6-sources.tar). 펌웨어 이미지가 아닌 소스 묶음입니다.

야바산시로 소스·빌드 자료: [src/saturn-standalone](https://github.com/pikachu220v/actionpi-knulli/tree/v1.0.9/src/saturn-standalone). 정확히 대응하는 전체 수정 소스 묶음을 릴리스에 첨부했습니다.

Flycast 스탠드얼론 전체 소스·빌드 자료: [한국어 안내](https://github.com/pikachu220v/actionpi-knulli/blob/v1.0.9/src/flycast-standalone-vulkan/README.ko.md). 대응 전체 소스는 릴리스에 첨부합니다.
