import sys,json
sys.path.insert(0,'/workspace/agentes/webs/cazorla/gen')
import cz_build as C
from content_cazorla import D,ALTS_OLD,ALTS_NEW
from knowledge_cazorla import KB
OUT='/workspace/agentes/webs/cazorla/repo'
OLD=dict(hero='hero',intro='intro',rooms=[f'h{i}' for i in range(1,9)],gallery=[f'g{i}' for i in range(10)])
NEW=dict(hero='hero',intro='intro',rooms=[f'c{i}' for i in range(1,9)],gallery=['g4','g1','g2','g3','g5'])
def run(stage):
    st=set(stage)
    C.build(D,KB,OUT,NEW if 'v1' in st else OLD,ALTS_NEW if 'v1' in st else ALTS_OLD,st)
if __name__=='__main__': run(sys.argv[1:]); print('built',sys.argv[1:])
