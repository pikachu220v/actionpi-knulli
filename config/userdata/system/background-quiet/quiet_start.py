#!/usr/bin/env python3
"""Stop only obsolete Action Pi progress copying and disabled telemetry workers."""
from pathlib import Path
import os,signal,subprocess,time,json

LOOP='(while :;do cp /var/run/boot.log /boot/boot/a30-progress.log 2>/dev/null;sleep 2;done)&'

def processes():
    result={}
    for p in Path('/proc').glob('[0-9]*'):
        try:
            cmd=[s.decode(errors='replace') for s in (p/'cmdline').read_bytes().split(b'\0') if s]
            raw=(p/'stat').read_text();s=raw[raw.rfind(')')+2:].split()
            result[int(p.name)]={'cmd':cmd,'ppid':int(s[1]),'born':s[19],'state':s[0]}
        except (OSError,IndexError,ValueError):pass
    return result

def terminate(pid,expected):
    now=processes().get(pid)
    if now and now['born']==expected['born'] and now['cmd']==expected['cmd']:
        try:os.kill(pid,signal.SIGTERM)
        except ProcessLookupError:pass

SNAPSHOT='(sleep 60;{ ps -ef;cat /proc/fb;for f in /sys/class/graphics/fb0/virtual_size /sys/class/graphics/fb0/stride /sys/class/graphics/fb0/bits_per_pixel /sys/class/drm/card0-*/status /sys/class/drm/card0-*/modes;do echo =$f;cat $f;done;cat /boot/boot/a30-es.log; } >/boot/boot/a30-runtime.log 2>&1)&'

def quiet():
    rc=Path('/etc/init.d/rcS');text=rc.read_text()
    if any(s in (LOOP,SNAPSHOT) for s in text.splitlines()):
        rc.write_text('\n'.join(s for s in text.splitlines() if s not in (LOOP,SNAPSHOT))+'\n')
    stopped=[]
    # An already-running shell has parsed the old loop. Its orphaned process is
    # identified by exact rcS command + its exact sleep/copy child, never by name alone.
    for _ in range(10):
        ps=processes();found=False
        for pid,p in ps.items():
            if p['cmd'] not in (['/bin/sh','/etc/init.d/rcS'],['sh','/etc/init.d/rcS']) or p['ppid']!=1:continue
            kids={k:v for k,v in ps.items() if v['ppid']==pid}
            matches=[v['cmd'] in (['sleep','2'],['/bin/sleep','2']) or
                     ('/var/run/boot.log' in v['cmd'] and '/boot/boot/a30-progress.log' in v['cmd']) for v in kids.values()]
            # Both known jobs are forked by the inherited rcS header.
            # Match the exact parent script and exact child command only.
            if SNAPSHOT in text.splitlines():
                matches += [v['cmd'] in (['sleep','60'],['/bin/sleep','60']) for v in kids.values()]
            if not any(matches):continue
            found=True;terminate(pid,p)
            for child,info in kids.items():terminate(child,info)
            stopped.append(pid)
        if stopped:break
        time.sleep(.2)
    telemetry=subprocess.run(['/usr/bin/knulli-settings-get','system.telemetry'],capture_output=True,text=True,timeout=5).stdout.strip()
    stats_stopped=[]
    if telemetry=='0':
        ps=processes()
        selected={pid for pid,p in ps.items() if any(s in ('/etc/init.d/S97stats','/usr/bin/knulli-report-stats') for s in p['cmd'])}
        while True:
            children={pid for pid,p in ps.items() if p['ppid'] in selected}
            if children<=selected:break
            selected|=children
        for pid in sorted(selected):terminate(pid,ps[pid]);stats_stopped.append(pid)
    return {'loop_stopped':stopped,'telemetry':telemetry,'stats_stopped':stats_stopped,
            'rcS_loop_removed':LOOP not in rc.read_text(),
            'boot_snapshot_removed':SNAPSHOT not in rc.read_text()}

if __name__=='__main__':print(json.dumps(quiet()))
