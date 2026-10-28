import sys,json,tempfile
from _rutas import ROOT
import cz_build as C
from content_cazorla import D,ALTS_OLD,ALTS_NEW
from knowledge_cazorla import KB
OUT=None   # carpeta de salida: 2.º argumento --out=DIR (por defecto, una carpeta temporal; nunca se pisa el repo sin pedirlo)
OLD=dict(hero='hero',intro='intro',rooms=[f'h{i}' for i in range(1,9)],gallery=[f'g{i}' for i in range(10)])
NEW=dict(hero='hero',intro='intro',rooms=[f'c{i}' for i in range(1,9)],gallery=['g4','g1','g2','g3','g5'])
def run(stage,out):
    st=set(stage)
    C.build(D,KB,out,NEW if 'v1' in st else OLD,ALTS_NEW if 'v1' in st else ALTS_OLD,st)
if __name__=='__main__':
    a=[x for x in sys.argv[1:] if not x.startswith('--out=')];o=[x[6:] for x in sys.argv[1:] if x.startswith('--out=')]
    out=o[0] if o else tempfile.mkdtemp(prefix='cazorla-build-')
    run(a,out); print('built',a,'->',out)
