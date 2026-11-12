---
name: seedance-prompts
description: >
  Genera prompts profesionales para Seedance 2.0 de ByteDance. Usa esta skill SIEMPRE que el usuario quiera crear videos con Seedance, spots publicitarios, videos de producto, reels, videos cinematográficos o cualquier generación de video con IA. También úsala cuando mencione Jimeng, Dreamina, CapCut Pro, Doubao, Xiaoyunque o cualquier plataforma que use Seedance. Incluye ingeniería de prompts CON y SIN imagen de referencia, storyboard por timestamps, cámara profesional, audio con lip-sync en español latino, sistema de referencias @, consistencia de personajes validada en producción real, tabla de errores con códigos y sistema anti-filtros. Aplica cuando diga "quiero hacer un video de mi producto", "genera un spot", "crea un reel con IA", "video publicitario", "haz un video sin imagen", o similares.
---

> ## 🔗 Integración con la Fábrica de Marketing con IA
> Si existen `Mi negocio/adn-de-marca.md` y `Mi negocio/diagnostico-situacional.md` en la carpeta de trabajo, **léelos primero** y úsalos como contexto: **no repitas preguntas** que ya responden (marca, colores, tono, claims, objetivos). Nunca uses la identidad de otra marca. Si te lanzó un agente `fm-agente-*` o el director `fm-director`, **no hagas preguntas al alumno**: usa el brief y el ADN, anota supuestos y entrega en la carpeta indicada. Cuando corresponda, reporta avance con la skill `fm-panel`.
> **Nota:** modelo de pago por créditos; usa Omni Flash (gratis en Flow) por defecto y esta skill solo si el alumno lo pide. Referencias exactas por clip, 9:16, sin texto ni música generados.

# Seedance 2.0 — Skill Definitiva de Ingeniería de Prompts

Guía completa construida con patrones documentados en cientos de generaciones reales y pruebas en producción (febrero–mayo 2026). Fusiona la base técnica original con todos los aprendizajes validados en sesiones reales con emprendedores y creadores.

> **Lee este archivo completo antes de generar cualquier prompt.** Luego consulta **references/prompt-engineering.md** para la fórmula, templates y vocabulario completo.

---

## Capacidades técnicas del modelo

Seedance 2.0 acepta hasta **12 archivos de referencia simultáneos**:
- Hasta 9 imágenes (30MB c/u)
- Hasta 3 clips de video (50MB c/u, 2–15 segundos)
- Hasta 3 archivos de audio (15MB c/u, hasta 15 segundos — óptimo 3–8 segundos, solo MP3)

Output: 4–15 segundos, resolución 720p–1080p (2K con upscaling en planes pagados), 24–60 fps.
Lip-sync nativo en 8+ idiomas incluyendo español. Audio y video generados en un solo paso unificado.

**NO soporta negative prompts.** Usa siempre declaraciones positivas de restricción.

---

## Workflow de entrevista

Antes de generar el prompt, identifica si el usuario tiene o no imagen de referencia. Es la bifurcación más importante. Si ya tienes la información en la conversación, no preguntes de nuevo.

### Preguntas universales (siempre hacer):

1. **¿Qué producto, personaje o tema es el video?** — descripción del sujeto principal
2. **¿Cuánto dura el video?** — máximo 15 segundos en Seedance 2.0
3. **¿Qué plataforma?** — vertical 9:16 (TikTok/Reels/Stories), horizontal 16:9 (YouTube/TV), cuadrado 1:1
4. **¿Qué tono?** — dinámico/energético, elegante/lento, emocional, informativo, cinematográfico
5. **¿Quiere narración/voz?** — si sí: idioma, acento, género del locutor
6. **¿Quiere música de fondo?** — género, BPM aproximado, mood

### Pregunta de bifurcación crítica:

7. **¿Tiene imagen/video/audio de referencia para subir?**
   - **SÍ → Modo con referencias (@)** — leer sección correspondiente en prompt-engineering.md
   - **NO → Modo solo texto** — leer sección correspondiente en prompt-engineering.md

Con esas respuestas, construye el prompt siguiendo **references/prompt-engineering.md**.

---

## Reglas críticas que nunca debes romper

Estas reglas aplican a TODOS los prompts de Seedance 2.0 sin excepción:

1. **Un solo verbo de acción por shot** — múltiples verbos en un mismo shot confunden al modelo
2. **Máximo 1–2 personajes por escena** — más de dos causa pérdida de consistencia de identidad
3. **Longitud del prompt: 30–200 palabras** — muy corto pierde control; muy largo hace que el modelo ignore detalles
4. **Nunca uses negative prompts** — Seedance 2.0 no los soporta; usa restricciones positivas ("maintain face consistency, no distortion")
5. **Nunca incluyas textos animados en pantalla** — Seedance los genera con errores; agrégalos en post-producción
6. **Siempre cierra el prompt** con el bloque de Quality keywords
7. **Siempre incluye palabras de restricción de consistencia** en cada shot: "Maintain face and clothing consistency, no distortion, high detail"
8. **Siempre especifica "unfixed camera"** cuando el prompt incluya movimientos de cámara
9. **Siempre declara el ROL del asset @** — sin esta declaración el modelo puede ignorarlo
10. **BPM de música: 75–115 según el tono** — BPM +120 comprime las sílabas del locutor y distorsiona el audio
11. **Evitar frases prohibidas** — ver tabla completa en sección "Palabras y frases PROHIBIDAS"
12. **No subir fotos realistas de personas reales** — ByteDance suspendió esta funcionalidad (anti-deepfake, vigente desde feb 10, 2026)
13. **NUNCA usar "photorealistic humans" ni "live action"** — activan Error 10043300 inmediatamente. Siempre usar "3D animated character" o "Pixar quality animation" como alternativa segura
14. **NUNCA combinar storyboard con instrucciones de humanización realista** — activa Error 10001301. Usar siempre "Pixar quality 3D animated character" como descriptor base
15. **Para escenas grupales siempre declarar número exacto de personajes** — "EXACTLY [N] characters. No duplicates. No additional figures" previene personajes fantasma y duplicados
16. **Truco cabeza inclinada para evitar filtro de rostros** — especificar "head tilted back, face NOT visible from this camera angle" permite generar figura humana sin activar filtro anti-deepfake
17. **Narración en español: usar solo palabras cortas y fonéticamente simples** — ver sección completa "Sistema de pronunciación en español"
18. **No incluir movimientos de cabeza en escenas con diálogo** — "nodding" y "turning head" compiten con el lip-sync y producen movimientos extraños

---

## Sistema de pronunciación en español para Seedance 2.0

Este sistema fue construido combinando pruebas en producción real y fuentes técnicas documentadas (Cutout.pro Audio Guide, CrePal Lip Sync Guide, abril 2026).

### El problema raíz

Seedance 2.0 genera audio y video en un solo paso unificado. El motor de lip-sync mapea fonemas a formas de boca (visemes). En español, ciertos patrones fonéticos lo confunden porque el modelo fue entrenado predominantemente en inglés y mandarín.

### Reglas de oro para narración en español

| Regla | Explicación |
|---|---|
| **Frases de 5–10 palabras máximo** | El lip-sync se deteriora ("mushy") pasado el segundo 8 con frases largas |
| **Palabras de 1–3 sílabas** | Palabras cortas = phonemas claros = sincronía perfecta |
| **Evitar esdrújulas largas** | "auténtico", "científicamente", "específicamente" = distorsión garantizada |
| **Sin tildes complejas en el texto del diálogo** | Escribir sin acentos ortográficos en el prompt: "extrane" en vez de "extrañé" |
| **Sin la letra Ñ en diálogos** | Reemplazar: "año" → "anyo", "señor" → "senyor", "niño" → "ninyo" |
| **Sin palabras con RR o combinaciones difíciles** | "ferrocarril", "desarrollar" → simplificar o reemplazar |
| **Pacing al 80% de velocidad natural** | Agregar en el prompt: "Voice calm and deliberate, slightly slower than natural pace" |
| **Máximo 2–3 líneas para 13 segundos de voz** | Más texto = más riesgo de distorsión y desincronía |
| **Un solo idioma por generación** | No mezclar español e inglés en el mismo diálogo |

### Tabla de reemplazos fonéticos para español neutro

| ❌ Palabra problemática | ✅ Reemplazar por | Razón |
|---|---|---|
| `auténtico` | `real`, `genuino` | Esdrújula larga |
| `científicamente` | `probado`, `comprobado` | Demasiadas sílabas |
| `específicamente` | `exactamente`, `justo` | Demasiadas sílabas |
| `extraordinario` | `increible`, `unico` | Esdrújula + longitud |
| `nutrición` | `salud`, `vida` | Tilde compleja |
| `próximamente` | `muy pronto`, `ya viene` | Esdrújula |
| `comunicación` | `mensaje`, `conexion` | Tilde compleja |
| `año` | `anyo` (fonético) | Letra Ñ |
| `señor` | `senyor` (fonético) | Letra Ñ |
| `niño` | `ninyo` (fonético) | Letra Ñ |
| `mañana` | `manyana` (fonético) | Letra Ñ |
| `extrañé` | `extrane` (fonético) | Ñ + tilde |
| `también` | `tambien` (sin tilde) | Tilde compleja |
| `además` | `ademas` (sin tilde) | Tilde compleja |
| `después` | `despues` (sin tilde) | Tilde compleja |

### Bloque de audio optimizado para español neutro latino

```
[Género] voiceover in Spanish with neutral Latin American accent,
no Spain accent, no regional slang, clear pronunciation,
warm [male/female/child] voice, calm and deliberate pace,
slightly slower than natural speed for clear articulation.
Voice starts at second 1, runs through second [N]:
"[Texto simple, palabras cortas, sin Ñ, sin tildes complejas]"
Voice must be clear, well paced, no rushing. Mouth movements 
fully synchronized to Spanish dialogue. Keep character face 
clearly visible and forward-facing during all speech.
```

### Instrucciones de pacing por personaje

| Personaje | Instrucción adicional |
|---|---|
| Narrador comercial | `"deliberate enunciation, commercial tone"` |
| Personaje emocional | `"calm, warm, low-energy delivery"` |
| Personaje energético | `"excited but clear, breathy, moderate pace"` |
| Niño/a | `"bright cheerful child voice, clear and simple"` |
| Adulto mayor | `"warm deep voice, slow and deliberate"` |

### Qué hacer si el audio sale mal

| Problema | Causa | Solución |
|---|---|---|
| Boca no sincroniza | Frase demasiado larga | Dividir en frases de máx 8 palabras |
| Pronunciación extraña | Palabra con Ñ o esdrújula | Usar reemplazo fonético de la tabla |
| Audio se corta | Texto muy largo | Máx 2–3 líneas para 13 segundos |
| Voz muy rápida | Sin instrucción de pacing | Agregar "slightly slower than natural pace" |
| Movimientos de boca extraños | Instrucción de movimiento de cabeza activa | Eliminar "nodding", "turning head" del prompt |
| Voz en inglés en vez de español | Sin declaración de idioma clara | Agregar "voiceover in Spanish" al inicio del bloque de audio |

### Alternativa profesional recomendada

Si el audio nativo de Seedance no da el resultado esperado en español:

```
PASO 1: Generar el video en Seedance SIN audio (texto puro, omitir bloque de audio)
PASO 2: Grabar voiceover en ElevenLabs con voz "Spanish Latin American"
PASO 3: Unir video + voiceover en CapCut o DaVinci Resolve
```

Resultado: animación de calidad Seedance + voz perfecta en español neutro. Este flujo es el más profesional disponible en 2026.

---

## ✅ Sistema de consistencia de personaje validado en producción real

Sistema probado y validado generando clips reales en Dreamina Seedance 2.0 (mayo 2026). Funciona para personajes **animados estilo Pixar** y para personajes **realistas**. La clave: NO subir ninguna imagen — solo texto puro con descriptores precisos.

### Fórmula ganadora de consistencia

```
[BLOQUE DE PERSONAJE detallado] + [SAME antes de cada rasgo en clip 2+] 
+ [Outfit 100% descrito] + [Rasgo físico único y memorable]
= Consistencia entre clips sin imagen de referencia ✅ VALIDADO
```

### Los 3 anclas más poderosas

| Ancla | Ejemplo | Por qué funciona |
|---|---|---|
| **Rasgo físico único** | "small scar on left eyebrow" / "almond-shaped dark brown eyes" | El modelo lo usa como identificador único del personaje |
| **Outfit completo y específico** | "long beige oversized wool coat, black turtleneck, dark straight leg trousers, white sneakers" | Ropa = identidad visual más estable que el rostro |
| **Palabra SAME** | "SAME long straight black hair", "SAME olive skin warm undertones" | Le indica explícitamente al modelo que replique sin innovar |

### Estructura del bloque de personaje

**Clip 1 — Presentación:**
```
MAIN CHARACTER — memorize every physical detail precisely:
[género] approximately [edad] years old, [complexión], 
[cabello: largo + textura + color], [tono de piel con subtono], 
[ojos: forma + color], [rasgos faciales únicos], 
[rasgo memorable único: scar / lunar / etc].
Wearing [prenda 1 + color + material], [prenda 2], 
[prenda 3], [calzado]. [expresión base del personaje].
```

**Clip 2 en adelante — Ancla de consistencia:**
```
MAIN CHARACTER — exact same details as previous clip:
SAME [género] approximately [edad] years old, SAME [complexión],
SAME [cabello], SAME [tono de piel], SAME [ojos],
SAME [rasgos únicos], SAME [rasgo memorable].
SAME [outfit completo]. Now showing [nueva emoción/estado].
```

### Reglas de oro para consistencia entre clips

1. **Clips de 5 segundos** son más fáciles de mantener consistentes que clips de 15 segundos
2. **Cambiar el escenario, no el personaje** — el modelo mantiene mejor la identidad cuando el entorno cambia
3. **Describir siempre primero el personaje**, luego la escena — el orden importa
4. **Un solo personaje principal por clip** para máxima consistencia facial
5. **Escenas grupales con 3+ rostros juntos** — usar siempre texto puro sin imagen de referencia

### Flujo de producción completo validado

```
PASO 1 — STORYBOARD
Nano Banana 2 / Freepik AI
→ Sketch B&N evita filtros de rostros en Dreamina

PASO 2 — VIDEO ANIMADO (personajes tipo Pixar)
Seedance texto puro sin imagen
→ "Pixar 3D animation style" evita errores 10043300 y 10001301
→ Clips de 5 segundos por escena para mayor consistencia

PASO 3 — VIDEO REALISTA (personas creadas desde prompt)
Seedance texto puro sin imagen
→ Descriptores físicos precisos + SAME = consistencia validada
→ Mismo personaje en escenarios distintos sin subir ninguna foto

PASO 4 — POST PRODUCCIÓN
CapCut → unir clips + agregar subtítulos y diálogos
ElevenLabs → voiceover en español neutro latino profesional
DaVinci Resolve → color grading y audio final
```

---

## Configuración de plataforma recomendada

| Parámetro | Valor recomendado |
|---|---|
| Modo (con imagen) | All-Round Reference / Multiframes |
| Modo (sin imagen) | Text-to-Video / Single-frame |
| Duración | 15s (máximo disponible) |
| Resolución | 2K / 1080p |
| Cámara | Unfixed camera (activado si hay movimientos) |
| Motion intensity | Alta |
| Audio | Habilitado |
| Ratio | 9:16 TikTok/Reels — 16:9 YouTube/TV — 1:1 cuadrado |

---

## Plataformas de acceso (mayo 2026)

| Plataforma | Acceso | Precio | Observación |
|---|---|---|---|
| **Dreamina** (dreamina.capcut.com) | Internacional | Desde $18/mes | ✅ Recomendada principal |
| CapCut Pro | Mercados seleccionados | Plan Pro | ✅ Alternativa |
| Jimeng / 即梦 | China (+86) | 69 RMB/mes (~$9.60) | Solo China |
| Xiaoyunque / 小云雀 | China (+86) | Gratis (120 créditos/día) | Solo China |
| Doubao | China (+86) | ~5 generaciones/día gratis | Solo China |
| **TikTok Symphony** | Internacional | Gratis con cuenta TikTok | ⚠️ SOLO para productos e-commerce. NO sirve para narrativas ni personajes. Pide `target_product` y `product_name` obligatorios |

> **Advertencia:** seedance2.ai, seedance2.app y seedance.tv NO son oficiales de ByteDance. Usar solo seed.bytedance.com o las apps mencionadas.

---

## Solución de errores comunes

| Error | Código | Causa probable | Solución |
|---|---|---|---|
| "No pudimos mostrar el resultado" | — | Palabra bloqueada por filtro | Revisar narración y quitar términos sensibles. Ver tabla de palabras prohibidas |
| "Video didn't pass safety check" | **10043300** | "photorealistic humans", "live action", "real person" combinadas con rostros | Reemplazar por "3D animated character", "Pixar quality animation". NUNCA usar "photorealistic humans" ni "live action movie" |
| "Infracción del control de seguridad de IA" | **10001301** | Storyboard con rostros + instrucciones de humanización realista | Usar "Pixar quality 3D animated character". Eliminar: "realistic skin texture", "natural human proportions", "pure cinematic photorealism" |
| "Video didn't pass safety check" | **10012301** | Dos o más storyboards con rostros subidos simultáneamente, o storyboard con 3+ rostros muy juntos en primer plano | Subir solo UNA imagen de referencia. Para escenas de abrazo grupal, festejo, soplar velas → texto puro sin ninguna imagen |
| Producto cambia entre shots | — | Referencia @ débil | Agregar en cada shot: "Product appearance strictly follows @NombreImagen" |
| Narración distorsiona palabras en español | — | Esdrújulas, Ñ, tildes complejas o frases largas | Usar tabla de reemplazos fonéticos. Máx 8 palabras por frase. Sin Ñ |
| Boca no sincroniza con diálogo | — | Frases muy largas o movimientos de cabeza activos | Dividir frases, eliminar "nodding" y "turning head" del prompt |
| Producto aparece volteado | — | Instrucción de órbita 360° | Reemplazar "360-degree orbit" por "slow pull-back hero reveal, always facing camera front, no rotation" |
| Video parece foto en movimiento | — | Falta de acción real | Agregar verbos de impacto: "bursts", "explodes", "crashes", "splashes", "flies through frame" |
| Generación lenta o falla | — | Prompt demasiado largo | Simplificar a 80–120 palabras por shot, máximo 200 palabras totales |
| Personaje cambia de cara entre clips | — | Sin sistema de consistencia | Aplicar Sistema de Consistencia validado: bloque MAIN CHARACTER + SAME en clip 2 |
| Imagen de persona rechazada | — | Anti-deepfake activado | Usar imágenes ilustradas, estilizadas o personajes no reales |
| Subtítulos aparecen solos | — | Modelo los genera por defecto | Agregar al bloque Quality: "Generate video without subtitles" |
| Muñeco sin cara en vez de persona | — | Storyboard tenía figura sin rostro y Seedance lo animó literalmente | Describir el personaje explícitamente. Usar truco de cabeza inclinada bebiendo |
| Personaje duplicado en escena grupal | — | Instrucción de abrazo grupal ambigua | Agregar: "EXACTLY [N] characters in this scene. No duplicates. No additional figures" |
| Audio se corta a mitad del clip | — | Referencia de audio supera el punto óptimo | Recortar referencias de audio a 3–8 segundos. Solo usar MP3 |
| Voz en inglés en lugar de español | — | Sin declaración de idioma en el bloque de audio | Añadir "voiceover in Spanish with neutral Latin American accent" explícitamente |

---

## ⛔ Palabras y frases PROHIBIDAS en Dreamina/Seedance

| ❌ PROHIBIDO | ✅ REEMPLAZAR POR |
|---|---|
| `photorealistic humans` | `3D animated characters` |
| `photorealistic Father/Mother/Son` | `animated Father/Mother/Son character` |
| `live action movie` | `Pixar quality animated film` |
| `pure cinematic photorealism` | `high quality 3D animation` |
| `realistic human skin texture` | `detailed 3D render texture` |
| `realistic human body proportions` | `natural cartoon body proportions` |
| `no cartoon style` | ❌ Eliminar completamente |
| `real person` | `animated character` |
| `transform sketch into real human` | `animate character in Pixar 3D style` |
| `humanize the drawing` | `bring character to life in 3D animation style` |
| `ghosting` | `artifacts` |
| `conservantes` / `preservatives` | `aditivos` / `additives` |
| `chemical` | `natural` |
| `deepfake` | ❌ Eliminar completamente |
| `celebrity name` (nombre real) | ❌ Eliminar completamente |
| `gore`, `violence`, `blood` | ❌ Eliminar completamente |

---

## Referencias

- **references/prompt-engineering.md** — Fórmula universal, anatomía del prompt, modo CON y SIN referencias, vocabulario de cámara, audio, templates por tipo de video, color grading, vocabulario de dinamismo, distribución de shots.

---

## Output esperado

Al finalizar, entrega siempre al usuario:

1. El prompt completo listo para copiar y pegar en Seedance
2. La configuración de plataforma recomendada (modo, duración, ratio, cámara)
3. Un aviso sobre los textos en pantalla (agregarlos en post con CapCut o DaVinci)
4. Si hay errores en generaciones previas, indicar el código exacto, la causa y cómo se corrigió
5. Si no tiene imagen de referencia, confirmar que el prompt está optimizado para modo texto puro
6. Si el usuario quiere múltiples clips con el mismo personaje, aplicar el Sistema de Consistencia validado — bloque MAIN CHARACTER + SAME en clip 2 en adelante
7. Si el usuario menciona TikTok Symphony, advertir que es solo para productos e-commerce y redirigir a Dreamina
8. Si el usuario quiere narración en español, aplicar el Sistema de Pronunciación y la tabla de reemplazos fonéticos antes de escribir el diálogo
