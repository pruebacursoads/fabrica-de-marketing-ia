---
name: fv-medios
description: Recibe y prepara los materiales del emprendedor. Analiza los archivos que entrega (un video con audio, varios clips, o clips más la voz real por separado), los une de forma profesional en 1080x1920 a 30 fps igualando formato y volumen, monta los clips sobre la voz real, quita silencios y transcribe con el segundo de cada palabra. Úsala cuando el alumno comparta videos, clips, audios o diga "te paso mis tomas".
---

# Medios: analizar, unir y transcribir

`<SKILLS>` = `%USERPROFILE%\.claude\skills` (Windows) o `~/.claude/skills` (Mac/Linux). El proyecto vive en `Reels/<fecha-tema>/` con `assets/` y `trabajo/`. La **voz es siempre real**.

## 1. Analizar lo que entregó
```bash
python "<SKILLS>/fv-medios/scripts/analizar_medios.py" Tomas --salida trabajo
```
Da: tamaño, orientación, fps, duración, volumen y la **ruta sugerida** (un video, varios clips con audio, o voz separada). Genera `trabajo/hojas/*.jpg` (6 fotogramas por clip): **mírelas** para entender qué se ve en cada clip.
Avisos típicos: orientaciones mezcladas, fps distintos, audio muy bajo o saturado, resolución baja (<720 px: no hacer zoom fuerte).

## 2. Acordar con el alumno
Pregunta (con opciones) lo que no sea obvio: **cuál archivo es la voz principal**, **el orden de los clips**, si hay **música suya**, y si los clips horizontales se **recortan** o se muestran **enteros sobre fondo desenfocado**.

## 3. Elegir la ruta
### A) Un solo video con su audio
Opcional, quitar silencios (pausas largas): 
```bash
python "<SKILLS>/fv-medios/scripts/quitar_silencios.py" Tomas/video.mp4 --salida trabajo/montaje.json --destino assets/base.mp4 --min 0.45
python "<SKILLS>/fv-medios/scripts/montar.py" trabajo/montaje.json
```
Si ahorra menos del 5 %, no vale la pena: usa el video tal cual (`montar.py` con un solo segmento para dejarlo en 1080x1920 y con cola).

### B) Varios clips con audio propio
Escribe `trabajo/montaje.json` con los clips en orden y `"audio": {"fuente": "clips", "normalizar": true}` (iguala el volumen de cada clip). `"xfade": 0.25` agrega fundidos suaves; `0` = corte directo (más dinámico para videos de ritmo rápido).

### C) Voz real separada + clips (b-roll)
1. **Transcribe primero la voz** (paso 4).
2. Lee `frases.txt` y las hojas de cada clip. Propón qué clip se ve en cada tramo de la voz (por significado: el clip que ilustra lo que se dice). Muéstrale al alumno la tabla `segundo → clip` y espera su visto bueno.
3. Escribe `montaje.json` con `"audio": {"fuente": "ruta/voz.wav"}`, la lista de segmentos (cada uno `archivo`, `ini`, `fin`) y `"cola": 1.3`. La suma de los clips debe alcanzar la duración de la voz (si falta, `montar.py` congela el último fotograma; si sobra, recorta).
4. `python "<SKILLS>/fv-medios/scripts/montar.py" trabajo/montaje.json`

Formato de `montaje.json` (rutas relativas a su carpeta):
```json
{"salida":"assets/base.mp4","encuadre":"cubrir","audio":{"fuente":"Tomas/voz.wav"},"xfade":0,"cola":1.3,
 "segmentos":[{"archivo":"Tomas/clip1.mp4","ini":0,"fin":5.2},{"archivo":"Tomas/clip2.mp4","ini":1,"fin":4}]}
```
`encuadre`: `cubrir` (llena la pantalla recortando) o `contener-difuminado` (clip entero sobre fondo desenfocado).

## 4. Transcribir
```bash
python "<SKILLS>/fv-medios/scripts/transcribir.py" assets/voz_o_video.ext --salida . --idioma es --prompt "marca, siglas, nombres propios, términos del negocio"
```
- `--modelo auto` (por defecto) elige según la memoria: `base` (<8 GB), `small` (<12 GB), `medium` (más). `medium` corrige mucho más pero necesita ~4 GB libres y tarda.
- El **prompt con el vocabulario** del alumno mejora siglas y nombres (ej. "RUC 10, RUC 20, TikTok, Google Flow").
- Entrega `words.json` (para los subtítulos), `transcripcion.txt` y `frases.txt`.
- **Revisa la transcripción y pregunta** lo dudoso (cifras, siglas, nombres). Si una palabra sale mal, corrígela en `words.json` y conserva los tiempos.

## 5. Antes de pasar al editor
- `assets/base.mp4` existe, es 1080x1920, 30 fps, y dura la voz + cola.
- `words.json` revisado.
- Anota la duración total: es `duracion` del plan.

## Errores típicos
- *Clip girado*: ffmpeg lo endereza solo; si no, revisar `rotacion` en `medios.json`.
- *Voz y video desfasados*: en la ruta C la voz manda; en la ruta B se usa el audio del propio clip.
- *Audio saturado*: pedir una toma nueva o usar `fv-sonido` con nivel `fuerte`.
