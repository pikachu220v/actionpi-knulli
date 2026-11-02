import pathlib,subprocess,os
r=pathlib.Path('work/flycast-vk').resolve();base=pathlib.Path('.').resolve()
os.environ['ZIG_GLOBAL_CACHE_DIR']=str(base/'work/zig-global-cache');os.environ['ZIG_LOCAL_CACHE_DIR']=str(base/'work/zig-local-cache')
cm=base/'work/buildtools/cmake/data/bin/cmake.exe';ninja=next((base/'work/buildtools').rglob('ninja.exe'))
opts={'CMAKE_MAKE_PROGRAM':ninja,'CMAKE_TOOLCHAIN_FILE':r/'aarch64-zig.cmake','CMAKE_BUILD_TYPE':'Release','CMAKE_POLICY_VERSION_MINIMUM':'3.5','CMAKE_SKIP_RPATH':'ON','CMAKE_DISABLE_FIND_PACKAGE_PkgConfig':'ON','CMAKE_DISABLE_FIND_PACKAGE_X11':'ON','USE_VULKAN':'ON','USE_OPENGL':'OFF','USE_GLES':'OFF','USE_HOST_SDL':'ON','SDL2_DIR':r/'sdk/SDL2','CURL_INCLUDE_DIR':r/'sdk/curl-src/include','CURL_LIBRARY_RELEASE':r/'sdk/lib/libcurl.so.4','USE_HOST_LIBZIP':'OFF','ENABLE_UPNP':'OFF','USE_BREAKPAD':'OFF','USE_LUA':'OFF','USE_ALSA':'OFF','USE_LIBAO':'OFF','USE_PULSEAUDIO':'OFF','USE_OPENMP':'OFF','ACTIONPI_NO_DREAMLINK':'ON','ENABLE_DC_PROFILER':'OFF'}
args=[str(cm),'-S',str(r/'source'),'-B',str(r/'build'),'-G','Ninja','--fresh']+['-D'+k+'='+str(v).replace('\\','/') for k,v in opts.items()]
with (r/'configure.log').open('w',encoding='utf-8') as f:p=subprocess.run(args,stdout=f,stderr=subprocess.STDOUT)
print((r/'configure.log').read_text()[-7000:]);raise SystemExit(p.returncode)
