---
name: fm-panel
description: Panel visual en vivo (oficina 3D con el equipo de agentes) y Guía de generación donde el emprendedor ve los prompts listos para copiar, las referencias en orden y sube sus archivos (se guardan solos en su computadora y Claude los revisa en tiempo real). Define cómo se crea y abre el panel, el protocolo de reporte de los agentes, el formato de la guía y cómo vigilar lo que el alumno sube. Úsala cuando el director lance el equipo, cuando un agente deba reportar o publicar su guía, cuando el alumno suba un archivo, o cuando pida "el panel", "dónde están los prompts" o "la demo".
---

# Panel en vivo (fm-panel) · v1.1

`Panel/index.html` tiene dos pestañas: **🏢 Oficina** (el equipo trabajando, en 3D) y **🎬 Guía de generación** (prompts para copiar, referencias en orden, cuadros para subir archivos y el veredicto de Claude). Se actualiza solo cada 2 s. Los agentes escriben archivos pequeños en `Panel/estado/`.

Dos formas de abrirlo:
- **Con servidor (recomendada):** `python Panel/servidor.py` (o doble clic en `Panel/ABRIR-PANEL.bat`) → abre `http://localhost:8765/Panel/index.html`. Habilita **subir archivos arrastrándolos** (se guardan en la carpeta correcta con el nombre correcto), vista previa de videos y detección de archivos copiados a mano.
- **Sin servidor:** doble clic en `Panel/index.html`. Se ve todo; si el servidor está encendido, la página **pasa sola** a la versión con subida. Si no, para subir hay que copiar los archivos a la carpeta que indica cada paso y pedirle a Claude `reportar.py medios`.

## Crear el panel (lo hace el director, una vez por carpeta de trabajo)
1. **Encuentra esta skill:** `<carpeta de trabajo>/.claude/skills/fm-panel/` → `~/.claude/skills/fm-panel/` (Windows: `%USERPROFILE%\.claude\skills\fm-panel\`) → `modulos/base/skills/fm-panel/` del paquete descomprimido.
2. **Copia a `Panel/`:** `panel/index.html` y **todo `scripts/`** (`reportar.py`, `servidor.py`, `vigilar.py`, `ABRIR-PANEL.bat`, `ABRIR-PANEL.sh`). Queda `Panel/index.html`, `Panel/reportar.py`… y crea `Panel/estado/`.
3. **Detecta Python:** `python --version` → `py -3 --version` → `python3 --version`. Usa el que responda (`PY`). Si no hay ninguno: **plan B sin Python** (abajo) y sin subida de archivos.
4. **Inicializa:** `PY Panel/reportar.py reiniciar`.
5. **Ábrelo con servidor y en segundo plano:** ejecuta `PY Panel/servidor.py --no-abrir` en segundo plano (Bash `run_in_background`), lee la URL de `Panel/estado/servidor.json` y ábrela para el alumno (navegador integrado de la app, o `start "" "<url>"`). Dile: *"Deja esta ventana visible: ahí ves a tu equipo trabajar y ahí te voy a dejar tus prompts para copiar y donde arrastrar tus archivos. Cuando quieras, doble clic en `Panel/ABRIR-PANEL.bat` para abrirlo tú."*
6. Comprobación: `PY Panel/reportar.py director --negocio "Prueba" --mensaje "Panel listo"` y confirma `Panel/estado/director.js`.

## Protocolo de reporte (agentes y director)
Cada agente escribe **solo sus propios archivos**. Desde la carpeta de trabajo:
```
PY Panel/reportar.py agente <id> --estado trabajando --tarea "Qué estoy haciendo" --progreso 35 --log "Frase corta"
PY Panel/reportar.py agente <id> --estado listo --progreso 100 --archivo "Entregables/2026-11-12-lanzamiento/anuncios/campana.md|Campaña de anuncios"
PY Panel/reportar.py director --negocio "Nombre" --etapa 4 --estado-etapa en-curso --mensaje "Producción en paralelo" --log "Lancé 6 agentes"
```
IDs: `estratega, oferta, imagenes, carruseles, video, anuncios, revisor`. Estados: `espera`, `trabajando`, `listo`, `ajustando`, `necesita-ayuda`. Etapas: 1 Diagnóstico · 2 ADN · 3 Plan · 4 Producción · 5 Revisión · 6 Entrega.
Reglas: reporta al empezar, en cada hito (máx. 1 vez cada ~20 s) y al terminar con archivos; frases cortas de emprendedor; rutas de `--archivo` relativas a la carpeta de trabajo; nunca claves ni teléfonos en el panel; si el panel falla, **no detengas el trabajo**.

## La Guía de generación (un paso a la vez, para una persona NO técnica)
Todo lo que el alumno deba **generar, subir o pegar** se publica aquí. En el panel ve **un solo paso grande a la vez** (con una fila de círculos 1, 2, 3… para saber dónde va); al recibir su archivo pasa solo al siguiente. Cada agente escribe un `guia.json` y lo publica:
```
PY Panel/reportar.py guia video --desde Entregables/<tema>/video/guia.json --md Entregables/<tema>/video/05-guia-de-generacion.md
```
### Reglas de redacción (obligatorias; el comando las valida)
- **Máximo 8-10 pasos.** Fusiona pasos; si una foto real del alumno sirve tal cual, no le pidas generar otra imagen.
- **`titulo` = una acción corta** (≤ 70 caracteres): «Crea la imagen de tu tienda», «Toma 1 · Entras al local (4 s)».
- **`hacer` = 1-2 frases simples (≤ 280 caracteres)** que dicen qué hace el alumno. Sin jerga: no escribas «plano», «push in», «POV», «contrapicado», «referencias» sin traducirlo («la cámara se acerca», «sube estas imágenes»). La jerga técnica va **solo dentro del prompt**.
- Nombres de `refs` cortos (≤ 70): «Imagen de tu tienda», «Tu avatar».
- **Lo largo va en `ayuda`** (por qué, consejos, qué hacer si falla); el alumno lo abre solo si quiere. Nunca pongas párrafos en `hacer`.
- Una sola variante de prompt por caja: si hay opciones (con foto / sin foto), usa `alternativas`.
### Formato (`guia.json`)
```json
{"titulo":"Video de 20 s","orden":1,"pasos":[
 {"id":"vid-fotos","fase":"material","titulo":"Pásame 3 fotos reales de tu local",
  "hacer":"Tómalas con el celular, en vertical y con la luz normal del lugar. Sin filtros.",
  "salida":"Mi negocio/fotos-producto/","multiple":true},
 {"id":"vid-escena","fase":"imagenes","titulo":"Crea la imagen de tu local",
  "hacer":"Sube tu foto a la herramienta y pega el texto. Te devuelve tu local mejorado, en vertical.",
  "herramienta":"Nano Banana 2 o GPT Image 2.6","enlace":"https://gemini.google.com",
  "refs":[{"nombre":"Tu foto real del local","slot":"vid-fotos"}],
  "prompt_titulo":"Con tu foto real","prompt":"Usa la imagen adjunta como escena exacta…",
  "alternativas":[{"titulo":"Sin foto (PROPUESTA)","prompt":"…"}],
  "salida":"Entregables/<tema>/video/imagenes/escena.png",
  "revisar":["Se reconoce como TU local","Sin muebles inventados"],"ayuda":"Si sale distinta, repite con la misma foto."},
 {"id":"vid-toma-01","fase":"clips","titulo":"Toma 1 · Entras al local (4 s)",
  "hacer":"En Google Flow carga tu avatar y la imagen del local. Pega el texto y genera.",
  "herramienta":"Google Flow","enlace":"https://labs.google/fx/tools/flow","palabras":"6 palabras · 4 s",
  "refs":[{"nombre":"Tu avatar (@me)","tipo":"avatar"},{"nombre":"Imagen de tu local","slot":"vid-escena"}],
  "prompt":"@me …","salida":"Entregables/<tema>/video/clips/toma-01.mp4","revisar":["Tu voz y la frase completa","Sin texto ni música"]},
 {"id":"vid-fin","fase":"edicion","titulo":"Cuando tengas todo, avísame","hacer":"Escríbele esta frase a Claude y pasamos a la edición.","decir":"Ya subí todas las tomas, pasa a la edición."}
]}
```
Campos: `id` (minúsculas, números, guiones; **único en todo el panel**, con prefijo de tu área: `vid-`, `img-`, `car-`, `ads-`), `fase` (`material`, `imagenes`, `clips`, `edicion`, `otro`), `titulo`, `hacer`, `ayuda`, `herramienta`, `enlace` (genera el botón grande «Abrir…»), `formato`, `duracion`, `refs` (**en el orden de carga**; `nombre`, y opcional `slot` para mostrar la miniatura del archivo de otro paso, `archivo` o `tipo:"avatar"`), `prompt` (completo, pegable) + `prompt_titulo`, `alternativas` (`[{titulo, prompt}]`), `palabras`, `revisar` (lista corta; lo revisa Claude por el alumno), `decir` (frase que el alumno copia y le dice a Claude), `salida` (ruta relativa que **empieza por `Entregables/` o `Mi negocio/`**; si termina en `/` y `multiple:true`, recibe varios archivos; sin `salida` el paso es solo informativo), `multiple`.
El comando valida el JSON (y rechaza textos largos), escribe `Panel/estado/guia-<id>.json`, regenera `guia.js` y, con `--md`, escribe la misma guía en Markdown. **El prompt vive solo en la guía.**

### En el chat: un paso a la vez, nunca el listado
El chat es la conversación; el panel es el tablero. Cuando toque un paso, escribe **solo ese paso**, en 3-4 líneas: qué hace («Paso 3 de 10: crea la imagen de tu tienda»), con qué herramienta (enlace), **el prompt dentro de un bloque de código** (para copiarlo desde el chat) y «cuando lo tengas, arrástralo al cuadro del paso 3 del panel». Cuando llegue el archivo (vigilar.py), responde con el veredicto en una frase y presenta el siguiente. No pegues la lista completa de pasos ni todos los prompts juntos.

## Lo que sube el alumno y cómo lo lees en tiempo real
- Al arrastrar un archivo a un paso, `servidor.py` lo guarda en `salida` con el nombre del paso (si hay una versión previa, pasa a `_anteriores/`) y actualiza `Panel/estado/medios.js`. Si copia el archivo a mano a esa carpeta, también se detecta (el servidor revisa cada 2 s).
- **Vigila en segundo plano** apenas publiques una guía: con la herramienta **Monitor** ejecuta `PY Panel/vigilar.py` (imprime `SUBIDA paso=<id> archivo=<ruta> tam=…MB` por cada archivo nuevo ya copiado completo). Cada línea te llega como aviso: **abre el archivo y revísalo** (imágenes: mírala; video: `ffprobe`, fotogramas con ffmpeg, transcripción con Whisper si existe). Si tu herramienta no tiene Monitor, pídele al alumno «avísame cuando subas algo» y ejecuta `PY Panel/vigilar.py --una-vez`.
- **Devuelve el veredicto al panel**, que lo muestra en la tarjeta del paso:
```
PY Panel/reportar.py revision --slot vid-toma-01 --estado revisando --nota "Mirándolo ahora"
PY Panel/reportar.py revision --slot vid-toma-01 --estado ok --nota "Voz y ropa bien; encuadre distinto al anterior"
PY Panel/reportar.py revision --slot vid-toma-01 --estado repetir --nota "Dice 'WhatsApp' en vez de 'por aquí'; regenera con la frase literal"
```
  Y dilo también en el chat en una frase. Cuando todos los pasos de clips estén en `ok`, pasa a la edición.
- Para fotos de `material`: mira cada foto y dile al alumno qué sirve y qué falta (frente, interior, producto, vertical, nítida).

## Plan B sin Python
Escribe `Panel/estado/<id>.js` (una línea; reescríbelo completo cada vez):
```
window.FM=window.FM||{};window.FM.agentes=window.FM.agentes||{};window.FM.agentes["estratega"]={"estado":"trabajando","tarea":"Armando calendario","progreso":35,"archivos":[],"log":[{"t":"10:02:11","m":"Definí 3 pilares"}]};
```
y `Panel/estado/director.js`:
```
window.FM=window.FM||{};window.FM.director={"negocio":"Mi negocio","etapas":["listo","listo","listo","en-curso","pendiente","pendiente"],"mensaje":"Producción en paralelo","log":[{"t":"10:00:00","ag":"Director","m":"Lancé 6 agentes"}]};
```
Sin Python no hay subida desde el panel ni `guia.js` automático: en ese caso entrega los prompts **en el chat y en un `.md`** (nunca solo "en la carpeta") y pide al alumno que copie sus archivos a las rutas indicadas.

## Reglas
- Nunca escribas datos sensibles en el panel. El servidor solo escucha en `127.0.0.1`, solo escribe en `Entregables/` y `Mi negocio/`, y acepta solo imágenes, video, audio, pdf y texto (máx. 1 GB).
- Modo demo: `Panel/index.html?demo=1` o el botón «Ver demo» muestra al equipo trabajando y una guía de ejemplo (ideal para clases).
- Si el alumno pregunta «¿dónde están los prompts?»: abre la pestaña **Guía de generación** (`#guia`), y además pégale en el chat el prompt del paso que toca.
