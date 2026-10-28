# berawa/build · scripts de comprobación y de generación

Todo se ejecuta **desde un clon normal del repositorio**: los scripts resuelven sus rutas desde la raíz del repo (`berawa/build/_rutas.py`, `Path(__file__).resolve().parents[1]`), sin rutas absolutas ni carpetas externas. Estos scripts **no van en el ZIP** (`dist/demo-cazorla-rural.zip`).

## Dependencias (solo para las comprobaciones)
```
python3 -m venv .venv && . .venv/bin/activate        # opcional
pip install -r berawa/build/requirements.txt          # playwright >=1.60,<2 (probado con 1.60.0 y 1.64.1) + Pillow
playwright install chromium                           # navegador que usa Playwright
(cd berawa/build && npm install)                      # axe-core 4.14.0 (package-lock.json incluido)
```
Opcional: `CHROME_PATH=/ruta/a/chrome` para usar otro Chrome/Chromium en vez del de Playwright; `AXE_DIR=/ruta/a/axe-core` para otra copia de axe-core.

## Comando único
```
python3 berawa/build/run_checks.py               # prueba el sitio de la raíz del repo por HTTP local
python3 berawa/build/run_checks.py --file        # y además abriendo index.html por file://
python3 berawa/build/run_checks.py --site DIR    # otra carpeta (p. ej. el ZIP descomprimido)
```
Levanta un servidor local en un puerto libre, no usa red externa y escribe los JSON de resultados en una carpeta temporal (`--out DIR` para elegirla). Sale con código 1 si algo falla.

## Scripts sueltos (desde la raíz del repo)
| Comprobación | Comando |
|---|---|
| Base de conocimiento: citas literales, cifras y **regla de precios P1–P6** (fuente con fecha, «confírmalo al reservar» en 4 idiomas) | `python3 berawa/build/check_kb.py` |
| 4 idiomas + chatbot contra la base | `python3 berawa/build/tests_cazorla.py URL salida.json --kb` |
| axe-core (6 etiquetas) + teclado | `python3 berawa/build/a11y_test.py URL salida.json` |
| Contraste de los nodos «incompletos» de axe | `python3 berawa/build/contrast_manual.py URL salida.json` |
| Claves del chat sin ambigüedad | `python3 berawa/build/keys_test.py URL` |
| Seguridad (estática + CSP efectiva) | `python3 berawa/build/sec_scan.py DIR URL salida.json` |
| ZIP determinista | `python3 berawa/build/pack_cazorla.py . dist/demo-cazorla-rural.zip` |

`URL` es p. ej. `http://127.0.0.1:8000/index.html` (tras `python3 -m http.server 8000` en la raíz) o `file:///…/index.html`.
Lighthouse (opcional, no incluido): `npx lighthouse@13.6.0 URL --preset=desktop` (o sin preset para móvil).

## Scripts de generación (procedencia)
`run_stage.py`, `cz_build.py`, `content_cazorla.py`, `knowledge_cazorla.py`, `make_kb_files.py`, `finalize_cazorla.py`. No hacen falta para verificar.
- `python3 berawa/build/run_stage.py kb a11y sec v1 --out=DIR` regenera `index.html`, `app.js` y `styles.css` en `DIR` (por defecto una carpeta temporal; nunca pisa el repo). Usa la plantilla base incluida en `vendor/webfactory/`. La salida es **idéntica byte a byte** a la entregada.
- `python3 berawa/build/make_kb_files.py` reescribe `berawa/knowledge.json`, `sources.json` y `evidence/source-text-*.json` desde `knowledge_cazorla.py` y el texto fuente guardado en el repo.
- `finalize_cazorla.py` (manifiesto de activos y `project.json`) necesita las fotos originales, que **no están en el repo**: `BERAWA_RAW=carpeta con assets.json y assets-raw/`. Sin esa variable termina con un mensaje claro.
