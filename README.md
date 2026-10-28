# Cazorla Rural · propuesta de rediseño (demo)

**Propuesta de rediseño independiente, no oficial.** Hecha por Berawa sin encargo del negocio. No es la web de Cazorla Rural ni está afiliada a ella. Lleva `noindex`.

Sitio estático (HTML + CSS + JS, sin servidor ni APIs ni servicios de terceros) en español, catalán, inglés y francés, con un asistente local que responde solo con datos publicados en cazorlarural.com (`berawa/knowledge.json`, con la fuente y una cita literal por respuesta).

## Ver en local
```
python3 -m http.server 8000      # y abrir http://localhost:8000
```
También funciona abriendo `index.html` directamente. Detalle de instalación en `INSTALACION.md`.

## Trazabilidad
- `berawa/project.json`: datos del negocio, nota de Maps (con fecha), estado de las auditorías.
- `berawa/sources.json` y `berawa/knowledge.json`: de dónde sale cada dato y cada respuesta del chat (lectura del 27/10/2026).
- `berawa/asset_manifest.json` y `LICENSES.md`: cada foto y fuente con autor, licencia, hash y evidencia.
- `berawa/V1.0-CAMBIOS.md`: cambios de la V1.0, separados de los de la auditoría.
- `CORRECCIONES.md` (solo en el repositorio, no va en el ZIP): cada problema de la auditoría de Codex, qué se hizo y cómo se comprobó.
