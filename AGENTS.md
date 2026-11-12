# AGENTS.md — Fábrica de Marketing con IA

Este repositorio es un **paquete de skills y agentes** (no una aplicación). Si eres un asistente de IA (Claude Code, Codex, Antigravity u otro) y un usuario te pidió instalarlo o usarlo:

## Estructura
- `modulos/base/skills/` — `fm-director`, `fm-diagnostico`, `fm-adn`, `fm-oferta-copy`, `fm-panel` + skills de contenido, imágenes, flyers y carruseles.
- `modulos/anuncios/skills/` — `meta-ads-andromeda` (leer SIEMPRE `references/estado-vigente.md`).
- `modulos/video/skills/` — Omni Flash, Seedance, Veo y la Fábrica de Video (`fabrica-de-video`, `fv-*`).
- `agentes/` — definiciones de subagentes `fm-agente-*` (van a `.claude/agents/`).
- `instalar.ps1` / `instalar.sh` — copian skills y agentes con respaldo.

## Si te piden instalar
Sigue `PROMPT-DE-INSTALACION.md`. El usuario no es técnico: explica simple, ejecuta tú los comandos, pide permiso antes de instalar software, nunca pidas contraseñas ni claves.

## Si te piden usarlo
Empieza por la skill `fm-director` (o lee `modulos/base/skills/fm-director/SKILL.md`). Si tu herramienta no soporta skills o subagentes, lee los archivos como instrucciones y ejecuta los agentes uno tras otro; el panel (`fm-panel`) funciona igual.

## Reglas que no se rompen
- La marca sale del ADN del alumno (`Mi negocio/adn-de-marca.md`); nunca la de otro.
- No inventar precios, cifras, testimonios ni garantías (`POR CONFIRMAR`).
- No crear ni editar nada en la cuenta de Meta del alumno sin confirmación explícita por acción.
- Lo que `meta-ads-andromeda/references/estado-vigente.md` marque como NO VERIFICADO no se presenta como hecho.
- Datos privados: nada de claves por chat.
