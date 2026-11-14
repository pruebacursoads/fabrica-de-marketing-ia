---
name: fm-panel
description: Panel visual en vivo donde el emprendedor ve trabajar a cada agente de su equipo de marketing (estado, tarea, progreso, actividad y entregables). Define cómo se crea el panel en la carpeta de trabajo y el protocolo con el que el director y los agentes reportan su avance. Úsala cuando el director lance el equipo, cuando un agente deba reportar avance, o cuando el emprendedor pida "ver cómo trabajan los agentes", "el panel" o "la demo".
---

# Panel en vivo (fm-panel)

Es una página local (`Panel/index.html`) que se actualiza sola cada 2 segundos. No necesita servidor, internet ni instalar nada: se abre con doble clic (también funciona si se sirve desde `localhost`). Los agentes le informan escribiendo archivos pequeños en `Panel/estado/`.

## Crear el panel (lo hace el director, una vez por carpeta de trabajo)
1. **Encuentra esta skill.** Busca la carpeta `fm-panel` en este orden y usa la primera que exista:
   1. `<carpeta de trabajo>/.claude/skills/fm-panel/`
   2. `~/.claude/skills/fm-panel/` (Windows: `%USERPROFILE%\.claude\skills\fm-panel\`)
   3. Si ninguna existe, busca `fm-panel` dentro de la carpeta del paquete descomprimido (`modulos/base/skills/fm-panel/`).
2. **Copia a la carpeta de trabajo**, en `Panel/`: `panel/index.html` **y** `scripts/reportar.py` (queda `Panel/index.html` y `Panel/reportar.py`). Así los agentes siempre usan la misma ruta, estén las skills donde estén. Crea `Panel/estado/`.
3. **Detecta Python:** prueba `python --version`; si falla, `py -3 --version`; si falla, `python3 --version`. Usa el que responda (en adelante, `PY`). Si no hay ninguno, usa el **plan B sin Python** (más abajo) y no detengas el trabajo.
4. **Inicializa:** `PY Panel/reportar.py reiniciar`.
5. **Ábrelo para el alumno:** Windows `start "" "Panel\index.html"`, Mac `open Panel/index.html`, Linux `xdg-open Panel/index.html`. Dile: "Deja esta ventana visible, ahí verás a tu equipo trabajar. Si algo no se abre, pulsa **▶ Ver demo**."
6. Comprobación rápida: `PY Panel/reportar.py director --negocio "Prueba" --mensaje "Panel listo"` y confirma que se creó `Panel/estado/director.js`.

## Protocolo de reporte
Cada agente escribe **solo su propio archivo** (así 6 agentes en paralelo no se pisan). Desde la carpeta de trabajo:
```
PY Panel/reportar.py agente <id> --estado trabajando --tarea "Qué estoy haciendo" --progreso 35 --log "Frase corta"
PY Panel/reportar.py agente <id> --estado listo --progreso 100 --archivo "Entregables/2026-11-12-lanzamiento/anuncios/campana.md|Campaña de anuncios"
```
(`reportar.py` ya sabe que el panel es su propia carpeta; no hace falta `--panel`.)

IDs válidos: `estratega, oferta, imagenes, carruseles, video, anuncios, revisor`.
Estados: `espera`, `trabajando`, `listo`, `ajustando` (corrigiendo tras la revisión), `necesita-ayuda` (te falta un dato del alumno).

### Plan B sin Python
Escribe `Panel/estado/<id>.js` con exactamente este formato (una sola línea de datos; reescribe el archivo completo cada vez):
```
window.FM=window.FM||{};window.FM.agentes=window.FM.agentes||{};window.FM.agentes["estratega"]={"estado":"trabajando","tarea":"Armando calendario","progreso":35,"archivos":[],"log":[{"t":"10:02:11","m":"Definí 3 pilares"}]};
```
y `Panel/estado/director.js`:
```
window.FM=window.FM||{};window.FM.director={"negocio":"Mi negocio","etapas":["listo","listo","listo","en-curso","pendiente","pendiente"],"mensaje":"Producción en paralelo","log":[{"t":"10:00:00","ag":"Director","m":"Lancé 6 agentes"}]};
```

### El director
```
PY Panel/reportar.py director --negocio "Nombre del negocio" --etapa 4 --estado-etapa en-curso --mensaje "Producción en paralelo" --log "Lancé 6 agentes"
```
Etapas: 1 Diagnóstico · 2 ADN de marca · 3 Plan · 4 Producción en paralelo · 5 Revisión · 6 Entrega. Al marcar una etapa, las anteriores quedan en "listo".

## Reglas
- Reporta **al empezar**, **en cada hito** (máx. 1 vez cada ~20 s) y **al terminar** con los archivos. Frases cortas, en lenguaje de emprendedor ("Escribiendo los títulos del anuncio"), sin jerga.
- Las rutas de `--archivo` son relativas a la carpeta de trabajo (la que contiene `Panel/`).
- Nunca escribas datos sensibles (claves, teléfonos de clientes) en el panel.
- Si el panel falla, **no detengas el trabajo**: el panel es un extra, el entregable es lo importante.
- Modo demo: `Panel/index.html?demo=1` o el botón "Ver demo" muestra al equipo trabajando con datos de ejemplo (ideal para clases).
