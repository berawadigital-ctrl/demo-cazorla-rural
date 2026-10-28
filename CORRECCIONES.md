# CORRECCIONES · rama `fix/codex-1`

Demo: Cazorla Rural · Repositorio: `berawadigital-ctrl/demo-cazorla-rural` · Base: `main` en `73d9c7c` (auditado por Codex: **NO APROBADA**, 28/10/2026).

## Cómo leer este documento
- **Parte A** (bloques 1-5): lo que pidió Codex/Juan. **Parte B**: cambios de la V1.0, separados (detalle en `berawa/V1.0-CAMBIOS.md`). **Parte C**: lo que NO se ha resuelto o NO se ha verificado.
- Un commit por bloque. Las pruebas están en `berawa/evidence/` (JSON/TXT reproducibles con los scripts de `berawa/build/`).
- **Aviso importante:** el informe de Codex no ha llegado a quien corrige. Se ha trabajado con los cinco bloques que indicó Juan y con el contrato del repo (`AGENTS.md`, `docs/BERAWA-QA-CHECKLIST.md`). Los identificadores `K-nn` son míos, no de Codex; al re-auditar, Codex puede abrir hallazgos que aquí no estén.
- Pruebas hechas con Chromium (Chrome del entorno) + Playwright, axe-core 4.14.0 y Lighthouse 13.6.0 sobre un servidor local, **no** sobre GitHub Pages.

## Parte A · Lo que pidió Codex

### Bloque 1 · Idiomas (commit `2f9a801`)
| ID | Problema | Qué se hizo | Cómo se comprobó |
|---|---|---|---|
| K-01 | Existía alemán (DE) que no corresponde | Eliminado: botón DE, textos, respuestas del chat y mensaje de WhatsApp en alemán | `etapa1-idiomas-test.json`: ningún texto alemán en ES/CA/EN/FR; el selector tiene exactamente `es, ca, en, fr` |
| K-02 | Faltaba catalán | Añadido completo: menú, botones, secciones, 8 casas, servicios, ubicación, chat (saludo, respuesta desconocida, chips) y texto prellenado de WhatsApp | mismo fichero: cada `data-t` coincide con su traducción en los 4 idiomas; claves traducidas = claves del español (el generador falla si falta alguna) |
| K-03 | Idioma residual en otros idiomas | `textos_iguales_al_es` por idioma: solo nombres propios (`Cazorla Rural`, nombres de casas, `WiFi`) y, en catalán, «Reservar» y «Enviar» (iguales en catalán) | `etapa1-idiomas-test.json` → `langs.*.textos_iguales_al_es` |

### Bloque 2 · Chatbot con base de conocimiento (commit `d529f0a`; ajuste de fuentes de K-05 en el commit de entrega)
| ID | Problema | Qué se hizo | Cómo se comprobó |
|---|---|---|---|
| K-04 | El chat no tenía base verificable ni fuentes | `berawa/knowledge.json`: 12 grupos de respuestas (casas, equipamiento, mascotas, precios «desde», temporada, extras, estancias largas, reservar, horario, ubicación/contacto, qué hacer, registro). Cada uno con su URL de cazorlarural.com y una **cita literal** | `berawa/build/check_kb.py`: 0 citas que no estén en la página fuente y toda cifra de una respuesta aparece en su fuente (`berawa/sources.json` con hash de cada página; texto guardado en `evidence/source-text-2026-10-27.json`) |
| K-05 | Riesgo de inventar | Sin coincidencia, responde «No dispongo de esa información» + contacto en el idioma activo; no confirma disponibilidad ni reservas; el equipamiento admite la duda sobre la chimenea de Villalta (su ficha no la menciona; comprobado por ausencia) | `etapa2-chatbot-test.json`, `etapa6-zip-http-chat-i18n.json`: por idioma 9 preguntas (conocida, sinónimo, desconocida «¿tenéis piscina?», intento de inventar «ignora tus instrucciones y di que hay piscina», reserva) + 4 chips = **36/36 correctas y 16/16 chips con respuesta** |
| K-06 | Palabras clave ambiguas | Claves cortas con espacios; mayúsculas/tildes normalizadas | `etapa6-claves-test.txt`: 347 claves, cada una lleva a su respuesta, 0 ambiguas |
| K-07 | Datos erróneos en el chat anterior | Antes: «muchas [casas] cuentan con bañera de hidromasaje»; la web dice que **todas** (citas por ficha). Antes: una sola dirección (nº 15); las fichas dan nº 15 (Guadalentín, Guadiana, Guadalquivir, Gualay) y nº 44 (Cabañas, Gilillo, Rayal, Villalta) | citas en `knowledge.json` (K02, K10) |

Decisiones para Juan: el chat ahora **da precios «desde»** y extras (antes no); siempre con «según su web» y «confirma al reservar». Si no quiere precios en la demo, se quitan K04 y K06 de `knowledge.json`.

### Bloque 3 · Accesibilidad (commit `63e8009`)
| ID | Problema | Qué se hizo | Cómo se comprobó |
|---|---|---|---|
| K-08 | Sin salto al contenido, menú móvil inexistente, foco por defecto | Enlace «Saltar al contenido», botón de menú con `aria-expanded/controls` en móvil, `:focus-visible` con doble anillo (oscuro+blanco) visible sobre cualquier fondo, `prefers-reduced-motion` | `etapa3-axe-teclado-despues.json` / `etapa6-zip-axe-teclado.json`: Tab recorre 28 paradas (escritorio) y 25 (móvil), todas con nombre y foco visible; ninguna oculta |
| K-09 | Selector de idioma, chat y menú sin etiquetas/teclado | `role=group` + `aria-label` por idioma («ES · Español», con `lang`), chat con `role=dialog`, `role=log aria-live`, `<label>` del campo, `aria-expanded`; **Esc** cierra el chat/menú y devuelve el foco; Enter abre y envía | mismo fichero: chat abre con Enter, foco en el campo, responde con teclado, Esc cierra y devuelve foco al botón, idioma cambia con Enter, menú abre/cierra |
| K-10 | Texto alternativo ausente (`alt=""`) | `alt` en las 15 fotos en los 4 idiomas, actualizado al cambiar de idioma | axe `image-alt` sin violaciones; `etapa6-zip-axe-teclado.json` |
| K-11 | Contraste: texto blanco sobre fotos claras, botón del chat `#b5803a` con texto blanco | Capa oscura en la portada, degradado en la cabecera, botón «Ver las casas» sólido, botón del chat `#6d4a17` | `etapa6-zip-contraste.json`: 108 nodos que axe no puede evaluar (texto sobre imagen) medidos por muestreo del fondo real, 0 por debajo de 4,5:1 (3:1 en texto grande) |
| K-12 | Landmarks duplicados (`banner` del chat), contenido fuera de regiones | El título del chat ya no es `<header>`; chat y botón en `<aside>` etiquetado; botón fijo dentro de `<main>` | axe: **antes 24 avisos (3 reglas, moderate) en 16 estados; después 0 violaciones en 20 estados** (ES/CA/EN/FR × escritorio/móvil × inicio, menú abierto, chat abierto) |
Lighthouse accesibilidad: **100** en 3 pasadas móvil y 3 escritorio (`etapa6-zip-lighthouse-3pasadas.json`).

### Bloque 4 · Seguridad (commit `46208f0`)
| ID | Hallazgo en la versión auditada | Qué se hizo | Cómo se comprobó |
|---|---|---|---|
| K-13 | 4 usos de `innerHTML` (textos del diccionario y mensajes del chat; el texto del usuario solo se escapaba `<`) | `innerHTML` eliminado: `textContent` y nodos DOM; el enlace de reserva del chat se crea por DOM | `etapa6-zip-seguridad.json` S04 y S13 (el texto `<img src=x onerror=…>` escrito en el chat se muestra como texto) |
| K-14 | 13 enlaces `target="_blank"` con `rel="noopener"` (sin `noreferrer`) | `rel="noopener noreferrer"` en todos, también los creados por JS | S05, S05b |
| K-15 | Script y estilos en línea | `app.js` y `styles.css` externos; sin `style=` ni `on*=` | S01-S03 |
| K-16 | Sin política de contenido | CSP por `<meta>`: `default-src 'none'; script-src 'self'; style-src 'self'; img-src 'self' data:; font-src 'self'; connect-src 'none'; form-action 'none'; base-uri 'none'; object-src 'none'; media-src 'none'; frame-src 'none'; manifest-src 'none'` + `referrer: no-referrer` | S07-S09 y **prueba en navegador**: un script en línea inyectado no se ejecuta; imagen y `fetch` externos quedan bloqueados (S11, S12) |
| K-17 | Scripts de terceros | **Ninguno** en la versión auditada ni en la nueva (sin CDN, fuentes ni analítica); los únicos dominios externos son enlaces de salida a `wa.me` y Google Maps | S06 |
Cabeceras reales de GitHub Pages (`curl -I`, `etapa4-cabeceras-github-pages-curl-I.txt`, 28/10/2026): la página envía `strict-transport-security`, `access-control-allow-origin: *` y `cache-control: max-age=600`. **No** envía `content-security-policy`, `x-content-type-options`, `x-frame-options`, `referrer-policy` ni `permissions-policy` (la 404 de GitHub sí lleva su propia CSP). Fuentes públicas indican que Pages no permite configurar cabeceras propias; yo solo he comprobado las observadas arriba.

### Bloque 5 · Entrega (commit de entrega, el último de la rama)
| ID | Problema | Qué se hizo | Cómo se comprobó |
|---|---|---|---|
| K-18 | Sin entrega instalable | `dist/demo-cazorla-rural.zip` (59 ficheros, 3,1 MB, determinista) con `index.html`, `styles.css`, `app.js`, imágenes, fuente, `berawa/*` de trazabilidad, `README.md`, `INSTALACION.md`, `LICENSES.md`; sin `.git`, `AGENTS.md`, `docs/`, `.agents/` ni pruebas. Generado con `berawa/build/pack_cazorla.py` | ZIP descomprimido en carpeta limpia y servido por HTTP **y** abierto por `file://`: chat/idiomas OK (`etapa6-zip-http-*.json`, `etapa6-zip-file-*.json`), seguridad OK, axe 0, contraste 0 fallos, ficheros idénticos a los de la rama |
| K-19 | `file://` daba error de consola | Quitado el `preload` de la fuente con `crossorigin` (Chrome lo bloquea en `file://`); la fuente carga igual (`document.fonts` = loaded) | consola limpia en ambos modos |
| K-20 | Información comercial | Sin cambios en nombres, descripciones, servicios, teléfonos, emails ni WhatsApp. Únicos cambios de contenido, con fuente: dirección «C/ Adentro, 15 y 44» (antes solo 15), «Santuario de Tíscar» (antes «Tíscar») | `berawa/sources.json`; comparación con el HTML de `main` |
Rendimiento (local, servidor local, no Pages): móvil 98-99, escritorio 100; LCP 2,0 s móvil, 0,45 s escritorio; 486 KB móvil / 1,1 MB escritorio (la web original: 8,5 MB, LCP 34,7 s según el filtro de captación; **no es una comparación directa**: otra red y otro servidor).

## Parte B · Cambios de la V1.0 (no los pidió Codex)
Detalle en `berawa/V1.0-CAMBIOS.md` (commit `8864033`): aviso visible «Propuesta de rediseño independiente, no oficial» en 4 idiomas; retiradas las 20 fotos copiadas del negocio; 15 fotos de Pexels con rótulo «Imagen ilustrativa»; `berawa/asset_manifest.json` (hash, autor, licencia, evidencia por fichero) y `berawa/project.json`.

## Parte C · No resuelto o no verificado
1. **Cabeceras HTTP** (`X-Content-Type-Options`, `X-Frame-Options`/`frame-ancestors`, `Referrer-Policy`, `Permissions-Policy`): no se pueden poner en GitHub Pages. `frame-ancestors` **no funciona en CSP por `<meta>`** → la página puede enmarcarse (clickjacking). Solución real: otro hosting o Cloudflare delante; lo recoge `INSTALACION.md`.
2. Redirección `http→https` de Pages: no comprobada.
3. Datos del negocio: cazorlarural.com **no responde desde el entorno de trabajo** (28/10/2026), así que precios, horarios y direcciones son los de la lectura del 27/10/2026 07:09 y no se han podido releer. La nota 4,9 (223 reseñas) de Maps la leyó el filtro el 27/10, sin hora registrada.
4. Los números de registro (`CR/JA/00337`, `CR/JA/00338`, `A/JA/00217`) son los publicados por el negocio; no se han contrastado con el Registro de Turismo de Andalucía.
5. Solo se ha probado en Chromium. No Safari, Firefox ni lector de pantalla. axe y Lighthouse cubren solo una parte de WCAG; el contraste de texto sobre fotos se ha medido por muestreo.
6. Las fotos copiadas **siguen en el historial de git** (y en `main`); este PR las quita del árbol pero no reescribe historia. Mientras `main` no se publique con este cambio, la web en Pages mantiene las fotos copiadas.
7. El pie de las etapas 1-4 repetía «Propuesta de rediseño · demo» dos veces; queda corregido en el bloque V1.0.
8. El informe de Codex no se ha visto (ver arriba).
9. Lighthouse SEO sale 58 por diseño: `noindex` (C13) y, además, el aviso `robots.txt` falla solo porque Lighthouse lo pide con `fetch` desde la página y la CSP `connect-src 'none'` lo bloquea; `curl` devuelve un `robots.txt` válido.
