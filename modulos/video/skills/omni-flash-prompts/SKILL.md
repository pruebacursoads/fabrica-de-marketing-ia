---
name: omni-flash-prompts
description: >
  Crea, adapta y corrige prompts para Gemini Omni Flash 1.2 (y 1.1) en Google
  Flow: avatar propio (@me) con voz propia, spots de producto o servicio,
  TikToks/Reels, videos informativos, ficción, selfies, edición de videos
  existentes (cambiar ángulos, fondo, reemplazar personaje) y animación de
  imágenes. Pensada para la primera etapa de la Fábrica de Contenido: producir
  los clips gratis, descargarlos y pasarlos a edición. Úsala cuando el usuario
  diga Omni Flash, Gemini Omni, Google Flow, "video con Gemini" o "mi avatar".
  No usar para Seedance, Veo ni Kling.
---

> ## 🔗 Integración con la Fábrica de Marketing con IA
> Si existen `Mi negocio/adn-de-marca.md` y `Mi negocio/diagnostico-situacional.md` en la carpeta de trabajo, **léelos primero** y úsalos como contexto: **no repitas preguntas** que ya responden (marca, colores, tono, claims, objetivos). Nunca uses la identidad de otra marca. Si te lanzó un agente `fm-agente-*` o el director `fm-director`, **no hagas preguntas al alumno**: usa el brief y el ADN, anota supuestos y entrega en la carpeta indicada. Cuando corresponda, reporta avance con la skill `fm-panel`.
> **Reglas aprendidas con clientes:** avatar con `@me` (si habla con su voz: "el avatar dice: …"), prompts ligeros por lineamientos, dinámico (nunca primer plano estático), **sin texto ni música generados** (sonido ambiente), 9:16, en español, clips ≤ 10 s, referencias exactas por clip y su orden, ≤ 30 s por video, sin cuchillos en cuadro y la cobertura/ubicación del negocio en todos los videos. Los clips se generan **a mano en Google Flow** y luego pasan a la Fábrica de Video.
> **Lee primero [`references/multi-toma-y-realismo.md`](references/multi-toma-y-realismo.md) (v1.1): manda sobre las demás reglas de video.** Un video es una secuencia de 5-6 tomas distintas (clips de 4-8 s; uno de 10 s solo con ≥3 cambios de cámara dentro), la continuidad es **por escena** (mismas referencias de lugar, producto y ropa) y **no** con el último fotograma del clip anterior, y la escena sale de **fotos reales** del alumno (Nano Banana 2 o GPT Image 2.6 las mejoran y reencuadran a 9:16), nunca de un local inventado "de película".

# Omni Flash 1.2 — Producción de clips (v4.0)

Investigación revisada el 8 de noviembre de 2026. Modelo objetivo: Gemini Omni
1.2 Flash (lanzado el 5-nov-2026). Superficie: Google Flow, plan gratis o pago.

## Rol dentro de la Fábrica de Contenido

Esta skill es la **etapa 1 (gratis)**: conseguir los clips. Hay dos caminos y
ambos terminan igual, con archivos descargados que entran a la Fábrica (edición,
subtítulos, música, motion graphics):

- **Camino A — Grabarse de verdad.** Esta skill entrega guion y plano sugerido.
- **Camino B — Generar con Omni Flash en Flow.** Esta skill entrega los prompts.

Sin API de pago: se genera a mano en Flow (ver "Límites y costos"). La API existe
y sirve para automatizar más adelante, pero no es necesaria.

Prompts ya armados con tus casos (evento, selfie del camión, seminuevo, ediciones):
[plantillas-hugo.md](references/plantillas-hugo.md). Cárgalo solo cuando el encargo se parezca.

### Entrega a la Fábrica (siempre al terminar)

Lista por clip: nombre (`01-gancho.mp4`), duración, qué dice (guion literal),
**qué texto/música/subtítulos se agregan en edición** y qué debe quedar limpio
(sin texto, sin música) para que la edición los pueda poner.

## Qué cambió en 1.2 (fuentes: Google, Flow Help)

| Tema | 1.1 | 1.2 |
|---|---|---|
| Duración | 4/6/8/10 s | **3 a 15 s** en pasos de 1 s. Sin plan de Google AI: 3–10 s. Con Plus/Pro/Ultra: hasta 15 s |
| Consistencia | Deriva de cara/ropa | Mejor del primer al último cuadro, menos deformación |
| Cámara | Cortes involuntarios | Movimientos continuos (órbita, retroceso, FPV) con menos cortes bruscos |
| Voz | Buena | Más natural, mejor sincronía labial, **varios hablantes** |
| Referencias | Imágenes | Imágenes de personaje/producto/estilo, clips de movimiento de hasta 3 s |
| Edición | Hasta 10 s | Multi-turn sobre clip completo; en Flow hasta 3 turnos de refinamiento |
| Extender | No | **Omni Extend** solo con plan de pago y solo en web (3–10 s por extensión) |
| Calidad | — | Borrador 360p/720p, subir a 1080p (4K solo Ultra) |

**Fechas:** Omni Flash 1.1 se retira de Flow el **5 de diciembre de 2026**.
Desde esa fecha todo corre en 1.2; actualiza los hábitos de 1.1 ya.

Google reconoce que sigue mejorando: acción deportiva rápida, cambios rápidos de
guion y física compleja. Evita pedirlos o aplica correcciones por turnos.

## Principio de trabajo (el más importante)

El modelo interpreta bien un **esqueleto corto**. Demasiadas instrucciones lo
marean y empeoran el resultado (confirmado por Hugo con 1.1 y por guías de Google
y de terceros: un prompt de 3–4 frases suele superar a uno largo).

Estructura sugerida (omite lo que no haga falta):
**encuadre + movimiento de cámara · estilo · luz · lugar · acción · sonido**.

Reglas:
- **Una instrucción de cámara principal.** Señales contradictorias dan un promedio flojo.
- Nombra el movimiento ("push in", "órbita lenta"), no describas su efecto.
- No expliques física que el modelo ya conoce ("el asfalto mojado refleja la luz").
- Si no dices algo, el modelo lo decide (música, ruido, plano). Dirige solo lo que importa.
- Las exclusiones van dentro del prompt ("sin música, sin subtítulos"); no hay
  campo de negativos. Agrúpalas en **una sola línea final**; no las repitas.
- Plano continuo: pide "una sola toma continua, sin cortes" (solo para producto o escenas sin
  avatar hablando). Dinámico con cortes: pide "cambios naturales de cámara y ángulo" o
  tramos `[0-3 s] … [3-6 s] …`. **Con avatar hablando nunca uses plano único**: cambia el
  encuadre dentro del clip o genera varias tomas (ver multi-toma-y-realismo.md).
- Con tiempos: lenguaje natural ("a los 3 segundos entra…") o `[0-5s] … [5-10s] …`.
  Úsalo solo si el orden de momentos importa.
- Frases cortas sincronizan mejor. Pocas frases por clip.

**Cuándo endurecer:** si algo falla (duplicados, ropa que cambia, entrar/salir de
un auto, objetos en la mano) añade una línea de estado inicial o de constantes.
Ya no se usa la plantilla STATE + SINGLE ACTION por defecto.

## Avatar propio (@me) — receta validada por Hugo

- Se invoca con `@me`. Voz propia: "el avatar dice: …" + "con su propia voz, en
  español latino con acento neutro (o peruano)". No describas timbre.
- Un solo bloque de **constantes** del avatar: rostro, peinado, lentes y vestimenta
  con código de color si hace falta ("terno gris 8F99A5"). Una vez, no repetido.
- **Dinámico siempre:** cambios de ángulo y encuadre, cámara en mano o selfie
  (el celular nunca se ve; si el avatar necesita las dos manos, "cámara en movimiento,
  como grabada por otra persona"). Un primer plano estático o un plano único se nota falso:
  varias tomas, no un clip fijo.
- Entrada con gancho en el primer segundo (aterriza, camina hacia cámara, gesto).
- Cierre con gesto directo a cámara. Gesto señalando a sí mismo si dice "estaré yo".
- Escenas sin el avatar: detalla escena, personajes y ambiente.
- Referencia de lugar/vehículo: "como en la imagen de referencia", con su rol.
- Hugo pide y recibe los prompts **en español**. Conserva tildes y ñ.
- Números en palabras ("catorce", "diecisiete", "treinta por ciento").

### Tiempo de habla (revisar siempre)

Español claro con energía ≈ 2,5–3 palabras por segundo, restando pausas y acción.
- 10 s → **24–28 palabras** (31 es justo y arriesga que se corte o se acelere).
- 15 s → 38–44 palabras. 6 s → 14–16.
Un guion literal no se cambia: si no cabe, ofrece versión abreviada o dividir en
dos clips con la misma frase de continuidad.

## Texto en pantalla y sonido

Dos modos; el proyecto elige, y el default de Hugo es el A:

- **A. Limpio (default para la Fábrica):** "sin texto en pantalla, sin subtítulos,
  sin música; solo sonido ambiente realista de [lugar]". Texto y música se ponen
  en edición, donde la ortografía es perfecta.
- **B. Texto corto del modelo:** máximo 3 palabras clave, literales y en mayúsculas
  ("NUEVA FUNCIÓN", "¡MIRA ESTO!"). Más texto marea. Revisa ortografía; si falla,
  pásalo a modo A y corrígelo en edición.
- Logos y precios: mejor en edición. Si se generan, clip aparte con solo el logo.

## Referencias

- Nómbralas en lenguaje natural con su rol ("la imagen es el local de la entrada;
  úsalo como escenario"). Las etiquetas tipo `<IMAGE_REF_0>` están obsoletas.
- Límites documentados en la API (Flow puede variar): hasta 6 imágenes, 3 por
  personaje y 2 personajes; clips de movimiento de hasta 3 s, solo al generar,
  no al editar ni extender. El audio de los videos de referencia se ignora.
- Sube solo lo que aparece en ese clip. No mezcles varios videos de referencia.
- `@me` es el avatar de Flow; no inventes otros `@`.

## Edición de video existente (video a video)

Casos de Hugo: mejorar ángulos y enfoque de un ponente, quitar un título, cambiar
el fondo, reemplazar a una persona por el avatar, convertir una toma fija en dinámica.

- **Prompt simple, un cambio por turno.** Los prompts muy descriptivos provocan
  cambios no deseados. Termina con "Mantén todo lo demás igual."
- Di qué se conserva: voz, contenido, tiempos. Para reemplazo: "Reemplaza a [quien]
  por @me; conserva movimientos, gestos, cámara, luz, escenario y duración; cambia
  solo el personaje y su ropa".
- En Flow: clip fuente hasta 60 s y 1 GB; se refina un tramo de 10 s (15 s en
  plan pago); hasta **3 turnos** de refinamiento. Para clips largos, recorta antes.
- La edición reinterpreta el video: el texto en pantalla y el diseño pueden cambiar.
  Verifica que la voz siga siendo la del avatar.
- Cambiar el fondo por un lugar con movimiento (calles de París con gente) funciona
  como un cambio de fondo; pídelo sin añadir texto en el mismo turno.
- Texto de impacto sobre el video: ponlo en la Fábrica salvo que se pida modo B.

## Multi-Turn y borradores (ahorra créditos)

1. Turno 1: genera a 360p y 10 s o menos.
2. Turnos 2–4: "Mantén todo igual. Cambia solo [un elemento]."
3. Solo el clip aprobado: subir a 1080p.
4. Si el problema es el guion o la acción, regenera; si es un detalle, edita.

## Límites y costos (para decidir el flujo gratis)

- **Gratis:** 3–10 s por clip. Referencias y edición de video disponibles en todos
  los planes. Extender y varias funciones de calidad requieren plan de pago.
- **Pago (Plus/Pro/Ultra):** 15 s, Omni Extend (web), más créditos mensuales.
- **Créditos:** Google confirma que 360p cuesta un tercio de 720p. Una página
  de terceros (Nereo) habla de 50 créditos diarios gratis, pero **no está confirmado**
  (esa página corre 1.1); confirma en el selector de modelo de Flow cuánto cuesta cada clip.
- **API (opcional, de pago):** unos 0,07 USD por segundo en 720p (≈0,70 USD un
  clip de 10 s). Solo para automatizar después.
- Funciones de voces personalizadas y algunas de Omni son por región.
- Los videos llevan marca de agua SynthID imperceptible.
- Frames a video (primer y último fotograma): solo en Flow web.

**Clips más largos que un clip:** divide en tomas autosuficientes de 4-8 s (10 s solo con
cambios de cámara dentro), repite las mismas referencias de escena, producto y ropa (no el
último fotograma del clip anterior) y une en la Fábrica. Con Omni Extend, el
modelo usa los últimos 10 s como contexto: vuelve a mencionar al personaje.

## Cámara y vocabulario

extreme close-up, close-up, medium shot, wide shot, establishing shot, low/high
angle, top-down, over-the-shoulder, POV; push in, pull back, pan, tilt, orbit,
tracking shot, FPV, handheld, locked off, dolly zoom, oner; shallow depth of
field, macro lens feel, telephoto compression. En español funcionan sus
equivalentes ("plano contrapicado", "cámara en mano"). Orienta, no garantiza.

## Errores frecuentes y correcciones

| Síntoma | Corrección |
|---|---|
| Cortes o fundidos no deseados | "Una sola toma continua, sin cortes" (o corte directo si hay varias escenas) |
| Vehículo o personaje duplicado | "Exactamente un [objeto]. Sin duplicados" |
| Ropa o rostro cambian | Bloque de constantes una vez; reforzarlo durante habla y giros |
| Avatar se ve falso | Quitar primer plano fijo; selfie en mano; cambios de ángulo |
| Se corta el habla / va muy rápido | Recortar el guion al conteo de palabras |
| Audio en inglés o con otro acento | Declarar "español latino, acento neutro" |
| Música o texto que no pedías | Declararlo en la línea de exclusiones |
| Celular visible en selfie | "El celular nunca aparece en cuadro" |
| Producto rota y queda al revés | Órbita parcial de frente a 3/4, siempre mirando a cámara |
| Texto con errores | Pasarlo a edición |
| Rechazo de la plataforma | Identificar el límite y reformular a una versión permitida; no buscar atajos |

## Entrega útil

1. Prompt principal en español, listo para copiar, sin explicaciones dentro.
2. Nota breve: qué cargar, `@me` o no, duración (3–15 s), orientación, resolución de borrador.
3. Conteo de palabras del guion contra la duración.
4. Para series: clip por clip, qué cargar, qué pasa y suma de duraciones.
5. Entrega a la Fábrica (texto, música y subtítulos que se agregan después).
6. Si el encargo es otro modelo, aclararlo y redirigir.

## Verificar antes de entregar

Propósito, verdad del mensaje, recursos, contradicciones (ropa fija vs cambio de
ropa, cámara fija vs movimiento, "sin texto" vs pedir letras), tiempo de habla.
No prometas retención ni ventas.

## Registro de aprendizaje

Por prueba: versión (1.1 o 1.2), plan (gratis/pago), recursos, duración, prompt,
resultado, siguiente decisión. Lo propuesto no está validado hasta probarlo.

### Probado por Hugo
- 1.1: prompts ligeros con esqueleto funcionan; con demasiado detalle empeoran.
- `@me` + "el avatar dice": voz propia; selfie dinámico, nunca estático.
- Sin música ni texto generados; se agregan en edición.
- Prompts en español funcionan bien.

### Por probar en 1.2 (propuestas)
- Si 31 palabras caben en 10 s o conviene 24–28.
- Si "una sola toma continua" mejora el selfie del camión.
- Si 15 s con avatar mantiene el rostro mejor que dos clips de 8 s.
- Costo real en créditos del plan gratis y calidad final de 360p subido a 1080p en 9:16.
- Si Omni Extend sirve para enlazar clips de avatar sin perder la voz.
