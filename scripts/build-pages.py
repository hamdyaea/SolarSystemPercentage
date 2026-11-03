#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein | Contact: info@daylightlinux.ch
from pathlib import Path
import subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'public-site'
subprocess.run([sys.executable,str(ROOT/'build.py'),'--source',str(ROOT/'data/orbital.json'),'--out',str(OUT)],check=True)
files=[p for p in OUT.rglob('*') if p.is_file()]
assert len(files)<=20000 and all(p.stat().st_size<=25*1024*1024 for p in files)
print('Pages ready:',len(files),'public files')
