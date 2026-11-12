# Ingeniería de Prompts — Veo 3.1

Referencia completa basada en la guía oficial de Google Cloud, Google DeepMind, Invideo, LTX Studio y Atlabs AI (2025–2026).

---

## La fórmula oficial de Google

Google define la fórmula base como:

```
[Cinematografía] + [Sujeto] + [Acción] + [Contexto] + [Estilo & Ambiente]
```

Invideo amplía esto a **7 capas** para mayor control profesional:

```
[Cámara & Lente] + [Sujeto] + [Acción & Física] + [Entorno] + [Iluminación] + [Estilo & Textura] + [Audio]
```

**Template maestro:**
```
[Movimiento de cámara + lente]: [Descripción del sujeto] [Acción con física], en [Entorno + atmósfera], iluminado por [Fuente de luz]. Estilo: [Textura/acabado]. Audio: [Diálogo/SFX/Ambience].
```

**Longitud ideal:** 100–150 palabras. Máximo 3–6 oraciones.

---

## MODO A — Solo texto (sin referencias visuales)

Usa este modo cuando el usuario NO tiene imágenes para subir.

La clave es **anclar al sujeto con máximo detalle al inicio** para evitar drift visual entre frames.

### Anatomía completa

```
[Shot type + camera movement + lens]. [Descripción detallada del sujeto: edad, rasgos, ropa con material específico], [acción física con fuerza/resistencia], en [entorno + qué está haciendo el fondo], iluminado por [fuente de luz nombrada + dirección + temperatura]. Estilo: [textura de piel/material, grado de contraste, acabado cinematográfico]. Audio: [Diálogo entre comillas o SFX: descripción + Ambience: descripción + Music: género, nivel]. No subtitles. No captions. No on-screen text.
```

### Ejemplo completo (spot de producto):

```
Slow cinematic dolly-in on a 35mm lens. A premium glass water bottle with a matte silver cap and textured grip, resting on a wet granite surface, condensation droplets sliding down its sides in real time, in a modern minimalist kitchen at golden hour, natural side light from a floor-to-ceiling window casting long warm shadows. Style: sharp product detail, visible water texture on glass, warm amber color grade, no overexposure. Audio: SFX: soft water drip, subtle clink of glass. Ambience: quiet kitchen hum. Music: warm acoustic piano, low in the mix. No subtitles. No on-screen text.
```

---

## MODO B — Con referencias visuales (imágenes de sujeto/escena/producto)

Usa este modo cuando el usuario tiene imágenes para subir. Hay 3 sub-modos:

### Sub-modo B1: Image-to-Video (una imagen de inicio)

La imagen se convierte en el primer frame. El prompt describe qué debe pasar a continuación.

```
[Describe la acción que ocurre a partir de la imagen]. [Movimiento de cámara]. [Iluminación y atmósfera]. [Audio]. No subtitles.
```

**Ejemplo:**
```
The product on the image slowly rotates as a slow dolly-in reveals its surface texture and label details. Warm studio side lighting with soft shadows. SFX: subtle product clink. Ambience: silent studio. No subtitles.
```

### Sub-modo B2: First & Last Frame (imagen inicial + imagen final)

Genera la transición entre dos estados. Ideal para revelaciones, transformaciones, cambios de hora del día, demolición → construcción, antes → después.

**Prompt para Veo:**
```
[Describe el movimiento de cámara que conecta ambas imágenes]. [Qué transformación ocurre visualmente durante la transición]. [Cómo debe fluir la cámara]. [Audio durante la transición]. No subtitles.
```

**Ejemplo (antes/después de inmueble):**
```
The camera performs a smooth slow pull-back, starting from the cluttered starting frame and gradually revealing the renovated final space. The transition flows through a gentle light sweep from left to right. SFX: soft ambient construction fade-out, then silence. Ambience: quiet, clean space. No subtitles.
```

**Ejemplo (transición de cámara 180°):**
```
The camera performs a smooth 180-degree arc shot, starting with the front-facing view of the singer and circling around her to end on the POV shot from behind her on stage. The singer says, "When you look me in the eyes, I can see a million stars." No subtitles.
```

### Sub-modo B3: Ingredients to Video (múltiples imágenes de referencia)

Subir múltiples imágenes (personaje + entorno + objeto/producto) y referenciarlas en el prompt. Ideal para escenas de diálogo o spots con personaje consistente.

```
Using the provided images for [personaje 1], [personaje 2 si aplica], and [entorno/producto], create a [shot type] of [descripción de la escena]. [Personaje] [acción]. [Diálogo entre comillas si aplica]. [Iluminación]. [Audio]. No subtitles.
```

**Ejemplo (escena de diálogo):**
```
Using the provided images for the detective and the woman and the office setting, create a medium shot of the detective behind his desk. He looks up at the woman and says in a weary voice, "Of all the offices in this town, you had to walk into mine." Dim noir lighting, single lamp source. SFX: rain against window. Ambience: quiet office hum. No subtitles.
```

---

## Vocabulario de cámara

Veo 3.1 entiende terminología cinematográfica profesional. Siempre en inglés.

### Tipos de plano

| Plano | Término |
|---|---|
| Detalle extremo | `extreme close-up` / `extreme macro` |
| Primer plano | `close-up shot` |
| Plano medio | `medium shot` |
| Plano americano | `medium wide shot` |
| Plano general | `wide shot` |
| Plano aéreo | `aerial shot` / `drone shot` |
| Punto de vista | `POV shot` |
| Sobre el hombro | `over-the-shoulder shot` |
| Dos personajes | `two-shot` |

### Movimientos de cámara

| Efecto | Término |
|---|---|
| Acercar suave | `slow dolly-in` |
| Alejarse para revelar | `slow pull-back` / `dolly-out` |
| Seguir al sujeto horizontal | `lateral tracking shot` |
| Seguir desde atrás | `camera following behind subject` |
| Órbita alrededor | `orbit shot around subject` |
| Grúa ascendente | `crane shot rising` |
| Descenso de dron | `aerial drone view slowly descending` |
| Estabilizado profesional | `gimbal stabilized shot` |
| Cámara en mano | `smooth handheld` |
| Fija | `tripod stable, locked-off` |
| Zoom rápido | `whip zoom` |
| Barrido rápido | `whip pan transition` |
| Cambio de foco | `rack focus from [A] to [B]` |
| Efecto vértigo | `dolly zoom` |
| Arco 180° | `smooth 180-degree arc shot` |

### Lentes y profundidad de campo

| Efecto | Término |
|---|---|
| Anguloso / espacioso | `16mm wide-angle lens` |
| Natural / retrato | `35mm lens` |
| Íntimo / comprimido | `85mm lens` |
| Profundidad mínima | `shallow depth of field` |
| Todo enfocado | `deep focus` |
| Macro extremo | `macro lens, extreme close-up` |

**Pro Tip:** Las lentes controlan profundidad, no distancia. 16mm expande el espacio, 85mm comprime el fondo para intimidad.

### Velocidad

| Efecto | Término |
|---|---|
| Cámara lenta extrema | `ultra slow motion, 240fps feel` |
| Cámara lenta | `slow motion, 120fps feel` |
| Tiempo real | `real time motion` |
| Acelerado | `time lapse feel` |

---

## Vocabulario de física y acción

La física realista se logra con verbos de fuerza/resistencia. **Un verbo de acción por clip.**

### Verbos de alto impacto (reemplazan verbos genéricos)

| En lugar de | Usar |
|---|---|
| walks | strides, paces, treads |
| talks | leans forward as he speaks, lifts one hand to emphasize |
| moves | sways, ripples, spirals |
| hits | slams, strikes, crashes |
| falls | plunges, drops, collapses |
| pours | cascades, splashes, streams |

### Micro-acciones para evitar video estático

Cuando la escena no tiene acción principal grande, añadir uno de estos:
- `subtle breath movement`
- `slight natural sway`
- `eyes shift toward camera`
- `steam rising gently`
- `condensation droplets sliding in real time`
- `fabric rippling in a light breeze`

---

## Iluminación

Siempre nombrar una fuente de luz física concreta. Veo genera sombras coherentes cuando hay una fuente nombrada.

| Estilo | Término |
|---|---|
| Hora dorada | `golden hour warm side light` |
| Luz natural suave | `soft natural daylight from a side window` |
| Estudio limpio | `clean studio lighting, soft key light` |
| Retroiluminación dramática | `dramatic backlight with rim lighting` |
| Neón nocturno | `neon sign glow, wet pavement reflections` |
| Único foco dramático | `single overhead spotlight` |
| Chiaroscuro / noir | `single lamp source, deep shadows, low key` |
| Exterior brillante | `bright natural sunlight, outdoor midday` |
| Claroscuro difuso | `overcast diffused light, no harsh shadows` |

---

## Sistema de audio

Veo 3.1 genera audio nativo simultáneamente con el video. Sin especificación, elige aleatoriamente.

### Estructura del bloque de audio

```
Audio: [Dialogue: "texto exacto" spoken by [descripción del personaje] in a [tono] voice]. SFX: [sonido 1], [sonido 2]. Ambience: [descripción del soundscape de fondo]. Music: [género], [instrumento principal], [nivel: low in the mix / subtle / prominent]. No subtitles. No captions.
```

### Sintaxis oficial de Google para diálogo

```
A [descripción del personaje] says, "[texto exacto aquí]"
```

O con tono:
```
He says in a weary voice, "Of all the offices in this town, you had to walk into mine."
```

**Reglas de diálogo:**
- Máximo 1 oración corta por clip de 8 segundos (una sola respiración)
- Identificar al hablante por rasgo visual si hay 2 personajes: "The woman in the red jacket says..."
- Para timestamps de diálogo: `[00:03-00:08] Character speaks...`
- Para idioma diferente: escribir el texto en el idioma deseado dentro de las comillas — Veo sincroniza lips automáticamente

### Etiquetas de audio que funcionan

| Etiqueta | Uso |
|---|---|
| `Dialogue:` | Texto hablado por personaje |
| `SFX:` | Efectos de sonido específicos |
| `Ambience:` | Soundscape de fondo del entorno |
| `Music:` | Música instrumental o de fondo |
| `No subtitles. No captions.` | Evitar texto generado automáticamente |

### Ejemplos de SFX precisos (mejor que descripciones vagas)

| En lugar de | Usar |
|---|---|
| "spooky sounds" | "faint transformer buzz, occasional metal creak, low ventilation hum" |
| "city sounds" | "distant traffic, crosswalk beep, muffled crowd chatter" |
| "coffee shop" | "espresso machine hiss, ceramic cup clink, soft background conversation" |
| "product sounds" | "glass clink, subtle fizz, liquid pour cascade" |

---

## Negative prompts (en positivo)

Veo 3.1 acepta negative prompts pero funcionan mejor cuando se describen en positivo:

| En lugar de | Usar |
|---|---|
| "no buildings" | "a barren landscape stretching endlessly, untouched by roads or buildings" |
| "no text on screen" | "No subtitles. No captions. No on-screen text." |
| "no people" | "an empty scene, no human presence" |
| "no blur" | "sharp, crisp detail throughout the frame" |
| "no color changes" | "consistent warm color grade throughout" |

---

## Timestamps para control de escena

Para clips de 8 segundos, puedes especificar qué pasa en cada momento:

```
[00:00-00:03] [Primera acción o estado].
[00:03-00:06] [Segunda acción o transformación]. SFX: [sonido].
[00:06-00:08] [Momento final o freeze]. Audio: [cierre musical].
```

**Ejemplo real (producto):**
```
[00:00-00:03] Macro close-up, the bottle in silhouette, slow dolly-in building anticipation.
[00:03-00:06] Side-light sweep reveals form and texture as camera pushes gently closer.
[00:06-00:08] Full close-up, sharp and polished. SFX: subtle glass clink. No subtitles.
```

---

## Estilo visual por género

| Género | Keywords |
|---|---|
| Comercial premium | `high-end commercial realism, warm amber color grade` |
| Cinematográfico / indie | `film grain texture, cinematic color grade, anamorphic lens flare` |
| Documental | `handheld documentary style, natural lighting, raw texture` |
| Sci-Fi / Tech | `cyberpunk neon lighting, cool blue tones, high contrast` |
| Lifestyle / natural | `warm golden hour, soft diffused light, authentic mood` |
| Noir | `film noir, chiaroscuro lighting, single source lamp, deep shadows` |
| Minimalista | `minimalist clean, matte white surface, soft key light` |
| Lujo / premium | `luxury aesthetic, muted tones with warm highlights, shallow DoF` |

### Referencias de director (muy efectivas en texto puro)

- `Blade Runner 2049 cinematography` — épico, neon, atmosphérico
- `Wes Anderson composition` — simétrico, paleta pastel, quirky
- `Denis Villeneuve style` — épico, visual, oscuro
- `Wong Kar-wai aesthetic` — melancólico, bokeh intenso, colores saturados
- `John Wick action choreography` — acción fluida, cámara activa
- `Apple commercial style` — minimalista, premium, limpio

---

## Plantillas listas por tipo de contenido

### Template 1: Spot de producto (solo texto, sin imagen)

```
[Shot type + camera movement + lens]. A [descripción detallada del producto: forma, color, material, acabado], [acción física: rotates slowly / condensation slides / cap twists open], on a [superficie], in [entorno], lit by [fuente de luz]. Style: [textura del material, color grade]. SFX: [sonido del producto]. Ambience: [entorno sonoro]. Music: [género, instrumento, nivel]. No subtitles. No on-screen text.
```

**Ejemplo:**
```
Slow cinematic dolly-in on a 35mm lens. A premium glass water bottle with matte silver cap and textured grip, condensation droplets sliding down its sides in real time, resting on wet dark granite, in a minimalist kitchen at golden hour, lit by warm natural side light from a floor-to-ceiling window. Style: sharp glass texture, visible condensation detail, warm amber color grade. SFX: soft water drip, subtle glass clink. Ambience: quiet kitchen hum. Music: warm acoustic piano, low in the mix. No subtitles. No on-screen text.
```

### Template 2: Spot de producto con imagen de referencia (Image-to-Video)

```
Starting from the provided image, [acción que ocurre]. [Movimiento de cámara]. [Efecto dinámico: gotas, vapor, luz]. [Iluminación]. Style: [acabado visual]. SFX: [sonido del producto]. Ambience: [entorno]. Music: [tipo]. No subtitles.
```

**Ejemplo:**
```
Starting from the provided image, the bottle slowly rotates as a gentle orbit shot reveals its label and texture details from all angles. Warm studio key light sweeps from left to right, highlighting surface reflections. Style: high-end commercial product photography feel, rich detail, sharp clarity. SFX: subtle product clink. Ambience: silent studio. No subtitles.
```

### Template 3: Transición First & Last Frame (revelación / antes-después)

```
The camera performs a [tipo de movimiento: smooth pull-back / slow push-in / 180-degree arc], transitioning from [descripción del frame inicial] to [descripción del frame final]. [Descripción de la transformación visual durante el movimiento]. SFX: [sonido de transición]. Ambience: [cambio de ambiente]. No subtitles.
```

**Ejemplo (inmueble antes/después):**
```
The camera performs a smooth slow pull-back, transitioning from the cluttered original space to the fully renovated room. A soft light sweep moves from left to right as the transformation occurs. SFX: ambient construction fade-out, then silence. Ambience: quiet, clean new space. Music: subtle warm strings begin as the final frame is revealed. No subtitles.
```

### Template 4: Lifestyle / Persona (texto puro)

```
[Shot type + camera movement + lens]. [Descripción detallada de la persona: edad, apariencia, material de ropa], [acción con física precisa], in [entorno + qué hace el fondo], lit by [fuente de luz nombrada]. Style: [textura, color grade, acabado]. Audio: [Dialogue opcional]. SFX: [ambiente del entorno]. Ambience: [soundscape]. Music: [tipo, nivel]. No subtitles.
```

**Ejemplo:**
```
Camera locked at eye level, medium close-up on a 35mm lens. A woman in her early 30s with dark curly hair wearing a terracotta linen shirt, lifting a ceramic mug slowly with both hands and closing her eyes as she inhales the steam, in a quiet sun-drenched café during morning hours, blurred patrons visible in the background, lit by soft warm daylight through a large window. Style: fine skin texture, visible linen fabric weave, warm golden color grade. SFX: soft ceramic clink. Ambience: low café chatter, espresso machine hiss. Music: soft lo-fi acoustic, low in the mix. No subtitles.
```

### Template 5: Inmueble / Real Estate

```
[Shot type: aerial / tracking / dolly]. [Descripción del inmueble o espacio: tipo, materiales, dimensiones visuales], [acción o movimiento que revela el espacio], in [contexto: ciudad, hora del día, clima], lit by [iluminación natural o artificial]. Style: [premium architectural photography feel]. Audio: SFX: [sonidos del entorno]. Ambience: [ambiente exterior/interior]. Music: [tipo elegante]. No subtitles. No on-screen text.
```

**Ejemplo (interior):**
```
Slow cinematic dolly forward on a 24mm wide-angle lens. A modern open-plan living room with floor-to-ceiling windows, polished concrete floors, and warm oak furniture, the camera moving from the entrance toward the window revealing a panoramic city view, in late afternoon golden hour. Lit by warm natural light flooding through the large windows casting long horizontal shadows. Style: high-end architectural photography, warm color grade, crisp material detail. SFX: subtle ambient silence. Ambience: faint city sound through glass. Music: minimal warm piano, very low in the mix. No subtitles.
```

**Ejemplo (exterior / drone):**
```
Aerial drone shot slowly descending from above. A modern white minimalist house with a pool surrounded by tropical landscaping, camera descending smoothly to reveal the full property from above, in bright midday sunlight. Lit by direct overhead sun with soft pool reflections. Style: premium real estate photography, vibrant greens, clean whites. SFX: light breeze, water ripple. Ambience: quiet residential ambience. Music: elegant acoustic guitar, subtle. No subtitles.
```

### Template 6: Cinematográfico / Narrativo (con diálogo)

```
[Shot type + angle]. [Descripción del personaje: edad, rasgos, ropa con material], [acción física con micro-movimiento], in [entorno detallado], lit by [fuente de luz nombrada]. [Personaje] says in a [tono de voz] voice, "[diálogo breve, máx 10 palabras]". SFX: [efectos]. Ambience: [soundscape detallado]. Music: [tipo, nivel]. No subtitles.
```

**Ejemplo:**
```
Medium shot at eye level on a 50mm lens. An old lighthouse keeper in his 70s, thick grey beard, wearing a worn navy wool sweater, leaning against the railing and gazing at the horizon, in a dramatic cliffside lighthouse at dusk, lit by the last warm rays of sunlight behind him with rim lighting. He says in a gravelly, distant voice, "Every storm passes. Every single one." SFX: crashing waves below, distant seagull call. Ambience: strong coastal wind, metal railing creak. Music: slow solo cello, low and melancholic. No subtitles.
```

### Template 7: Educativo / Informativo (a cámara directa)

```
[Shot type: medium shot, eye level]. [Descripción del presentador: edad, rasgos, ropa con material], [acción de hablar con micro-físca precisa], in [entorno limpio: oficina, estudio, exterior], lit by [fuente de luz]. [Presentador] says, "[mensaje breve y directo]". Style: [clean, professional]. SFX: [ambiente]. Ambience: [soundscape]. No subtitles. No captions.
```

**Ejemplo:**
```
Medium close-up, camera locked at eye level on a 35mm lens. A startup founder in his late 30s with short dark hair and light stubble, wearing a charcoal cotton hoodie, leaning slightly forward as he speaks and lifting one hand to emphasize a point, then relaxing back, in a quiet modern office during late afternoon, blurred monitors glowing faintly in the background, lit by soft natural daylight from a side window with gentle fill on the opposite side. He says, "This update cuts setup time in half." Style: fine skin texture, visible fabric weave, subtle contrast, no gloss. SFX: none. Ambience: quiet office hum. No subtitles.
```

### Template 8: Acción / Deportes / Energético

```
[Shot type: low angle / tracking / aerial]. [Descripción del atleta: edad, ropa deportiva con material], [acción explosiva con verbo de fuerza], in [entorno deportivo o urbano], lit by [iluminación dramática]. Style: [high contrast, cinematic sports feel]. SFX: [impacto, ambiente del entorno]. Ambience: [crowd, wind, urban]. Music: [energético, BPM alto]. No subtitles.
```

**Ejemplo:**
```
Low angle tracking shot, 24mm wide lens. A female runner in her mid-20s wearing a black compression top and bright orange running shoes, strides powerfully through rain-soaked city streets at dawn, each footfall sending water splashing upward in slow motion, buildings blurring behind her. Lit by dramatic overcast diffused light with wet street reflections. Style: high contrast sports photography, desaturated cool tones with warm subject. SFX: powerful footsteps, water splash impact, rain hiss. Ambience: distant city traffic. Music: driving electronic beat, high energy, builds throughout clip. No subtitles.
```

### Template 9: Mapa / Ubicación (con imagen de mapa)

```
Starting from the provided map image, [efecto visual sobre el mapa: neon lines draw along streets / pin pulses with glow / route animates from A to B]. Camera [stays locked / slowly pushes in toward the pin]. [Descripción del efecto visual: color del neon, grosor, velocidad del trazo]. Style: clean map aesthetic, [color scheme]. SFX: [subtle tech tone / pin drop sound]. No subtitles. No on-screen text.
```

---

## Workflow avanzado: multi-shot con clips encadenados

Para videos de más de 8 segundos, Veo 3.1 se usa en cadena:

1. **Generar Clip 1** (imagen inicio → imagen fin)
2. **Tomar el último frame del Clip 1** como imagen de inicio del **Clip 2**
3. **Generar Clip 2** con la misma lógica
4. **Repetir** para más escenas
5. **Unir todos los clips** en Flow, CapCut, DaVinci Resolve o Premiere

**Pro Tip:** Compartir el frame de transición entre clips mantiene la cámara, iluminación e identidad del sujeto consistente. Así el resultado parece una sola toma continua.

---

## Errores comunes de prompting a evitar

| ❌ Falla | ✅ Corrección |
|---|---|
| "Create a video of a woman drinking coffee" | "Slow dolly-in on 35mm. A woman in her 30s with dark hair, wearing a cream linen blouse, lifting a ceramic mug with both hands, steam rising, in a sun-drenched café at morning. Lit by soft side daylight." |
| "A man walks and talks and gestures" | "A man leans forward as he speaks, lifting one hand to emphasize a point." (una sola acción dominante) |
| "5 people in a room" | "A small group of colleagues gathered around a conference table" |
| "No buildings in background" | "A wide open field stretching to the horizon, untouched and empty" |
| "Spooky audio" | "SFX: faint creak of old wood, distant wind howl. Ambience: hollow, quiet silence." |
| Prompt de 300 palabras | Máximo 100–150 palabras. Cortar todo lo redundante. |

---

## Post-producción recomendada

Lo que Veo 3.1 NO hace bien y debe hacerse en post:

| Elemento | Herramienta |
|---|---|
| Textos / títulos animados | CapCut, DaVinci Resolve, Adobe Premiere |
| Logos y branding | After Effects, CapCut |
| Subtítulos finales | CapCut auto-subtítulos |
| Unión de múltiples clips | Google Flow, CapCut, DaVinci |
| Color grading fino | DaVinci Resolve |
| Música con licencia comercial | Epidemic Sound, Artlist |
| Imágenes de referencia (ingredients) | Gemini 2.5 Flash Image (Nano Banana) |
| Extensión de clip más allá de 8s | Función Extend en Google Flow o Invideo |
