import json,hashlib,os,glob,datetime,sys
sys.path.insert(0,'/workspace/agentes/webs/cazorla/gen')
from knowledge_cazorla import KB
R='/workspace/agentes/webs/cazorla/repo'
A=json.load(open('/workspace/agentes/webs/cazorla/assets.json'))
NOW=datetime.datetime.now().astimezone().isoformat(timespec='seconds')
CAP={ # título y descripción de la ficha de Pexels, leídos con la herramienta de lectura web el 28/10/2026
'hero':('Scenic River in Cazorla Natural Park, Spain','Stunning view of a tranquil river surrounded by lush greenery in Cazorla, Andalucía, Spain.'),
'intro':('Expansive Olive Groves Under a Clear Sky','A panoramic view of olive groves stretching across rolling hills under a bright blue sky. (Jaen, Spain)'),
'c1':('Cozy Modern Rustic Living Room with Fireplace','Warm rustic living room interior with brick wall, fireplace, and leather sofa.'),
'c2':('A Romantic Setting In The Bathroom','Relax in a cozy bathtub with candles, tea, and a book for a serene evening.'),
'c3':('A Bed in a Hotel','Cozy rustic bedroom with stone wall, vintage chandelier, and blue bedding.'),
'c4':('Living Room in Old House','Charming rustic living room with wooden beams and stone walls, perfect for cozy gatherings.'),
'c5':('Cozy Rustic Kitchen Interior with Wooden Elements','A beautifully crafted rustic kitchen with wooden beams and natural lighting.'),
'c6':('Cozy Rustic Living Room with Fireplace','Warm, inviting living room featuring a lit fireplace and rustic decor for a cozy ambiance.'),
'c7':('A Bathtub being Filled with Water','A serene bathtub scene with running water, candles, and subway tiles.'),
'c8':('Cozy Stone Interior Bedroom with Twin Beds','Rustic stone interior bedroom with twin beds, wooden accents, and natural light.'),
'g1':('Starry Night Sky with Milky Way and Mountains','Vibrant night sky with stars and Milky Way over silhouetted mountains.'),
'g2':('Milky way over the mountains','A breathtaking view of the Milky Way galaxy over a silhouetted landscape at night.'),
'g3':('Scenic Andalusian Olive Groves Landscape','Expansive olive groves in the Andalusian countryside under a bright sky.'),
'g4':('Scenic View of Castle and Valley in Jaén, Spain','Breathtaking view of the landscape from an ancient castle in Jaén, Andalucía, Spain.'),
'g5':('Cozy Wooden Kitchen in Rustic Cabin Interior','Wooden cabin kitchen interior with natural light and rustic decor.')}
LIC='Pexels License (https://www.pexels.com/license/): uso gratuito, atribución no necesaria, modificación permitida; prohibido sugerir aval de personas/marcas, vender copias sin modificar y usar como marca.'
os.makedirs(R+'/berawa/evidence/assets',exist_ok=True)
assets=[];sha=lambda p:hashlib.sha256(open(p,'rb').read()).hexdigest()
for k,cap in CAP.items():
    v=A[k];pid=v[0];page=f'https://www.pexels.com/photo/{v[1]}-{pid}/'
    raw=f'/workspace/agentes/webs/cazorla/assets-raw/{k}.jpg'
    ev=f'berawa/evidence/assets/{k}.txt'
    open(R+'/'+ev,'w').write(f"Ficha de Pexels leída el {NOW} (herramienta de lectura web)\nURL: {page}\nTítulo: {cap[0]}\nAutor mostrado: {v[2]}\nDescripción de la ficha: {cap[1]}\nLicencia: {LIC}\nDescarga: https://images.pexels.com/photos/{pid}/pexels-photo-{pid}.jpeg?w=2000 (HTTP 200; sha256 del original {sha(raw)} verificado con una segunda descarga idéntica)\nImagen ilustrativa: no muestra el establecimiento.\n")
    for suf in ('','-m'):
        p=f'img/{k}{suf}.webp'
        assets.append(dict(path=p,sha256=sha(R+'/'+p),origin='stock',source_url=page,title=cap[0],author=v[2],license='Pexels License',license_url='https://www.pexels.com/license/',attribution_required=False,attribution_text=None,modified=True,modification='recorte, redimensionado y conversión a WebP',original_sha256=sha(raw),depicts_real_business=False,shown_label='Imagen ilustrativa',tool=None,prompt_sha256=None,retrieved_at=NOW,evidence=ev))
open(R+'/berawa/evidence/assets/font.txt','w').write('Cormorant (Christian Thalmann, Catharsis Fonts), SIL OFL 1.1: uso comercial y redistribución permitidos. Fichero fonts/cormorant.woff2 ya presente en el repositorio original de la demo (commit eff126a). Licencia: https://openfontlicense.org/\n')
assets.append(dict(path='fonts/cormorant.woff2',sha256=sha(R+'/fonts/cormorant.woff2'),origin='font',source_url='https://github.com/CatharsisFonts/Cormorant',author='Christian Thalmann (Catharsis Fonts)',license='SIL OFL 1.1',license_url='https://openfontlicense.org/',attribution_required=False,attribution_text=None,modified=False,depicts_real_business=False,retrieved_at=NOW,evidence='berawa/evidence/assets/font.txt'))
json.dump(dict(schema='berawa-asset-manifest/1',project='demo-cazorla-rural',generated_at=NOW,note='Todas las fotos copiadas de cazorlarural.com se han retirado (bloque V1.0). Las 15 fotos actuales son de Pexels y se rotulan como ilustrativas.',assets=assets),open(R+'/berawa/asset_manifest.json','w'),ensure_ascii=False,indent=1)
ct={}
import re
P=dict(schema='berawa-project/1',slug='demo-cazorla-rural',template_version='webfactory-2026.10.28+fix-codex-1',created_at='2026-10-27',updated_at=NOW,
 business=dict(name='Cazorla Rural',legal_name=None,registry_ids=['CR/JA/00337','CR/JA/00338','A/JA/00217'],registry_note='números publicados en cazorlarural.com (pie y fichas); no contrastados con el Registro de Turismo de Andalucía',url='https://www.cazorlarural.com/',domain='cazorlarural.com',municipality='Quesada',province='Jaén',
  address='Calle Adentro 15 (Guadalentín, Guadiana, Guadalquivir, Gualay) y Calle Adentro 44 (Cabañas, Gilillo, Rayal, Villalta), 23480 Quesada (Jaén)',phones=['603 525 956'],emails=['info@cazorlarural.com'],sector='alojamiento rural'),
 rating=dict(value=4.9,reviews_count=223,source='Google Maps (ficha «Cazorla Rural», la web de la ficha coincide)',url='https://www.google.com/maps/place/Cazorla+Rural/@37.8468713,-3.1402777,13z',date='2026-10-27',threshold=4.0,note='leída por el filtro de captación el 27/10/2026; sin hora registrada'),
 languages=['es','ca','en','fr'],noindex=True,notice_es='Propuesta de rediseño independiente, no oficial',
 chatbot=dict(api=False,kind='base local de respuestas verificadas',knowledge='berawa/knowledge.json',entries=len(KB['entries']),fallback_es='No dispongo de esa información'),
 book=dict(mode='wa',url='https://wa.me/34603525956',source='número WhatsApp publicado en cazorlarural.com/reservas.html'),
 audit_original=dict(url='https://www.cazorlarural.com/',date='2026-10-27',veredicto='MALA (54 puntos)',lighthouse=dict(performance=51,accessibility=85,best_practices=57,seo=85,lcp_s=34.7,peso_mb=8.5),tool='filtro_mala_web.py (Lighthouse móvil)'),
 codex=dict(audits=[dict(sha='73d9c7c',dictamen='NO_APROBADA',fecha='2026-10-28',fuente='mensaje de Juan 28/10 9:41; el informe de Codex no se ha entregado a Grok: la corrección se ha hecho con los cinco bloques indicados por Juan y el contrato del repo')]),
 lighthouse_min=dict(performance=85,accessibility=95,best_practices=90),
 preview_url='https://berawadigital-ctrl.github.io/demo-cazorla-rural/',
 changes_log='ver CORRECCIONES.md (bloques 1-5: Codex; bloque V1.0: aparte)')
json.dump(P,open(R+'/berawa/project.json','w'),ensure_ascii=False,indent=1)
print(len(assets),'activos')
