import re,json,hashlib,sys
sys.path.insert(0,'/workspace/agentes/webs/cazorla/gen')
from knowledge_cazorla import KB
t=open('/workspace/demos-2710/raw/cazorla/text.txt').read()
pages={}
for b in re.split(r'\n(?====== https)',t):
    m=re.match(r'===== (\S+) \|',b)
    if m: pages[m.group(1)]=pages.get(m.group(1),'')+re.sub(r'[ \t]+',' ',b).strip()+'\n'
used=sorted({s['url'] for e in KB['entries'] for s in e['sources']})
R='/workspace/agentes/webs/cazorla/repo/berawa'
json.dump(KB,open(R+'/knowledge.json','w'),ensure_ascii=False,indent=1)
src=dict(schema='berawa-sources/1',site='https://www.cazorlarural.com/',read_at='2026-10-27T07:09:00+01:00',
 method='Texto de cada página leído de la web pública el 27/10/2026; guardado en evidence/source-text-2026-10-27.json. cazorlarural.com no respondió desde el entorno de trabajo el 28/10/2026, por eso no se ha podido releer.',
 pages=[dict(url=u,sha256=hashlib.sha256(pages[u].encode()).hexdigest(),chars=len(pages[u])) for u in used])
json.dump(src,open(R+'/sources.json','w'),ensure_ascii=False,indent=1)
json.dump({u:pages[u] for u in used},open(R+'/evidence/source-text-2026-10-27.json','w'),ensure_ascii=False,indent=1)
print(len(used),'páginas fuente')
