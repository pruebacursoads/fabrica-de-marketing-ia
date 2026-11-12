# ⚙️ PROMPT ENGINEERING — Guía Técnica para IA Imagen 2026

Leer ANTES de construir los prompts finales de los slides.
Compatible con: Nanobanana 2, Gemini 3.1 Flash Image, GPT Image 2.0,
Ideogram 3, Flux Pro 1.1, Midjourney v7.

---

## ANATOMÍA DE UN PROMPT PERFECTO

Un prompt de IA imagen para carruseles tiene 3 capas:

```
CAPA 1 — INTENCIÓN MAESTRA (qué estamos creando)
CAPA 2 — ESPECIFICACIONES TÉCNICAS (cómo debe verse)
CAPA 3 — RESTRICCIONES (qué debe evitar)
```

---

## ESTRUCTURA COMPLETA DE PROMPT — TEMPLATE

```
[INSTRUCCIÓN MAESTRA]
Create a professional social media carousel slide for [tipo de negocio].
This is slide [N] of [total]. [Objetivo específico del slide].
Canvas: [dimensiones]px, [proporción], optimized for mobile Instagram feed.

[BACKGROUND]
Background: [descripción técnica detallada del fondo con HEX]

[SUBJECT — solo si hay persona]
Subject: [descripción de persona — expresión, pose, vestimenta, posición en frame]
Photography style: [estudio / lifestyle / editorial]
Lighting: [descripción técnica de iluminación]

[TYPOGRAPHY ZONES]
Typography layout:
  - HEADLINE ZONE: [posición — upper/center/lower third], 
    text "[COPY EXACTO]", ultra-bold display typeface, 
    [tamaño relativo], color #[HEX], [tracking]
  - SUBHEADLINE ZONE: [posición], text "[COPY]", 
    [peso tipográfico], color #[HEX]
  - BODY ZONE (si aplica): [posición], [descripción]
  - All text must be PERFECTLY LEGIBLE at mobile screen size

[CONTENT ELEMENT — protagonista visual del slide]
Content element: [descripción detallada del elemento central — icono 3D, 
número gigante, producto, ilustración, gráfico, etc.]
Position: [centrado / tercio superior / composición asimétrica]
Scale: [tamaño relativo al canvas]

[ELEMENT ANCHOR — se repite en todos los slides]
Brand anchor element: [descripción exacta del elemento ancla]
Position: [posición exacta y consistente]
Text EXACTLY: '[texto de marca]' — NO other text. NO invented words.

[BADGE NUMERADOR]
Slide counter badge: [forma] in upper-right corner,
background color #[HEX], number text "[N/TOTAL]" in #[HEX],
[borde si aplica], [tamaño — small/medium]

[ACCENT DETAILS]
Accent details: [elementos decorativos mínimos que elevan la calidad]
[líneas, puntos, formas geométricas, gradientes sutiles]

[EFFECTS]
Visual effects: [grain, profundidad, sombras, iluminación, glow, etc.]
Lighting: [descripción técnica]
Atmosphere: [descripción del ambiente visual general]

[QUALITY DIRECTIVE]
Ultra-high resolution, 4K output quality, sharp focus, professional 
commercial grade, no AI artifacts, no watermarks, magazine-quality visual polish.
Photorealistic render with perfect text legibility throughout.
```

---

## EJEMPLOS DE PROMPTS COMPLETOS — REFERENCIA

### EJEMPLO 1: Portada — Marca Personal Coaching (Premium Dark)

```
Create a professional social media carousel slide for a business coaching brand.
This is slide 1 of 8 — COVER SLIDE. Stop-the-scroll impact in under 1.5 seconds.
Canvas: 1080×1350px, 4:5 portrait ratio, optimized for Instagram mobile feed.

Background: Deep black background #0A0A0A with subtle photographic grain 
texture at 4% opacity, no vignette, premium editorial feel.

Subject: Confident Latin American woman, 35-40 years old, business professional,
wearing structured black blazer, looking directly into camera with 
calm authority and subtle smile. Upper body portrait, positioned slightly 
left of center. Studio photography style, dramatic single soft key light 
from 45° upper-left, deep natural shadows, no heavy retouching.

Typography layout:
  - Small overline top-center: "SI SIGUES HACIENDO ESTO" in #C9A84C, 
    11px sans-serif regular, 4px letter-spacing, uppercase
  - HEADLINE: center-left alignment below subject eye-line,
    text "TU NEGOCIO NUNCA VA A ESCALAR" in #FFFFFF, 
    ultra-condensed extrabold display, 52px equivalent, 
    tight -2% letter-spacing, 2-line break after "NEGOCIO"
  - SUBHEADLINE below: "Desliza para descubrir los 7 errores" 
    in #C9A84C, 16px sans-serif medium

Content element: No additional content element — person IS the element.

Brand anchor element: Thin gold horizontal line #C9A84C, 2px height, 
full width, positioned 28px from bottom edge.
Text EXACTLY: '@[HANDLE]' centered below the line in #C9A84C, 
10px sans-serif regular — NO other text. NO invented words.

Slide counter badge: Rounded square (8px radius) upper-right corner,
24px from edges, background #C9A84C, text "1/8" in #0A0A0A, 
bold sans-serif, medium size.

Accent details: Very subtle gold gradient overlay at bottom 15% of frame 
(#C9A84C at 8% opacity), creating depth for the anchor bar area.

Visual effects: Dramatic studio lighting, cinematic contrast, 
film grain aesthetic, deep blacks with clean highlights.

Ultra-high resolution, 4K output quality, sharp focus throughout, 
professional commercial photography grade, no AI artifacts, 
no watermarks, magazine editorial quality. Perfect text legibility.
```

**NEGATIVE:** blurry, low quality, distorted text, illegible typography, 
watermark, overexposed, flat lighting, amateur design, cluttered layout, 
washed out colors, low contrast, pixelated, empty spaces, AI artifacts, 
cartoon style, illustrated person, green background, extra fingers, 
deformed face, floating limbs, multiple people, text hallucinations

---

### EJEMPLO 2: Slide de Estadística — Producto de Salud (Clean Professional)

```
Create a professional social media carousel slide for a health supplement brand.
This is slide 3 of 8 — DATA IMPACT SLIDE. Deliver one powerful statistic.
Canvas: 1080×1350px, 4:5 portrait ratio, Instagram mobile optimized.

Maintain exact visual consistency with previous slide: same background 
treatment #F8F9FA, same color palette [#1A2E4A, #00B4D8, #F8F9FA], 
same lighting style, same anchor bar element, same render quality.

Background: Clean off-white background #F8F9FA, flat and minimal, 
no texture, professional medical/wellness aesthetic.

Typography layout:
  - Small label top-center: "¿SABÍAS QUE...?" in #00B4D8, 
    12px sans-serif bold, 6px letter-spacing
  - GIANT NUMBER centered: "87%" in #1A2E4A, 
    display extrabold, 220px equivalent, tight tracking
  - Context text below number: "de las personas que toman [PRODUCTO]" 
    in #1A2E4A, 18px sans-serif regular, centered, max 2 lines
  - Highlight line below: "reportan mejoras en menos de 30 días" 
    in #00B4D8, 20px sans-serif bold, centered
  - Source small: "Estudio interno 2024, n=847" in #9CA3AF, 
    10px sans-serif regular, bottom area

Content element: Minimal circular progress ring around the "87%" number,
stroke 8px, filled arc representing 87% in #00B4D8, 
remaining 13% in #E2E8F0, 320px diameter.

Brand anchor element: Left sidebar accent bar #00B4D8, 6px width, 
80% height of slide, centered vertically, 32px from left edge.
Text EXACTLY: '[NOMBRE MARCA]' vertical rotated 90°, 
10px sans-serif light #1A2E4A — NO other text.

Slide counter badge: Circle, upper-right, background #1A2E4A, 
text "3/8" in #FFFFFF, bold, medium size, no border.

Accent details: Very subtle drop shadow on the number (0 4px 16px 
#1A2E4A15), enhancing depth without clutter.

Ultra-high resolution, 4K, razor-sharp text, professional infographic 
quality, clean and clinical precision aesthetic.
```

**NEGATIVE:** blurry, low quality, distorted text, illegible typography,
watermark, cluttered layout, low contrast, pixelated, AI artifacts,
people, human figures, faces, person, man, woman, silhouette, body parts,
generic stock photo look, complex backgrounds, busy patterns

---

### EJEMPLO 3: Slide de Cierre con CTA — E-commerce (Vibrant Energy)

```
Create a professional social media carousel slide for an e-commerce sportswear brand.
This is slide 8 of 8 — CLOSING CTA SLIDE. Convert viewers into buyers.
Canvas: 1080×1350px, 4:5 portrait ratio, Instagram mobile optimized.

Maintain exact visual consistency with previous slide: same background 
treatment #FF3D00, same color palette [#FF3D00, #FFDE03, #FFFFFF], 
same lighting style, same anchor element, same render quality.

Background: Vibrant orange-red background #FF3D00, radial gradient 
slightly darker at edges (10% deeper #CC3100), high energy, bold, clean.

Subject: Athletic Latin American man, 25-32 years old, wearing brand 
sportswear (dark activewear), dynamic pose — one arm extended pointing 
toward text/camera, energetic wide smile, full confidence. 
Right side of frame, lower 60% of slide. High-key studio lighting, 
bright even illumination, 5500K, punchy saturation.

Typography layout:
  - HEADLINE upper-left third: "¿LISTO PARA" in #FFDE03, 
    ultra-condensed extrabold display, 58px, all-caps, tight tracking
  - LINE 2: "TRANSFORMARTE?" in #FFFFFF, same style, 64px
  - CTA BOX below text: rounded rectangle 600px wide, background #FFFFFF,
    text "ESCRÍBENOS 'QUIERO INFO'" in #FF3D00, 20px bold sans-serif
  - URGENCY LINE: "Cupos limitados este mes" in #FFDE03, 
    14px sans-serif medium, below CTA box
  - Handle/bio: "@[HANDLE] · Link en bio" in #FFFFFF80, 
    11px sans-serif regular, very bottom

Brand anchor element: Top horizontal band #FFDE03, full width, 
8px height, 0px from top. NO text in this band.

Slide counter badge: Hexagonal, upper-right corner, background #0A0A0A,
text "8/8" in #FFDE03, bold, medium size, 2px gold border.

Accent details: Three small abstract speed lines behind subject 
in #FFDE03 at 20% opacity, suggesting motion and energy.

Dynamic high-key lighting, punchy saturation, energetic commercial 
photography quality, ultra-high resolution 4K output, 
no AI artifacts, magazine sports brand quality.
```

**NEGATIVE:** blurry, low quality, distorted text, illegible typography,
watermark, flat lighting, amateur design, low contrast, pixelated, 
AI artifacts, cartoon style, extra fingers, deformed anatomy, 
multiple people in background, text hallucinations, wrong brand colors

---

## TÉCNICAS DE CORRECCIÓN RÁPIDA

### Problema: Texto inventado o ilegible
**Solución — añadir al prompt:**
```
CRITICAL TEXT INSTRUCTION: 
- Text zone 1: ONLY display text "[TEXTO EXACTO]" — nothing else
- Text zone 2: ONLY display "[TEXTO EXACTO]" — no other characters
- NO random letters, NO invented words, NO decorative text
- If uncertain about text, leave zone empty rather than invent
```

### Problema: Fondo inconsistente entre slides
**Solución — coherencia prompt:**
```
CONSISTENCY LOCK: This slide is part of a visual series.
Replicate EXACTLY: background color #[HEX], grain texture level,
lighting atmosphere, overall visual weight and contrast ratio.
Deviation from established visual DNA is NOT acceptable.
```

### Problema: Persona con dedos mal generados
**Solución — especificación de manos:**
```
HANDS: Keep hands out of frame OR show only as a natural extension
of the pose with minimal detail. DO NOT show open palms or 
spread fingers close to camera. Natural position only.
```

### Problema: Elemento ancla diferente en cada slide
**Solución — instrucción precisa:**
```
ANCHOR ELEMENT (MANDATORY - IDENTICAL TO ALL SLIDES):
[Descripción tan detallada que no admite variación]
Position: exactly [Npx] from [edge], [alineación], 
dimensions: [WxH px equivalent], color: #[HEX EXACTO],
style: [descripción técnica], no variations allowed.
```

### Problema: Badge numerador mal colocado
**Solución:**
```
COUNTER BADGE (upper-right corner, MANDATORY):
[forma], positioned [Npx] from top edge and [Npx] from right edge,
background fill #[HEX], border [descripción], 
text "[N/TOTAL]" in [estilo tipográfico] #[HEX],
size: approximately 48×48px equivalent.
```

---

## PROMPTS NEGATIVOS MAESTROS

### Negativos universales (van en TODO):
```
blurry, low quality, distorted text, illegible typography, watermark,
overexposed, flat lighting, amateur design, cluttered layout, 
washed out colors, low contrast, pixelated, empty unused spaces, 
AI artifacts, uncanny valley, generic stock photo look, 
oversaturated colors, text hallucinations, invented words in design
```

### Añadir para slides SIN persona:
```
people, human figures, faces, person, man, woman, silhouette, 
body parts, hands, arms, legs, fingers, eyes
```

### Añadir para slides CON persona:
```
cartoon style, illustrated character, anime, digital art person,
green background, distorted face, extra fingers, floating limbs,
deformed anatomy, multiple heads, asymmetric face, doll-like skin
```

### Añadir para slides de producto:
```
fake products, generic packaging, stock photo products, 
off-brand colors, incorrect logo representation, 
product floating without ground shadow
```

### Añadir para slides de datos/estadísticas:
```
pie charts, complex graphs, multiple data points competing,
tiny unreadable numbers, cluttered information design,
inconsistent scale, misleading visual hierarchy
```

---

## ESPECIFICACIONES TÉCNICAS POR PLATAFORMA

### Instagram Feed (recomendado):
- Dimensiones: 1080×1350px (4:5) — 20% más pantalla que cuadrado
- Zona segura UI: evitar contenido crítico en primeros y últimos 150px (arriba/abajo)
- Texto mínimo legible: equivalente a 14px en display 6"
- El PRIMER slide determina el aspecto de TODOS los demás

### TikTok / Instagram Reels Cover:
- Dimensiones: 1080×1920px (9:16)
- Zona segura UI: evitar los 350px inferiores (barra de TikTok)
- Zona segura superior: evitar 100px superiores
- Texto crítico: zona central 1080×1200px

### LinkedIn (si aplica):
- Dimensiones: 1080×1080px (1:1) o 1080×1350px (4:5)
- Estilo: más formal, datos más prominentes, personas en contexto profesional
