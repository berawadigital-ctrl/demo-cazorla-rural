# Prompt fijo para auditorías de Codex (Berawa)

Pegar tal cual en Codex, cambiando solo `{REPO}`, `{SHA}` y `{PR}`. No cambiar la redacción: el formato de salida es lo que Grok ejecuta.

````text
Usa $berawa-demo-qa para auditar el SHA {SHA} (40 caracteres) del repositorio {REPO} (PR {PR}) conforme a AGENTS.md y docs/BERAWA-QA-CHECKLIST.md.
No cambies el sitio, no hagas commits, no publiques, no envíes nada.
Si el SHA no es el último commit de la rama del PR, o no puedes comprobarlo, el dictamen es BLOQUEADA_POR_FALTA_DE_EVIDENCIA.

Devuelve EXACTAMENTE dos partes, en este orden:

PARTE 1 · INFORME PARA PERSONAS (markdown, en castellano)
- Identificadores: negocio, repositorio, URL publicada, PR, SHA auditado, fecha, auditor, entorno y versión del navegador.
- Dictamen: APROBADA_TECNICAMENTE | CORREGIR | RECHAZADA | BLOQUEADA_POR_FALTA_DE_EVIDENCIA.
- Tabla C01-C16: PASS | FAIL | NO_VERIFICADO, con evidencia (archivo:línea, comando reproducible, captura o URL).
- Resumen de 10 líneas como máximo, sin adornos.
- Si es una re-auditoría: estado de cada hallazgo anterior (RESUELTO | PERSISTE | EMPEORADO).

PARTE 2 · LISTA DE CORRECCIONES (un único bloque ```json, sin texto dentro ni después)
{
  "schema": "berawa-codex-audit/1",
  "repo": "{REPO}",
  "sha": "<40 caracteres>",
  "fecha": "<AAAA-MM-DDTHH:MM+01:00>",
  "dictamen": "APROBADA_TECNICAMENTE | CORREGIR | RECHAZADA | BLOQUEADA_POR_FALTA_DE_EVIDENCIA",
  "hallazgos": [
    {
      "id": "F-001",
      "severidad": "P0 | P1 | P2 | P3",
      "area": "repositorio | identidad | licencias | diseño | movil | escritorio | idiomas | chatbot | cta | aviso | seguridad | accesibilidad | entrega | rendimiento | otro",
      "control": "C01..C16",
      "archivo_o_selector": "ruta[:línea] o selector CSS o URL",
      "problema": "qué falla, en una frase comprobable",
      "criterio_de_aceptacion": "condición binaria que se puede cumplir o no (qué debe ser verdad para cerrarlo)",
      "como_verificarlo": "comando o pasos exactos y reproducibles",
      "evidencia": "lo que viste: salida, captura, línea"
    }
  ],
  "previos": [ { "id": "F-001", "estado": "RESUELTO | PERSISTE | EMPEORADO", "nota": "…" } ],
  "no_verificado": [ { "control": "C..", "motivo": "…" } ]
}

Reglas:
1. Un hallazgo = un problema = un criterio de aceptación medible. Nada de «mejorar», «revisar» o «considerar».
2. Conserva los id F-nnn de auditorías anteriores para el mismo problema; los nuevos siguen la numeración.
3. No pongas PASS sin evidencia: si no puedes comprobarlo, NO_VERIFICADO y va a «no_verificado».
4. No propongas cambiar datos comerciales (precios, direcciones, teléfonos, nombres) sin citar la fuente que los contradice.
5. P0 = bloquea enviar al cliente (legal, seguridad, datos falsos); P1 = rompe una función o un idioma; P2 = calidad visible; P3 = mejora.
6. Si hay algún P0 o P1 abierto, el dictamen no puede ser APROBADA_TECNICAMENTE.
7. La aprobación vale solo para el SHA indicado y caduca con cualquier commit posterior.
````

## Qué hace Grok con la respuesta
1. Valida que el JSON cumple el esquema y que `sha` coincide con el último commit.
2. Convierte cada `hallazgos[]` en un commit pequeño que cita su `id` y ejecuta `como_verificarlo`.
3. Anota en `CORRECCIONES.md`: problema, qué se hizo, cómo se comprobó (con la salida).
4. Pide la re-auditoría del nuevo SHA con este mismo prompt.
