# Ingeniería de Prompts — Seedance 2.0

Referencia completa para construir prompts profesionales. Basada en patrones documentados con cientos de generaciones reales en Seedance 2.0 (ByteDance, febrero–abril 2026).

---

## Fórmula universal del prompt

Todo prompt de Seedance 2.0 sigue esta estructura base:

```
Sujeto + Acción + Escena + Iluminación + Movimiento de cámara + Estilo + Calidad + Restricciones
```

**Longitud ideal:** 80–120 palabras por shot. El total del prompt no debe superar 200 palabras.
**Regla de oro:** Un verbo de acción por shot. Un solo personaje principal por shot (máximo dos).

---

## MODO A — CON referencias @ (imágenes / video / audio)

Usa este modo cuando el usuario tenga archivos que subir a la plataforma.

### Cómo funciona el sistema @

Seedance 2.0 asigna automáticamente etiquetas a los archivos subidos:
- Imágenes → @Image1, @Image2... (hasta @Image9)
- Videos → @Video1, @Video2, @Video3
- Audios → @Audio1, @Audio2, @Audio3

### Declaración de referencia (siempre al inicio del prompt)

```
@NombreExactoDelArchivo is the [ROL]. Preserve [qué conservar] exactly in every shot. Do not change the [diseño/apariencia].
```

**El ROL es obligatorio.** Sin él, el modelo puede ignorar el asset.

| Tipo de asset | Sintaxis de declaración |
|---|---|
| Imagen de producto | `@Image1 is the main product reference. Preserve label, colors and shape exactly.` |
| Imagen de personaje | `@Image1 is the character reference. Maintain face and clothing consistency.` |
| Video de estilo | `@Video1 is the camera movement reference. Replicate its framing and pacing.` |
| Audio de fondo | `@Audio1 is the background music reference. Match its rhythm and mood.` |
| Múltiples imágenes | `@Image1 is the main product. @Image2 provides side-view structure. @Image3 shows material detail.` |

### Estructura completa — Con referencias (15 segundos)

```
@[archivo] is the [ROL]. Preserve [detalles] exactly in every shot. Do not change the [elemento].

[0-3s] [Movimiento de cámara]. [Descripción escena + acción]. [Efecto dinámico]. [Iluminación].
Maintain face and clothing consistency, no distortion, high detail.

[3-7s] [Movimiento de cámara]. [Descripción escena + acción]. [Efecto dinámico]. [Iluminación].
Maintain face and clothing consistency, no distortion, high detail.

[7-11s] [Movimiento de cámara]. [Descripción escena + acción]. [Efecto dinámico]. [Iluminación].
Maintain face and clothing consistency, no distortion, high detail.

[11-15s] [Movimiento de cámara]. [Hero reveal / cierre]. [Freeze frame opcional].
Maintain face and clothing consistency, no distortion, high detail.

Audio: [Género musical] background music, [BPM] BPM, [mood]. Full bass throughout.
[Género locutor] voiceover in [idioma] with [acento] accent, [tono] tone,
starts at second 1 runs through second 14:
"[Texto de narración simple]"
Voice must be clear, calm and well paced. No rushing.
[Efectos de sonido] at second [N].

Quality: 2K cinematic commercial. Ultra HD. Rich details. Sharp clarity.
Warm color grading. No blur. No artifacts. Stable picture.
Smooth dynamic transitions between shots. Generate video without subtitles.
Professional [tipo] advertising style.
```

---

## MODO B — SIN referencias (solo texto)

Usa este modo cuando el usuario NO tiene imagen, video ni audio para subir. Es el modo más común para usuarios nuevos y para videos de lifestyle, narrativos o cinematográficos.

### Diferencias clave vs Modo A

- No hay declaración @ al inicio
- La descripción del sujeto debe ser más detallada y específica (color, material, forma, edad, ropa)
- Usa referencias estilísticas de directores o films: "Denis Villeneuve style", "Wong Kar-wai aesthetic", "Blade Runner 2049 cinematography"
- La consistencia del personaje se mantiene con la frase de restricción, no con un asset

### Estructura completa — Sin referencias (15 segundos)

```
[Descripción detallada del sujeto: edad, apariencia, ropa, materiales, colores específicos].

[0-3s] [Movimiento de cámara]. [Descripción escena + acción + entorno]. [Iluminación].
Maintain character appearance and clothing consistency, no distortion, high detail.

[3-7s] [Movimiento de cámara]. [Descripción escena + acción]. [Efecto dinámico]. [Iluminación].
Maintain character appearance and clothing consistency, no distortion, high detail.

[7-11s] [Movimiento de cámara]. [Descripción escena + acción]. [Iluminación].
Maintain character appearance and clothing consistency, no distortion, high detail.

[11-15s] [Movimiento de cámara]. [Cierre / hero reveal / momento emocional].
Maintain character appearance and clothing consistency, no distortion, high detail.

Audio: [Género musical] background music, [BPM] BPM, [mood]. Full bass throughout.
[Efectos de sonido opcionales].

Quality: 2K cinematic. Ultra HD. Rich details. Sharp clarity. [Color grading].
No blur. No artifacts. Stable picture. Smooth dynamic transitions.
Generate video without subtitles. [Estilo visual: film grain / cinematic texture / etc.].
Professional [tipo] style.
```

### Técnica de capas (para usuarios nuevos sin imagen)

Construir el prompt por capas ayuda a obtener mejores resultados:

1. **Base:** "A young woman walking"
2. **+ Entorno:** "A young woman in a red linen dress walking through a sunlit market"
3. **+ Cámara:** "...slow tracking shot following from the right"
4. **+ Estilo:** "...golden hour warm lighting, shallow depth of field, film grain"
5. **+ Restricciones:** "...4K Ultra HD, no distortion, stable picture, no subtitles"

---

## Vocabulario de cámara

Seedance 2.0 entiende terminología cinematográfica profesional. Úsala siempre en inglés.

### Movimientos de cámara

| Efecto deseado | Término en el prompt |
|---|---|
| Acercar suave | `slow dolly-in` |
| Acercar agresivo | `fast aggressive dolly push-in` |
| Alejar para revelar | `slow pull-back hero reveal` |
| Paneo lateral | `lateral tracking shot` |
| Seguir al sujeto | `camera following behind subject` |
| Cámara baja subiendo | `low angle ground level pushing up` |
| Órbita alrededor del sujeto | `orbit shot around subject` (nunca 360° para productos) |
| Cámara en mano natural | `smooth handheld with slight organic motion` |
| Estabilizada profesional | `gimbal stabilized shot` |
| Fija sin movimiento | `tripod stable, locked-off` |
| Dron descendiendo | `aerial drone view slowly descending` |
| Zoom rápido | `whip zoom into subject` |
| Transición de barrido | `whip pan transition` |
| Cambio de foco | `rack focus from [A] to [B]` |
| Grúa ascendente | `crane shot rising` |
| Efecto vértigo | `dolly zoom (Hitchcock effect)` |

**Modificadores de velocidad:** Combinar `slow` / `medium` / `fast` con el movimiento. Ej: `slow dolly-in, 1-2 feet`.
**Movimientos compuestos:** Describir en beats temporales. Ej: `Start: slow dolly-in. Then: gentle pan right for the final 2 seconds.`

### Ángulos de cámara

| Ángulo | Término |
|---|---|
| Plano detalle extremo | `extreme macro close-up` |
| Primer plano | `close-up shot` |
| Plano medio | `medium shot` |
| Plano general | `wide shot` |
| Ángulo bajo | `low angle shot` |
| Ángulo alto | `high angle shot` |
| Punto de vista | `POV (first-person perspective)` |
| Sobre el hombro | `over-the-shoulder shot` |

### Velocidad y tiempo

| Efecto | Término |
|---|---|
| Cámara lenta extrema | `ultra slow motion 240fps feel` |
| Cámara lenta | `slow motion 120fps feel` |
| Tiempo real | `real time motion` |
| Acelerado | `time lapse` |

---

## Vocabulario de dinamismo

Para evitar que el video se vea como "foto en movimiento", usa estos verbos y efectos:

### Verbos de alto impacto (uno por shot)

`bursts into frame`, `explodes outward`, `crashes beside`, `splashes dramatically`, `flies through frame`, `races down`, `rushes in`, `whips past`, `shatters into`, `ignites`, `erupts`, `glides through`, `slices across`

### Efectos físicos para bebidas y líquidos

- `water droplets explode outward from the base`
- `juice particles fly across the frame catching golden sunlight`
- `liquid rushing and splashing visibly inside the bottle`
- `condensation droplets race down the glass in real time`
- `droplets suspend mid-air in slow motion`
- `ice cubes shift and clink dramatically`
- `liquid swirls and splashes in extreme slow motion`

### Efectos de luz dinámica

- `golden backlight flares dramatically behind the subject`
- `light rays burst from behind the product`
- `dramatic lens flare sweeps across frame`
- `rim lighting pulses on the surface`
- `soft light reflects off the glass`

---

## Iluminación

| Estilo | Término en el prompt |
|---|---|
| Luz natural cálida | `warm golden side-lighting` |
| Luz de estudio limpia | `clean studio lighting, commercial product style` |
| Retroiluminación dramática | `dramatic backlight, rim lighting` |
| Luz de sol exterior | `bright natural sunlight, outdoor` |
| Hora dorada | `golden hour warm light` |
| Luz baja / misterioso | `low key dramatic lighting, single source` |
| Chiaroscuro | `harsh chiaroscuro lighting, deep shadows` |
| Luz difusa suave | `soft diffused natural light, overcast sky` |

---

## Estilos visuales por género

| Género | Keywords recomendados |
|---|---|
| Vida diaria / lifestyle | `healing fresh`, `Japanese fresh style`, `Korean mood`, `artistic` |
| Sci-Fi / acción | `cyberpunk`, `dark premium`, `retro film`, `IMAX cinematic texture` |
| Minimalista | `minimalist clean`, `premium texture`, `realistic photography` |
| Cinematográfico | `cinematic texture`, `film grain`, `anamorphic lens flare` |
| Film noir | `film noir`, `chiaroscuro lighting`, `high contrast` |
| Animación / anime | `anime style`, `thick oil paint texture`, `Van Gogh Post-Impressionism` |
| Lujo / premium | `luxury aesthetic`, `muted tones with warm highlights`, `shallow depth of field` |

### Referencias de director (solo texto — muy efectivas)

- `Denis Villeneuve style` — épico, visual, atmosférico
- `Wong Kar-wai aesthetic` — melancólico, bokeh intenso, colores saturados
- `Blade Runner 2049 cinematography` — sci-fi, neon, dramático
- `Wes Anderson composition` — simétrico, paleta pastel, flat lay
- `John Wick action choreography` — acción fluida, cámara activa

---

## Color grading

| Estilo | Descriptor |
|---|---|
| Comercial cálido | `warm orange and teal color grade` |
| Muted artístico | `desaturated muted colors with warm highlights` |
| Saturado vibrante | `vibrant saturated palette` |
| Azul frío | `monochromatic cool blue tones` |
| Natural | `natural color grading, true to life` |
| Vintage | `vintage 1970s film look, faded warm tones` |

---

## Bloque de Audio

```
Audio: [Género musical] background music, [BPM] BPM, [mood descriptors], full bass throughout.
[Género locutor] voiceover in [idioma] with [acento] accent, [tono] tone,
starts at second 1 runs through second 14:
"[Texto de narración simple, sin tildes complejas, sin palabras largas]"
Voice must be clear, calm and well paced. No rushing.
[Efectos de sonido]: [sonido] at second [N].
```

### Keywords de audio especiales

Seedance 2.0 tiene motor nativo de audio. Estas palabras activan efectos específicos:

| Keyword | Efecto |
|---|---|
| `reverb` | Reverberación de espacio grande (salas, catedrales) |
| `muffled` | Sonido amortiguado (espacios cerrados, bajo el agua) |
| `echoing` | Eco (cámaras grandes) |
| `metallic clink` | Sonido de colisión metálica |
| `crunchy` | Sonidos texturizados (gravel, crujidos) |
| `high-pitched` | Sonidos agudos |
| `crackling fire` | Crepitar de fuego |
| `reverb` | Sonido espacial |

### Rangos de BPM recomendados

| Tono del video | BPM | Riesgo |
|---|---|---|
| Elegante / premium / emocional | 75–85 | Ninguno |
| Comercial estándar / lifestyle | 90–100 | Ninguno |
| Energético / dinámico / acción | 105–115 | Bajo |
| Muy alto impacto | 120+ | Alto — riesgo de distorsión vocal |

### Géneros musicales que funcionan bien

- `Upbeat Latin pop` — energético, comercial
- `Tropical pop` — fresco, veraniego
- `Cinematic orchestral` — épico, emocional
- `Electronic upbeat` — moderno, dinámico
- `Acoustic warm` — natural, familiar
- `Soft jazz` — elegante, urbano
- `Hip-hop trap beats` — urbano, energético

### Reglas de narración

- Usar frases cortas con palabras simples
- Evitar esdrújulas largas (reemplazar "auténtico" por "real", "científicamente" por "probado")
- NO usar guiones entre sílabas
- Máximo 2–3 líneas de narración para 13 segundos de voz
- Elegir UN solo idioma para la narración (no mezclar)

---

## Bloque de Quality (siempre al final)

```
Quality: 2K cinematic commercial. Ultra HD. Rich details. Sharp clarity.
[Color grading style]. No blur. No artifacts. Stable picture.
Smooth dynamic transitions between shots. Generate video without subtitles.
Maintain face and clothing consistency throughout. Professional [tipo] advertising style.
```

Personaliza `[tipo]`: `beverage`, `food`, `fashion`, `tech`, `beauty`, `lifestyle`, `automotive`, etc.

---

## Distribución de shots recomendada (15 segundos)

| Shot | Tiempo | Propósito |
|---|---|---|
| Shot 1 | 0–3s | Gancho visual / presentación del sujeto |
| Shot 2 | 3–7s | Demostración / detalle / beneficio clave |
| Shot 3 | 7–11s | Lifestyle / contexto / persona usando el producto |
| Shot 4 | 11–15s | Hero reveal / cierre de marca / freeze frame |

Para videos más cortos (4–8s): usar 2 shots con mayor desarrollo cada uno.

---

## Templates por tipo de video

### Template 1: Spot de producto con imagen de referencia

```
@[archivo] is the main product reference. Preserve [detalles: colores, etiqueta, forma] exactly in every shot. Do not change the product design.

[0-3s] Fast aggressive dolly push-in crashing into extreme macro close-up. The [producto] bursts into frame. [Efecto líquido/condensación]. Warm golden backlight flares behind the product. High-end commercial product style. Maintain product appearance consistency, no distortion.

[3-7s] Rack focus, ultra slow motion. [Ingrediente/elemento clave] falls and explodes beside the product. [Partículas] fly across frame in golden sunlight. Vivid saturated color grade. Maintain product appearance consistency.

[7-11s] Lateral tracking shot, smooth handheld. A young [descripción persona] uses/drinks the product outdoors. [Ambiente: parque, playa, ciudad]. Genuine satisfaction expression. Natural warm lighting. Maintain product appearance consistency.

[11-15s] Slow pull-back hero reveal. Product always facing camera front, no rotation. Product floats centered on [color] background with light rays. Camera pulls back to full hero shot. Freeze frame at second 14. Maintain product appearance consistency.

Audio: [género] background music, [BPM] BPM, [mood], full bass throughout. [Género] voiceover in Spanish with Latin American accent, [tono] tone, starts at second 1 runs through second 14: "[Narración simple]" Voice clear and well paced. No rushing. [Efectos de sonido].

Quality: 2K cinematic commercial. Ultra HD. Rich details. Sharp clarity. Warm color grading. No blur. No artifacts. Stable picture. Smooth dynamic transitions. Generate video without subtitles. Professional beverage advertising style.
```

### Template 2: Spot de producto SIN imagen de referencia

```
A [descripción detallada del producto: forma, color, material, etiqueta, tamaño]. [Color/textura del envase].

[0-3s] Extreme macro close-up, fast aggressive dolly push-in. The [producto] bursts into frame from black. [Efecto dinámico: gotas, vapor, brillo]. Dramatic warm backlight. High-end commercial product style. No distortion, stable picture.

[3-7s] Ultra slow motion, rack focus. [Elemento visual clave] crashes beside the product. [Partículas] fly across frame catching warm sunlight. Vivid saturated colors. Maintain product color and shape consistency.

[7-11s] Smooth lateral tracking shot. A young person in [ropa/entorno] interacts with the product. [Acción: holds it, opens it, tastes it]. Natural golden hour lighting outdoors. Genuine expression. Maintain product consistency.

[11-15s] Slow pull-back hero reveal. Product centered on [color] background. Light rays emanate from behind. Full hero shot. Freeze frame at second 14. No rotation.

Audio: [género] music, [BPM] BPM, [mood], full bass. [Género] voiceover in Spanish with Latin American accent: "[Narración simple]" Clear, calm, well paced. [Efectos].

Quality: 2K cinematic commercial. Ultra HD. Sharp clarity. Warm color grading. No blur. No artifacts. Stable picture. Smooth transitions. Generate video without subtitles. Professional advertising style.
```

### Template 3: Video lifestyle / persona

```
[Descripción de la persona: edad, apariencia, ropa específica, entorno].

[0-4s] Medium shot, slow push-in. [Persona] in [entorno]. Warm natural lighting. Relaxed and authentic mood. Maintain character appearance consistency.

[4-9s] Lateral tracking shot following subject. [Acción principal con el producto o actividad]. Fast rack focus between person and detail. Vivid colors, energetic feel. Maintain character consistency.

[9-15s] Slow pull-back wide shot revealing full scene. [Momento emocional: sonrisa, reacción]. Hero product reveal centered on screen. Maintain character consistency.

Audio: [género] music, [BPM] BPM, warm and uplifting. Voiceover: "[Texto simple]"

Quality: 2K cinematic. Ultra HD. Natural color grading. No blur. No artifacts. Stable picture. Generate video without subtitles.
```

### Template 4: Video cinematográfico / marca premium

```
[Descripción detallada del producto o sujeto con detalles de lujo: materiales, acabados, colores].

[0-5s] Extreme macro close-up, tripod stable, very slow dolly-in. [Producto o elemento de marca] in dramatic low key lighting. Single warm light source. Shallow depth of field. Film grain texture. Luxury aesthetic. No distortion.

[5-10s] Low angle ground shot, slow crane rising. [Escena lifestyle de lujo]. Camera rises from ground level to reveal full scene. Cinematic color grade, muted tones with warm highlights. Maintain visual consistency.

[10-15s] Slow pull-back hero reveal. [Producto centrado]. Freeze frame on product. Elegant and minimal. No rotation.

Audio: Cinematic orchestral music, 80 BPM, elegant and emotive. No voiceover. Subtle ambient sounds only.

Quality: 2K cinematic. Ultra HD. Cinematic color grading. Film grain. No blur. No artifacts. Generate video without subtitles. Premium brand advertising style.
```

### Template 5: Video educativo / informativo (sin imagen)

```
[Descripción del concepto, producto o proceso a explicar].

[0-4s] Medium shot, slow push-in. [Persona o elemento explicativo] in [entorno limpio: oficina, laboratorio, estudio blanco]. Clean professional lighting. Informative mood. Maintain visual consistency.

[4-9s] Close-up, tripod stable. [Detalle del producto o proceso clave]. Text overlay NOT included. Visual demonstration only. Clean studio lighting. Sharp focus. Maintain visual consistency.

[9-15s] Medium wide shot. [Conclusión visual: persona satisfecha, producto en uso, resultado]. Warm natural lighting. [Acción de cierre]. Maintain visual consistency.

Audio: Neutral acoustic background music, 90 BPM, clear and informative. [Género] voiceover in [idioma]: "[Explicación simple y directa]" Clear and well paced.

Quality: 2K commercial. Ultra HD. Clean and sharp. Natural color grading. No blur. No artifacts. Stable picture. Generate video without subtitles. Professional educational style.
```

### Template 6: Video de acción / deportes / energético (sin imagen)

```
[Descripción del atleta o personaje: edad, ropa deportiva, entorno].

[0-3s] Low angle shot, fast aggressive dolly push-in. [Atleta] bursts into frame. [Acción explosiva: sprints, jumps, dives]. Dynamic motion blur on background, sharp subject. High energy.

[3-7s] Fast follow camera, tight close-ups. [Secuencia de movimientos: close-up de cara, boots hitting ground, wide shot of full action]. Quick cuts with natural transitions. Maintain character consistency.

[7-11s] Aerial drone descending shot. [Escena más amplia del entorno deportivo]. Epic wide establishing. High contrast dramatic lighting.

[11-15s] Slow motion 120fps feel. [Momento cumbre: reach the finish, score the goal, land the jump]. Freeze frame. Hero moment. Golden rim lighting.

Audio: Energetic [hip-hop/electronic/rock] music, 110 BPM, high intensity. Ambient crowd/nature sounds. No voiceover.

Quality: 2K cinematic. Ultra HD. High contrast color grade. Sharp clarity. No blur on subject. No artifacts. Stable hero shots. Generate video without subtitles. Professional sports advertising style.
```

---

## Palabras a evitar (activan filtros de contenido)

| Evitar | Reemplazar por |
|---|---|
| ghosting | artifacts |
| conservantes | aditivos |
| preservatives | additives |
| chemical | natural |
| deepfake | (eliminar) |
| celebrity name | (eliminar — anti-deepfake) |
| realistic human face photo | use illustrated or stylized character |
| gore, violence, blood | (eliminar — violación de políticas) |

---

## Post-producción recomendada

Lo que Seedance NO hace bien y debe hacerse en post:

| Elemento | Herramienta recomendada |
|---|---|
| Textos animados en pantalla | CapCut, DaVinci Resolve, Adobe Premiere |
| Corrección de pronunciación vocal | ElevenLabs (voz en español peruano/latino) |
| Logos y branding final | CapCut, After Effects |
| Subtítulos | CapCut auto-subtítulos |
| Color grading fino | DaVinci Resolve |
| Música con licencia comercial | Epidemic Sound, Artlist |
| Extensión de video (+15s) | Usar función de extensión de Dreamina / Jimeng y unir clips |

---

## Template 7: Cortometraje animado con personajes de fruta (Pixar style)

Para personajes animados tipo Pixar con cabezas de frutas u otros elementos no humanos. Validado en producción real.

```
3D animated short film, Pixar and Illumination quality style, 
warm golden color grading. 

CHARACTER DESIGN maintain exact consistency:
- [PERSONAJE 1]: [descripción completa: tipo de fruta, ropa, proporciones, edad aparente]
- [PERSONAJE 2]: [descripción completa]
- [PERSONAJE 3]: [descripción completa si aplica]

[0:00–0:0X] [Escena con acción única]. [Personajes] [acción específica].
[Descripción de entorno]. [Iluminación]. Camera [movimiento].
EXACTLY [N] characters. Maintain character consistency.

[0:0X–0:0X] [Escena siguiente]. [Personaje] [acción].
[Entorno]. [Iluminación]. Camera [movimiento].
Maintain character consistency.

Pixar quality 3D animation throughout. Detailed character textures.
Warm golden color grading. Shallow depth of field.
Smooth fluid camera movements. High detail.
EXACTLY [N] characters in every scene. No duplicates. No extra figures.
No camera shake. No flickering. Generate video without subtitles.
1080p resolution. [ratio] format. [duración] seconds total.
```

---

## Template 8: Consistencia de personaje realista — Multi-clip

Para crear múltiples clips con el mismo personaje realista sin subir ninguna foto. Validado en producción real (mayo 2026).

**CLIP 1:**
```
Cinematic [género] scene, [estilo: thriller/drama/comercial], 
[ambiente: interior/exterior], photorealistic quality.

MAIN CHARACTER — memorize every physical detail precisely:
[género] approximately [edad] years old, [complexión],
[cabello: largo + textura + color], [tono de piel con subtono],
[ojos: forma + color], [rasgos faciales clave],
[rasgo memorable único: scar / lunar / forma de nariz / etc].
Wearing [outfit completo: cada prenda con color y material].
[Expresión base y actitud del personaje].

[0:00–0:0X] [Escena y acción única]. [Entorno específico].
[Iluminación cinematográfica]. Camera [movimiento].
Maintain character face and clothing consistency.

[Bloque de calidad].
[ratio] vertical format. [duración] seconds.
```

**CLIP 2 (y siguientes):**
```
Cinematic [mismo género/estilo] continuation.
EXACT SAME character from previous clip, identical appearance.

MAIN CHARACTER — exact same details as previous clip:
SAME [género] approximately [edad] years old, SAME [complexión],
SAME [cabello], SAME [tono de piel], SAME [ojos],
SAME [rasgos únicos], SAME [rasgo memorable].
SAME [outfit completo idéntico]. Now showing [nueva emoción].

[0:00–0:0X] [Nueva escena — entorno diferente al clip 1].
[Acción única coherente con la narrativa]. [Nueva iluminación].
Camera [movimiento]. Maintain exact character consistency from clip 1.

[Bloque de calidad — idéntico al clip 1].
[ratio] vertical format. [duración] seconds.
```

---

## Sistema anti-filtro para storyboards con personajes

Cuando el usuario tiene un storyboard y quiere animarlo, aplicar estas reglas según el contenido:

| Tipo de escena en el storyboard | Estrategia |
|---|---|
| Personajes separados, sin primer plano facial | ✅ Subir storyboard como @Image1, usar como referencia |
| 1–2 personajes con rostros visibles | ⚠️ Subir storyboard pero usar prompt con estilo Pixar 3D |
| 3+ personajes con rostros muy juntos (abrazo, festejo) | ❌ NO subir imagen — usar texto puro siempre |
| Figura sin rostro (muñeco, silueta) | ⚠️ El modelo lo animará literalmente — describir el personaje real en el prompt |
| Storyboard B&N sketch sin detalles faciales | ✅ Más seguro — menor riesgo de filtros |

**Truco del storyboard B&N:** Generar primero un storyboard en blanco y negro estilo boceto con figuras humanas de cabeza inclinada (sin rostro visible) antes de pasar a Seedance. Esto evita que Dreamina detecte múltiples rostros y active los filtros 10043300, 10001301 y 10012301.

**Truco de la cabeza inclinada:** Para personajes bebiendo, mirando al cielo o en acción donde el rostro no sea necesario, especificar "head tilted back, face NOT visible from this camera angle". Permite generar figura humana sin activar filtros.

