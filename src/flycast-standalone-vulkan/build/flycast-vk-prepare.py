import pathlib,sys,json,urllib.request,tarfile,io
sys.path.insert(0,'work/buildtools')
from elftools.elf.elffile import ELFFile
root=pathlib.Path('work/flycast-vk').resolve();src=root/'source';sdk=root/'sdk'
def archive(repo,ref,dest,only=None):
    if (dest/'CMakeLists.txt').exists() and only is None:return
    raw=urllib.request.urlopen('https://codeload.github.com/'+repo+'/tar.gz/'+ref,timeout=45).read()
    with tarfile.open(fileobj=io.BytesIO(raw),mode='r:gz') as tf:
        for m in tf.getmembers():
            parts=pathlib.PurePosixPath(m.name).parts[1:]
            if not parts or not m.isfile():continue
            if only and not '/'.join(parts).startswith(only):continue
            p=dest.joinpath(*parts);p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(tf.extractfile(m).read())
sources=json.loads((root/'SOURCES.json').read_text())
for x in sources['standard_archives']:
    if x['path'].startswith('core/deps/freetype') or 'tinycmmc' in x['path']:
        archive(x['repo'],x['ref'],src/x['path'])
archive('curl/curl','curl-8_10_1',sdk/'curl-src','include/curl/')
cm=src/'CMakeLists.txt';t=cm.read_text()
# External DreamLink USB accessories are unrelated to the built-in gamepad.
t=t.replace('if (NOT NINTENDO_SWITCH)\n\t\t\t# DreamLink','if (NOT NINTENDO_SWITCH AND NOT ACTIONPI_NO_DREAMLINK)\n\t\t\t# DreamLink')
t=t.replace('execute_process(COMMAND getconf PAGESIZE OUTPUT_VARIABLE PAGE_SIZE OUTPUT_STRIP_TRAILING_WHITESPACE)','set(PAGE_SIZE 4096) # Action Pi target page size, not Windows host')
t=t.replace('set(GIT_VERSION "v0.0.0-0-g000000000")','set(GIT_VERSION "v2.7-actionpi-vulkan-test")').replace('set(GIT_HASH "000000000")','set(GIT_HASH "5aa091fde")')
cm.write_text(t)
zig=(pathlib.Path('work/toolchains/zig-windows-x86_64-0.13.0/zig.exe').resolve()).as_posix()
tool=f'''set(CMAKE_SYSTEM_NAME Linux)
set(CMAKE_SYSTEM_PROCESSOR aarch64)
set(CMAKE_C_COMPILER "{zig}")
set(CMAKE_C_COMPILER_ARG1 "cc -target aarch64-linux-gnu.2.38")
set(CMAKE_CXX_COMPILER "{zig}")
set(CMAKE_CXX_COMPILER_ARG1 "c++ -target aarch64-linux-gnu.2.38")
set(CMAKE_ASM_COMPILER "{zig}")
set(CMAKE_ASM_COMPILER_ARG1 "cc -target aarch64-linux-gnu.2.38")
set(CMAKE_AR "{zig}")
set(CMAKE_C_ARCHIVE_CREATE "<CMAKE_AR> ar qc <TARGET> <LINK_FLAGS> <OBJECTS>")
set(CMAKE_CXX_ARCHIVE_CREATE "<CMAKE_AR> ar qc <TARGET> <LINK_FLAGS> <OBJECTS>")
set(CMAKE_C_ARCHIVE_FINISH "<CMAKE_AR> ranlib <TARGET>")
set(CMAKE_CXX_ARCHIVE_FINISH "<CMAKE_AR> ranlib <TARGET>")
set(CMAKE_TRY_COMPILE_TARGET_TYPE EXECUTABLE)
set(CMAKE_FIND_ROOT_PATH "{sdk.as_posix()}")
set(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)
set(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_PACKAGE ONLY)
set(CMAKE_EXE_LINKER_FLAGS_INIT "-Wl,--allow-shlib-undefined")
'''
(root/'aarch64-zig.cmake').write_text(tool)
# Host SDL discovery points only at the existing device library and official headers.
cfg=sdk/'SDL2';cfg.mkdir(exist_ok=True)
(cfg/'SDL2Config.cmake').write_text(f'''set(SDL2_FOUND TRUE)
set(SDL2_INCLUDE_DIRS "{(src/'core/deps/SDL/include').as_posix()}")
set(SDL2_LIBRARIES "{(sdk/'lib/libSDL2-2.0.so.0').as_posix()}")
if(NOT TARGET SDL2::SDL2)
add_library(SDL2::SDL2 SHARED IMPORTED)
set_target_properties(SDL2::SDL2 PROPERTIES IMPORTED_LOCATION "${{SDL2_LIBRARIES}}" INTERFACE_INCLUDE_DIRECTORIES "${{SDL2_INCLUDE_DIRS}}")
endif()
''')
(cfg/'SDL2ConfigVersion.cmake').write_text('set(PACKAGE_VERSION "2.32.10")\nset(PACKAGE_VERSION_COMPATIBLE TRUE)\n')
for name in ['flycast','libSDL2-2.0.so.0']:
    p=sdk/'lib'/name
    with p.open('rb') as f:
        elf=ELFFile(f);print('ELF',name,elf['e_machine'])
        d=elf.get_section_by_name('.dynamic')
        print('NEEDED',[x.needed for x in d.iter_tags() if x.entry.d_tag=='DT_NEEDED'])
        tab=elf.get_section_by_name('.dynsym')
        print('RELEVANT_SYMBOLS',[x.name for x in tab.iter_symbols() if any(k in x.name for k in ['SDL_Vulkan','SDL_CreateWindow','SDL_GL_Create','vkCreate','vkGetInstance'])])
    if name=='libSDL2-2.0.so.0':
        b=p.read_bytes();print('KMS_VK_STRINGS',[(x,x.encode() in b) for x in ['VK_KHR_display','Vulkan support is either not configured in SDL','KMSDRM']])
print('PREPARED')
