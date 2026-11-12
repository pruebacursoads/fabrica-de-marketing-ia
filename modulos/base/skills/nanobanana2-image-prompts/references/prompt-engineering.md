# Ingeniería de Prompts — Nano Banana 2 para Imágenes

Referencia completa para convertir cualquier idea de imagen en un prompt profesional. Basada en documentación oficial de Google Cloud, Google DeepMind, patrones de los 100 prompts probados, y comunidades verificadas (2025–2026).

---

## La fórmula universal

Todo prompt profesional para Nano Banana 2 sigue esta estructura. No todas las capas son obligatorias en todos los casos — pero omitir alguna produce resultados genéricos.

```
[VERBO DE APERTURA] + [SUJETO PRINCIPAL] + [ACCIÓN O ESTADO] +
[SUPERFICIE O ENTORNO INMEDIATO] + [CAPAS DE FONDO] +
[ILUMINACIÓN] + [DETALLES DEL SUJETO] + [CALIDAD Y CIERRE]
```

### El verbo de apertura — crítico

Nano Banana 2 procesa mejor cuando el prompt empieza con un verbo que define la operación:

| Intención | Verbo de apertura |
|---|---|
| Crear desde cero | `Create`, `Generate`, `Render` |
| Transformar una foto existente | `Transform this [foto/product/portrait] into...` |
| Mejorar manteniendo la persona | `Enhance this portrait keeping the exact same person...` |
| Cambiar solo el fondo | `Keep the exact same [person/product] — replace only the background with...` |
| Añadir efecto a producto existente | `Add a [efecto] to this product photo. The product remains exactly as shown...` |
| Corregir un problema | `Correct the [lighting/perspective/background] in this photograph...` |
| Upscale / restaurar | `Upscale and enhance this image to ultra-high definition...` |

---

## Las 6 capas del prompt de imagen

### CAPA 1 — El sujeto principal

Describir con máxima especificidad. El modelo no puede adivinar lo que no está escrito.

**Para personas:**
```
[edad aproximada], [rasgos físicos clave: color de cabello, longitud], [ropa con material específico: "tailored navy blazer over white shirt", "charcoal cotton hoodie"], [postura: "standing upright, shoulders back, arms crossed"], [expresión: "direct confident eye contact", "genuine warm smile"], [acción si aplica: "mid-stride walking toward camera"]
```

**Para productos:**
```
[forma: "slim cylindrical bottle", "square matte black box"], [dimensiones aproximadas: "250ml"], [material: "frosted glass", "brushed aluminum", "matte kraft paper"], [color con hex: "#1A1A1A matte black"], [acabado: "polished", "matte", "metallic", "textured"], [detalles: "embossed gold logo on front", "silver twist cap"], [etiqueta: "white label with minimal black typography, fully legible"]
```

**Para comida:**
```
[nombre del plato], [presentación: "fine dining plated", "rustic wooden board", "street food casual"], [temperatura percibida: "steam rising", "condensation on glass", "golden crispy crust"], [colores dominantes: "rich deep browns, vibrant green herbs, glossy sauce"]
```

**Para espacios:**
```
[tipo de espacio: "modern open-plan office", "cozy café interior", "luxury boutique"], [materiales dominantes: "polished concrete floors, exposed brick walls"], [dimensiones percibidas: "high ceilings, floor-to-ceiling windows"], [elementos de marca: "logo visible on reception desk"]
```

---

### CAPA 2 — Superficie o entorno inmediato

La superficie donde está el sujeto y los elementos en su entorno directo.

| Tipo de superficie | Descripción en el prompt |
|---|---|
| Mármol negro | `polished black marble surface with subtle veining reflections` |
| Mármol blanco | `white Carrara marble surface with natural gold veining running diagonally` |
| Madera oscura | `dark walnut wood surface with visible natural grain texture, warm tones #5C3A1E` |
| Madera clara | `light oak wood surface with fine grain, warm natural tones` |
| Metal cepillado | `brushed stainless steel surface with fine horizontal grain texture` |
| Acero reflectivo | `polished dark reflective surface resembling black mirror` |
| Tela lino | `light natural linen texture fabric, soft and organic` |
| Concreto | `raw concrete surface with subtle texture and natural imperfections` |
| Vidrio/agua | `ultra-thin layer of still water creating a perfect mirror reflection` |
| Nada / flotando | `the subject appears to float in mid-air with no visible surface support` |

**Reflexión del sujeto en superficie:**
```
A perfect specular reflection of the [product/subject] visible on the surface below
```

---

### CAPA 3 — Fondo (siempre describir las 3 capas)

```
Foreground (primer plano): [elemento más cercano a cámara — puede ser bokeh, props, manos]
Midground (plano medio): [el sujeto principal]
Background (fondo): [atmósfera, degradado, ambiente — descripción detallada]
```

**Fondos más usados y cómo describirlos:**

| Fondo | Descripción exacta en el prompt |
|---|---|
| Negro dramático | `deep gradient background from dark charcoal #1A1A1A to pure black #050505, completely blurred` |
| Blanco minimalista | `seamless white gradient background #FFFFFF to #F0F0F0 at bottom edges, clean and pure` |
| Gris neutro studio | `seamless gradient from warm light gray #D8D8D8 to soft white #F5F5F5, completely out of focus` |
| Color de marca | `seamless background using [color] #hex, smooth and out of focus creating depth` |
| Urbano bokeh | `blurred urban street scene with warm bokeh lights, buildings and city elements completely out of focus at f/1.4 aperture simulation` |
| Oficina desenfocada | `modern open office completely blurred — large windows, contemporary furniture, plants out of focus` |
| Hogar de lujo | `blurred luxury home interior with floor-to-ceiling windows, contemporary neutral decor, warm ambient light` |
| Restaurante bokeh | `warm blurred restaurant interior — candlelight bokeh, other tables blurred, pendant lighting creating warm pools` |
| Natural exterior | `blurred outdoor environment with natural light, green elements and soft natural bokeh` |
| Abstracto oscuro | `deep dark infinite background #050505, mysterious and atmospheric` |

---

### CAPA 4 — Iluminación

**Siempre nombrar:** tipo + dirección + temperatura de color + efectos secundarios.

La iluminación es la diferencia entre una foto de teléfono y una fotografía profesional.

#### Setups de iluminación principales

**Three-point studio (el más versátil):**
```
Three-point studio lighting: soft key light from upper left at 45 degrees creating gentle directional shadows, fill light from right at 40% intensity reducing harsh shadows to a 3:1 ratio, subtle rim light from behind creating natural edge separation from background
```

**Rembrandt (dramático, autoridad):**
```
Rembrandt lighting setup — key light from upper left at 45 degrees creating a triangular light patch on the shadow cheek, strong rim light from behind right creating bright separation outline, subtle fill light at 20% preventing total shadow collapse
```

**Butterfly (fashion, retratos femeninos):**
```
Classic butterfly lighting — key light directly in front slightly above face level creating even illumination with a small butterfly shadow under the nose, soft fill lights on both sides at 50% intensity for balanced professional look
```

**Golden hour (calidez, lifestyle):**
```
Golden hour simulation — warm directional key light from left at 30 degrees at color temperature 2800K creating golden warmth, subtle rim light from behind creating a glowing halo, gentle fill light preventing harsh shadows
```

**Backlight dramático (productos premium):**
```
Strong golden backlight from directly behind the subject creating a dramatic halo rim light effect, secondary soft fill light from left at 45 degrees preserving subject detail visibility
```

**Natural window (auténtico, lifestyle):**
```
Soft natural window light from upper left as primary key light creating flattering directional illumination at 5500K, subtle white reflector fill from right reducing shadows to a natural 2:1 ratio
```

**Neón bicolor (urbano, nocturno):**
```
Dramatic neon studio setup — electric [color1] #hex LED key light from left creating cool sharp highlights, neon [color2] #hex accent light from right for color contrast, the two colors clash and blend where they meet on the subject creating a [color3] transition zone
```

**Cold/Ice (bebidas, frescura):**
```
Cold blue-white key light from upper left at 6500K creating crisp cold illumination, catching every condensation droplet as a bright specular highlight, subtle blue rim light from behind creating cold atmospheric separation
```

**Warm Edison/Artisan:**
```
Warm Edison-style key light from upper left at 2700K creating golden amber illumination, subtle fill from right preventing full shadow collapse, soft backlight creating warm separation
```

#### Temperatura de color de referencia rápida

| Temperatura | Sensación | Uso |
|---|---|---|
| 2700K | Vela, Edison, muy cálido | Artesanal, comida, hogar íntimo |
| 3000K | Cálido ámbar | Restaurante, lifestyle cálido |
| 3500K | Cálido natural | Retratos dorados, lifestyle |
| 4000K | Neutro cálido | Lifestyle, hogar moderno |
| 4500K | Neutro | Corporativo cálido, productos naturales |
| 5000K | Luz día equilibrada | Estudio neutro, e-commerce |
| 5500K | Luz día natural | Exterior soleado, lifestyle natural |
| 6500K | Frío nítido | Bebidas frías, tecnología, dramático |

---

### CAPA 5 — Detalles técnicos de cámara y lente

Nano Banana 2 entiende terminología fotográfica real y la aplica.

#### Tipos de plano

| Plano | Término en inglés |
|---|---|
| Detalle extremo | `extreme macro close-up` |
| Primer plano | `close-up shot` |
| Plano medio | `medium shot` — muestra de cintura arriba |
| Plano americano | `medium wide shot` — muestra hasta rodillas |
| Plano completo | `full body shot` |
| Plano general | `wide shot` — sujeto en contexto |
| Cenital | `perfectly perpendicular 90-degree overhead shot` |
| Ángulo bajo | `low angle worm's eye view, camera close to ground, angled upward` |
| 45 grados | `three-quarter view from front-right at 45 degrees horizontal rotation` |
| Over the shoulder | `over-the-shoulder perspective from behind, looking past shoulder toward subject` |

#### Lentes y profundidad de campo

| Efecto | Descripción |
|---|---|
| Gran angular / espacioso | `wide-angle lens, expanded space perception` |
| Natural / retrato | `85mm portrait lens, natural perspective` |
| Íntimo / comprimido | `telephoto lens, compressed background` |
| Profundidad mínima | `shallow depth of field, f/1.4 aperture simulation, smooth bokeh blur` |
| Todo en foco | `deep focus, everything sharp from foreground to background` |
| Macro extremo | `macro lens, razor sharp focal point with smooth bokeh toward edges` |

#### Ángulos especiales

| Ángulo | Cómo describir |
|---|---|
| Frontal puro | `camera at product eye level, perfectly centered, zero tilt — pure frontal view` |
| Desde abajo | `extremely low camera position at ground level, angled upward at 20-30 degrees` |
| Flat lay cenital | `perfectly perpendicular 90-degree top-down view, centered directly above subject` |
| Diagonal 45° | `camera at product mid-height level, three-quarter view at 45 degrees` |
| Back/Lateral | `camera positioned directly behind the product at 180 degrees from front` |

---

### CAPA 6 — Efectos especiales

Para cuando el alumno quiere añadir un efecto sobre el sujeto.

#### Efectos de agua y líquidos

```
SPLASH: an explosive crystalline water splash erupting from the base in all directions — frozen in motion at high shutter speed simulation, creating a perfect crown shape with individual water droplets suspended mid-air catching light like jewels. Water: perfectly transparent and crystalline — not milky or opaque.

CONDENSACIÓN: heavy cold condensation on the surface — hundreds of tiny water droplets clinging to the outer surface catching light as brilliant specular highlights, showing the product is ice cold.

REFLEJO EN AGUA: the product standing on an ultra-thin layer of still water — creating a perfect mirror reflection below. Subtle circular ripples radiating from the base. Water: perfectly transparent with slight blue tint.

HIELO: surrounded by crushed and block ice — irregular chunks of clear ice in blue and white tones with internal light refraction.
```

#### Efectos de atmósfera

```
HUMO DE COLOR: rich volumetric colored smoke flowing organically around the subject — rising from below and swirling in layers. Colors: deep [color1] and [color2] smoke layers interweaving. Background: pure black making the colored smoke glow luminously.

VAPOR (caliente): natural steam rising in delicate wisps from the hot surface, catching the backlight and becoming luminous and translucent.

PARTÍCULAS DE LUZ: small floating particles of light dust surrounding the subject, giving a magical atmospheric quality.

NIEBLA BAJA: subtle atmospheric mist in the lower third of the frame, soft and ethereal, not obscuring the subject.
```

#### Efectos de impacto visual

```
POLVO DE COLORES: dynamic explosion of fine colored powder erupting outward — powder particles frozen in motion creating an explosive radial burst pattern. Colors: vibrant [color1] and [color2] powder clouds mixing. Background: pure black for maximum contrast. Powder: dense and opaque near the base, becoming lighter and more particle-like toward the edges.

EXPLOSIÓN DE INGREDIENTES: the product's key ingredients floating and orbiting around it in a dynamic arranged explosion — all elements suspended in mid-air at different distances. Each ingredient: sharp, perfectly lit, realistic texture.

LLUVIA DE INGREDIENTES: key ingredients falling from above in a natural rain pattern — rotating naturally as they fall at different speeds and distances, sharp near the subject and increasingly blurred higher up.

LEVITACIÓN: the product floats in mid-air, slightly tilted at 10-15 degrees. Below: a dramatic pool of light radiating upward from the surface. Atmosphere: small floating particles of light dust adding to the magical effect.

LUZ INTERIOR: the product appears to contain an intense light source within — a powerful glow radiates from inside through translucent areas. The light color matches the product's brand color. Background: pure black for maximum impact.
```

#### Efectos de neón

```
NEÓN BICOLOR: electric [color1] #hex neon light washing the left half, [color2] #hex neon illuminating the right half — the two colors clash and blend where they meet creating a [color3] transition zone. The dark reflective surface below shows vivid neon color reflections.
```

#### Efectos florales y botánicos

```
FLORES NATURALES: surrounded by fresh natural botanical elements — [tipo de flores] in [colores] partially in frame creating depth layers, green [tipo] leaves, scattered petals on the surface. Flowers look freshly placed, not artificially arranged. Lighting: soft natural diffused daylight.
```

---

## Protocolos por categoría

### PROTOCOLO A — Foto de perfil / Retrato profesional

**Anatomía del prompt:**
```
Transform this portrait into a [estilo: premium executive / lifestyle / editorial / LinkedIn] professional headshot.

Keep the exact same person, pose, clothing and expression.

Background: [descripción del fondo con hex y tratamiento de blur]

Lighting: [setup de iluminación específico con dirección, intensidad y temperatura]

Skin: natural retouching preserving real skin texture, clean pores visible, no plastic effect, controlled shine.

Eyes: sharp focus with natural catchlights in both pupils.

Color grading: [tono de color grade: neutral / warm / cool / cinematic].

Aspect ratio 1:1. Ultra-detailed, 8K resolution, professional [tipo] headshot photography, sharp focus, no watermark.
```

**Negative prompt estándar para retratos:**
```
blurry, overexposed, harsh shadows, plastic skin, heavy retouching, busy background, low quality, yellow tint, red skin, different person, changed pose, changed clothing, changed facial features, artificial looking skin
```

---

### PROTOCOLO B — Render de producto (sin persona)

**Anatomía del prompt:**
```
Transform this product photo into an ultra-high-end commercial product photography render.

[Descripción física del producto: forma, material, color hex, acabado, etiqueta]

Place the product [posición: centered / slightly left / center-right] on [superficie detallada].

Background: [descripción con hex y tratamiento].

Lighting: [setup de iluminación completo con dirección, intensidad, efectos].

[Efecto especial si aplica: splash / smoke / glow / etc.]

Product label and details must be razor sharp and perfectly legible.

Color grading: [descripción del grade]. No props, no distractions — product as absolute hero.

Ultra-detailed, 8K resolution, award-winning commercial product photography, sharp focus, professional color grading, no watermark.
```

**Negative prompt estándar para producto:**
```
blurry, flat lighting, low quality, distorted product shape, incorrect label, overexposed highlights, amateur lighting, extra objects, watermark, plastic looking surface, wrong colors, blurry text on label
```

---

### PROTOCOLO C — Efecto especial sobre producto

**Anatomía del prompt:**
```
Transform this product photo into a [nombre del efecto] commercial product photography render.

Place the product as the centered hero with [descripción del efecto específico y su comportamiento físico].

Background: [fondo que maximice el contraste con el efecto].

Lighting: [iluminación que potencia el efecto].

Product: [instrucción de preservación] — perfectly sharp, label fully legible, original colors preserved.

Color grading: [grade que complementa el efecto].

Ultra-detailed, 8K resolution, award-winning [tipo] product photography, sharp focus, no watermark.
```

---

### PROTOCOLO D — Persona con producto / UGC

**Anatomía del prompt:**
```
Create a [lifestyle / influencer-style / action / luxury] product [in-use / presentation / group] photography render.

Show a [descripción de la persona: edad, apariencia, ropa con material] [acción específica con el producto].

[Si manos solo: "A pair of well-groomed hands hold the product naturally — clean nails with subtle neutral manicure"]

The product is the primary focus — [cómo está siendo usado/sostenido].

Background: [descripción del entorno desenfocado].

Lighting: [iluminación natural o de estudio apropiada para el contexto].

Product: clearly visible, label identifiable, colors accurate.

Color grading: [grade de lifestyle o editorial].

Ultra-detailed, 8K resolution, professional lifestyle photography, [sharp focus on product / natural authentic feel], no watermark.
```

**Negative prompt estándar para persona con producto:**
```
blurry product, product label hidden, sharp background, harsh studio lighting, unnatural pose, forced smile, stock photo generic feel, low quality, wrong scale between person and product, product not visible
```

---

### PROTOCOLO E — Fotografía de comida y bebida

**Anatomía del prompt:**
```
Transform this [food/beverage] photo into a [dramatic dark fine dining / bright overhead editorial / warm rustic artisan / cold refreshing beverage] photography render.

Place the [dish/drink] as the absolute hero [posición y descripción del plato o vaso].

[Descripción de superficie con textura específica].

Background: [descripción del fondo con hex].

Lighting: [setup de iluminación específico para comida: siempre nombrar temperatura].

[Efectos específicos: steam rising / condensation / splash / flowing chocolate / etc.]

Every ingredient visible: textures sharp, colors vibrant and accurate, [descripción de elementos específicos del plato].

Color grading: [grade apropiado: warm fine dining / cool refreshing / warm artisan].

Ultra-detailed, 8K resolution, award-winning [tipo] food photography, sharp focus, no watermark.
```

**Negative prompt estándar para comida:**
```
unappetizing colors, flat lighting, blurry food, washed out, cold blue tones on warm food, warm tones on cold beverage, low quality, messy plating, static drink with no condensation or steam, plastic looking food
```

---

### PROTOCOLO F — Moda y ropa

**Anatomía del prompt:**
```
Transform this [clothing/accessory] photo into a [premium e-commerce / luxury boutique / editorial fashion / lifestyle] photography render.

[Si solo la prenda: descripción del garment — material, silhouette, detalles, colores]

[Si con persona: descripción de la persona + cómo lleva la prenda]

Background/surface: [descripción apropiada para el estilo].

Lighting: [setup de iluminación para moda].

Fabric textures: perfectly rendered — weave, stitching, [detalles específicos] razor sharp and accurate.

Color grading: [grade de moda / editorial].

Ultra-detailed, 8K resolution, professional [fashion/editorial/e-commerce] photography, every stitch sharp, no watermark.
```

---

### PROTOCOLO G — Cambio de postura, contexto o fondo

**Anatomía del prompt:**
```
Transform this portrait keeping the exact same person's face, hair and clothing — change ONLY the [body posture / environment / lighting / background].

New [posture/environment]: [descripción detallada de lo nuevo].

[Si es postura nueva: descripción física exacta de la postura + qué comunica corporalmente]

[Si es entorno nuevo: descripción del nuevo ambiente con materiales y elementos]

New lighting: [descripción del nuevo setup de luz apropiado para el nuevo contexto].

Color grading: [grade del nuevo entorno].

Ultra-detailed, 8K resolution, [tipo] portrait photography, no watermark.
```

**Negative prompt crítico para cambio de contexto:**
```
changed face, changed facial features, changed clothing, changed hair, different person, low quality, obvious photo manipulation, inconsistent lighting between subject and new environment, wrong scale
```

---

### PROTOCOLO H — Mejora y corrección de imagen existente

**Determinar el problema y aplicar el protocolo correcto:**

**H1 — Upscale / Baja resolución:**
```
Upscale and enhance this low-resolution image to ultra-high definition quality. Intelligent upscaling with AI detail reconstruction — recreate all fine details lost in the original. [Faces: reconstruct natural skin texture, pores, hair strands / Products: restore label text, material textures / Architecture: restore edge sharpness]. Eliminate all pixelation and staircase artifacts. Restore full color accuracy. Output: as if originally shot on a high-end camera at full resolution. Ultra-detailed, 8K resolution output, professional image restoration, no watermark.
```

**H2 — Corrección de iluminación:**
```
Correct the lighting in this [underexposed/overexposed/harshly lit/flat] photograph. [Describir el problema específico]. Apply professional lighting correction: [instrucciones específicas de corrección]. The subject matter unchanged — only lighting quality transformed. Natural skin tones restored, product colors accurate. Ultra-detailed, 8K resolution, professional photo lighting correction, no watermark.
```

**H3 — Eliminación de fondo:**
```
Remove the existing background from this image completely and replace it with [descripción del nuevo fondo]. Background removal: precise edge detection on all subjects — [hair strands/clothing edges/product contours] — no harsh cuts, no missing edge detail. New background: [descripción detallada]. [Drop shadow: add subtle realistic drop shadow beneath matching original lighting direction]. Edge quality: all subject edges appear naturally separated — no halo, no fringing. Ultra-detailed, 8K resolution, professional background removal and replacement, seamless composite, no watermark.
```

**H4 — Corrección de color:**
```
Enhance the color grading and contrast of this flat/dull photograph. Step 1 — Color correction: correct white balance, fix [color cast], restore accurate skin tones. Step 2 — Tone curve: deepen blacks, lift whites, create natural S-curve contrast. Step 3 — Color grading: apply [warm lifestyle / clean commercial / cinematic] grade appropriate to the content. Step 4 — Selectively boost key colors to their natural vibrant state. Final: alive, three-dimensional, professional. Ultra-detailed, 8K resolution, professional color grading, no watermark.
```

**H5 — Eliminación de elementos no deseados:**
```
Clean this photograph by removing [describir exactamente qué eliminar: background people / cables / unwanted objects / signage] while keeping the main subject completely intact. Removal technique: content-aware reconstruction that fills naturally — walls match wall texture, floors match floor pattern. Removal must be completely invisible at full resolution. Main subject: completely untouched. Ultra-detailed, 8K resolution, professional image retouching, no watermark.
```

**H6 — Corrección de perspectiva:**
```
Correct all perspective and lens distortion in this photograph. Vertical perspective: correct converging verticals — [buildings/walls/products] should have perfectly parallel vertical lines. Barrel distortion: correct outward bulging from wide-angle lens. Tilt correction: level any rotation. After geometric correction: crop to largest clean rectangle. Ultra-detailed, 8K resolution, professional geometric correction, no watermark.
```

**H7 — Transformación amateur a profesional:**
```
Transform this casual amateur photograph into a professional advertising campaign quality image. Keep the exact same subject — [person/product/scene] — unchanged. Transform: background → [nuevo fondo profesional], lighting → [setup profesional], composition → [reencuadre profesional], retouching → natural professional polish, color grading → [grade comercial apropiado]. Final standard: indistinguishable from a professionally produced campaign photograph. Ultra-detailed, 8K resolution, award-winning commercial photography quality, no watermark.
```

---

## Prompt negativo universal

Usar como base y añadir restricciones específicas según la categoría:

```
blurry, low quality, flat lighting, amateur photography, distorted proportions, wrong colors, plastic skin effect, heavy artificial retouching, watermark, overexposed highlights with no detail, crushed blacks with no shadow detail, generic stock photo feel, obvious AI artifacts, inconsistent lighting direction, wrong shadow physics, unnatural skin texture, low resolution, pixelated, noise artifacts
```

---

## Técnicas avanzadas

### 1. Material cues para estabilizar el sujeto

Cuando hay una persona, describir el material de la ropa ayuda al modelo a mantener consistencia visual:

```
"charcoal cotton hoodie" → perfil de reflexión de luz específico
"tailored navy wool blazer" → textura y caída natural del tejido
"white silk blouse" → translucencia y brillos correctos
"dark denim jeans" → textura de tela específica con desgaste
```

### 2. Instrucciones de preservación explícitas

Para edición de fotos existentes, siempre especificar qué preservar:

```
"Keep the exact same person, face, hair and clothing — change ONLY the background and lighting"
"Maintain the product's exact label, color, shape and proportions — replace only the background"
"Preserve all original content of the scene — remove ONLY [elemento específico]"
```

### 3. Physics anchors para efectos

Los efectos se ven reales cuando se describe el comportamiento físico:

```
"frozen at high shutter speed simulation" → agua o polvo congelado
"crystalline and transparent, not milky or opaque" → agua limpia
"dense and opaque near the base, becoming lighter toward the edges" → polvo realista
"viscous rivers flowing down the sides" → chocolate o caramelo
"individual droplets clinging to the surface catching light as brilliant specular highlights" → condensación real
```

### 4. Iteración conversacional

Nano Banana 2 permite refinar sin reescribir el prompt completo. Después de la primera generación, guiar al alumno con ajustes conversacionales:

- `"Make the background darker and more dramatic"`
- `"Increase the golden warmth in the lighting"`
- `"Make the product label more legible and sharper"`
- `"Add more condensation droplets on the surface"`
- `"Shift the color grade to cooler tones"`
- `"Move the subject slightly to the left"`

### 5. Search Grounding para referencias reales

Para productos, lugares o personas reales conocidas:

```
"Use Google Search to find visual references for [nombre del producto/lugar real], then create [tipo de imagen] incorporating the authentic visual characteristics you found"
```

---

## Ejemplos completos por categoría

### Ejemplo 1 — Foto de perfil LinkedIn (desde foto propia)

```
Transform this portrait into a perfect LinkedIn professional headshot. Keep the exact same person, pose, clothing and expression.

Background: seamless gradient from corporate navy blue #1B3A6B to deep blue #0D2240, completely out of focus, creating a trustworthy professional atmosphere.

Lighting: classic butterfly lighting — key light directly in front slightly above face level creating even illumination with a small shadow under the nose, soft fill lights on both sides at 50% intensity for balanced professional look, subtle rim light from behind for separation.

Skin: clean even tone, natural texture preserved, minimal retouching, professional appearance. Eyes: direct confident gaze, sharp focus, clear catchlights projecting trustworthiness.

Color grading: cool professional tones, corporate magazine quality.

Aspect ratio 1:1. Ultra-detailed, 8K resolution, professional LinkedIn headshot photography, sharp focus, no watermark.

Negative prompt: casual setting, warm tones, blurry, flat lighting, plastic skin, heavy retouching, different person, changed pose, distracting background elements, changed facial features.
```

### Ejemplo 2 — Render de producto premium desde foto de teléfono

```
Transform this product photo into an ultra-high-end commercial product photography render.

The product: a slim 250ml glass bottle with a white label showing the brand name in clean black serif typography, silver metallic twist cap, frosted glass finish.

Place the product centered slightly left on a polished black marble surface with a perfect specular reflection below. Background: deep gradient from dark charcoal #1A1A1A to pure black #050505, completely blurred.

Lighting: three-point studio setup — key light from upper left at 45 degrees creating sharp highlights on product edges and surfaces, soft fill light from right at 30% intensity, strong rim light from behind creating a bright separation outline around the entire product silhouette. Add subtle volumetric light rays from upper left touching the product surface.

Product label and details must be razor sharp and perfectly legible. Color grading: rich deep shadows, bright specular highlights, vibrant product colors fully preserved. No props, no distractions — product as absolute hero.

Ultra-detailed, 8K resolution, award-winning commercial product photography, sharp focus, professional color grading, no watermark.

Negative prompt: blurry, flat lighting, white background, low quality, distorted product shape, incorrect label, overexposed highlights, amateur lighting, extra objects, wrong colors.
```

### Ejemplo 3 — UGC / Persona sosteniendo producto (sin imagen de persona)

```
Create a lifestyle product presentation photography render.

Show a young woman in her late 20s with natural warm skin tones, wearing a white linen casual shirt, holding the product up naturally at chest height with one hand, slight natural smile conveying genuine enthusiasm. The product label faces directly toward camera.

Background: blurred modern home interior with warm afternoon light — white walls, wooden furniture elements, a plant partially visible — completely out of focus creating an authentic lifestyle atmosphere.

Lighting: soft natural window light from the left at 4500K creating warm flattering illumination on face and product, subtle fill light from right maintaining natural shadows.

Product: perfectly visible and sharp, label fully legible, colors accurate. Person appearance: natural relatable attractiveness, clean skin, genuine and approachable expression.

Color grading: warm bright social media lifestyle aesthetic, vibrant skin tones.

Ultra-detailed, 8K resolution, professional lifestyle social media content photography, no watermark.

Negative prompt: eyes looking away from camera, product hidden or facing wrong direction, harsh shadows on face, stiff formal pose, forced unnatural expression, low quality, dark background, wrong scale.
```

### Ejemplo 4 — Efecto splash de agua sobre producto existente

```
Transform this product photo into a dynamic water splash commercial product photography render.

The product remains exactly as shown — perfectly sharp, label fully legible, original colors and shape preserved.

Add an explosive crystalline water splash erupting from the product's base in all directions — frozen in motion at high shutter speed simulation, creating a perfect crown shape rising on both sides with individual water droplets suspended in mid-air catching light like jewels. A single large crystal water drop falls from above toward the product creating the primary impact moment.

Background: deep dark gradient from #050520 to pure black creating maximum contrast for the transparent water.

Lighting: strong backlight from behind creating translucency through the water, key light from upper left creating catchlights in every individual droplet, rim light on the product edges. Water: perfectly transparent and crystalline — not milky or opaque.

Color grading: deep dark background, electric blue water tones, frozen motion clarity.

Ultra-detailed, 8K resolution, award-winning water splash product photography, sharp focus, no watermark.

Negative prompt: blurry water, milky opaque water, blurry product, bright background, static water, wrong water physics, product altered, low quality.
```

### Ejemplo 5 — Transformación de foto amateur a campaña

```
Transform this casual amateur photograph into a professional advertising campaign quality image. Keep the exact same subject — [persona/producto] — completely unchanged in identity and appearance.

Transform everything else:

Background: replace with a premium clean studio-quality environment appropriate to the subject — seamless gradient from warm light gray #D8D8D8 to soft white #F5F5F5.

Lighting: apply full three-point studio professional lighting — soft key light from upper left at 45 degrees, fill light from right at 40% intensity, subtle rim light from behind for separation. Eliminate all amateur lighting characteristics.

Retouching: natural professional polish — skin clean and natural preserving real texture, product colors accurate and saturated, environment pristine.

Composition: reframe to professional advertising composition with subject following rule of thirds, appropriate breathing room.

Color grading: professional commercial grade appropriate to the content type — warm neutral with slight saturation boost.

Final standard: the output must be indistinguishable from a professionally produced advertising photograph.

Ultra-detailed, 8K resolution, award-winning commercial advertising photography quality, no watermark.

Negative prompt: subject altered or changed, amateur lighting characteristics remaining, obvious AI manipulation artifacts, over-processed unnatural result, low quality remaining in any area.
```
