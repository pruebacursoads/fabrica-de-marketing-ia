---
name: nanobanana2-flyer-prompts
description: >
  Genera prompts profesionales y detallados para crear flyers, piezas publicitarias, portadas, mockups y contenido visual de alto impacto con Nano Banana 2 de Google (Gemini 3.1 Flash Image). Usa esta skill SIEMPRE que el usuario quiera crear un flyer, poster, banner, pieza de Meta Ads, portada, imagen publicitaria, diseño gráfico, o cualquier contenido visual con Nano Banana 2, Gemini Image, Google AI Studio o Freepik AI. Aplica cuando el usuario diga "genera un flyer", "crea un diseño", "quiero una imagen para mis redes", "haz un poster", "pieza para Meta Ads", "diseña mi publicidad", o simplemente comparta la idea de su negocio o evento. Si el usuario sube una imagen (logo, foto de producto, flyer de referencia), analízala primero con ojo de director creativo ANTES de hacer preguntas. El prompt final debe funcionar directamente en Nano Banana 2 sin edición adicional.
---

> ## 🔗 Integración con la Fábrica de Marketing con IA
> Si existen `Mi negocio/adn-de-marca.md` y `Mi negocio/diagnostico-situacional.md` en la carpeta de trabajo, **léelos primero** y úsalos como contexto: **no repitas preguntas** que ya responden (marca, colores, tono, claims, objetivos). Nunca uses la identidad de otra marca. Si te lanzó un agente `fm-agente-*` o el director `fm-director`, **no hagas preguntas al alumno**: usa el brief y el ADN, anota supuestos y entrega en la carpeta indicada. Cuando corresponda, reporta avance con la skill `fm-panel`.
> **Al entregar prompts:** lista siempre **qué referencias cargar y en qué orden** (IDs `REF-xx` del ADN), usa los HEX y tipografías del ADN, texto dentro de la imagen mínimo y exacto (tildes y ñ), y no dupliques el botón nativo de WhatsApp de Meta dentro de la imagen.

# Nano Banana 2 — Skill de Flyers y Piezas Publicitarias

Guía completa para crear flyers y piezas visuales de alto impacto con Nano Banana 2 (Gemini 3.1 Flash Image) de Google DeepMind. Basada en la guía oficial de Google Cloud, comunidades verificadas, y el sistema creativo de un agente de Meta Ads de alto rendimiento (2025–2026).

> **Lee este archivo completo antes de generar cualquier prompt.** Luego construye el prompt usando **references/prompt-engineering.md**.

---

## Por qué Nano Banana 2 es ideal para flyers

Nano Banana 2 es un modelo de pensamiento — no empareja etiquetas, **entiende intención, física y composición**. Esto lo hace único para piezas publicitarias porque:

- **Renderiza texto legible** dentro de la imagen: títulos, subtítulos, precios, fechas, CTAs — sin letras distorsionadas
- **Entiende lenguaje de director creativo**: "jerarquía tipográfica en tercio inferior", "god rays desde arriba izquierda", "glassmorphism card"
- **Respeta colores hex exactos** cuando se especifican en el prompt
- **Mantiene consistencia** de hasta 14 objetos/elementos por diseño
- **Aspect ratios nativos** para cualquier placement de Meta Ads: 1:1, 4:5, 9:16, 16:9

**Regla de oro (fuente: Google Cloud oficial):** NO escribas palabras clave sueltas ("fondo dinámico azul"). Habla como director creativo ("fondo con degradado de azul marino #0D1B2A a negro #050505 con partículas de luz dorada en el tercio superior derecho").

---

## Capacidades técnicas del modelo

| Parámetro | Valores |
|---|---|
| Resoluciones | 512px, 1K, 2K, 4K |
| Aspect ratios | 1:1, 3:2, 2:3, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9, 1:4, 4:1, 1:8, 8:1 |
| Referencias visuales | Hasta 14 imágenes/objetos por prompt |
| Texto en imagen | Legible, multiidioma, múltiples tipografías |
| Modo Thinking | Activar SOLO para diseños muy complejos con múltiples capas de info |

---

## FASE 0 — Detección de modo de entrada

Al recibir la solicitud del alumno, detecta en qué modo está:

- **MODO A** — Describe su negocio o campaña con texto
- **MODO B** — Sube imagen(es): logo, foto de producto, flyer de referencia, foto de local
- **MODO C** — Combinación de imagen + información

**Si detectas MODO B o C — ANALIZA PRIMERO, PREGUNTA DESPUÉS:**

Antes de hacer cualquier pregunta, analiza cada imagen con ojo de director creativo y extrae:
- **Logo**: paleta exacta de colores (hex aproximados), estilo tipográfico, elementos gráficos, personalidad de marca
- **Foto de producto**: forma, colores dominantes, materiales, texturas, qué comunica por sí solo
- **Flyer de referencia**: composición, jerarquía tipográfica, paleta, efectos, qué funciona y qué mejorarías
- **Foto de local/servicio**: ambiente, colores, estilo, elementos de marca presentes

Luego pregunta solo lo que NO puedas inferir de las imágenes.

---

## Workflow de entrevista

Haz máximo 4 preguntas a la vez, en tono amigable. Explica brevemente por qué necesitas cada dato.

### Preguntas universales:

1. **¿Qué vende, promueve o comunica?** — producto, servicio, evento, emprendimiento
2. **¿Cuál es el mensaje o gancho principal?** — oferta, propuesta de valor, fecha, urgencia
3. **¿Quién es tu cliente ideal?** — edad, perfil, contexto cultural, qué problema le resuelves
4. **¿Dónde vas a publicar esto?** — Feed 1:1 o 4:5, Stories/Reels 9:16, banner 16:9
5. **¿Qué tono visual quieres?** — premium/lujo, juvenil/energético, minimalista, cálido/artesanal, profesional
6. **¿Tienes colores de marca o logo?** — pedir hex si los tiene

### Bifurcación crítica:

7. **¿Tienes imagen(es) de referencia para subir?**
   - **SÍ → Modo multimodal** — analizar y usar logo, foto del producto, flyer de referencia como ancla visual
   - **NO → Modo texto puro** — describir todos los elementos con máximo detalle en el prompt

---

## Reglas críticas que nunca debes romper

1. **Lenguaje de director, nunca keywords** — "fondo con degradado de azul marino #0D1B2A a negro #050505 con partículas de luz dorada flotando en el tercio superior derecho, densidad media, efecto bokeh suave" es correcto. "fondo dinámico con colores vibrantes" está prohibido
2. **Siempre especificar el texto ENTRE COMILLAS** — Nano Banana 2 trata el texto en comillas como contenido a renderizar exactamente: `"GRAN APERTURA"`, `"50% OFF"`, `"Solo hasta el domingo"`
3. **Siempre describir el estilo de cada tipografía** — familia + peso + color + efecto: "bold condensed white sans-serif", "Century Gothic thin italic in gold #D4AF37"
4. **Siempre definir la jerarquía visual** — qué ocupa el 60% (protagonista), el 30% (apoyo), el 10% (detalles)
5. **Siempre confirmar que no hay zonas vacías** — cada área del flyer debe tener un rol visual claro
6. **Siempre nombrar la fuente de luz** — "golden backlight from above-left", "soft studio key light at 45°", "single overhead dramatic spotlight"
7. **Nunca adjetivos vacíos** — "hermoso", "moderno", "impactante" sin especificar cómo se logra visualmente, prohibidos
8. **Siempre cerrar con calidad** — "ultra-detailed, 8K resolution, award-winning commercial advertising design, sharp focus, professional color grading, no watermark"
9. **Siempre incluir prompt negativo** — para refinar el resultado
10. **Framing siempre en positivo** — no "sin autos", sino "empty street, no vehicles in sight"
11. **Validar con el alumno antes de generar** — presentar la propuesta visual en lenguaje descriptivo y preguntar: "¿Apruebas esta dirección o ajustamos algo antes de generar?"

---

## Configuración recomendada por placement de Meta Ads

| Placement | Ratio | Resolución |
|---|---|---|
| Feed Instagram/Facebook cuadrado | 1:1 (1080x1080px) | 2K o 4K |
| Feed Instagram vertical | 4:5 (1080x1350px) | 2K o 4K |
| Stories / Reels | 9:16 (1080x1920px) | 2K o 4K |
| YouTube / TV banner | 16:9 | 2K o 4K |
| Banner web horizontal | 4:1 o 8:1 | 1K o 2K |
| Pinterest | 2:3 | 2K |

**Zona segura Stories/Reels:** mantener elementos clave entre el 14% superior e inferior para evitar que la UI de Meta los tape.

---

## Plataformas de acceso (2026)

| Plataforma | Acceso |
|---|---|
| Google AI Studio (aistudio.google.com) | Gratis con cuenta Google |
| Gemini App (gemini.google.com) | Gratis / Ultra $20/mes para 4K |
| Freepik AI | Ilimitado 1K-2K con Premium+ |
| Vertex AI | Empresas / API |

---

## Solución de errores comunes

| Error | Causa | Solución |
|---|---|---|
| Texto garbled / ilegible | No se usaron comillas | Encerrar CADA texto en comillas: `"OFERTA ESPECIAL"` |
| Composición plana o genérica | Prompt tipo keyword soup | Reescribir como briefing narrativo de director creativo |
| Colores incorrectos | Sin hex exactos | Especificar siempre: `deep navy blue #0D1B2A` |
| Zonas vacías en el diseño | Sin instrucción de profundidad | Añadir las 3 capas: primer plano / plano medio / fondo |
| Fondo aburrido | Sin descripción de atmósfera | Añadir: degradado, partículas, bokeh, textura, god rays |
| Tipografía genérica | Sin estilo definido | Especificar: familia + peso + color hex + efecto |
| Producto no reconocible | Sin descripción física | Describir: forma, material, color hex, detalles: "matte black cylindrical bottle with gold cap and embossed logo" |
| Texto en imagen excesivo | Más del 20% del área | Avisar al alumno sobre límite de Meta Ads y sugerir Stories 9:16 o Carrusel |

---

## Validación antes de publicar en Meta Ads

Si el flyer es para Meta Ads, antes de entregar el prompt final, confirmar:

- [ ] ¿El texto en imagen no supera el 20% del área visual?
- [ ] ¿Los colores garantizan contraste legible en móvil pequeño?
- [ ] ¿El elemento clave está en zona segura para Stories (si aplica)?
- [ ] ¿El diseño funciona en 1:1 Y en 4:5 o hay que adaptar?

---

## Referencias

- **references/prompt-engineering.md** — Fórmula completa de 7 capas, modo texto puro, modo multimodal con referencias, tipografía avanzada, iluminación, composición, paleta hex, efectos, plantillas por tipo de flyer, prompt negativo, ejemplos completos.

---

## Output esperado

Al finalizar, entrega al alumno:

1. **Propuesta visual** — descripción en español de lo que se va a generar, con justificación de cada decisión creativa. Preguntar aprobación antes de generar.
2. **Prompt positivo** — listo para copiar y pegar directamente en Nano Banana 2
3. **Prompt negativo** — para refinar el resultado
4. **Configuración** — aspect ratio, resolución, modo Thinking on/off
5. **Tip específico** — qué puede fallar en este tipo de pieza y cómo evitarlo
6. **Nota Meta Ads** — si el diseño excede el 20% de texto en imagen, avisar y sugerir alternativa
