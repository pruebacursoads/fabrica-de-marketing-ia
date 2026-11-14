# Por dentro (para mantener y ampliar el paquete)

## Mapa
```
fm-director ──► fm-diagnostico ─► Mi negocio/diagnostico-situacional.md
            ├─► fm-adn         ─► Mi negocio/adn-de-marca.md
            ├─► plan en tabla  (aprobación del alumno)
            ├─► agentes en paralelo (fm-agente-*)  ──► Entregables/<tema>/<área>/
            │        estratega · oferta · imagenes · carruseles · video · anuncios
            ├─► fm-agente-revisor ─► revision-final.md
            └─► 00-LEEME-PRIMERO.md + aprendizajes.md
                         ▲
                fm-panel (Panel/index.html + estado/*.js) ◄── todos reportan
```

## Panel en vivo
- **v1.1:** `Panel/index.html` tiene dos pestañas. **Oficina**: escena **3D isométrica en CSS puro** (sin librerías ni internet): suelo continuo, paredes con ventanas, alfombras por zona con el nombre pintado en el piso y letreros en la pared, escritorios y sillas como cajas 3D; los personajes son "carteles" que se contra-rotan para quedar de pie frente a la cámara (`transform: rotateZ(45deg) rotateX(-58deg)` sobre el origen en los pies). **Guía de generación**: pasos con prompt + botón copiar, referencias en orden (con miniatura), cuadro para soltar archivos, vista previa del imagen/video recibido y veredicto de Claude.
- `scripts/servidor.py` (stdlib): sirve la carpeta de trabajo en `127.0.0.1`, recibe subidas (`POST /api/subir?slot=<paso>`, cabecera `X-FM: 1`, solo dentro de `Entregables/` y `Mi negocio/`, extensiones permitidas, 1 GB), soporta `Range` para adelantar videos, archiva la versión anterior en `_anteriores/` y reescribe `estado/medios.js` cada 2 s (detecta también lo copiado a mano). `scripts/vigilar.py` imprime una línea por archivo nuevo para que Claude lo lea en tiempo real con la herramienta Monitor.
- **Guía:** cada agente escribe `guia.json` → `reportar.py guia <id> --desde … --md …` (valida, guarda `estado/guia-<id>.json`, regenera `guia.js` y el `.md`). Claude devuelve veredictos con `reportar.py revision --slot … --estado ok|repetir|revisando`.
- `Panel/index.html` es estático. Cada 2 s inyecta `<script src="estado/<id>.js">` para `director` y los 7 agentes; cada archivo asigna `window.FM...`. Así funciona abierto con doble clic (`file://`) y sin servidor.
- **Un archivo por agente** → cero conflictos en paralelo. `scripts/reportar.py` escribe de forma atómica (`.tmp` + `os.replace`) y conserva el historial (30 eventos).
- Sin Python, el agente reescribe su archivo con el formato documentado en `fm-panel/SKILL.md`.
- Modo demo: `?demo=1` o botón; la línea de tiempo está en `DEMO_AG` dentro del HTML.
- Para cambiar el roster, edita `AGENTES` en `index.html` y `IDS` en `reportar.py`.
- **Oficina animada:** el movimiento de los personajes se **deriva del estado**, sin cambiar el protocolo. Etapa 3 (Plan) y etapa final → todos a la sala de reuniones (en la final celebran con confeti); etapa 4 → cada uno en su estudio, tecleando mientras `trabajando`; al pasar a `listo` el agente camina al escritorio del director y entrega; cuando `video` o `anuncios` empiezan, `imagenes` / `oferta` les llevan material (`COLLAB`); en la etapa 5 la revisora recorre los escritorios. Las salas, escritorios y asientos están en `SALAS`, `AGENTES[].seat/desk/meet`; los nombres y roles de los personajes, en `AGENTES` y `DIRECTOR`.

## Agentes
- Viven en `agentes/*.md` y se instalan en `~/.claude/agents/`. El director los lanza con varias llamadas a `Agent` en **un solo mensaje** (paralelo real). Si la herramienta no permite subagentes, el director ejecuta las instrucciones una tras otra.
- Los agentes **no preguntan al alumno**: leen el ADN, el diagnóstico y `aprendizajes.md`, y devuelven Supuestos y Faltantes.
- Generados con un script desde una plantilla común; el protocolo común (leer ADN, reportar al panel, claims, devolver resumen) está al final de cada archivo.

## Mantener Meta Ads al día
1. Edita `modulos/anuncios/skills/meta-ads-andromeda/references/estado-vigente.md`: actualiza la fecha, la tabla y las fuentes.
2. Etiquetas: OFICIAL (Meta, WhatsApp Business o esquema de la API) · SECUNDARIA (blogs) · NO VERIFICADO · HEURÍSTICA.
3. Puntos pendientes al 2026-11-12: cantidad exacta de clientes/pedidos para habilitar "compras por mensajes" (hoy ~10, observado), ruta exacta del "uso compartido de datos" de WhatsApp, límites del impulso de la entrega por anuncio y detalle de las campañas Advantage+ de ventas. Ya confirmados con capturas de un Administrador real: impulso de la entrega por anuncio, objetivo de compras por mensajes y que el objetivo de rendimiento no se edita tras publicar.
4. Si cambia una regla, ajusta también `SKILL.md` (Fase 5) y `fm-agente-anuncios.md`/`fm-agente-revisor.md`.

## Lecciones de clientes incorporadas (sin datos de clientes)
Marca propia por negocio · claims Nivel A y políticas de Meta · estructura de video ganadora (gancho 2 s, ≤ 30 s, prueba visual, cobertura siempre visible) · reglas de Omni Flash (@me, ligero, sin texto/música) · referencias exactas por pieza · propuesta antes de producir · convención de nombres para cruzar anuncios con ventas · privacidad de datos y claves.

## Probar una instalación sin tocar tu equipo
`.\instalar.ps1 -Destino C:\ruta\de\prueba` (Windows) · `bash instalar.sh --destino /ruta/de/prueba` (Mac/Linux).

## Pendientes conocidos
- Probar el recorrido completo con un alumno real y en equipo limpio (Windows 10/11, Mac, 8 GB).
- Landing, CRM de WhatsApp y dashboard de ventas: existen como plantillas aparte; falta decidir cómo se entregan (repos plantilla) y documentarlo.
- Publicar la guía visual (artifact) del paquete y subir el ZIP.
