---
name: fm-adn
description: ADN de marca del emprendedor: identidad gráfica (logo, paleta de colores con códigos HEX medidos del logo, tipografías, estilo visual, referencias), voz y tono, claims permitidos y prohibidos, inventario de fotos de referencia, avatar y reglas de video/imagen. Guarda Mi negocio/adn-de-marca.md, que leen TODAS las demás skills y agentes para que cada pieza salga con la marca del alumno. Úsala al empezar, cuando el alumno suba su logo, fotos o referencias, o cuando una pieza "no se ve como mi marca".
---

# ADN de marca (fm-adn)

Es la única fuente de verdad visual y de voz del negocio. Si el alumno ya tiene `Mi negocio/adn-de-marca.md`, léelo y pregunta solo qué cambió. **Nunca** uses la paleta, tipografía o tono de otra marca (ni de Hugo) como valor por defecto.

## Paso 1 · Reúne materiales (pídelos de forma simple)
Pide que copie a `Mi negocio/` (o los **arrastre al panel**, pestaña Guía de generación): **logo** (PNG con fondo transparente si tiene), **5-10 fotos reales** del producto/servicio/equipo, y **3 referencias visuales** (cuentas, anuncios o marcas que le gustan; pueden ser capturas).
**Fotos reales del lugar (clave para que el video no se vea falso):** 3 a 6 fotos del local o espacio de trabajo tomadas con el celular, **en vertical y con la luz normal del lugar, sin filtros**: frente/entrada, interior general, zona de venta o mostrador, producto en su exhibidor. Mensaje listo: *"Para que el video se vea real, pásame 3 a 6 fotos de tu local con el celular, en vertical y con la luz normal del lugar. No las arregles ni les pongas filtros: yo las uso de referencia y las mejoro."* Mira cada foto y dile qué sirve y qué falta.
Si no tiene nada, trabajas con entrevista y propones una dirección, marcándola `PROPUESTA` (para escenas: describe un negocio común de ese tipo y lugar, estilo cotidiano, **nunca un set de catálogo o atelier de lujo**).

## Paso 2 · Entrevista (de a 2 preguntas)
1. Cómo describiría su marca en 3 palabras y qué NO quiere parecer.
2. Cómo le habla a su cliente (tú/usted, cercano/profesional, humor, fe, etc.) y 5 palabras que usa y 5 que evita.
3. Qué emoción debe sentir quien vea sus piezas.
4. Qué promesas puede hacer y cuáles **no** (claims). Pregunta por restricciones de su rubro (salud, estética, finanzas, niños, etc.).
5. Cierre estándar de sus piezas: llamada a la acción, enlace/WhatsApp, zona o distritos de cobertura que **deben aparecer siempre**.
6. Si habrá persona en cámara o avatar (Omni Flash con `@me`): quién, tono de voz, ropa/ambiente.

## Paso 3 · Mide la paleta del archivo (no a ojo)
Con el logo: extrae los colores reales. Si hay Python con Pillow, ejecuta `scripts/extraer_paleta.py <logo>`; si no, **mira la imagen** y propón HEX marcándolos `ESTIMADO`. Para cada color define su uso (fondo, acento, texto) y **verifica contraste**: texto sobre fondo claro y sobre fondo de acento deben ser legibles (si no, define un tono más oscuro para texto, como hicimos en marcas reales con un coral oscuro para escribir sobre crema). Ofrece 1 variante clara y 1 oscura.

## Paso 4 · Tipografías
Elige 2 (títulos y texto) de https://fonts.google.com, gratuitas y con tildes y ñ. Respeta las del logo si existen. Evita más de 2 familias.

## Paso 5 · Inventario de referencias (clave para generar con IA)
Numera cada foto del alumno con un ID corto y qué muestra: `REF-01 · cuchareable de pistacho, vista frontal`, `REF-05 · interior del local, mostrador a la izquierda`. Las fotos del lugar se usarán como **escena exacta** (la IA las mejora y reencuadra a 9:16, no las reinventa). Los agentes usarán estos IDs para decir **exactamente qué referencia cargar y en qué orden** en cada imagen o clip. Describe proporciones solo con la referencia visual, nunca en centímetros.

## Paso 6 · Reglas de producción (rellénalas con el alumno)
- Formatos: video 9:16 siempre; imagen 4:5 (feed) y 9:16 (historias); carrusel 4:5.
- Zona segura de Reels/Stories: texto entre ~15% y ~65% de la altura (evita lo que tapan los botones).
- Subtítulos: palabra clave resaltada con el color de acento.
- En clips generados con IA: **sin texto ni música de la IA** (se ponen después), sonido ambiente solo.
- Qué se ve y qué no (por ejemplo: sin armas ni cuchillos en cuadro; sin antes/después de cuerpos si es salud).
- Idioma/acento: español de su zona.

## Paso 7 · Redacta `Mi negocio/adn-de-marca.md`
Usa `references/plantilla-adn.md`. Muéstrale un resumen visual (paleta con HEX, tipografías, 3 adjetivos, ejemplos de frase "sí" y "no") y pregunta **"¿Esto se siente como tu marca?"**. Guarda solo con su aprobación. Informa al director y al panel (etapa 2 lista).

## Adaptación por tipo de negocio (aprendida con clientes)
| Tipo | Ajusta |
|---|---|
| Público espiritual o de fe | Tonos cálidos (crema, dorado), subtítulos en minúscula grande, música suave, cero efectos agresivos, versículos solo si los aporta el alumno |
| Alimentos "saludables" | Claims **cualitativos** (sin cifras de salud ni "sin X" como promesa médica), decir ingredientes como ingrediente, no acusar a otros, confirmar con nutricionista antes de publicar |
| Moda y ropa infantil | Fotos reales del producto, detalles de tela y tallas, precio visible y ejecución cuidada (nada de "plantilla plana"), no duplicar el botón nativo de WhatsApp en la imagen |
| Servicios locales / inmuebles | Zona y contacto siempre visibles, prueba social real, oferta clara |
| Infoproductos / mentorías | Prueba real y límites claros: sin testimonios ni cifras inventadas; datos del producto `POR CONFIRMAR` hasta tenerlos |

## Reglas
- Todo HEX, fuente y claim debe venir del alumno o del archivo. Lo estimado se etiqueta.
- Mejora continua: cuando el alumno corrija ("no me gusta este amarillo"), actualiza `adn-de-marca.md` y `aprendizajes.md`.
- Para video, pasa los colores/tipografías a `fv-marca` (módulo Video) para que arme `estilo.json` sin volver a preguntar.
