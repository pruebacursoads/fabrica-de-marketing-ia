---
name: fm-panel
description: Panel visual en vivo donde el emprendedor ve trabajar a cada agente de su equipo de marketing (estado, tarea, progreso, actividad y entregables). Define cómo se crea el panel en la carpeta de trabajo y el protocolo con el que el director y los agentes reportan su avance. Úsala cuando el director lance el equipo, cuando un agente deba reportar avance, o cuando el emprendedor pida "ver cómo trabajan los agentes", "el panel" o "la demo".
---

# Panel en vivo (fm-panel)

Es una página local (`Panel/index.html`) que se actualiza sola cada 2 segundos. No necesita servidor, internet ni instalar nada: se abre con doble clic. Los agentes le informan escribiendo archivos pequeños en `Panel/estado/`.

## Crear el panel (lo hace el director, una vez por carpeta de trabajo)
1. Ubica esta skill: `~/.claude/skills/fm-panel/` (en Windows `%USERPROFILE%\.claude\skills\fm-panel\`).
2. Copia `panel/index.html` a `<carpeta de trabajo>/Panel/index.html` y crea `Panel/estado/`.
3. Inicializa: `python <skill>/scripts/reportar.py --panel Panel reiniciar` (en Windows, si `python` no existe, `py -3`). Si no hay Python, escribe `Panel/estado/director.js` a mano con el formato de abajo.
4. Ábrelo para el alumno: Windows `start "" "Panel\index.html"`, Mac `open Panel/index.html`, Linux `xdg-open Panel/index.html`. Dile: "Deja esta ventana visible, ahí verás a tu equipo trabajar. Si algo no se abre, pulsa **▶ Ver demo**."

## Protocolo de reporte
Cada agente escribe **solo su propio archivo** (así 6 agentes en paralelo no se pisan). Con Python:
```
python reportar.py --panel Panel agente <id> --estado trabajando --tarea "Qué estoy haciendo" --progreso 35 --log "Frase corta"
python reportar.py --panel Panel agente <id> --estado listo --progreso 100 --archivo "Entregables/2026-11-12-lanzamiento/anuncios/campana.md|Campaña de anuncios"
```
IDs válidos: `estratega, oferta, imagenes, carruseles, video, anuncios, revisor`.
Estados: `espera`, `trabajando`, `listo`, `ajustando` (corrigiendo tras la revisión), `necesita-ayuda` (te falta un dato del alumno).

Sin Python, escribe `Panel/estado/<id>.js` con exactamente este formato (una sola línea de datos, reescribe el archivo completo):
```
window.FM=window.FM||{};window.FM.agentes=window.FM.agentes||{};window.FM.agentes["estratega"]={"estado":"trabajando","tarea":"Armando calendario","progreso":35,"archivos":[],"log":[{"t":"10:02:11","m":"Definí 3 pilares"}]};
```

### El director
```
python reportar.py --panel Panel director --negocio "Nombre del negocio" --etapa 4 --estado-etapa en-curso --mensaje "Producción en paralelo" --log "Lancé 6 agentes"
```
Etapas: 1 Diagnóstico · 2 ADN de marca · 3 Plan · 4 Producción en paralelo · 5 Revisión · 6 Entrega. Al marcar una etapa, las anteriores quedan en "listo".

## Reglas
- Reporta **al empezar**, **en cada hito** (máx. 1 vez cada ~20 s) y **al terminar** con los archivos. Frases cortas, en lenguaje de emprendedor ("Escribiendo los títulos del anuncio"), sin jerga.
- Las rutas de `--archivo` son relativas a la carpeta de trabajo (la que contiene `Panel/`).
- Nunca escribas datos sensibles (claves, teléfonos de clientes) en el panel.
- Si el panel falla, **no detengas el trabajo**: el panel es un extra, el entregable es lo importante.
- Modo demo: `Panel/index.html?demo=1` o el botón "Ver demo" muestra al equipo trabajando con datos de ejemplo (ideal para clases).
