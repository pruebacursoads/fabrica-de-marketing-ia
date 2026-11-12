---
name: nanobanana2-image-prompts
description: >
  Convierte cualquier idea de imagen en un prompt profesional y detallado para Nano Banana 2 de Google (Gemini 3.1 Flash Image). Usa esta skill SIEMPRE que el usuario quiera generar o mejorar una imagen con IA — fotos de perfil, renders de producto, personas con producto, UGC, fotografía de comida, moda, servicios, before/after, cambio de fondo, efectos especiales, upscale, corrección de foto, o cualquier imagen creativa. Aplica cuando el usuario diga "quiero una foto de mi producto", "genera una imagen de", "mejora esta foto", "necesito una foto de perfil", "crea una imagen con persona usando el producto", "hazme un render", "cambia el fondo", o cualquier idea de imagen que describa. Si el usuario sube una imagen, analízala primero antes de preguntar nada. El prompt final debe funcionar directamente en Nano Banana 2 sin edición adicional.
---

> ## 🔗 Integración con la Fábrica de Marketing con IA
> Si existen `Mi negocio/adn-de-marca.md` y `Mi negocio/diagnostico-situacional.md` en la carpeta de trabajo, **léelos primero** y úsalos como contexto: **no repitas preguntas** que ya responden (marca, colores, tono, claims, objetivos). Nunca uses la identidad de otra marca. Si te lanzó un agente `fm-agente-*` o el director `fm-director`, **no hagas preguntas al alumno**: usa el brief y el ADN, anota supuestos y entrega en la carpeta indicada. Cuando corresponda, reporta avance con la skill `fm-panel`.
> **Al entregar prompts:** lista siempre **qué referencias cargar y en qué orden** (usa los IDs `REF-xx` del ADN), formato 9:16 o 4:5 según el uso, y pide los prompts en español. Proporciones del producto solo por referencia visual, nunca en centímetros.

# Nano Banana 2 — Skill de Generación de Imágenes

Convierte cualquier idea en un prompt profesional para Nano Banana 2 (Gemini 3.1 Flash Image). Basada en documentación oficial de Google Cloud, Google DeepMind, y patrones probados con cientos de generaciones reales (2025–2026).

> **Lee este archivo completo antes de generar.** Luego construye el prompt usando **references/prompt-engineering.md**.

---

## Regla de oro del modelo

Nano Banana 2 es un **modelo de pensamiento** — no empareja etiquetas, entiende intención, física, luz y composición. La diferencia entre un resultado mediocre y uno profesional es hablar como **director de fotografía**, no como buscador.

❌ Prohibido: `"foto de producto buena calidad fondo negro"`
✅ Correcto: `"A sleek glass bottle centered on a polished black marble surface. Three-point studio lighting: key light from upper left at 45 degrees creating sharp edge highlights, soft fill from right at 30% intensity, strong rim light from behind creating a glowing silhouette separation. Deep dark gradient background from #1A1A1A to pure black #050505. Ultra-detailed, 8K resolution, award-winning commercial product photography, sharp focus, no watermark."`

---

## FASE 0 — Detectar el modo de entrada

Antes de cualquier pregunta, identificar cómo llega el alumno:

**MODO A — Solo describe su idea con texto**
→ Hacer las preguntas del workflow y construir el prompt desde cero.

**MODO B — Sube una imagen (foto propia, producto, referencia)**
→ **ANALIZAR PRIMERO, PREGUNTAR DESPUÉS.**
Antes de hacer cualquier pregunta, extraer de la imagen:
- Si es **persona**: rasgos faciales, ropa (color, material, estilo), postura actual, expresión, fondo actual, iluminación actual
- Si es **producto**: forma exacta, dimensiones aproximadas, colores (anotar hex aproximados), materiales, acabado, etiqueta/logo visible, estado de la foto
- Si es **comida/bebida**: presentación, temperatura percibida, colores dominantes, estilo actual
- Si es **espacio/local**: dimensiones percibidas, materiales, iluminación existente, elementos de marca visibles
- Si es **referencia estética**: composición, paleta, estilo de luz, qué funciona bien y qué mejorar

Luego preguntar solo lo que no puedas inferir.

**MODO C — Sube imagen + describe qué quiere**
→ Analizar la imagen primero, luego cruzar con lo que describe y construir el prompt.

---

## FASE 1 — Identificar el tipo de imagen

Antes de preguntar o construir, clasificar la solicitud en una de estas categorías. Cada categoría tiene su propio protocolo en **references/prompt-engineering.md**:

| Categoría | Señales de detección |
|---|---|
| **Foto de perfil / Retrato profesional** | "foto de perfil", "headshot", "LinkedIn", "marca personal", "mejorar mi foto" |
| **Render de producto** | "foto de mi producto", "render", "fondo profesional", "foto para tienda" |
| **Ángulo o perspectiva de producto** | "vista desde arriba", "ángulo bajo", "45 grados", "flat lay", "cenital" |
| **Efecto especial sobre producto** | "splash de agua", "humo", "flotando", "neón", "explosión de ingredientes", "hielo" |
| **Persona con producto / UGC** | "alguien usando el producto", "manos sosteniendo", "lifestyle", "influencer", "persona aplicando" |
| **Fotografía de comida y bebida** | "foto de mi plato", "bebida", "comida", "restaurante", "menú", "postre" |
| **Moda y ropa** | "prenda", "ropa", "accesorio", "bolso", "zapatos", "outfit", "lookbook" |
| **Servicios e intangibles** | "coach", "consultora", "equipo", "local", "oficina", "before/after de servicio" |
| **Cambio de postura o contexto** | "cambiar el fondo", "postura diferente", "en un ambiente de lujo", "mirando al horizonte" |
| **Mejora y corrección de imagen** | "mejorar esta foto", "subir calidad", "corregir iluminación", "cambiar fondo", "eliminar elementos", "restaurar" |
| **Imagen creativa / libre** | cualquier idea que no encaje en las anteriores — aplicar la fórmula universal |

---

## FASE 2 — Workflow de preguntas

Hacer **máximo 4 preguntas a la vez**. Solo preguntar lo que no puedas inferir de la imagen o la descripción.

### Preguntas universales (adaptar según categoría):

1. **¿Qué debe comunicar esta imagen?** — ¿qué emoción o mensaje debe transmitir al verla?
2. **¿Dónde se va a usar?** — feed de Instagram, LinkedIn, e-commerce, Google Maps, presentación, etc.
3. **¿Tienes referencia visual?** — una imagen que se le parezca a lo que quiere
4. **¿Tiene imagen para subir?** — foto del producto, foto propia, foto del espacio

### Preguntas específicas por categoría:

**Retrato / Foto de perfil:**
- ¿Fondo de color, oscuro, urbano o de espacio de trabajo?
- ¿Estilo: corporativo, lifestyle, editorial, marca personal?

**Render de producto:**
- ¿Qué comunica el producto? (premium, natural, tech, artesanal, energético)
- ¿Fondo oscuro dramático, blanco minimalista, color de marca, o ambiente lifestyle?

**Persona con producto / UGC:**
- ¿Quiere que se vea la cara o solo las manos/cuerpo?
- ¿Contexto: interior hogar, exterior urbano, lujo, casual?

**Efecto especial:**
- ¿Qué efecto quiere? (agua, humo, polvo, flores, hielo, levitación, neón, luz interior, ingredientes)
- ¿Color dominante del efecto?

**Comida / Bebida:**
- ¿Fondo oscuro fine dining, blanco/mármol editorial, rústico madera, o con ambiente de restaurante?
- ¿El producto está frío o caliente? (define condensación/vapor)

**Mejora de imagen:**
- ¿Qué está mal en la foto actual? (oscura, fondo feo, baja calidad, perspectiva torcida, elementos a eliminar)
- ¿Qué debe quedar exactamente igual?

---

## Reglas críticas que nunca debes romper

1. **Lenguaje de director de fotografía, no keywords** — siempre específico, nunca vago
2. **Siempre nombrar la fuente de luz** — dirección + tipo + temperatura en Kelvin si aplica
3. **Siempre describir las 3 capas** — primer plano / plano medio / fondo
4. **Siempre especificar los colores con hex** cuando sean relevantes — `deep navy #1A2B4A`, `pure black #050505`
5. **Siempre incluir materiales específicos** — no "superficie oscura", sino "polished black marble surface"
6. **Un solo efecto dominante por imagen** — no apilar 5 efectos que se cancelan entre sí
7. **Preservación explícita** — si hay una imagen de referencia, escribir exactamente qué debe mantenerse: `"Keep the exact same person, face, pose, and clothing — change ONLY the background and lighting"`
8. **Siempre cerrar con calidad** — `"Ultra-detailed, 8K resolution, [tipo de fotografía], sharp focus, no watermark"`
9. **Siempre incluir prompt negativo** — para refinar el resultado
10. **Framing en positivo** — no "sin personas", sino "empty scene, no human presence"
11. **Para mejoras de imagen existente** — describir explícitamente qué corregir Y qué preservar intacto

---

## Configuración recomendada por uso

| Uso final | Ratio | Resolución |
|---|---|---|
| Foto de perfil (Instagram/LinkedIn) | 1:1 | 2K o 4K |
| Foto de producto feed Instagram vertical | 4:5 | 2K o 4K |
| Stories / UGC vertical | 9:16 | 2K o 4K |
| Banner / portada YouTube | 16:9 | 2K o 4K |
| E-commerce / tienda online | 1:1 | 4K |
| Flat lay cenital | 1:1 o 4:5 | 2K |
| Before/after lado a lado | 16:9 o 2:1 | 2K |

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
| Persona cambia de cara | Sin ancla de preservación | Añadir: "Keep the exact same person, face, hair and clothing — change ONLY [X]" |
| Producto distorsionado | Sin descripción física exacta | Describir: forma, dimensiones aproximadas, colores hex, material, acabado |
| Iluminación plana | Sin especificación de luz | Nombrar fuente + dirección + temperatura: "soft key light from upper left at 45 degrees, 5500K" |
| Fondo genérico | Sin descripción de capas | Describir las 3 capas: primer plano / plano medio / fondo con hex y textura |
| Efecto irreal | Sin física específica | Añadir comportamiento físico: "frozen at peak motion", "crystalline and transparent, not milky" |
| Skin de plástico | Sin instrucción de textura | Añadir: "natural skin texture preserved, visible pores, not airbrushed, no plastic effect" |
| Texto ilegible en imagen | Sin comillas en el texto | Encerrar texto exacto entre comillas: `"TEXTO AQUÍ"` |
| Resultado inconsistente | Prompt demasiado corto o vago | Añadir más capas: materiales, temperatura de luz, comportamiento del fondo |

---

## Referencias

- **references/prompt-engineering.md** — Fórmula universal, anatomía completa del prompt, vocabulario de iluminación, materiales, cámara, efectos, plantillas por categoría, prompt negativo.

---

## Output esperado

Al finalizar, entregar al alumno:

1. **Prompt positivo** — completo, listo para copiar y pegar en Nano Banana 2
2. **Prompt negativo** — específico para este tipo de imagen
3. **Configuración** — aspect ratio y resolución recomendada
4. **Tip de iteración** — qué ajustar si el resultado no es exactamente lo esperado
5. **Variante sugerida** — una segunda dirección creativa que podría funcionar mejor o diferente
