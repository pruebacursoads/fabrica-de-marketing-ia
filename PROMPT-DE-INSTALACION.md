# Prompt de instalación (sin terminal)

No necesitas saber de programación ni de comandos. Descomprime el ZIP, abre **Claude Code** (o Codex o Antigravity) **dentro de la carpeta descomprimida** `fabrica-de-marketing-ia`, pega este texto y deja que la herramienta haga todo.

## Prompt 1: instalar

```
Eres mi asistente de instalación de la Fábrica de Marketing con IA. Yo no sé de programación ni de terminal: explícame todo en palabras simples y no me pidas escribir comandos, ejecútalos tú.

1. Esta carpeta es el paquete descomprimido (tiene README.md, instalar.ps1, instalar.sh, una carpeta modulos y una carpeta agentes). Léela.
2. Pregúntame qué niveles quiero instalar, explicando cada uno en una frase: BASE (director, diagnóstico, marca, oferta, panel, contenidos, imágenes, flyers y carruseles), ANUNCIOS (Meta Ads con información vigente) y VIDEO (Omni Flash y la Fábrica de Video, edición profesional). Recomiéndame según lo que te cuente de mi negocio.
3. Instala los niveles elegidos con el instalador de esta carpeta: en Windows instalar.ps1 con -Modulos, en Mac o Linux instalar.sh con --modulos. Si por algún motivo no puedes ejecutarlo, copia las carpetas de modulos/<nivel>/skills a la carpeta de skills de mi usuario (en Claude Code: .claude/skills) y los archivos de agentes/ a .claude/agents. Si ya existe algo con el mismo nombre, el instalador hace respaldo; confírmamelo.
4. Si elegí el nivel VIDEO: audita mi computadora (sistema, RAM, disco, internet) y revisa si tengo ffmpeg, Node.js 20 o superior, Python 3.10 o superior, Whisper y Google Chrome o Edge. Muéstrame una tabla con qué tengo, qué falta y para qué sirve cada cosa. Pídeme permiso e instala SOLO lo que falte con instaladores oficiales (winget, brew, pip), un comando a la vez, diciéndome cuál ejecutas. No uses contraseñas ni descargues de sitios desconocidos.
5. Verifica: que aparezcan las skills fm-director, fm-adn, fm-diagnostico, fm-oferta-copy y fm-panel, los 7 agentes fm-agente-*, y que el archivo del panel exista (skills/fm-panel/panel/index.html). Abre ese panel en mi navegador en modo demo (index.html?demo=1) para que yo vea al equipo trabajando.
6. Termina con un resumen: qué instalaste, qué falló y cuál es mi siguiente paso. Dime con claridad si debo cerrar y abrir el programa.
```

## Prompt 2: si te pidió cerrar y abrir el programa

```
Continúa la instalación de la Fábrica de Marketing con IA. Vuelve a verificar que estén las skills fm-* y los agentes fm-agente-*, instala lo que todavía falte y dime cuál es mi siguiente paso.
```

## Prompt 3: empezar a trabajar

Crea una carpeta **Mi Fábrica de Marketing** en Documentos, abre la herramienta dentro de esa carpeta y escribe:

```
Quiero empezar
```

El director te hará preguntas sencillas sobre tu negocio y tu marca, te mostrará un plan, y cuando digas "vamos" verás a tu equipo trabajar en el panel.

## Notas
- Probado en **Claude Code**. En Codex o Antigravity la ubicación de skills y agentes puede ser distinta: la herramienta lo adapta o lee los archivos como instrucciones (los agentes entonces trabajan uno tras otro, y el panel funciona igual).
- Si algo falla, copia el mensaje de error completo y pásaselo a tu profesor.
- Nunca pegues contraseñas ni claves en el chat.
