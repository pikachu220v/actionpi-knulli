"""Default standalone Vulkan dispatch; leaves libretro and all other apps alone."""
from pathlib import Path
import configparser,os,re,sys
BASE=Path('/userdata/system/flycast-standalone-vulkan')
ROTATION=Path('/userdata/system/flycast-vulkan/rotation')
DISABLE=Path('/boot/ACTIONPI_FIXES/DISABLE_FLYCAST_STANDALONE_VULKAN')

def write_config(path,cfg):
    temp=path.with_name(path.name+'.actionpi-settings-new')
    with temp.open('w') as f:cfg.write(f)
    os.chmod(temp,path.stat().st_mode);os.replace(temp,path)

def preserve_settings(before,after,system):
    """Keep app preferences unless ES explicitly selected an override."""
    options={
        ('config','rend.Resolution'):('flycast_render_resolution',),
        ('config','rend.WideScreen'):('flycast_ratio',),
        ('config','rend.Rotate90'):('flycast_rotate',),
        ('config','pvr.rend'):('flycast_renderer','flycast_sorting'),
        ('config','rend.AnisotropicFiltering'):('flycast_anisotropic',),
        ('config','rend.PerStripSorting'):('flycast_sorting',),
        ('config','Dreamcast.Language'):('flycast_language',),
        ('config','Dreamcast.Region'):('flycast_region',),
        ('config','Dreamcast.AutoLoadState'):('flycast_loadstate',),
        ('config','Dreamcast.AutoSaveState'):('flycast_savestate',),
        ('config','Dreamcast.ForceWindowsCE'):('flycast_winCE',),
        ('config','aica.DSPEnabled'):('flycast_DSP',),
    }
    for n in range(1,5):
        options['input','device%d'%n]=()
        options['input','device%d.1'%n]=()
        options['input','device%d.2'%n]=('flycast_ctrl%d_pack'%n,)
        options['config','rend.CrossHairColor%d'%n]=('flycast_lightgun%d_crosshair'%n,)
    changed=False
    for (section,key),es_options in options.items():
        custom='flycast.'+section+'.'+key
        if not before.has_option(section,key) or custom in system.config or any(system.isOptSet(x) for x in es_options):continue
        value=before.get(section,key)
        if after.get(section,key,fallback=None)==value:continue
        if not after.has_section(section):after.add_section(section)
        after.set(section,key,value);changed=True
    return changed

def install_generator():
    if os.environ.get('ACTIONPI_MALI_SESSION')!='1' or DISABLE.exists() or not (BASE/'ENABLED').is_file():return
    from configgen.generators.flycast import flycastGenerator as generator
    original=generator.FlycastGenerator.generate
    if getattr(original,'_actionpi_preserve_settings',False):return
    def generate(self,system,*args,**kwargs):
        path=generator.FLYCAST_CONFIG
        before=configparser.ConfigParser(interpolation=None);before.optionxform=str;before.read(path)
        # Keep built-in pad remaps made in Flycast's own menu. Keyboard/HOME
        # and the current controller-to-port assignment remain configgen-owned.
        mappings={p:p.read_bytes() for p in (path.parent/'mappings').glob('SDL_adc_gamepad*.cfg') if p.is_file()}
        result=original(self,system,*args,**kwargs)
        after=configparser.ConfigParser(interpolation=None);after.optionxform=str;after.read(path)
        if preserve_settings(before,after,system):write_config(path,after)
        for p,data in mappings.items():
            if p.read_bytes()!=data:p.write_bytes(data)
        return result
    generate._actionpi_preserve_settings=True
    generator.FlycastGenerator.generate=generate

def set_menu(mapping):
    """Configgen has just generated this built-in pad mapping: L3 is SDL button 10."""
    if not mapping.is_file():return False
    original=mapping.read_text();cfg=configparser.ConfigParser(interpolation=None)
    cfg.read_string(original)
    if not cfg.has_section('digital'):return False
    for key,value in cfg.items('digital'):
        if value.split(':',1)[0]=='10':
            if value=='10:btn_menu':return False
            cfg.set('digital',key,'10:btn_menu');break
    else:
        indices=[int(k[4:]) for k in cfg['digital'] if re.fullmatch(r'bind\d+',k)]
        cfg.set('digital','bind%d'%(max(indices,default=-1)+1),'10:btn_menu')
    temp=mapping.with_name(mapping.name+'.actionpi-menu-new')
    with temp.open('w') as f:cfg.write(f)
    os.chmod(temp,mapping.stat().st_mode);os.replace(temp,mapping)
    return True

def prepare(args,env):
    command=[str(x) for x in args]
    index=0 if command and command[0]=='/usr/bin/flycast' else 3 if command[:4]==['nice','-n','-4','/usr/bin/flycast'] else None
    if index is None or env.get('ACTIONPI_MALI_SESSION')!='1' or DISABLE.exists() or not (BASE/'ENABLED').is_file():return None
    binary=BASE/'bin/flycast'
    if not binary.is_file() or not (ROTATION/'libvulkan.so.1').is_file():
        print('ACTIONPI_FLYCAST_STANDALONE_VULKAN unavailable; using original GL',file=sys.stderr,flush=True);return None
    configroot=Path(env.get('XDG_CONFIG_HOME','/userdata/system/configs'))/'flycast'
    cfg=configparser.ConfigParser(interpolation=None);cfg.optionxform=str
    cfg.read(configroot/'emu.cfg')
    renderer=5 if cfg.get('config','pvr.rend',fallback='0').strip() in ('3','5') else 4
    # Persist the Vulkan selection rather than marking it transient, so changes
    # to sorting in Flycast's settings can be saved for the next launch.
    if cfg.get('config','pvr.rend',fallback=None)!=str(renderer):
        if not cfg.has_section('config'):cfg.add_section('config')
        cfg.set('config','pvr.rend',str(renderer));write_config(configroot/'emu.cfg',cfg)
    for name in ['SDL_adc_gamepad.cfg','SDL_adc_gamepad_arcade.cfg']:set_menu(configroot/'mappings'/name)
    env=dict(env)
    rotations={'app_output_rotation.so','retroarch_output_rotation.so','flycast_gl_rotation.so','sdl_output_rotation.so','od_commander_rotation.so','retroarch_gles3_context.so','actionpi_port_gles_context.so'}
    libs=[x for x in env.get('LD_PRELOAD','').replace(' ',':').split(':') if x and Path(x).name not in rotations]
    if libs:env['LD_PRELOAD']=':'.join(libs)
    else:env.pop('LD_PRELOAD',None)
    libpath=[x for x in env.get('LD_LIBRARY_PATH','').split(':') if x and x!=str(ROTATION)]
    env.update(LD_LIBRARY_PATH=':'.join([str(ROTATION),*libpath]),VK_ICD_FILENAMES='/usr/share/vulkan/icd.d/mali_icd.json',SDL_VULKAN_LIBRARY=str(ROTATION/'libvulkan.so.1'),SDL_VIDEODRIVER='kmsdrm',SDL_NO_SIGNAL_HANDLERS='1')
    for key in ['DISPLAY','WAYLAND_DISPLAY','SDL_RENDER_DRIVER']:env.pop(key,None)
    command[index]=str(binary)
    print('ACTIONPI_FLYCAST_STANDALONE_VULKAN renderer=%d L3=menu'%renderer,file=sys.stderr,flush=True)
    return command,env
