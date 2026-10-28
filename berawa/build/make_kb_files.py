"""Escribe berawa/knowledge.json, sources.json y evidence/source-text-*.json a partir de knowledge_cazorla.py.
Texto de las paginas: por defecto el guardado en el repo (berawa/evidence/source-text-2026-10-27.json); BERAWA_RAW_TEXT=ruta/text.txt usa el texto crudo original."""
import re,json,hashlib,sys,os
from _rutas import ROOT,SOURCE_TEXT
from knowledge_cazorla import KB
raw=os.environ.get('BERAWA_RAW_TEXT')
pages={}
if raw:
    t=open(raw,encoding='utf-8').read()
    for b in re.split(r'\n(?====== https)',t):
        m=re.match(r'===== (\S+) \|',b)
        if m: pages[m.group(1)]=pages.get(m.group(1),'')+re.sub(r'[ \t]+',' ',b).strip()+'\n'
else: pages=json.load(open(SOURCE_TEXT,encoding='utf-8'))
used=sorted({s['url'] for e in KB['entries'] for s in e['sources']})
R=str(ROOT/'berawa')
json.dump(KB,open(R+'/knowledge.json','w'),ensure_ascii=False,indent=1)
src=dict(schema='berawa-sources/1',site='https://www.cazorlarural.com/',read_at='2026-10-27T07:09:00+01:00',
 method='Texto de cada página leído de la web pública el 27/10/2026; guardado en evidence/source-text-2026-10-27.json. cazorlarural.com no respondió desde el entorno de trabajo el 28/10/2026, por eso no se ha podido releer.',
 pages=[dict(url=u,sha256=hashlib.sha256(pages[u].encode()).hexdigest(),chars=len(pages[u])) for u in used])
json.dump(src,open(R+'/sources.json','w'),ensure_ascii=False,indent=1)
json.dump({u:pages[u] for u in used},open(R+'/evidence/source-text-2026-10-27.json','w'),ensure_ascii=False,indent=1)
print(len(used),'páginas fuente')
