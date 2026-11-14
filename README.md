# ⚡ Fábrica de Marketing con IA

**Tu agencia de marketing completa, dentro de tu computadora.**
Escribes *"Quiero empezar"* y un equipo de agentes de IA trabaja **en paralelo** mientras tú los ves en un **panel en vivo**: estrategia, ofertas, flyers, carruseles, video y anuncios de Meta, todo con **tu marca**.

Creada por **Hugo López — El Marketero del Pueblo** para emprendedores que no son técnicos.

---

## Qué obtienes

Al terminar recibes una **Campaña lista**: una carpeta con todo para publicar y pautar, más una guía de pasos con enlaces.

| Agente | Qué te entrega |
|---|---|
| 🧭 Estratega | Plan de 90 días, pilares y calendario de 4 semanas |
| ✍️ Oferta y copy | Tu oferta, respuestas a objeciones y el guion de venta por WhatsApp |
| 🖼️ Imágenes y flyers | Prompts listos para Nano Banana 2, con las referencias exactas por pieza |
| 🎠 Carruseles | Prompt de cada slide + texto de publicación |
| 🎬 Video | Guiones de 20-30 s y prompts de Omni Flash con tu avatar |
| 📣 Anuncios Meta | Campaña vigente (Andromeda, Advantage+, **compras por WhatsApp**), copy y plan de pruebas |
| 🛡️ Revisor | Revisa marca, claims, políticas de Meta y datos inventados antes de entregar |

Antes de producir, el **director** hace tu **diagnóstico de negocio** (objetivos, números, semáforo de preparación) y tu **ADN de marca** (logo, colores medidos del archivo, tipografías, tono, claims, referencias). Todo lo que sale lleva tu identidad, nunca la de otro.

## Novedades de la versión 1.1.0
- **Panel con oficina 3D** y una nueva pestaña **Guía de generación**: aquí ves tus prompts listos para copiar, qué referencias cargar y en qué orden, y **arrastras tus imágenes y clips** para que se guarden solos en tu computadora. Claude los revisa en tiempo real y te dice si pasan o qué repetir. (Abre el panel con doble clic en `Panel/iniciar-panel.bat`.)
- **Video con varias tomas:** un video de 20 s son 5-6 tomas distintas (no un plano fijo) y la continuidad se arma en la edición con las mismas referencias de escena, sin usar el último fotograma del clip anterior.
- **Más realista:** se parte de **fotos reales** de tu local o producto (la IA las mejora y reencuadra a 9:16 con Nano Banana 2 o GPT Image 2.6) y se evita el "set de película".
- El **revisor** ahora también exige dinamismo, continuidad por escena, realismo y que nada quede "al aire" fuera de la guía.

## Niveles (instala lo que necesites)

| Nivel | Incluye | Para quién |
|---|---|---|
| **Base** | Director, diagnóstico, ADN de marca, oferta y copy, panel, contenidos, imágenes, flyers y carruseles | Todos |
| **Anuncios** | Meta Ads con información vigente (verificada y fechada) | Quienes tienen presupuesto |
| **Video** | Omni Flash, Seedance, Veo y la **Fábrica de Video** (edición profesional con tu voz real) | Quienes quieren el nivel Pro |

## Instalación

### Opción 0 · Un solo enlace (la más fácil)
Abre **Claude Code** en una carpeta vacía y pega el **Prompt 0** de `PROMPT-DE-INSTALACION.md` (o simplemente: *«Instala la Fábrica de Marketing con IA desde https://github.com/pruebacursoads/fabrica-de-marketing-ia»*). Claude te pide permiso, descarga el paquete oficial desde GitHub, lo instala y lo verifica. No necesitas que nadie te pase un ZIP.

### Opción A · Sin terminal (recomendada)
1. Descarga este repositorio como ZIP (botón verde **Code → Download ZIP**) y descomprímelo en el Escritorio.
2. Abre **Claude Code** (o Codex / Antigravity) **dentro de la carpeta descomprimida**.
3. Abre `PROMPT-DE-INSTALACION.md`, copia el **Prompt 1** y pégalo. Tu asistente revisa tu equipo, te pregunta qué niveles quieres, instala y verifica.
4. Cierra y vuelve a abrir el programa. Crea una carpeta **Mi Fábrica de Marketing** en Documentos, ábrelo dentro y escribe: **Quiero empezar**.

### Opción B · Un clic
- **Windows:** clic derecho en `instalar.ps1` → *Ejecutar con PowerShell*. Para elegir niveles: `powershell -ExecutionPolicy Bypass -File instalar.ps1 -Modulos base,anuncios`
- **Mac / Linux:** `bash instalar.sh` (o `bash instalar.sh --modulos base,anuncios`)

El instalador copia las skills a `~/.claude/skills` y los agentes a `~/.claude/agents`, y **respalda** lo que ya tuvieras.

## Verlo funcionar antes de empezar
Abre `modulos/base/skills/fm-panel/panel/index.html` en tu navegador y pulsa **▶ Ver demo**: verás una **oficina animada** con tu equipo (cada personaje con su nombre y rol): se reúnen en la sala de reuniones para el plan, trabajan en su estudio, se pasan material entre ellos, entregan al director, la revisora recorre los escritorios y al final celebran la campaña lista. También muestra la actividad en vivo y los entregables.

## Cómo se usa
1. **Quiero empezar** → el director te entrevista (diagnóstico + marca) con preguntas sencillas.
2. Te muestra un **plan en tabla**: qué hará cada agente y qué tendrás que generar tú a mano. Dices **"vamos"**.
3. Se abre tu **panel en vivo** y los agentes trabajan en paralelo.
4. El **revisor** controla todo. Recibes `00-LEEME-PRIMERO.md` con los pasos y **cada enlace** que necesitas.

## Qué NO hace (para que no te lleves sorpresas)
- Las **imágenes y los clips los generas tú** en Gemini/Nano Banana y Google Flow: los agentes te dan los prompts y las referencias exactas. No usa APIs de pago.
- **No toca tu cuenta de Meta** sin tu confirmación en cada acción; por defecto entrega el plan y el copy.
- No promete resultados de ventas.
- Los agentes en paralelo gastan más cuota de tu plan de Claude: el director lanza 3-4 a la vez.
- Probado en Windows. Mac/Linux: scripts incluidos, sin probar en equipo limpio. El nivel Video necesita ffmpeg, Node, Python y Whisper (se instalan con tu permiso).

## Requisitos
Un plan de **Claude** (o una herramienta compatible con skills y agentes). Todo lo demás es gratis.

## Actualizaciones
**Automáticas:** cada mejora se publica en este repositorio y el director (skill `fm-actualizar`) avisa al empezar cuando hay una versión nueva; si dices que sí, la descarga de aquí y la instala (respaldando lo anterior y actualizando tu Panel). También puedes pedir: *«actualiza la fábrica»*.

Meta cambia sus reglas seguido. La skill de anuncios trae `references/estado-vigente.md` con **qué está confirmado, qué es de fuentes secundarias y qué no está verificado**, con fecha. Si pasan 45 días, avisa y vuelve a verificar. Para actualizar el paquete: descarga la versión nueva y vuelve a ejecutar el instalador (respalda lo anterior).

## Más
- `docs/GUIA-DE-CLASE.md` — guion para presentarlo en clase.
- `docs/POR-DENTRO.md` — arquitectura, protocolo del panel y mantenimiento.
- `AVISOS-DE-LICENCIAS.md` — licencias y créditos.
- Versión: ver `VERSION`.
