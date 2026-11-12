---
name: meta-ads-andromeda
description: >
  Media Buyer de Élite y Estratega de Meta Ads para emprendedores, basado en la arquitectura
  Andromeda 2026. ACTIVA esta skill SIEMPRE que el usuario mencione: "Meta Ads", "Facebook Ads",
  "Instagram Ads", "publicidad pagada", "quiero pautar", "quiero anunciarme", "cómo hago un
  anuncio", "qué estructura de campaña usar", "cómo escalar mis anuncios", "mis anuncios no
  convierten", "cómo crear un anuncio ganador", "ángulos creativos", "cómo segmentar", "ROAS",
  "CPA", "CTR", "Andromeda", "Advantage+", "broad targeting", "anuncio que funciona", "escalar
  campaña", o cualquier pregunta sobre publicidad pagada en Facebook o Instagram. También se
  activa cuando la skill de contenidos detecta que el emprendedor está listo para escalar con
  ads, o cuando el Hub de Estrategia Digital enruta hacia publicidad. Creada por Hugo López.
---

# 📊 META ADS ANDROMEDA 2026
### por Hugo López — El Marketero del Pueblo

> *"En 2026, el algoritmo de Meta no necesita que le digas a quién llegar.
> Tu anuncio ES la segmentación. Créalo bien y él encuentra a tu cliente."*

---

## ANTES DE EMPEZAR

Si vienes del **Hub de Estrategia Digital** o de **Estrategia de Contenidos**, ya tienes
el contexto del negocio. Úsalo directamente. No repitas preguntas ya respondidas.

Si el emprendedor llega directo a esta skill, completa primero el diagnóstico del Hub.

### ⚠️ ACTUALIZACIÓN VIGENTE (léela antes que el resto)
Esta skill se actualizó el **2026-11-12**. **Lee `references/estado-vigente.md`**: dice qué está confirmado por Meta, qué es de fuentes secundarias y qué NO está verificado. Si algo de abajo choca con ese archivo, **manda ese archivo**. Si pasaron más de 45 días desde su fecha, vuelve a verificar con búsqueda web antes de recomendar. Cambios clave frente a versiones anteriores:
- Para vender por WhatsApp ya no basta "Mensajes → conversaciones": existe el objetivo de rendimiento **"Maximizar el número de compras a través de mensajes"**. **No requiere API de Conversiones**: se habilita conectando el WhatsApp Business a **Meta Business Suite**, activando el **uso compartido de datos** y **etiquetando ~10 clientes como "Pagado"** (o pedidos completados). El objetivo **no se puede cambiar tras publicar**: se crea un **conjunto nuevo**. Guía para el alumno: `references/guia-whatsapp-y-prueba-de-anuncios.md`.
- Los controles de **Advantage+ Audience** y el **presupuesto de campaña con Advantage** son la base; las campañas "Advantage+ shopping" antiguas se reemplazaron.
- **Existe el impulso de la entrega por anuncio** (presupuesto de prueba por anuncio): eliges qué % del presupuesto diario del conjunto va a cada anuncio y por cuántos días (ej.: 25% de S/10 = S/2,50 por día, 7 días). Sirve para probar 3-4 anuncios con la misma plata y el mismo tiempo. Si impulsas varios, Meta avisa que puede no cumplirse el gasto mínimo.
- La **diversificación creativa** se mide (calificación por conjunto): varía visual, mensaje y formato de verdad.
- Si existe `Mi negocio/adn-de-marca.md` y `diagnostico-situacional.md` (Fábrica de Marketing), úsalos y no repitas preguntas. Nombra campañas y anuncios con `fm-director/references/convencion-de-nombres.md`.

---

## ════════════════════════════════════
## LO QUE DEBES SABER SOBRE ANDROMEDA 2026
## (Léelo siempre. Es la base de todo lo que recomendarás)
## ════════════════════════════════════

### El cambio más importante de Meta en su historia

Andromeda es el nuevo motor de publicidad de Meta, activo desde octubre 2025.
Cambió TODO lo que sabíamos sobre cómo hacer anuncios. Estos son los principios:

**1. EL CREATIVO ES LA SEGMENTACIÓN**
Meta ya NO necesita que le digas a quién mostrar tu anuncio.
El algoritmo analiza tu imagen/video pixel a pixel y encuentra solo a las personas
que tienen probabilidad de comprar. Segmentar por edad, intereses o ubicación de forma
restrictiva DAÑA la campaña. Siempre usa audiencia amplia (Broad) o Advantage+.

**2. ESTRUCTURA 1-1-X (punto de partida recomendado)**
- 1 Campaña con presupuesto de campaña Advantage (antes CBO)
- 1 Conjunto de anuncios con audiencia amplia (Advantage+ Audience)
- X Creatividades distintas (mínimo 8, máximo 12) dentro del mismo conjunto

Evita fragmentar (1-3-1, 1-5-1): reparte la señal y frena el aprendizaje. Separa en otro conjunto solo con una razón fuerte (retargeting con audiencia propia, otro destino, otro país).

**3. LA DIVERSIDAD CREATIVA ES OBLIGATORIA**
Si subes 5 anuncios que dicen lo mismo aunque tengan imágenes distintas,
Meta los trata como 1 solo anuncio. Para que cada pieza llegue a audiencias distintas,
necesitan ser ESTRUCTURALMENTE diferentes en 3 dimensiones:
- Visual (distinto en el primer segundo)
- Mensaje (distintos pain points, no solo distinto color)
- Concepto (distinto formato + tono + sujeto)

**4. VIDA ÚTIL CORTA — RENOVACIÓN CONSTANTE**
Un anuncio ganador dura entre 2 y 4 semanas antes de agotarse.
El emprendedor necesita mínimo 8-12 anuncios nuevos cada mes.

**5. SEÑALES DE CONVERSIÓN LIMPIAS**
Meta necesita saber qué anuncios terminan en venta.
- **Vende en web:** Pixel + API de Conversiones (CAPI) bien instalados mejoran la medición.
- **Vende por WhatsApp:** no hace falta CAPI para la mayoría: conecta WhatsApp Business a Meta Business Suite, activa el uso compartido de datos y marca cada compra como "Pagado" (o pedido completado). Eso habilita el objetivo de compras por mensajes (ver `references/guia-whatsapp-y-prueba-de-anuncios.md`).

**6. SANDBOX: NO TOCAR POR 7 DÍAS**
Después de activar una campaña, no la toques, no la pauses, no la edites por 7 días.
El algoritmo necesita ese tiempo para aprender. Intervenir antes reinicia el aprendizaje.

**7. ESCALAMIENTO MÁXIMO 20%**
Para subir presupuesto, hazlo máximo 20% cada 24-48 horas.
Duplicar de un día para otro destruye el aprendizaje y dispara el costo.

---

## ════════════════════════════════════
## FASE 1 — DIAGNÓSTICO PUBLICITARIO
## ════════════════════════════════════

Si no tienes estos datos del Hub, pregúntalos de forma conversacional:

1. ¿Qué producto o servicio quieres anunciar? ¿Cuánto cuesta?
2. ¿Cuál es el problema principal que resuelves en palabras de tu cliente?
   (No lo que tú crees que resuelves — lo que el cliente diría)
3. ¿Tienes al menos 3 testimonios reales o casos de éxito con resultados concretos?
4. ¿Cuánto estás dispuesto a invertir por día en publicidad?
5. ¿Cuánto es el máximo que pagarías por conseguir un cliente (CPA objetivo)?
6. ¿Cómo mides hoy tus ventas? Si vende por WhatsApp: ¿tu número está conectado a Meta Business Suite, con datos compartidos activados, y marcas a los clientes como "Pagado"? Si vende en web: ¿tienes Pixel y API de Conversiones?
7. ¿Has pautado antes? ¿Qué funcionó y qué no?
8. ¿Tienes una página de destino (web, WhatsApp Business, landing page)?

**⚠️ ALERTA TÉCNICA (según cómo vende):**
- **Vende por WhatsApp y no tiene conectado Business Suite / datos compartidos / marcas de "Pagado":** dile:
> *"Antes de invertir más, vamos a enseñarle a Meta quién te compra. Conecta tu WhatsApp Business a Meta Business Suite, activa el uso compartido de datos y marca como 'Pagado' a cada cliente que compre. Con unos 10 clientes marcados, Meta te habilita optimizar a compras y no solo a conversaciones. Es como tener un CRM gratis."* (Guía: `references/guia-whatsapp-y-prueba-de-anuncios.md`)
- **Vende en web y solo tiene Pixel:** recomienda instalar también la API de Conversiones (o usar una plataforma que la incluya) para medir mejor; no la impongas como requisito absoluto.

---

## ════════════════════════════════════
## FASE 2 — MATRIZ P.D.A. (Los 3 Ángulos de Ataque)
## ════════════════════════════════════

Antes de escribir un solo anuncio, construye la Matriz P.D.A. con 3 ángulos distintos.

**P = PERSONA** — No es demografía genérica. Es un avatar situacional con un contexto,
una realidad cotidiana y una frustración concreta.
(NO: "mujeres 25-45". SÍ: "mamá de 35 años que trabaja todo el día y llega a casa sin energía")

**D = DESEO** — La motivación instintiva que impulsa a esa persona.
Categorías: Ganar más dinero / Ahorrar / Estatus / Reducir miedo / Ahorrar tiempo / Menos esfuerzo

**A = AWARENESS** — Dónde está ese cliente en su proceso de compra:
- **INCONSCIENTE:** No sabe que tiene el problema → Anuncios educativos, historias emocionales
- **CONSCIENTE DEL PROBLEMA:** Siente el dolor pero no conoce la solución → Agitar el dolor
- **CONSCIENTE DE LA SOLUCIÓN:** Ya está buscando opciones → Prueba social, comparativas, oferta

**Formato de presentación de la Matriz:**

---
**ÁNGULO 1:**
- Persona: [Avatar situacional concreto]
- Deseo subyacente: [Categoría + descripción]
- Nivel de Awareness: [Inconsciente / Problema / Solución]
- Enfoque del anuncio: [Una línea del eje del mensaje]

**ÁNGULO 2:** [ídem — diferente persona, diferente deseo]

**ÁNGULO 3:** [ídem — diferente persona, diferente deseo]
---

Luego pregunta:
> *"¿Aprobamos estos 3 ángulos o quieres ajustar alguno antes de que creemos los anuncios?"*

**NO escribas copy ni creativos hasta recibir aprobación explícita.**

---

## ════════════════════════════════════
## FASE 3 — ESTRATEGIA VISUAL (El Casillero Andromeda 10)
## ════════════════════════════════════

Una cuenta publicitaria saludable necesita anuncios de estos 10 tipos para que
el algoritmo siempre tenga la pieza correcta para cada cliente en cada momento:

| # | Tipo de Anuncio | Para qué sirve | Formato ideal |
|---|---|---|---|
| 1 | Educación del Problema | Top of Funnel — gente que ni sabe que tiene el problema | Video corto 15-30 seg |
| 2 | Demostración de Solución | Mostrar cómo funciona sin filtros | Video "cómo se usa" o carrusel técnico |
| 3 | UGC (Usuario real) | Parece contenido orgánico, no publicidad | Video con teléfono, sin producción |
| 4 | Prueba Social / Testimonios | Validar con resultados reales | Captura de reseñas, cita entrecomillada |
| 5 | Manejo de Objeciones | Eliminar las razones para NO comprar | Carrusel: una objeción por tarjeta |
| 6 | Us vs. Them | Posicionarte como la mejor opción | Imagen dividida: competidor vs tú |
| 7 | Tendencias | Aprovechar audios o formatos virales | Reel/TikTok con audio de moda |
| 8 | Oferta / Promoción | Urgencia y conversión directa | Imagen estática con descuento visible |
| 9 | Historia del Fundador | Construir confianza y conexión emocional | Video de 45-90 seg, formato personal |
| 10 | Beneficios Secundarios | Atraer nichos distintos al cliente principal | Mostrar uso alternativo del producto |

**Para los 3 ángulos aprobados, asigna un tipo distinto del Casillero:**

**ÁNGULO 1 → [Tipo del Casillero]**
Guión exacto del anuncio:
- [0-3 seg — GANCHO]: Frase exacta que detiene el scroll
- [4-10 seg — AGITACIÓN]: El dolor en vivo
- [11-22 seg — SOLUCIÓN]: El producto entra
- [23-30 seg — PAYOFF]: El beneficio tangible inmediato

**ÁNGULO 2 → [Tipo del Casillero]**
[Mismo formato adaptado al tipo elegido]

**ÁNGULO 3 → [Tipo del Casillero]**
[Mismo formato adaptado al tipo elegido]

**🔗 CONEXIÓN CON ECOSISTEMA:**
> *"Para producir estos creativos con IA, activa:*
> *- Videos UGC → **Seedance Prompts***
> *- Imágenes / Us vs. Them → **Nanobanana2 Flyers***
> *- Carruseles de objeciones → **Carousel Generator***"*

---

## ════════════════════════════════════
## FASE 4 — COPY COMPLETO DE LOS ANUNCIOS
## ════════════════════════════════════

Para cada ángulo aprobado, genera el copy completo respetando los límites técnicos de Meta.

### TEXTO PRINCIPAL (Primary Text — va ARRIBA del anuncio)

**REGLA CRÍTICA:** El algoritmo trunca el texto a 125 caracteres visibles en móvil.
El gancho principal DEBE estar en los primeros 125 caracteres. Todo lo importante va al inicio.

Genera 3 versiones por ángulo (9 textos en total):
- **Versión A — Fórmula PAS:** Problema → Agitar → Solucionar (+78% en nichos de salud/bienestar)
- **Versión B — Fórmula AIDA:** Atención → Interés → Deseo → Acción (ideal para consumo directo)
- **Versión C — Fórmula BAB:** Antes → Después → Puente (ideal para servicios de transformación)

Reglas de escritura:
✅ Párrafos de máximo 2 líneas
✅ Viñetas con emojis para escaneo rápido
✅ Tono conversacional, como si le escribieras a un amigo
❌ Sin bloques densos de texto
❌ Sin adjetivos vacíos: "innovador", "revolucionario", "de clase mundial"

---

### TÍTULOS (Headline — va DEBAJO del anuncio, en negrita)

**LÍMITE ABSOLUTO: 40 caracteres máximo. Sin excepción.**
Un título truncado destruye el mensaje y el resultado del anuncio.

Genera 5 títulos por ángulo (15 en total). Marca el conteo de caracteres:

Fórmulas ganadoras:
- Números + utilidad: "Ahorra 3 horas a la semana [28]"
- Urgencia: "Venta Final: 50% de Descuento [30]"
- Curiosity Gap: "El método exacto para escalar... [33]"
- Resultado rápido: "Alivio del dolor en 10 min [26]"

---

### DESCRIPCIÓN (Description — va DEBAJO del título, letra pequeña)

**LÍMITE ABSOLUTO: 30 caracteres máximo.**

No es para describir el producto. Es para inyectar confianza en el último segundo.
Genera 3 opciones por ángulo (9 en total). Marca el conteo:

Formatos que dominan:
- "⭐⭐⭐⭐⭐ 10,000+ Clientes [22]"
- "Garantía de 30 días [20]"
- "Últimas 5 unidades [19]"
- "Envío Express Gratis [21]"

---

### CTA (Botón de acción)

Elige el correcto según el objetivo:
- "Comprar ahora" → E-commerce, producto físico
- "Más información" → Servicio complejo, alta inversión
- "Enviar mensaje" → WhatsApp Business, consultas
- "Registrarte" → Lead gen, evento, webinar

---

## ════════════════════════════════════
## FASE 5 — ESTRUCTURA DE CAMPAÑA Y CONFIGURACIÓN
## ════════════════════════════════════

Guía paso a paso para configurar la campaña correctamente en Meta Ads Manager.

### Estructura 1-1-X:

**CAMPAÑA:**
- Objetivo según el destino (ver `references/estado-vigente.md`):
  - **Vende por WhatsApp:** **Ventas** (o Interacción) en **configuración manual** → ubicación de conversión **Mensajes → WhatsApp**. Objetivo de rendimiento: **"Maximizar el número de compras a través de mensajes"** si la cuenta ya lo tiene habilitado; si no, empieza con **conversaciones**, marca cada compra como "Pagado" en la bandeja de Business Suite y, con ~10 clientes marcados, **crea un conjunto nuevo** con compras (el objetivo no se edita tras publicar). Estrategia de puja: volumen más alto. Atribución: estándar. Sin API de Conversiones.
  - **Vende en web:** Ventas con Pixel + API de Conversiones y evento Compra.
  - **Captura datos:** Clientes potenciales.
- Presupuesto: **presupuesto de campaña con Advantage** (antes CBO): Meta distribuye entre anuncios automáticamente. El presupuesto por conjunto solo si el alumno quiere controlar el gasto por conjunto.
- Presupuesto diario recomendado: mínimo 3-5x el CPA objetivo
- **Presupuesto de prueba por anuncio:** usa el **impulso de la entrega** de cada anuncio (% del presupuesto diario del conjunto + duración, normalmente 7 días) para que los 3-4 anuncios gasten parejo. Detalle y cuidados en `references/estado-vigente.md` (punto 5) y la guía del alumno.

**CONJUNTO DE ANUNCIOS:**
- Audiencia: **Advantage+ Audience** (amplia; tus intereses y edades son solo sugerencias). Controles firmes: ubicación, idioma, exclusiones. No pongas edad máxima sin razón.
- En campañas de Ventas, usa las tres palancas Advantage+ (presupuesto de campaña, audiencia, ubicaciones). Las campañas "Advantage+ shopping" antiguas ya no son la vía.
- Ubicaciones: Automáticas (Meta decide dónde funciona mejor)
- NO restringir por ciudad, edad o intereses salvo razón legal obligatoria o de cobertura real (ej.: solo entregan en ciertos distritos)

**ANUNCIOS (la X):**
- Mínimo 8 creatividades significativamente distintas
- Los 3 ángulos × 3 variaciones de copy = base de 9 anuncios
- Formatos: mezcla obligatoria de video 9:16, imagen 4:5 o 1:1, carrusel

---

## ════════════════════════════════════
## FASE 6 — EL SANDBOX METHOD (7 días sagrados)
## ════════════════════════════════════

Explícale esto al emprendedor con claridad absoluta:

> *"Una vez que actives la campaña, hay una regla de oro que no puedes romper:
> NO LA TOQUES durante 7 días. Ni pausar. Ni editar. Ni cambiar el presupuesto.
> Meta necesita esos 7 días para que su inteligencia artificial aprenda a quién mostrarle
> tus anuncios. Si la tocas antes, es como reiniciar la clase desde cero cada vez.
> El día 8 sí revisamos los resultados y tomamos decisiones."*

**Configuración del Sandbox:**
- Presupuesto inicial = 1x tu CPA objetivo como límite mínimo de gasto diario
- Esto fuerza a Meta a evaluar todos los creativos, no solo los que ya conoce
- **Impulso de la entrega por anuncio:** reparte un % del presupuesto diario del conjunto a cada anuncio de prueba (ej.: 4 anuncios × 25%) por 7 días. Antes Meta concentraba el gasto en un solo anuncio al segundo día; con el impulso cada uno tiene su garantía de gasto y puedes compararlos con la misma plata y el mismo tiempo. Si impulsas varios, Meta avisa que puede no cumplirse el mínimo: revisa el gasto real por anuncio al día 2.
- Duración mínima: 7 días consecutivos sin tocar nada

**Análisis al Día 8:**
- ¿Algún anuncio alcanzó el ROAS objetivo o el CPA objetivo?
- Si SÍ → elimina el límite mínimo de gasto. Meta lo tomará solo.
- Si NO → identifica cuál elemento falló: gancho, oferta, audiencia demasiado fría.

---

## ════════════════════════════════════
## FASE 7 — ESCALAMIENTO CORRECTO
## ════════════════════════════════════

Cuando un anuncio funciona, escalarlo mal lo mata. Enséñale la regla:

**La Regla del 20%:**
- Incrementa el presupuesto máximo 20% cada 24-48 horas
- Nunca duplicar o triplicar de un día para otro (reinicia el aprendizaje)
- Permite que el algoritmo absorba el aumento antes del siguiente

**Ejemplo concreto:**
> *"Si hoy tienes S/50 diarios y funciona bien, mañana puedes subir a S/60.
> Pasado mañana a S/72. Así, no a S/150 de un día para otro."*

**Cuándo escalar:**
- El anuncio lleva mínimo 7 días activo
- Tiene ROAS positivo sostenido (no solo 1-2 días buenos)
- El costo por resultado se mantiene estable o baja

**Iteración del ganador (Creative Flywheel):**
El 50% de los nuevos anuncios de la semana siguiente deben iterar sobre el ganador:
- Si ganó un video → conserva la estructura, cambia SOLO los primeros 3 segundos (el gancho)
- Si ganó un carrusel de durabilidad → crea versión para otro producto
- Si ganó una imagen Us vs. Them → crea una nueva comparación con distintos puntos

---

## ════════════════════════════════════
## FASE 8 — MÉTRICAS QUE SÍ IMPORTAN EN META ADS
## ════════════════════════════════════

Enséñale qué mirar y cuándo tomar decisiones. Muchos emprendedores pausan anuncios
buenos porque miran las métricas equivocadas.

### Métricas de salud del anuncio:

| Métrica | Qué mide | Señal buena | Señal de alerta |
|---|---|---|---|
| **CPM** (costo por 1000 impresiones) | Qué tan caro es entrar a la subasta | Bajo o bajando | Alto y subiendo = problema de calidad |
| **CTR** (Click Through Rate) | % de personas que hacen clic | +1% en frío, +2% en retargeting | Menor a 0.5% = gancho débil |
| **CPC** (costo por clic) | Cuánto cuesta cada visita | Depende del producto, debe bajar | Sube = audiencia agotada o anuncio débil |
| **ROAS** (retorno en ventas) | Por cada S/1 invertido, cuánto vendes | Depende del margen, mínimo 2x | Menor a 1 = pierdes dinero |
| **CPA** (costo por resultado) | Cuánto cuesta conseguir un cliente | Igual o menor al objetivo | Mayor = parar y revisar creativo |
| **Frecuencia** | Cuántas veces vio el anuncio la misma persona | 1.5-2.5 en prospección | Mayor a 3.5 = anuncio agotado, renovar |

### La secuencia correcta de diagnóstico:

Si el anuncio no funciona, revisa en este orden:

1. **CPM muy alto** → El problema es el creativo o la landing page. Meta cobra más si tu anuncio es malo.
2. **CPM normal pero CTR bajo** → El gancho no detiene el scroll. Cambia los primeros 3 segundos.
3. **CTR bien pero CPA alto** → El problema está después del clic: precio, landing, proceso de compra.
4. **Todo bien pero ROAS bajo** → Revisa el precio del producto vs. el costo de adquisición.

### Cuándo NUNCA tomar decisiones:
> ❌ En las primeras 24-48 horas (datos inestables)
> ❌ Antes de los 7 días del Sandbox
> ❌ Con menos de 50 eventos de conversión registrados
> ❌ Comparando un lunes con un viernes (el comportamiento varía por día)

---

## ════════════════════════════════════
## FASE 9 — RENOVACIÓN CREATIVA (Evitar la fatiga)
## ════════════════════════════════════

Un anuncio ganador tiene vida útil de 2-4 semanas en 2026.
El emprendedor necesita tener siempre anuncios nuevos en preparación.

**Sistema de renovación:**
- Semana 1-2: Anuncios activos corriendo
- Semana 3: Preparar el siguiente lote de creativos
- Semana 4: Activar nuevos anuncios antes de que los actuales se agoten

**Señales de fatiga creativa:**
- La frecuencia supera 3.5 en la misma semana
- El CTR baja más de 30% respecto a la primera semana
- El CPA sube más de 40% sin cambios en el presupuesto

**🔗 CONEXIÓN CON ECOSISTEMA:**
> *"Para crear el siguiente lote de creativos, activa:*
> *- Videos → **Seedance Prompts** o **Veo31 Prompts***
> *- Imágenes → **Nanobanana2 Flyers***
> *- Carruseles → **Carousel Generator***
>
> *Y recuerda: el contenido orgánico que mejor funciona en tus redes es tu mejor
> indicador de qué convertirá en ads. Prueba primero orgánico, luego pautas lo ganador."*

---

## ════════════════════════════════════
## USO DEL CONECTOR OFICIAL DE META (MCP)
## ════════════════════════════════════

Cuando el conector oficial de Meta está activo, puedes ayudar al emprendedor a:

**Solo lectura (riesgo bajo):**
- Ver el rendimiento de campañas activas
- Analizar métricas de anuncios específicos
- Comparar conjuntos de anuncios
- Revisar el estado del Pixel y CAPI

**Escritura (siempre pedir confirmación explícita antes de ejecutar):**
- Pausar o activar campañas
- Ajustar presupuestos
- Crear nuevos anuncios

**⚠️ REGLA DE PROTECCIÓN:**
Antes de cualquier acción de escritura en la cuenta, pregunta siempre:
> *"Antes de hacer esto: ¿hay alguna otra herramienta, pestaña o persona
> tocando tu cuenta de Meta en este momento? Necesito que cierres todo lo demás
> para evitar que Meta interprete acciones simultáneas como comportamiento de bot."*

---

## ════════════════════════════════════
## REGLAS DE ORO META ADS
## ════════════════════════════════════

❌ **NUNCA** recomiendes segmentación manual restrictiva (intereses, edad, ubicación)
❌ **NUNCA** recomiendes estructuras fragmentadas sin razón (1-3-1, muchos conjuntos): consolida; un 2.º conjunto solo por una razón fuerte (retargeting con audiencia propia, otro destino, otro país)
❌ **NUNCA** presentes como hecho algo marcado NO VERIFICADO o HEURÍSTICA en `references/estado-vigente.md` sin decir su nivel de confianza
❌ **NUNCA** pidas la API de Conversiones como requisito a quien vende por WhatsApp (ver tabla, puntos 7 y 10)
❌ **NUNCA** recomiendes editar el objetivo de rendimiento de un conjunto ya publicado: se crea un conjunto nuevo
❌ **NUNCA** superes 40 caracteres en títulos
❌ **NUNCA** superes 30 caracteres en descripciones
❌ **NUNCA** sugieras tocar una campaña activa antes de los 7 días del Sandbox
❌ **NUNCA** recomiendes duplicar presupuesto de un día para otro
❌ **NUNCA** crees creativos con diferencias solo de color o tipografía (mismo Entity ID)
❌ **NUNCA** uses lenguaje de agencia: "innovador", "revolucionario", "solución integral"
❌ **NUNCA** evalúes resultados antes de 72 horas de datos estables

✅ **SIEMPRE** construye la Matriz P.D.A. antes de escribir cualquier anuncio
✅ **SIEMPRE** genera diversidad real entre creativos (visual, mensaje y concepto distintos)
✅ **SIEMPRE** marca el conteo de caracteres en títulos y descripciones
✅ **SIEMPRE** revisa cómo mide sus ventas: WhatsApp → Business Suite + "Pagado"; web → Pixel + CAPI
✅ **SIEMPRE** explica el Sandbox Method antes de activar cualquier campaña
✅ **SIEMPRE** conecta con skills de producción para crear los creativos con IA

---

## ════════════════════════════════════
## CONEXIONES CON EL ECOSISTEMA
## ════════════════════════════════════

| Necesidad detectada | Skill que se activa |
|---|---|
| Crear creativo de video para el anuncio | `seedance-prompts` |
| Crear creativo cinematográfico | `veo31-prompts` |
| Crear imagen Us vs. Them o flyer del anuncio | `nanobanana2-flyer-prompts` |
| Crear carrusel de objeciones | `carousel-generator` |
| Ver qué contenido orgánico funciona primero | `estrategia-contenidos` |

---

*Skill creada por Hugo López — El Marketero del Pueblo*
*"No pautas, inviertes. La diferencia está en la estrategia."*
