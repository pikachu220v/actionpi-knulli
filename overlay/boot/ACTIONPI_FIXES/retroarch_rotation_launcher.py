"""Run the original configgen wrapper; scope output correction to SDL2 RetroArch only."""
import os,runpy,subprocess,sys,threading,time
from pathlib import Path

Popen=subprocess.Popen
def rotated_popen(args,*pos,**kwargs):
    command=[str(x) for x in args] if isinstance(args,(list,tuple)) else []
    if '/userdata/roms/ports/PortMaster.sh' in command:
        sys.path.insert(0,'/boot/ACTIONPI_FIXES')
        from actionpi_portmaster_fix import prepare
        prepare()
    is_ra=bool(command) and (command[0]=='/usr/bin/retroarch' or command[:4]==['nice','-n','-4','/usr/bin/retroarch'])
    is_port=any('/roms/ports/' in x and x.endswith('.sh') for x in command)
    is_pm=any(Path(x).name in ('PortMaster.sh','Install.PortMaster.sh') for x in command)
    if is_port and not is_pm:
        sys.path.insert(0,'/boot/ACTIONPI_FIXES')
        from actionpi_app_launcher import preload
        env=preload(dict(kwargs.get('env') or os.environ))
        kwargs['env']=env
    # ACTIONPI_FLYCAST_STANDALONE_ROTATION: preserve all unrelated preloads.
    is_flycast=bool(command) and (command[0]=='/usr/bin/flycast' or command[:4]==['nice','-n','-4','/usr/bin/flycast'])
    if is_flycast:
        env=dict(kwargs.get('env') if kwargs.get('env') is not None else os.environ)
        prepared=None
        if env.get('ACTIONPI_MALI_SESSION')=='1':
            sys.path.insert(0,'/boot/ACTIONPI_FIXES')
            from actionpi_flycast_standalone_vulkan import prepare
            prepared=prepare(args,env)
        if prepared is not None:
            args,kwargs['env']=prepared
        else:
            helper=Path('/boot/ACTIONPI_FIXES/flycast_gl_rotation.so')
            if env.get('ACTIONPI_MALI_SESSION')=='1' and helper.is_file():
                rotations={'app_output_rotation.so','retroarch_output_rotation.so','flycast_gl_rotation.so','sdl_output_rotation.so','od_commander_rotation.so'}
                libs=[x for x in env.get('LD_PRELOAD','').replace(' ',':').split(':') if x and Path(x).name not in rotations]
                env['LD_PRELOAD']=':'.join([str(helper),*libs])
                kwargs['env']=env
    child=Popen(args,*pos,**kwargs)
    if command[:3]==['nice','-n','-4'] and len(command)>3:
        sys.path.insert(0,'/boot/ACTIONPI_FIXES')
        from home_exit import register
        register(child.pid,command[3])
    for name in ('flycastvl','flycast-xtreme'):
        if any(name+'_libretro.so' in x for x in command) and Path('/boot/ACTIONPI_FIXES/ENABLE_FAULT_TRACE').exists():
            tracer=Path('/boot/ACTIONPI_FIXES/flycast_fault_trace.py')
            if tracer.exists() and (tracer.parent/'ENABLE_FAULT_TRACE').exists():
                Popen([sys.executable,str(tracer),str(child.pid),str(tracer.parent/(name+'-fault'))],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
            def record(p=child,label=name):
                dest=Path('/boot/ACTIONPI_FIXES')/(label+'-maps.txt')
                for _ in range(12):
                    try:
                        text=Path('/proc/%d/maps'%p.pid).read_text()
                        if label+'_libretro.so' in text:dest.write_text(text)
                    except OSError:break
                    time.sleep(.1)
            threading.Thread(target=record,daemon=True).start()
    return child

def launch():
    if os.environ.get('ACTIONPI_MALI_SESSION')=='1':
        sys.path.insert(0,'/boot/ACTIONPI_FIXES')
        from actionpi_flycast_standalone_vulkan import install_generator
        install_generator()
    subprocess.Popen=rotated_popen
    try:runpy.run_path('/run/actionpi-emulatorlauncher-original',run_name='__main__')
    finally:subprocess.Popen=Popen

if __name__=='__main__':launch()
