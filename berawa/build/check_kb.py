import re,json,sys
sys.path.insert(0,'.')
from knowledge_cazorla import KB
t=open('/workspace/demos-2710/raw/cazorla/text.txt').read()
pages={}
for b in re.split(r'\n(?====== https)',t):
    m=re.match(r'===== (\S+) \|',b)
    if m: pages[m.group(1)]=pages.get(m.group(1),'')+' '+re.sub(r'\s+',' ',b)
bad=0
for e in KB['entries']:
    for s in e['sources']:
        p=pages.get(s['url'])
        if p is None: print('SIN PAGINA',e['id'],s['url']);bad+=1;continue
        q=s['quote']
        if q.startswith('!'):
            if q[1:] in p: print('AUSENCIA FALSA',e['id'],s['url'],q);bad+=1
            continue
        if re.sub(r'\s+',' ',s['quote']) not in p: print('CITA NO ENCONTRADA',e['id'],s['url'],'|',s['quote'][:70]);bad+=1
print('entradas',len(KB['entries']),'fallos',bad)
# cifras de las respuestas deben aparecer en alguna fuente citada de la entrada
for e in KB['entries']:
    src=' '.join(pages[s['url']] for s in e['sources'] if s['url'] in pages)
    for l,a in e['a'].items():
        for n in set(re.findall(r'\d+',a)):
            if n not in src and n not in ('8',): print('CIFRA SIN FUENTE',e['id'],l,n)
