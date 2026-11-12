---
name: fv-marca
description: Entrevista de marca para el emprendedor. Define de forma conversada su logo, colores, tipografía, tono, nombre en pantalla, cierre (CTA) y estilo de subtítulos, pide referencias de ediciones que le gusten (videos o capturas) y las analiza, y guarda todo en estilo.json. Úsala la primera vez que alguien usa la Fábrica de Video, cuando quiera cambiar su estilo, o cuando diga "quiero que se vea como…".
---

> ## 🔗 Integración con la Fábrica de Marketing con IA
> Si existen `Mi negocio/adn-de-marca.md` y `Mi negocio/diagnostico-situacional.md` en la carpeta de trabajo, **léelos primero** y úsalos como contexto: **no repitas preguntas** que ya responden (marca, colores, tono, claims, objetivos). Nunca uses la identidad de otra marca. Si te lanzó un agente `fm-agente-*` o el director `fm-director`, **no hagas preguntas al alumno**: usa el brief y el ADN, anota supuestos y entrega en la carpeta indicada. Cuando corresponda, reporta avance con la skill `fm-panel`.
> **Dentro del paquete:** si existe `Mi negocio/adn-de-marca.md`, **toma de ahí logo, colores, tipografías y claims** para armar `Mi estilo/estilo.json` y pregunta solo lo específico de video (subtítulos, música, cierre). No vuelvas a hacer la entrevista de marca.

# Marca del emprendedor

`<SKILLS>` = `%USERPROFILE%\.claude\skills` (Windows) o `~/.claude/skills` (Mac/Linux). El resultado es `Mi estilo/estilo.json`, que lee el motor de edición.

## Cómo conversar
Usa preguntas con opciones (máximo 4 por tanda, tu recomendación primero). No preguntes lo que ya sabes. Habla simple: nada de "tokens" ni "paleta cromática".

**Tanda 1 · Quién es**
1. ¿Cómo se llama tu marca o tu nombre en pantalla? ¿Tu usuario de redes?
2. ¿A quién le hablas y qué vendes o enseñas? (sirve para el tono)
3. ¿Cómo hablas? cercano · directo · elegante · divertido
4. ¿Tienes logo? (pásalo como PNG con fondo transparente) · no tengo (se usará tu nombre escrito)

**Tanda 2 · Cómo se ve**
5. **Referencias**: "Pásame 2 o 3 videos o capturas de cuentas que te gusten cómo se ven." Pídelos como archivos en `Mi estilo/referencias/`. No intentes descargar videos de redes: pide archivos o capturas.
6. Estilo de partida (muéstralos con una frase cada uno): `oscuro-pro` (fondo oscuro, moderno) · `calido` (tonos cálidos, redondeado) · `minimal-claro` (limpio, fondo claro) · `metodo-el-marketero` (amarillo y violeta, mayúsculas).
7. Colores: ¿tienes colores de marca? (códigos o "el naranja de mi logo"). Si no, propón desde las referencias.
8. Tipografía: ofrece 2-3 de la lista según el tono (Montserrat, Poppins, Inter, Outfit, Nunito, Playfair Display, Oswald, League Gothic, Archivo Black, EB Garamond, Lato, Roboto, Open Sans). **Solo esas**: vienen incluidas; una fuente de afuera exige agregar su archivo.

**Tanda 3 · Cómo cierra**
9. Llamado a la acción al final (ej. "ESCRÍBEME", "ÚNETE EN MI PERFIL") y una línea de apoyo.
10. Música: calma · energía · ninguna · tengo la mía. (En videos serios o con mucha voz, "ninguna" o "calma" bajita.)
11. ¿Subtítulos grandes de impacto o más discretos? ¿en mayúsculas?

## Analizar las referencias
```bash
python "<SKILLS>/fv-marca/scripts/analizar_referencias.py" "Mi estilo/referencias/ref1.png" "Mi estilo/referencias/ref2.mp4" --salida "Mi estilo/referencias.json"
```
Da la paleta dominante, una sugerencia (fondo, acento, texto) y los cortes por minuto de cada video. **Además, MIRA tú las imágenes o fotogramas** (extráelos con ffmpeg si son videos) y describe lo que no se mide: tipo de letra, dónde van los subtítulos, qué gráficos usan, ritmo. Resume al alumno en 3 líneas: "veo que te gusta X, Y, Z".

## Crear el archivo de estilo
```bash
python "<SKILLS>/fv-marca/scripts/crear_estilo.py" --preset oscuro-pro --nombre "Mi Marca" --handle @mimarca --fuente Poppins --acento "#FF8800" --secundario "#8B5CFF" --fondo "#07080F" --cta "ESCRÍBEME" --cta-sub "Link en mi perfil" --mood calma --logo "Mi estilo/logo.png" --salida "Mi estilo"
```
- `--listar` muestra estilos base y fuentes disponibles.
- Avisa si el **contraste** es débil (texto/acento sobre fondo) o si la fuente no está incluida. Corrige con el alumno, no en silencio.
- Genera también `Reglas-de-estilo.md` legible. Muéstraselo y pide su visto bueno.

## Reglas de diseño que siempre aplican (explícalas si preguntan)
Ningún texto menor de 28 px · un gráfico por idea · un hueco, un gráfico a la vez · nada tapa la cara · nada importante bajo y=1540 (botones de la red) · máximo 1 palabra clave de color por frase.

## Aprender con el tiempo
Cada vez que el alumno diga qué le gusta o qué no ("mis textos nunca arriba", "quiero más zoom"), agrégalo a `Reglas-de-estilo.md` y, si afecta a números (tamaño, posición), a `estilo.json`.

## Qué NO hacer
- No inventes un logo ni uses logos de terceros. Si no tiene, el nombre escrito en su tipografía es su marca.
- No copies el estilo de otra persona al pie de la letra; usa las referencias para inspirarte.
