---
name: veo31-prompts
description: >
  Genera prompts cinematográficos profesionales para Veo 3.1 de Google DeepMind, el modelo de generación de video con IA más avanzado de Google en 2026. Usa esta skill SIEMPRE que el usuario quiera crear videos con Veo, Veo 3, Veo 3.1, Google Flow, VideoFX, Vertex AI Video, o cualquier plataforma que use el modelo Veo de Google. Incluye ingeniería de prompts completa para TODOS los tipos de contenido: productos, inmuebles, lifestyle, cinematográfico, educativo, diálogo con personajes, transiciones first/last frame, y uso de referencias visuales (ingredients to video). Aplica también cuando el usuario diga "quiero hacer un video con Google", "genera un spot con Veo", "crea contenido para redes con IA de Google", "video publicitario con Veo", "anima esta imagen con Google", o similares. Cubre tanto el modo texto puro como el modo con imágenes de referencia.
---

> ## 🔗 Integración con la Fábrica de Marketing con IA
> Si existen `Mi negocio/adn-de-marca.md` y `Mi negocio/diagnostico-situacional.md` en la carpeta de trabajo, **léelos primero** y úsalos como contexto: **no repitas preguntas** que ya responden (marca, colores, tono, claims, objetivos). Nunca uses la identidad de otra marca. Si te lanzó un agente `fm-agente-*` o el director `fm-director`, **no hagas preguntas al alumno**: usa el brief y el ADN, anota supuestos y entrega en la carpeta indicada. Cuando corresponda, reporta avance con la skill `fm-panel`.
> **Nota:** modelo de pago por créditos; usa Omni Flash (gratis en Flow) por defecto y esta skill solo si el alumno lo pide. Referencias exactas por clip, 9:16, sin texto ni música generados.

# Veo 3.1 — Skill de Ingeniería de Prompts

Guía completa para generar videos profesionales con Veo 3.1 de Google DeepMind. Basada en la guía oficial de Google Cloud, Google DeepMind, y comunidades verificadas (2025–2026).

> **Lee este archivo completo antes de generar cualquier prompt.** Luego consulta **references/prompt-engineering.md** para la fórmula, plantillas y ejemplos detallados.

---

## Capacidades técnicas del modelo

- **Resolución:** 720p o 1080p
- **Duración por clip:** 4, 6 u 8 segundos (máximo 8 segundos)
- **Aspect ratio:** 16:9 (YouTube/TV) o 9:16 (TikTok/Reels/Shorts)
- **Audio nativo:** diálogo con lip-sync, SFX y ambience generados simultáneamente
- **Idiomas de lip-sync:** múltiples idiomas incluyendo español
- **Marca de agua:** SynthID (invisible, marca todos los videos como generados por IA)
- **Velocidades:** Standard (calidad máxima) y Fast (iteración rápida)

### Modos de generación disponibles

| Modo | Descripción | Cuándo usarlo |
|---|---|---|
| Text-to-Video | Solo prompt de texto | Sin imágenes de referencia |
| Image-to-Video | Anima una imagen de inicio | Cuando hay una foto base |
| First & Last Frame | Transición entre dos imágenes | Revelaciones, transformaciones |
| Ingredients to Video | Múltiples refs de personaje/escena/objeto | Consistencia de personaje/producto |
| Add/Remove Object | Añadir o eliminar objetos de un video | Edición post-generación |

---

## Workflow de entrevista

Antes de generar el prompt, recopila esta información. Si ya la tienes, no preguntes de nuevo.

### Preguntas universales:

1. **¿Qué producto, servicio, inmueble o tema es el video?**
2. **¿Cuántos segundos?** — 4, 6 u 8 segundos (recomendado: 8s para mayor impacto)
3. **¿Qué plataforma?** — 16:9 (YouTube/TV) o 9:16 (TikTok/Reels/Shorts)
4. **¿Qué tono?** — comercial dinámico, elegante/premium, emocional, informativo, cinematográfico
5. **¿Quiere diálogo o voz?** — si sí: texto exacto a decir, tono de voz, idioma
6. **¿Quiere música/SFX?** — género, mood, efectos de sonido específicos

### Pregunta de bifurcación crítica:

7. **¿Tiene imagen(es) de referencia para subir?**
   - **SÍ → Modo con referencias** — image-to-video, first/last frame, o ingredients to video
   - **NO → Modo texto puro** — descripción detallada del sujeto en el prompt

Con esas respuestas, construye el prompt siguiendo **references/prompt-engineering.md**.

---

## Reglas críticas que nunca debes romper

1. **Un clip = una escena, una acción dominante** — múltiples acciones simultáneas rompen la física
2. **Máximo 100–150 palabras por prompt** — demasiado largo dilluye el control del modelo
3. **El sujeto va primero y debe estar muy descrito** — sin ancla visual, el personaje deriva entre frames
4. **Siempre definir la cámara** — sin instrucción de cámara, Veo elige genérico
5. **Siempre definir el audio** — si no se especifica, Veo genera audio aleatorio que puede no coincidir
6. **Nunca stacking de acciones** — "camina, habla y gesticula" = video roto. Un verbo por escena
7. **No usar conteos exactos de personas** — "5 personas" falla; usar "un grupo pequeño de colegas"
8. **Negative prompts = en positivo** — nunca "no man-made structures", sino "a barren landscape untouched by roads or buildings"
9. **Diálogo: usar comillas** — A woman says, "We have to leave now." — y mantener frases de máximo 1 respiración
10. **Añadir "no subtitles / no captions"** al final si no se quiere texto en pantalla
11. **Material cues estabilizan al sujeto** — "charcoal cotton hoodie" da un perfil de reflexión de luz que evita drift visual
12. **Para multi-shot: generar clips separados** y editar en post (Flow, CapCut, DaVinci)

---

## Configuración recomendada

| Parámetro | Valor recomendado |
|---|---|
| Duración | 8 segundos (máximo, mayor control) |
| Resolución | 1080p |
| Modo de velocidad | Standard (producción) / Fast (pruebas) |
| Audio | Activado siempre |
| Ratio | 9:16 Reels/Shorts — 16:9 YouTube/TV |

---

## Plataformas de acceso (2026)

| Plataforma | Acceso | Precio aproximado |
|---|---|---|
| Google Flow (labs.google/flow) | Gemini Ultra suscriptores | $20/mes (Gemini Ultra) |
| Google AI Studio | Limitado / experimental | Gratis con cuota |
| Vertex AI | Empresas y desarrolladores | API por uso |
| VideoFX (aitestkitchen) | Waitlist experimental | Gratis (waitlist) |
| Invideo AI | Internacional | Desde $20/mes |
| LTX Studio | Internacional | Planes Pro/Enterprise |
| Atlabs AI | Internacional | Planes disponibles |

---

## Solución de errores comunes

| Error | Causa probable | Solución |
|---|---|---|
| Personaje cambia de cara entre frames | Sujeto mal definido | Añadir edad, color de cabello, ropa con material específico al inicio del prompt |
| Movimiento parece flotante / irreal | Verbos de acción vagos | Usar verbos de fuerza: "leans forward", "slams", "sways", "ripples" |
| Audio no coincide con la acción | Sin especificación de audio | Añadir bloque Audio: con SFX, Ambience y Dialogue explícitos |
| Subtítulos aparecen solos | Veo los genera por defecto | Añadir al final: "No subtitles. No captions. No on-screen text." |
| Cámara genérica / plana | Sin instrucción de cámara | Definir siempre: shot type + camera movement + lens |
| Diálogo mal sincronizado | Frase demasiado larga | Reducir a máx 1 oración corta por breath. Máx 10–12 palabras |
| El personaje equivocado habla | Dos personajes sin ancla | Identificar al hablante por rasgo visual: "The woman in the red jacket says..." |
| Video se siente estático | Sin acción física en el sujeto | Añadir micro-movimientos: "subtle breath", "slight sway", "eyes shift" |
| Resultado inconsistente | Prompt demasiado largo o abstracto | Simplificar a 100–150 palabras con lenguaje cinematográfico concreto |
| Objetos o personas a escala incorrecta | Sin reglas espaciales | Añadir: "People at natural human scale relative to environment" |

---

## Referencias

- **references/prompt-engineering.md** — Fórmula de 7 capas, modo CON y SIN referencias, vocabulario de cámara, audio, timestamps, plantillas por tipo de contenido (producto, inmueble, lifestyle, diálogo, cinematográfico, transición, comercial).

---

## Output esperado

Al finalizar, entrega al usuario:

1. El prompt completo listo para copiar y pegar en Veo 3.1
2. La configuración recomendada (duración, ratio, modo, audio on/off)
3. Herramientas recomendadas para este tipo de contenido
4. Un tip específico basado en lo que puede fallar en este tipo de video
5. Pregunta: ¿Quieres ajustar algo o generar otra escena?
