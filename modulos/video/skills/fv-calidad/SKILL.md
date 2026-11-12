---
name: fv-calidad
description: Control de calidad y entrega. Revisa el video antes de renderizar (choques de texto con un auditor automático, errores de HyperFrames, fotogramas de los momentos clave que Claude debe mirar), renderiza el MP4 final con el número de procesos adecuado a la memoria del equipo, verifica tamaño, duración y volumen, y crea una versión ligera para ver rápido. Úsala siempre antes de entregar un video, y cuando el render se cierre solo o el alumno pida cambios.
---

# Calidad y render

`<SKILLS>` = `%USERPROFILE%\.claude\skills` (Windows) o `~/.claude/skills` (Mac/Linux).

## 1. Revisar antes de renderizar
```bash
python "<SKILLS>/fv-calidad/scripts/revisar.py" Reels/mi-video
```
La primera vez instala `puppeteer-core` (auditor de choques; necesita Chrome o Edge). Hace tres cosas:
1. **Choques**: detecta textos que se pisan o se salen del panel (mira el tiempo exacto que indica).
2. **HyperFrames check**: errores reales (ignora el ruido conocido).
3. **Fotogramas** de los momentos clave en `.hyperframes/artifacts/snapshots/…/frame-*.png`.

**MIRA los fotogramas tú mismo** (herramienta de lectura de imágenes) y revisa: rostro libre, nada cortado, nada pisado, texto legible y con contraste, subtítulos dentro de la zona segura. Describe al alumno qué viste. Un "0 choques" automático no reemplaza tus ojos.
Si hay problemas, vuelve a `fv-editor`, corrige `plan.json` y repite.

## 2. Render de prueba (recomendado) y final
```bash
python "<SKILLS>/fv-calidad/scripts/render.py" Reels/mi-video --nombre PRUEBA.mp4 --borrador
python "<SKILLS>/fv-calidad/scripts/render.py" Reels/mi-video --nombre FINAL-mi-video.mp4
```
- Elige 1, 2 o más procesos según la **memoria libre**. Con menos de 1 GB libre **se niega** a renderizar: pide cerrar Chrome y otros programas (con permiso del alumno; nunca Claude ni la terminal).
- Tarda: un video de 30 s puede demorar de 2 a 10 minutos según el equipo. Avisa y no cierres la ventana. En equipos ligeros, valida con `--borrador` y renderiza el final una sola vez.
- Verifica con ffprobe: 1080×1920, duración, tamaño, **≈ −14 LUFS**, pico ≤ −1,5 dB.
- Crea `VER-AQUI-*.mp4` en 720p, liviano, para ver rápido en el celular.

## 3. Entrega
Dile al alumno: la **ruta del MP4**, la versión ligera, y esta lista para que mire:
- Primeros 4 segundos (el gancho).
- Subtítulos al ritmo de la voz.
- Gráficos que no tapen la cara.
- Volumen y música.
Pídele notas con el **segundo exacto**. Cada nota se vuelve una regla: guárdala en `Mi estilo/Reglas-de-estilo.md` (con `fv-marca`).

## Si el render falla
- *Se cierra solo / código −1073740791*: poca memoria. Cerrar Chrome y otros programas, `--procesos 1`, `--borrador`.
- *Navegador no encontrado*: instalar Chrome (`fv-diagnostico`).
- *Fuente no se ve*: la tipografía debe estar en la lista de `fv-marca`; revisar internet (se descarga la primera vez).
- *Quedó negro o sin audio*: revisar que `plan.json` apunte a `assets/base.mp4` y `assets/mix.wav` existentes.
- Si nada funciona: guarda el mensaje de error completo y pásalo al profesor.
