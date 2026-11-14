# Video con avatar: varias tomas, continuidad por escena y realismo (v1.1)

Aprendido en producciones reales de Hugo (Bloguera FIT, Marita) y corregido tras la prueba de "ternos" (nov 2026), donde un solo plano fijo de 10 s, un local que parecía un atelier de película y el uso del último fotograma del clip anterior dieron un resultado que **se nota falso y pierde retención**. Esta guía manda sobre cualquier otra regla de video del paquete.

## 1. Un video = una secuencia de tomas distintas (nunca un plano fijo)
El ojo detecta cuando mira el mismo encuadre mucho rato; con avatar se nota todavía más. La retención se gana cambiando de toma.

- **Video de 20 s = 5 o 6 tomas** (3–5 s cada una; máximo 8 s). Clips de Flow de **4, 6 u 8 s** (gratis: 3–10 s).
- **Un clip de 10 s solo si el prompt trae cambios de cámara dentro** (al menos 3: `[0-3 s] … [3-6 s] … [6-10 s] …`, cada uno con encuadre o ángulo distinto) y nunca "cámara fija" ni "una sola toma continua" con avatar hablando.
- **Cada toma cambia el encuadre respecto a la anterior.** Banco de tomas: plano general del lugar · plano medio · primer plano del avatar · **plano detalle del producto** (manos, tela, textura, envase) · contrapicado (cámara baja) · picado · plano lateral o 3/4 · por encima del hombro · seguimiento (camina con la cámara) · POV (la mano que muestra el producto a cámara) · **inserto sin avatar** (solo producto o ambiente).
- **Al menos 2 tomas sin avatar** (producto, local, detalle): son más baratas, casi nunca fallan y rompen el ritmo.
- **El avatar no repite encuadre dos veces seguidas** y no pasa de 5 s en pantalla sin un corte o un cambio de ángulo.
- **El habla se reparte entre tomas** (frases cortas, 10 s ≈ 22–24 palabras; 4 s ≈ 8–9; 6 s ≈ 13–15; 8 s ≈ 19). El audio del avatar se genera en cada toma con avatar; en las tomas sin avatar hay solo sonido ambiente y la voz continúa desde la edición (puede traslaparse con un corte tipo J/L).
- **Costo honesto:** más tomas = más generaciones para el alumno. Dilo en la propuesta ("6 tomas: 4 con avatar y 2 de detalle, ~6-9 generaciones con repeticiones").

Ficha por toma (así se entrega al alumno): n.º · duración · tipo de plano y movimiento · acción · ¿avatar? · frase que dice · referencias **en orden**.

## 2. Continuidad por ESCENA, no por último fotograma
Cada toma se genera **con las mismas referencias de escena** y la continuidad se arma en la edición con cortes, mismo fondo, mismo color y sonido ambiente continuo. **No se carga el último fotograma del clip anterior** (así se trabajó Bloguera FIT con resultado espectacular).

Referencias, siempre en este orden (se nombran por su contenido, no por "la primera/segunda"):
1. `@me` (el avatar; no se sube foto).
2. **La escena**: imagen del lugar (de una foto real del alumno, ver §3) — la misma en todas las tomas de ese lugar.
3. **Los elementos**: imagen del producto o de la percha/mostrador con lo que se muestra (si la toma lo muestra).
4. **La ropa del avatar**: imagen de la ropa sola sobre fondo blanco (maniquí fantasma, sin persona ni cabeza ni manos). Prompt tipo: *"Copia exactamente la ropa que lleva la persona de la imagen de referencia. Foto de producto 9:16, vista frontal, fondo blanco puro, luz suave de estudio. Solo la ropa, sin persona, centrada. Sin logos ni letras."*

Lo que cambia entre tomas es **el encuadre y la acción** (en el prompt), no las referencias. Excepción: si el alumno quiere una acción continua real (por ejemplo, abrir una puerta y entrar), se usa Omni Extend o un solo clip largo, y se avisa del riesgo.

## 3. Realismo: que el cliente reconozca el lugar
Un local inventado "de revista" se ve falso y rompe la confianza (en la prueba de ternos pedimos un taller en el Centro de Lima y salió un atelier cinematográfico que no existe ahí).

1. **Pide fotos reales** al alumno desde el ADN (etapa 2): 3 a 6 fotos con el celular, **en vertical**, luz normal del lugar (sin filtros): frente/entrada, interior general, mostrador o zona de venta, producto en su exhibidor, y cómo se ve por dentro de un probador o estante si aplica.
   Mensaje listo: *"Para que el video se vea real, pásame 3 a 6 fotos de tu local tomadas con el celular, en vertical y con la luz normal del lugar. No las arregles ni les pongas filtros: yo las uso de referencia y las mejoro."*
2. **La IA mejora y reencuadra la foto, no la reinventa.** Imagen de escena con **Nano Banana 2** (https://aistudio.google.com o https://gemini.google.com) **o GPT Image 2.6** (el que usó Hugo para la cocina de Bloguera FIT; el alumno elige el que tenga). Prompt base:
   *"Usa la imagen adjunta como escena exacta: el mismo local, los mismos muros, mostrador, estantes y productos. Mejora la nitidez y la luz natural y reencuádrala en vertical 9:16, sin personas. No embellezcas ni agregues muebles, cuadros, plantas ni luces que no estén en la foto. Sin texto legible, sin logos, sin tijeras ni objetos filosos."*
3. **Si todavía no hay foto real**, marca la escena como `PROPUESTA` y descríbela **como es un negocio común de ese tipo y lugar**, no como un set: *"foto tomada con celular, luz fría de tubos LED de tienda, piso de cerámica, mostrador con vitrina, perchero metálico, espejo de cuerpo entero, cajas y bolsas visibles, paredes lisas, nada decorativo ni cinematográfico"*. Evita palabras como atelier, boutique de lujo, cálido cinematográfico, taller artesanal. Para un local en galería comercial: vitrina de vidrio, cartel genérico sin texto legible, pasillo de la galería al fondo.
   Nunca nombres marcas, galerías ni calles reales sin que el alumno lo confirme.
4. **Prueba del realismo antes de generar clips** (el revisor la aplica): "¿un cliente que conoce el local diría 'sí, es ese'?" Si no, se pide otra foto o se corrige el prompt. No se pasa a los clips con una escena que parezca de catálogo.
5. En los prompts de **clip**, la escena se refiere a la imagen ("el lugar de la imagen del local"), sin volver a describirla (describirla de nuevo la reinventa).

## 4. Prompts de tomas con avatar (ligeros, pero con la cámara dirigida)
Una instrucción de cámara por tramo y el avatar con `@me`. Ejemplo de 8 s con cambios:
*"@me en el local de la imagen del local, viste exactamente la ropa de la imagen de la ropa. [0-3 s] cámara en mano, plano medio, @me camina hacia la cámara y dice el gancho. [3-6 s] corte a primer plano en contrapicado, señala hacia el perchero. [6-8 s] la cámara gira a un plano lateral y @me toma una prenda. El avatar dice: "…". Con su propia voz, español latino. Sin texto ni música; solo sonido ambiente del local."*
Reglas que siguen vigentes: prompts en español; sin texto ni música generados; sin cuchillos/tijeras/objetos filosos en cuadro (dilo en positivo: "solo cinta métrica e hilo"); no pedir "selfie" si el avatar usa las dos manos; ubicación del negocio en el video (en voz o en pantalla).

## 5. Edición para retención (lo hace `fv-editor`)
Corte cada 1,5–3 s, punch-in de 105–115 % al cortar, tomas sin avatar intercaladas, texto animado para datos, sonido ambiente continuo y música baja que une los cortes, cierre con ubicación y llamada a la acción. Recorta 0,3–0,5 s al inicio de cada clip generado y tapa o recorta cualquier etiqueta con letras que la IA invente en las prendas.

## 6. Checklist del revisor (video)
- [ ] ¿Hay 5–6 tomas (o clips de 10 s con ≥3 cambios de cámara dentro)? ¿Ninguna toma repite el encuadre anterior?
- [ ] ¿Hay ≥2 tomas sin avatar y plano detalle del producto?
- [ ] ¿Ninguna toma carga el último fotograma del clip anterior?
- [ ] ¿La escena sale de una foto real del alumno, o está marcada `PROPUESTA` con estilo cotidiano (no de set)?
- [ ] ¿Las referencias van por contenido y en orden, y cada toma dice cuáles cargar?
- [ ] ¿Todo está publicado en la Guía del Panel (prompt, referencias, dónde subir)?
