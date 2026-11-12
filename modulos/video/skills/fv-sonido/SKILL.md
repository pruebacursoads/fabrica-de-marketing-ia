---
name: fv-sonido
description: Audio profesional con la voz REAL del emprendedor. Limpia la voz (ruido de sala, claridad, volumen parejo), genera efectos de sonido y música simple propios sin derechos de autor, y mezcla todo con la música bajando cuando hablas y volumen final de -14 LUFS para Instagram, TikTok y Shorts. Úsala cuando el alumno diga "se oye mal mi audio", "ponle música", "quiero efectos", o después de construir el video.
---

# Sonido

`<SKILLS>` = `%USERPROFILE%\.claude\skills` (Windows) o `~/.claude/skills` (Mac/Linux). **La voz es la del alumno: no se reemplaza ni se imita con IA.**

## 1. Limpiar la voz
```bash
python "<SKILLS>/fv-sonido/scripts/limpiar_voz.py" assets/base.mp4 assets/voz_limpia.wav --nivel normal
```
| Nivel | Cuándo |
|---|---|
| `suave` | Audio ya bueno (micrófono de solapa, cuarto tranquilo) |
| `normal` | Lo habitual: quita ruido de sala, aclara y parejo el volumen |
| `fuerte` | Eco, oficina, celular lejos. Puede sonar algo "seco": avísalo |

Entrada puede ser el video montado o la voz suelta. Ningún filtro arregla una grabación mala: si hay mucho ruido, recomienda regrabar con el celular cerca de la boca.

## 2. Efectos y música propios
```bash
python "<SKILLS>/fv-sonido/scripts/generar_sonidos.py" efectos assets/sfx
python "<SKILLS>/fv-sonido/scripts/generar_sonidos.py" musica calma 32 assets/musica.wav
```
- Efectos: `uiclick, whoosh, impact, riser, glitch, chime`. El motor (`construir.py`) ya decide cuándo suena cada uno y los guarda en `sfx_eventos.json`.
- Música: `calma` o `energia`, de la duración del video. **Es simple (fondo suave), no una canción.** Dilo con honestidad. Si el alumno tiene música con licencia, úsala en su lugar.
- Para videos con mucha voz, música `calma` bajita o ninguna.

## 3. Mezclar
Crea `mezcla.json`:
```json
{"dur": 31.2, "voz": "assets/voz_limpia.wav", "musica": "assets/musica.wav", "efectos_dir": "assets/sfx",
 "eventos": "sfx_eventos.json", "salida": "assets/mix.wav", "pico_voz": -3, "pico_musica": -25}
```
```bash
python "<SKILLS>/fv-sonido/scripts/mezclar.py" mezcla.json
```
- `musica: null` para no usar música. `riser` opcional antes del cierre.
- La música baja sola cuando hablas (ducking). El máster queda en ≈ −14 LUFS con pico ≤ −1,5 dB; el script imprime el valor medido.
- El plan del editor debe apuntar a `"audio": "assets/mix.wav"`.

## 4. Revisar
- Imprime y comprueba el LUFS (entre −15 y −13 está bien).
- Pide al alumno que **escuche con audífonos** el primer minuto: voz clara, música que no tapa, efectos discretos. Ajusta `pico_musica` (más bajo = más discreta) o `pico_voz` según su oído.

## Errores típicos
- *Voz con "burbujeo"*: bajar de `fuerte` a `normal`.
- *Música tapa palabras*: bajar `pico_musica` a −28.
- *Se oye saturado*: la grabación original estaba saturada; usar `suave` y avisar.
