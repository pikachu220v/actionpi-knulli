# Flycast 스탠드얼론 Vulkan / v1.0.9

릴리스의 flycast-standalone-v1.0.9-sources.tar.xz는 실제 수정 소스·고정된 의존 소스·라이선스·Zig 0.13.0 교차 빌드 자료·디스플레이 패치·최종 BOOT 연결을 포함합니다. 바이너리는 집 실기에서 검증한 바이트 그대로이며 버전 표시는 v2.7-actionpi-vulkan-test입니다. 공식 소스 커밋과 해시는 SOURCES.json에 기록합니다.

Vulkan 전용 렌더링·ARM64 JIT·SDL2 입력/소리를 사용합니다. VK_KHR_display에서 논리 960×720 모드를 고르는 앱 전용 패치가 핵심이며, 기존 회전 로더가 게임과 메뉴 전체를 물리 720×960으로 출력합니다. 커널·시스템 SDL2·Mali 라이브러리는 바꾸지 않습니다.

전체 소스 압축을 풀고 build 폴더의 스크립트·로그를 참고하여 절대 경로와 target SDK를 자신의 환경에 맞춥니다. 상속된 독점 SDK/Mali 바이너리는 소스 묶음에 포함하지 않습니다. 다른 SDK에서 같은 바이너리 해시가 재현된다고 주장하지 않습니다. 설정 유지에는 configgen 전 install_generator와 실행 전 prepare가 모두 필요합니다.

사용자가 Vulkan 화면·방향·L3·HOME·종료 후 설정 유지를 확인했습니다. 성능은 사용자 체감 평가이며, 최종 Vulkan 상태의 별도 재부팅·GL 되돌리기 전환·최종 이미지 새 SD 설치는 별도 확인하지 않았습니다. ROM·BIOS·세이브·인증정보·개인 설정·기기 복구 tar는 포함하지 않습니다.
