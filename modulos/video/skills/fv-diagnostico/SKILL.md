---
name: fv-diagnostico
description: Revisa la computadora del emprendedor (memoria, disco, ffmpeg, Node.js, Python, Whisper, Chrome), explica en lenguaje simple qué falta y para qué sirve, e instala lo que falte con su permiso. Decide el modo normal o ligero según la memoria. Úsala al empezar con la Fábrica de Video, cuando un comando no se reconozca (ffmpeg, npx), cuando un render se cierre solo o cuando el alumno diga "no me funciona".
---

# Diagnóstico del equipo

`<SKILLS>` = `%USERPROFILE%\.claude\skills` en Windows, `~/.claude/skills` en Mac/Linux.

## 1. Revisar
```bash
python "<SKILLS>/fv-diagnostico/scripts/diagnostico.py" --json "Reels con Claude/diagnostico.json"
```
No instala nada. Muestra ✅/❌ por herramienta, el modo recomendado y los comandos de instalación.

## 2. Explicar (sin jerga)
| Herramienta | Qué decirle al alumno |
|---|---|
| ffmpeg | "El programa que corta, une y limpia el audio y el video." |
| Node.js | "El motor que hace funcionar HyperFrames, la herramienta que arma el video." |
| Python | "Ejecuta los scripts de la Fábrica." |
| Whisper | "Escucha tu voz y escribe el texto con el segundo de cada palabra." |
| Chrome | "HyperFrames lo usa para dibujar los fotogramas y para revisar que nada se pise." |
| HyperFrames | "Lo creó HeyGen y es gratis y de código abierto. No necesitas cuenta de HeyGen." (se descarga solo con `npx`) |

## 3. Instalar (con permiso, uno por uno)
- Pregunta antes de cada instalación y muestra el comando exacto.
- **Windows** (`winget`): `winget install --id Gyan.FFmpeg -e` · `winget install OpenJS.NodeJS.LTS` · `winget install Python.Python.3.11` · `winget install Google.Chrome` · `pip install openai-whisper`
- **Mac** (`brew`): `brew install ffmpeg node python@3.11` · `brew install --cask google-chrome` · `pip3 install openai-whisper`. Si no tiene Homebrew, **no ejecutes tú el instalador**: dale la instrucción oficial de brew.sh para que la pegue en la Terminal.
- Usa solo instaladores oficiales. Nada de descargas de sitios desconocidos.
- Después de instalar ffmpeg o Node: **cerrar y abrir la terminal y la app**, y volver a ejecutar el diagnóstico.
- Whisper descarga un modelo la primera vez (140 MB a 1,4 GB). Avisa que tarda.
- HyperFrames no se instala aparte: `npx --yes hyperframes doctor` lo descarga. Las marcas rojas de whisper-cpp, Kokoro, MusicGen y Docker en `doctor` son opcionales: ignóralas.

## 4. Modo normal o ligero
- **Ligero** si la memoria total es menor de 12 GB: transcripción `base`/`small`, render en `--borrador` para probar y 1 proceso, videos de hasta ~1 minuto, pocos efectos.
- Si hay **menos de 2 GB libres**: pide permiso para cerrar Chrome y programas pesados (nunca cierres Claude ni la terminal). Con menos de 1 GB libre el render se cierra solo.
- Disco: al menos 10 GB libres.

## 5. Si el alumno se atasca
Guarda el informe (`diagnostico.json`) y dile que se lo pase a su profesor junto con el mensaje de error completo.

## Errores típicos
- *"ffmpeg no se reconoce"*: cerrar y abrir terminal/app; si sigue, reinstalar y revisar el PATH.
- *Python no encontrado*: en Windows usar `py` en lugar de `python`.
- *Ruta demasiado larga al descargar*: trabajar en una carpeta corta (Escritorio).
