---
name: fv-editor
description: Motor de edición. Convierte el plan aprobado por el emprendedor (más su video, la transcripción con tiempos y su estilo) en un video HyperFrames con subtítulos palabra por palabra, gancho, tarjetas con icono, datos grandes, sellos, listas, titulares, etiquetas, tarjeta de nombre, capítulos con barra de progreso, zooms de cámara y cierre. Valida que nada tape la cara, que nada se pise y que el texto sea legible. Úsala después de tener el video montado, la transcripción y el estilo.
---

# Editor: del plan al video

`<SKILLS>` = `%USERPROFILE%\.claude\skills` (Windows) o `~/.claude/skills` (Mac/Linux).
Requiere en la carpeta del proyecto: `assets/base.mp4`, `words.json`, y el `estilo.json` del alumno (`Mi estilo/`).

## 1. Proponer el plan en TABLA (obligatorio)
Con `frases.txt` y `words.json`, arma una tabla y **espera la aprobación escrita del alumno**:

| Segundo | Lo que dice | Qué aparece | Dónde |
|---|---|---|---|
| 0:00–0:04 | "…" | Gancho: título grande | arriba |
| 0:06 | "…" | Tarjeta con icono | arriba |

Criterios:
- **Un gráfico por idea**, solo cuando refuerza lo que dice. Menos es más: 6–10 eventos para 30 s.
- **Solo lo que el alumno dijo.** Prohibido inventar cifras, pasos, precios o llamados a la acción. El cierre sigue lo que dice; si no hay cierre hablado, usa el CTA de su `estilo.json`.
- **Un tutorial** puede llevar el texto debajo de la persona; en un video de rostro, arriba o abajo, nunca sobre la cara.
- Marca la **palabra clave** de cada frase con asteriscos: `"DE *EMPRESA*"`.
- Mira un fotograma del video para ubicar la cara (`rostro_y` y `rostro: {y1, y2}`).

## 2. Escribir `plan.json`
Parte de `ejemplos/plan_ejemplo.json`. Campos:
- `duracion`, `video` (`assets/base.mp4`), `audio` (`assets/mix.wav` o el audio del video), `words` (`words.json`)
- `rostro_y` (centro del zoom) y `rostro: {y1,y2}` (zona que ningún gráfico puede tapar)
- `zonas`: `arriba`, `medio`, `abajo` con `y` y `h` (por defecto 170/440, 640/420, 1420/110)
- `claves`: palabras que se resaltan en los subtítulos · `zoom_max` (máx. 1.2) · `zooms_auto` (true) o lista `zooms:[{t, escala}]`
- `gancho`: `{tag, fin, lineas:[{t, tam}]}`
- `capitulos` (opcional): `[{t, badge:"1", texto:"…"}]` con barra de progreso
- `cierre`: `{t, y, texto?, sub?, handle?}`. Ponlo bajo la cara (ej. `y: 1390`), sobre `y < 1540`.
- `eventos`: lista con `tipo` (`tarjeta` `dato` `sello` `lista` `titular` `etiqueta` `nombre`), `t` (segundo), `dur`, `pos` (`arriba|medio|abajo`), y según tipo:
  - tarjeta: `icono`, `titulo`, `sub`, `entrada` (`derecha`)
  - dato: `valor`, `etiqueta`, `color`
  - sello: `texto`, `color` (`alerta|positivo|acento`)
  - lista: `titulo`, `items`, `cada`
  - titular: `texto` (usa `\n`)
  - etiqueta/nombre: `texto`, `icono`, `color`
- Iconos disponibles: check, cross, warning, star, rocket, chart, trend, megaphone, chip, lock, unlock, shield, user, building, store, phone, camera, mic, globe, heart, cart, money, clock, bulb, target, calendar, play, link, gear, spark, arrow_up, arrow_right, question, thumb.

## 3. Construir y validar
```bash
python "<SKILLS>/fv-editor/scripts/construir.py" --proyecto Reels/mi-video --estilo "Mi estilo/estilo.json" --validar
```
Genera `index.html` (HyperFrames) y `sfx_eventos.json`. El **validador** detiene o avisa si:
- dos gráficos ocupan el mismo hueco a la vez,
- un gráfico tapa la cara o la banda de subtítulos,
- algo queda bajo y=1540 (botones de la red social) o sobre y<150,
- un texto no cabe a ≥ 28 px.
Corrige el plan (mover, acortar, separar en el tiempo) y repite hasta que no haya errores. **Nunca lo silencies.**

## 4. Pasa a sonido y calidad
`fv-sonido` (mezcla `assets/mix.wav`) → `fv-calidad` (revisar y renderizar).

## Layout "pantalla arriba + tú abajo" (v1.1)
Para videos con una **grabación de pantalla** (analítica, tutorial, demo) y la cámara del alumno. Motor aparte, mismo flujo de plan aprobado y revisión:
```bash
python "<SKILLS>/fv-editor/scripts/construir_pantalla_cara.py" --proyecto Reels/mi-video
```
1. **Recorta, no tapes.** Si el video original trae banners, textos fijos o barras pegadas, sepáralos con ffmpeg: la pantalla en `assets/screen.mp4` y la cámara en `assets/face.mp4` (30 fps, mismo largo con `tpad` para el cierre). Recorta también lo que muestre datos personales (pestañas, menús, barra de tareas) y los bordes de color de exportaciones de apps (8–11 px).
2. **Plan** (`plan.json`, ver `ejemplos/plan_pantalla_cara_ejemplo.json`): `gancho` (dolor al inicio), `empuje` (acercamiento lento), `pantalla_zooms` (`cx`,`cy` en coordenadas de la ventana de 1000×544; escala ≤ 1.35 para filas anchas, ≤ 1.8 para un dato), `anillos` (marcan lo que se dice, a la hora exacta de la palabra), `eventos` de la franja inferior (`texto`, `pasos`, `stats`, `sello`, `comparar`, `dato`), `cierre`, `camara_zooms`, `claves`, `correcciones` de palabras (`t`, `de`, `a`; `a: null` borra).
   Opciones añadidas con la noticia de Omni Flash: `capturas` (imágenes del alumno que se muestran dentro de la ventana de pantalla, ya recortadas a 1000×544, con sus propios `anillos`), `pasos` con `icono_pasos` (`cross` tacha, `check` confirma), `gancho.pildora2` (segunda promesa), `cierre.zona: "franja"` (el cierre ocupa solo la franja inferior y **no hay cola congelada**: el video termina cuando termina la voz) y `camara_cortes` (tiempos de los cortes; la cámara alterna 1.0 y 1.1 en cada uno para disimularlos).
3. **Mide antes de anillar.** La pantalla se desplaza: extrae fotogramas cada 2 s (`fps=0.5,tile`) y anota en qué intervalos el contenido está quieto; ubica anillos y zooms solo en esos intervalos.
4. Misma revisión de `fv-calidad`. Lee `LECCIONES.md` antes de empezar.

## Video de avatar armado con varias tomas (v1.2)
Cuando el material son **5-6 tomas generadas** (avatar y tomas de detalle) del mismo lugar:
1. **Orden por el guion, no por el nombre del archivo**; une con cortes secos, cada 1,5-3 s de plano visible. La voz del avatar sigue por encima de las tomas de detalle (corte tipo J/L): el avatar habla mientras se ve el producto.
2. **Recorta 0,3-0,5 s** al inicio de cada toma (la voz arranca con la primera sílaba) y la cola muda al final.
3. **Punch-in 105-115 %** en algunos cortes y alterna escalas para disimular costuras; nunca pases de 1.2.
4. **Continuidad en la edición:** mismo gradiente de color en todas las tomas (iguala brillo y tono), **sonido ambiente continuo** debajo de todo y música baja que une los cortes.
5. **Tapa o recorta lo que la IA inventó** (etiquetas con letras en prendas, carteles, objetos filosos); si no se puede, repite la toma.
6. Datos que no se dicen (precio, tallas, colores, ubicación) van como tarjetas animadas; la **ubicación del negocio y la llamada a la acción** siempre aparecen en el cierre.
7. Si una toma repite el encuadre de la anterior, pídele al alumno otra toma o corta antes: el ojo detecta el plano repetido.

## Cambios del alumno
Cada nota ("en 0:12 el texto tapa") se traduce en un cambio de `plan.json` o de `estilo.json`; reconstruye solo eso. Si pide algo que el motor no hace (otro tipo de gráfico, otra composición), dilo claro y ofrece la alternativa más cercana.

## Límites que debes decir
- El motor está hecho para video con **una persona a pantalla completa** (1080×1920). Tutoriales con pantalla + cámara pequeña o capturas de pantalla animadas requieren trabajo a medida.
- Los zooms nunca pasan de 1.2.
