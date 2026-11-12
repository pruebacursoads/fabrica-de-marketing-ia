# Ingeniería de Prompts — Nano Banana 2 para Flyers y Piezas Publicitarias

Referencia completa basada en la guía oficial de Google Cloud, Google AI Developers, Deep Dream Generator, eWeek y Freepik (2025–2026).

---

## La fórmula de 7 capas (para flyers profesionales)

```
[ESTILO VISUAL] + [COMPOSICIÓN Y JERARQUÍA] + [ILUMINACIÓN] +
[PROTAGONISTA / PRODUCTO] + [TIPOGRAFÍA Y TEXTOS] +
[PALETA, FONDO Y EFECTOS] + [CALIDAD Y CIERRE]
```

Cada capa es obligatoria. Saltarse una produce un resultado genérico.

---

## MODO A — Solo texto (sin imágenes de referencia)

Usa cuando el alumno no tiene logo ni foto para subir. La descripción debe ser tan específica que el modelo no necesite adivinar nada.

### Anatomía completa del prompt

```
[TIPO DE PIEZA Y ESTILO]
[tipo exacto: flyer de evento / portada de redes / banner publicitario / póster de producto]
[estilo visual: movimiento artístico o referencia concreta — "editorial Scandinavian minimalism", "luxury cosmetics campaign", "urban streetwear graphic", "warm handmade artisan market"]

[COMPOSICIÓN Y JERARQUÍA]
Protagonista visual (60% del espacio): [qué elemento domina y dónde está posicionado]
Elemento de apoyo (30%): [qué complementa y cómo lo hace]
Detalles (10%): [logo, datos, íconos secundarios]
Distribución espacial: [regla de los tercios / diagonal / centrado / off-center con intención]
Profundidad de capas:
  — Primer plano: [elemento más cercano al espectador]
  — Plano medio: [protagonista o producto principal]
  — Fondo: [atmósfera, textura, degradado, ambiente]
Confirmación de zonas activas: every zone of the design has a visual purpose — no empty unused spaces

[ILUMINACIÓN]
Tipo: [soft studio key light / dramatic single overhead spotlight / golden backlight / neon glow / natural window light]
Dirección: [from above-left at 45° / from behind the subject / from below for drama]
Temperatura: [warm 3200K amber glow / cool 6500K blue-white / neutral 5000K daylight]
Efectos secundarios: [rim lighting separating subject from background / god rays piercing through / lens flare from upper right / soft bokeh on background]

[PROTAGONISTA O PRODUCTO]
Descripción física exacta: [forma, material, color con hex, acabado, detalles — "matte black cylindrical bottle, 250ml, with embossed gold logo and metallic twist cap"]
Postura o presentación: [ángulo de presentación, orientación, acción si aplica]
Relación con el espectador: [invita / desafía / inspira / seduce / informa]
Estilo de render: [photorealistic commercial product shot / illustrated 3D render / hybrid photo-illustration]

[TIPOGRAFÍA Y TEXTOS — todos entre comillas]
Título principal:
  Texto: "[TEXTO EXACTO AQUÍ]"
  Estilo: [familia tipográfica + peso + características — "bold condensed white sans-serif, all caps, letter-spacing tight"]
  Posición: [upper third centered / lower left / diagonal overlay]
  Tratamiento: [efecto, sombra, degradado, glow — "white text with subtle golden glow and soft drop shadow"]

Subtítulo:
  Texto: "[texto exacto]"
  Estilo: [complementario al título, más ligero — "thin italic sans-serif in soft gray #C0C0C0"]

CTA visual dentro del flyer:
  Texto: "[TEXTO DEL BOTÓN O LLAMADA A LA ACCIÓN]"
  Formato: [pill button / badge circular / texto destacado con subrayado / tag con fondo de color]
  Color: [hex específico del acento]

Datos adicionales:
  "[fecha, hora, lugar, precio, contacto, URL]"
  Estilo: [small, clean, legible — "small regular sans-serif in white #FFFFFF, bottom center"]

[PALETA Y FONDO]
Color dominante: [hex — nombre — X% del diseño — justificación emocional]
Color secundario: [hex — nombre — X% del diseño]
Color acento: [hex — nombre — usado en CTA y detalles críticos]
Color texto principal: [hex — garantiza contraste legible en pantalla móvil pequeña]
Lógica de contraste: [cómo los colores garantizan legibilidad]
Fondo detallado: [descripción específica — "gradient from deep navy #0D1B2A at top to black #050505 at bottom, with floating golden light particles in the upper right quadrant, medium density, soft bokeh effect"]

[EFECTOS Y DETALLES DE PRODUCCIÓN]
Efectos de imagen: [grain 15% for analog feel / subtle vignette / anamorphic horizontal lens flare / glassmorphism overlay card]
Elementos gráficos: [thin gold geometric lines framing the composition / circular badge in upper right / diagonal stripe texture in background]
Referencias estéticas: [2-3 marcas o campañas concretas como norte visual — "inspired by Dior fragrance print campaigns, Balenciaga editorial aesthetic, and Spotify's bold typographic style"]

[CALIDAD]
ultra-detailed, 8K resolution, award-winning commercial advertising design, sharp focus, professional color grading, no watermark
```

---

## MODO B — Con referencias visuales (logo / foto de producto / flyer de referencia)

Usa cuando el alumno tiene imágenes para subir. El prompt cambia: las imágenes anclan el diseño y el texto describe qué hacer con ellas.

### Fórmula oficial de Google para multimodal

```
[Referencias subidas] + [Instrucción de relación] + [Nuevo escenario / composición]
```

### Caso B1 — Logo como referencia de marca

```
Using the provided logo as the brand anchor, [descripción de qué hacer con el logo: mantenerlo intacto en posición específica, extraer su paleta de colores, replicar su estilo tipográfico]. Create a [tipo de pieza] that respects the brand identity: [colores de la marca extraídos de la imagen]. [Resto del prompt con la fórmula de 7 capas].
```

**Ejemplo:**
```
Using the provided brand logo as the visual anchor, preserve it exactly in the upper center third of the design. Extract its color palette — deep forest green #1A4A2E and warm cream #F5E6C8 — as the dominant and secondary colors throughout. Create a professional event flyer for a farmers market. The protagonist is a flat-lay overhead shot of fresh organic vegetables arranged artistically in the center. Typography: "MERCADO VERDE" in bold condensed serif font, forest green on cream background, upper section. Below: "Todos los sábados" in thin italic, smaller size. CTA badge: "Entrada libre" in cream text on circular green badge, lower right. Background: warm cream textured paper with subtle grain. Lighting: soft warm natural overhead light. ultra-detailed, 8K resolution, award-winning commercial design, no watermark.
```

### Caso B2 — Foto de producto como referencia

```
Using the provided product image as the hero element, place it [posición y ángulo exacto] in the composition. Maintain the product's exact appearance, colors, and branding. [descripción del entorno, iluminación y composición que rodea al producto]. [Tipografía, CTA y demás capas].
```

**Ejemplo:**
```
Using the provided product bottle as the hero element, place it center-right in a dramatic hero shot, slightly tilted at 15 degrees, occupying 55% of the vertical space. Maintain the product's exact label, color, and cap design. Surround it with an explosion of fresh citrus slices and water droplets suspended mid-air in ultra slow motion. Background: gradient from deep black #0A0A0A to dark charcoal #1C1C1C. Lighting: strong golden backlight from above creating a dramatic rim light around the bottle, separating it from the dark background. Typography: "NUEVA FÓRMULA" in bold white condensed sans-serif, upper left third. Subtitle: "Energía real, sin azúcar" in thin italic light gray #B0B0B0. CTA pill button: "DESCÚBRELA" in black text on bright golden #F5C400 background, bottom center. ultra-detailed, 4K resolution, award-winning beverage commercial photography style, no watermark.
```

### Caso B3 — Flyer de referencia (replicar o mejorar estilo)

```
Using the provided reference flyer as the creative direction, [elegir: replicate this exact style / improve this design maintaining its essence / use it only as aesthetic reference]. [Describir qué del flyer original se mantiene: paleta, composición, tipografía]. [Describir qué se mejora o cambia]. [Prompt completo con la fórmula de 7 capas].
```

---

## Vocabulario de composición

### Posicionamiento espacial

| Zona | Términos en inglés |
|---|---|
| Tercio superior izquierdo | `upper left third` |
| Tercio superior centrado | `upper center third` |
| Tercio superior derecho | `upper right third` |
| Centro del diseño | `dead center / centered focal point` |
| Tercio inferior izquierdo | `lower left third` |
| Tercio inferior centrado | `lower center third` |
| Fondo completo | `full-bleed background` |
| Diagonal descendente | `diagonal composition from upper-left to lower-right` |

### Distribución de capas (siempre describir las 3)

```
Foreground (primer plano): [elemento más cercano — puede ser tipografía o detalle de producto]
Midground (plano medio): [protagonista principal — producto, persona, concepto]
Background (fondo): [atmósfera, textura, degradado, ambiente]
```

### Regla de zonas activas (de tu PDF — crítica)

Cada zona del diseño debe tener un rol visual claro. Al finalizar el prompt, añadir:
`every zone of the design has a clear visual purpose — no empty unused spaces, no unintentional blank areas`

---

## Vocabulario de iluminación

| Estilo | Descripción en el prompt |
|---|---|
| Estudio limpio | `clean studio three-point lighting: soft key light from left, subtle fill from right, gentle rim light separating subject from background` |
| Backlight dramático | `strong golden backlight from directly behind subject, creating a dramatic halo rim light effect` |
| God rays | `cinematic god rays piercing through from upper left, warm amber #F5A623 light beams at 45 degrees` |
| Hora dorada | `warm golden hour sunlight from the left at 10 degrees above horizon, casting long warm shadows` |
| Neón nocturno | `neon sign glow in deep magenta #FF00FF and electric blue #00FFFF, wet surface reflections, night atmosphere` |
| Luz de vela/artesanal | `soft warm candlelight from below-left, creating intimate amber glow, rustic and handmade feel` |
| Spotlight dramático | `single hard spotlight from directly above, creating sharp circular light pool on the subject, everything else in darkness` |
| Luz difusa natural | `soft diffused overcast natural light, no harsh shadows, even and clean illumination` |

---

## Vocabulario tipográfico

### Estilos que Nano Banana 2 ejecuta bien

| Efecto tipográfico | Descripción en el prompt |
|---|---|
| Bold editorial | `bold condensed sans-serif, all caps, tight letter-spacing, high visual weight` |
| Lujo / premium | `elegant thin serif font, wide letter-spacing, all caps, gold #D4AF37 color` |
| Manuscrita artesanal | `flowing handwritten script font, organic and imperfect, warm ink texture` |
| Retro / vintage | `vintage condensed display font with slight distress texture, retro color palette` |
| Tipografía 3D | `bold 3D extruded letterforms emerging from the surface, metallic gold finish, deep drop shadow` |
| Minimalista | `ultra-thin sans-serif, generous whitespace, lowercase, soft gray #888888` |
| Street / urbano | `heavy graffiti-style display font, spray paint texture edges, high contrast` |

### Reglas de texto para Nano Banana 2 (oficiales de Google)

1. **Siempre usar comillas** para el texto exacto: `"OFERTA ESPECIAL"`, `"50% OFF"`
2. **Describir el font por nombre si se conoce**: `"Century Gothic 12px"`, `"Brush Script flowing font"`
3. **Text-first hack**: para diseños con mucho texto, primero generar el concepto de textos conversacionalmente, luego pedir la imagen con ese texto definido
4. **Multiidioma**: especificar idioma si el texto es en español: `text in Spanish: "GRAN OFERTA"`

---

## Vocabulario de efectos y atmósfera

### Efectos de fondo

| Efecto | Descripción en el prompt |
|---|---|
| Degradado premium | `gradient from deep navy #0D1B2A at top to pure black #050505 at bottom` |
| Partículas de luz | `floating golden light particles in the upper right quadrant, medium density, soft bokeh effect` |
| Bokeh | `soft circular bokeh lights in the background, warm golden tones, shallow depth of field` |
| Textura papel | `warm cream textured paper background with subtle grain and soft worn edges` |
| Glassmorphism | `frosted glass card overlay with subtle transparency, white border with 20% opacity, backdrop blur effect` |
| Grunge / urban | `concrete wall texture background with subtle graffiti undertones and urban grit` |
| Marble luxury | `white Carrara marble surface background with delicate gray veining` |
| Smoke / mist | `atmospheric smoke and mist in the lower third, soft and ethereal` |

### Efectos de imagen

| Efecto | Descripción |
|---|---|
| Grain analógico | `subtle film grain texture at 15% opacity, analog photography feel` |
| Viñeta | `soft vignette darkening the edges by 20%, focusing attention on the center` |
| Lens flare | `anamorphic horizontal lens flare in the upper right, warm golden tones` |
| Chromatic aberration | `subtle chromatic aberration on the edges for a digital glitch aesthetic` |
| Halftone retro | `vintage halftone dot pattern overlay at 10% opacity` |

---

## Paleta y referencias estéticas por categoría

### Por sector / tipo de negocio

| Sector | Paleta recomendada | Referencias estéticas |
|---|---|---|
| Bebidas / alimentos | Amber #D4741A + negro #0A0A0A + crema #F5E6C8 | Coca-Cola campaign, Heineken premium ads |
| Fitness / deporte | Eléctrico #00E5FF + negro #000000 + blanco puro | Nike campaign, Adidas Black Series |
| Lujo / premium | Oro #D4AF37 + negro profundo #0D0D0D + blanco hueso #F8F4EE | Dior fragrance, Chanel beauty |
| Salud / bienestar | Verde salvia #7DAA7B + blanco #FFFFFF + nude #E8D5C4 | Goop editorial, Lululemon campaigns |
| Tecnología | Azul eléctrico #0057FF + negro #0A0A0A + blanco | Apple product ads, Google brand |
| Artesanal / local | Terra cotta #C4602C + crema #F5E6C8 + verde hoja #2D5A27 | Farmer's market aesthetic, Etsy brand |
| Educación / cursos | Azul royal #2563EB + blanco + acento coral #FF6B6B | Coursera, MasterClass ads |
| Eventos / fiestas | Magenta #FF006E + dorado #FFD700 + negro | Spotify campaign, festival branding |
| Inmobiliaria | Azul marino #1A2B4A + dorado #C9A84C + blanco | JLL, CBRE premium brand |
| Restaurante premium | Negro #0A0A0A + dorado #D4AF37 + rojo vino #6B1A1A | Nobu, Cipriani restaurant branding |

---

## Plantillas completas por tipo de flyer

### Template 1: Spot de producto — Sin imagen de referencia

```
Commercial advertising poster for [producto]. Style: [estilo visual — ej: "high-end beverage campaign inspired by Heineken premium ads and Red Bull editorial photography"].

COMPOSITION: The [producto] occupies the center of the design as the hero element (60% of vertical space), placed slightly off-center to the right. On the left, [elemento dinámico: explosión de ingredientes / splash de líquido / ingredientes flotando] fills 30% of the space. The remaining 10% is distributed between the logo zone in the upper left and the text hierarchy at the bottom. Every zone has a clear visual purpose — no empty unused spaces.

PROTAGONIST: [Descripción física exacta del producto: "a slim dark glass bottle, 330ml, with a minimalist white label showing the brand name in bold black serif font, metallic silver cap, with condensation droplets on the glass surface"].

LIGHTING: [tipo de iluminación: "Strong golden backlight from directly behind the bottle, creating a dramatic halo rim light. Secondary soft fill light from the left at 45 degrees. Water droplets catch the backlight creating micro-specular highlights"].

BACKGROUND: [descripción de las 3 capas: "Foreground: fresh citrus slices in extreme macro detail. Midground: the hero bottle. Background: gradient from deep black #0A0A0A at center to dark forest green #0A1F0A at edges, with soft bokeh ambient light"].

TYPOGRAPHY:
Title: "[NOMBRE DEL PRODUCTO]" in bold condensed white sans-serif, all caps, upper center, subtle golden glow effect.
Subtitle: "[tagline o promesa]" in thin italic light gray #C0C0C0, below the title.
CTA: "[LLAMADA A LA ACCIÓN]" in black text on golden #F5C400 pill button, bottom center.
Additional info: "[precio / fecha / contacto]" in small regular white sans-serif, bottom edge.

PALETTE:
Dominant: deep black #0A0A0A — 60% — power and premium.
Secondary: forest green #0A3D1A — 25% — natural and fresh.
Accent: golden #F5C400 — 10% — CTA and highlights.
Text: pure white #FFFFFF — legible contrast on dark background.

EFFECTS: Subtle film grain at 10% opacity, soft vignette darkening edges by 15%, anamorphic horizontal lens flare from upper right in warm gold tones.

REFERENCES: inspired by Heineken premium campaign photography, Red Bull action editorial, and Apple product commercial aesthetics.

ultra-detailed, 8K resolution, award-winning commercial advertising photography, sharp focus, professional color grading, no watermark
```

### Template 2: Flyer de evento — Sin imagen de referencia

```
Event promotional flyer for [nombre del evento]. Style: [estilo visual — ej: "bold urban festival branding inspired by Coachella visual identity and Spotify campaign typography"].

COMPOSITION: Large bold typography dominates the upper 40% of the design. The center 40% features [elemento visual principal: una ilustración de la escena / foto atmosférica del lugar / concepto abstracto]. The lower 20% houses logistics and CTA. Every zone has a clear visual purpose — no empty unused spaces.

LIGHTING: [tipo: "Dramatic neon glow from multiple colored sources — deep magenta #FF006E from left and electric blue #00BFFF from right, creating a moody nightlife atmosphere with strong color contrast shadows"].

BACKGROUND: [capas: "Foreground: scattered geometric confetti shapes in accent colors. Midground: atmospheric smoke wisps at the bottom third. Background: deep black #000000 with a subtle radial gradient to dark purple #1A0033 at the center"].

TYPOGRAPHY:
Event name: "[NOMBRE DEL EVENTO]" in massive bold condensed display font, all caps, full width, white with multicolor gradient overlay from magenta to electric blue.
Date: "[FECHA COMPLETA]" in medium weight sans-serif, golden #FFD700, centered below event name.
Venue: "[LUGAR]" in thin regular sans-serif, light gray #AAAAAA.
Supporting acts or info: "[INFORMACIÓN ADICIONAL]" in small regular, white #FFFFFF.
CTA: "[COMPRA TUS ENTRADAS / REGÍSTRATE GRATIS]" in bold white on deep magenta #CC0055 pill button, lower center.

PALETTE:
Dominant: pure black #000000 — 55%.
Secondary: deep magenta #FF006E — 25%.
Accent: electric blue #00BFFF + golden #FFD700 — 15%.
Text: white #FFFFFF + golden — maximum legibility.

EFFECTS: Subtle chromatic aberration on typography edges, soft smoke atmospheric effect in lower third, glowing neon halo around key typographic elements.

REFERENCES: inspired by Coachella 2024 visual identity, Spotify Bold campaign, and Dua Lipa concert tour branding.

ultra-detailed, 8K resolution, award-winning event poster design, sharp focus, professional color grading, no watermark
```

### Template 3: Oferta / Promoción — Sin imagen de referencia

```
Promotional discount flyer for [negocio / producto]. Style: [estilo — ej: "high-energy retail sale poster, bold and attention-grabbing, inspired by Supreme drop campaigns and ZARA sale editorial"].

COMPOSITION: The discount percentage "[50% OFF]" dominates the center as the hero element (50% of visual space), rendered in massive bold 3D typography. Behind it, [elemento visual de apoyo: el producto en acción / persona usando el producto / fondo dinámico con energía]. Upper zone: logo and brand name. Lower zone: conditions, dates, and CTA. Every zone has a clear visual purpose — no empty unused spaces.

LIGHTING: [tipo: "Hard dramatic spotlight from directly above, creating a strong circular light pool on the discount typography, with deep shadow edges giving it a stage-performance energy"].

BACKGROUND: [capas: "Foreground: scattered abstract geometric shapes in brand colors adding kinetic energy. Midground: the discount figure in massive 3D type. Background: deep [color de marca] gradient from center to edges"].

TYPOGRAPHY:
Main discount: "[PORCENTAJE O MONTO DE DESCUENTO]" in massive ultra-bold 3D extruded display font, [color acento], occupying the full center.
Brand name: "[NOMBRE DEL NEGOCIO]" in bold brand font, upper center.
Offer description: "[DESCRIPCIÓN DE LA OFERTA]" in medium weight, white, below the main discount.
Validity: "[Válido hasta el fecha / Solo por hoy]" in small italic, light tone.
CTA: "[VISÍTANOS / COMPRA AHORA / LLÁMANOS]" in bold contrasting text on solid accent button, lower center.

PALETTE: [adaptar a colores de marca o sector]

EFFECTS: Bold poster energy with slight halftone texture overlay at 8%, strong vignette pushing focus to center, subtle film grain for authenticity.

ultra-detailed, 8K resolution, award-winning retail advertising design, sharp focus, professional color grading, no watermark
```

### Template 4: Portada de redes sociales / Servicio profesional — Sin imagen de referencia

```
Professional social media post for [tipo de servicio: consultoría / coaching / academia / clínica]. Style: [estilo — ej: "clean corporate editorial inspired by McKinsey brand materials and HubSpot campaign design"].

COMPOSITION: The professional visual element (person or concept graphic) occupies the left 55% of the design. The right 45% is a clean typographic zone with the message hierarchy. Clear visual separation between zones through subtle color or thin geometric line. Every zone has a clear visual purpose — no empty unused spaces.

LIGHTING: [tipo: "Soft clean three-point studio lighting. Soft key light from left creating gentle facial shadows, subtle rim light on right edge, clean neutral gray background with soft gradient"].

PROTAGONIST (si hay persona):
[Descripción física precisa: "A confident professional in their mid-40s wearing a tailored navy blazer over a clean white shirt, slight forward lean communicating engagement, direct eye contact with camera creating viewer connection"].

BACKGROUND: [capas: "Foreground: subtle geometric line element framing the typographic zone. Midground: the professional subject. Background: clean light gray #F4F4F4 with subtle gradient to white, professional and distraction-free"].

TYPOGRAPHY:
Main message: "[MENSAJE PRINCIPAL / PROPUESTA DE VALOR]" in bold clean sans-serif, dark charcoal #1A1A1A, right zone upper half.
Supporting text: "[DESCRIPCIÓN O BENEFICIO]" in regular weight, medium gray #555555, below main message.
CTA: "[AGENDA TU CONSULTA / MÁS INFORMACIÓN]" in white text on solid brand-color pill button.
Brand: "[NOMBRE / WEB / TELÉFONO]" in small regular, bottom of typographic zone.

PALETTE:
Dominant: white #FFFFFF + light gray #F4F4F4 — clean and professional.
Brand color: [hex del cliente] — for CTA and accent details.
Text: dark charcoal #1A1A1A — maximum legibility.

ultra-detailed, 8K resolution, award-winning professional service advertising, sharp focus, professional color grading, no watermark
```

### Template 5: Flyer de inmueble / Real Estate — Sin imagen de referencia

```
Premium real estate marketing flyer for [tipo de propiedad: departamento / casa / local comercial]. Style: [estilo — ej: "luxury real estate editorial inspired by Sotheby's International Realty campaign photography and JLL brand materials"].

COMPOSITION: The hero property shot (exterior or interior) occupies the full bleed background (70% visual weight). An elegant frosted glass card overlay in the lower 35% houses all text information. The real estate agency logo sits in the upper right corner. Every zone has a clear visual purpose — no empty unused spaces.

LIGHTING: [tipo: "For interior: warm golden hour natural light flooding through floor-to-ceiling windows, casting long warm shadows, photorealistic architectural photography style. For exterior: bright midday sunlight from upper left, crisp shadows, vibrant landscape"].

PROPERTY VISUAL:
[descripción de la propiedad: "A modern open-plan living room with 3-meter ceilings, polished concrete floors, floor-to-ceiling windows overlooking the city, minimalist furniture in warm neutral tones, lush tropical plant in the corner"].

TYPOGRAPHY (all on the frosted glass card):
Property headline: "[NOMBRE O DESCRIPCIÓN IMPACTANTE]" in elegant thin-weight serif font, all caps, wide letter-spacing, charcoal #1A1A1A.
Price: "[PRECIO]" in bold medium-weight sans-serif, dark charcoal.
Key features: "[m² / dormitorios / baños / estacionamientos]" in small clean icons + regular sans-serif text.
CTA: "[AGENDA TU VISITA / CONTÁCTANOS]" in white text on solid deep navy #1A2B4A pill button.
Contact: "[teléfono / web / agencia]" in small regular, lower edge of card.

PALETTE:
Overlay card: white #FFFFFF at 80% opacity, frosted glass effect.
Accent: deep navy #1A2B4A — CTA and premium details.
Gold accent: #C9A84C — for luxury property tier markers.
Text: dark charcoal #1A1A1A on white card — clean legibility.

EFFECTS: Subtle vignette on photo edges pushing attention to center, frosted glass card with backdrop blur effect, thin gold line framing the card edges.

ultra-detailed, 8K resolution, award-winning luxury real estate photography and design, sharp focus, professional color grading, no watermark
```

---

## Prompt negativo universal (usar en todos los casos)

```
blurry, low quality, distorted text, illegible typography, garbled letters, generic stock photo look, watermark, overexposed, flat lighting, amateur design, cluttered layout, washed out colors, low contrast, pixelated, dull composition, empty unused spaces, symmetric boredom, unintentional blank areas, plastic AI look, waxy skin texture, unnatural proportions, floating elements with no spatial logic, mismatched lighting directions, inconsistent shadows
```

---

## Técnicas avanzadas

### 1. Text-First Hack (para flyers con mucho texto)

Cuando el flyer tiene muchos textos a renderizar, usar esta secuencia:
1. Primero generar conversacionalmente con Nano Banana 2: "Ayúdame a estructurar los textos para este flyer: título, subtítulo, CTA, y datos"
2. El modelo devuelve la estructura de textos optimizada
3. Luego pedir la imagen con esos textos ya definidos entre comillas en el prompt

### 2. Iteración conversacional (ventaja única de Nano Banana 2)

Nano Banana 2 permite refinar conversacionalmente sin reescribir el prompt completo:
- "Hazlo más oscuro y dramático"
- "Cambia el fondo a un degradado azul marino"
- "Mueve el CTA al tercio inferior derecho"
- "Agrega partículas de luz dorada en el fondo"
- "Aumenta el tamaño del título un 30%"

### 3. Search Grounding para localizaciones específicas

Para flyers que necesiten referencias visuales reales (un restaurante específico, una ciudad, un producto real):
```
Use Google Search to find visual references for [lugar/producto/marca específica], then create a [tipo de flyer] incorporating the authentic visual style and elements you found.
```

### 4. Consistencia de elementos a través de múltiples flyers

Para crear una serie de flyers con la misma estética (campaña de Meta Ads):
```
[Describir los elementos fijos de la marca: colores hex, posición del logo, tipografía principal]
Maintain these brand elements consistent throughout: logo in upper left, brand color palette #hex1 and #hex2, [nombre de tipografía] as the primary font, [estilo visual general].
```

---

## Post-generación: Si el alumno sube el resultado para revisión

Analizar con ojo de director creativo y entregar feedback en este formato:

**✅ LO QUE ESTÁ FUNCIONANDO:**
[Lista específica de lo que quedó bien y por qué — ser específico]

**⚠️ LO QUE SE PUEDE MEJORAR:**
[Lista específica con la solución exacta para cada punto]

**📐 VALIDACIÓN TÉCNICA META ADS:**
[Confirmación o alerta sobre: texto en imagen >20%, zona segura Stories, legibilidad en móvil pequeño, zonas vacías sin intención]

**🔄 AJUSTE SUGERIDO AL PROMPT:**
[El fragmento exacto del prompt positivo modificado para la segunda iteración — no el prompt completo, solo la parte que cambia]
