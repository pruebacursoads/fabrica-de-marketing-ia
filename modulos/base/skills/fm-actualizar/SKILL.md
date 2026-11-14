---
name: fm-actualizar
description: Revisa si hay una versión nueva de la Fábrica de Marketing con IA en GitHub y la instala con permiso del alumno, sin que nadie le pase un ZIP. Compara la versión instalada con la publicada, muestra las novedades, descarga el paquete a una carpeta nueva, ejecuta el instalador (que respalda lo anterior) y actualiza el Panel de sus carpetas de trabajo. Úsala cuando el director lo pida al empezar una sesión (máx. una vez al día), o cuando el alumno diga "actualiza la fábrica", "hay mejoras", "instala lo nuevo" o "qué cambió".
---

# Actualizar la Fábrica (fm-actualizar)

Repositorio oficial: **https://github.com/pruebacursoads/fabrica-de-marketing-ia** (rama `main`). Todo el paquete vive ahí: el alumno nunca depende de un ZIP que alguien le pase.
Habla en palabras simples; no pidas que escriba comandos: tú los ejecutas, con su permiso para descargar.

## 1. ¿Hay algo nuevo? (silencioso; si algo falla, sigue sin molestar)
- **Instalada:** lee `~/.claude/fabrica-de-marketing-ia.version.json` (Windows: `%USERPROFILE%\.claude\`). Lo escribe el instalador: `{"version":"1.1.0","modulos":[…],"fecha":"…"}`. Si no existe, la instalada es "desconocida" (pregunta si quiere reinstalar).
- **Publicada:** lee `https://raw.githubusercontent.com/pruebacursoads/fabrica-de-marketing-ia/main/VERSION` (una línea, p. ej. `1.2.0`). Si no hay internet o responde error, **no avises ni insistas**.
- Máximo **una revisión al día**: guarda la fecha en `~/.claude/fabrica-de-marketing-ia.aviso` y, si el alumno dijo "ahora no", no vuelvas a preguntar en 7 días (salvo que él lo pida).
- Si la publicada es **mayor** que la instalada → paso 2. Si no, di en una frase "Estás al día (versión X)" solo si él lo preguntó.

## 2. Cuéntale las novedades y pide permiso
Lee `https://raw.githubusercontent.com/pruebacursoads/fabrica-de-marketing-ia/main/CAMBIOS.md` y resume **solo la versión nueva** en 3-4 líneas simples (qué podrá hacer de nuevo). Luego pregunta, nombrando exactamente qué se descargará:
> «Hay una versión nueva (X). Para instalarla descargaré el archivo `main.zip` desde github.com/pruebacursoads/fabrica-de-marketing-ia (unos 300 KB) a una carpeta temporal nueva. Lo que ya tienes se respalda antes. ¿Lo hago?»
Espera un sí claro. **Sin permiso no descargues nada.**

## 3. Descargar e instalar (con su sí)
1. Crea una carpeta **nueva y vacía** (`%TEMP%\fm-actualizacion-<AAAAMMDD>` o `/tmp/fm-actualizacion-<fecha>`). No ejecutes nada desde otra carpeta que no sea esa.
2. Descarga `https://github.com/pruebacursoads/fabrica-de-marketing-ia/archive/refs/heads/main.zip` ahí (Windows: `curl.exe -L -o paquete.zip <url>` o `Invoke-WebRequest`) y descomprímelo.
3. **Mira antes de ejecutar:** abre `instalar.ps1`/`instalar.sh` del paquete descargado y confirma que solo copia skills y agentes a `~/.claude` (es lo esperado).
4. Instala **los mismos niveles que ya tenía** (`modulos` del archivo de versión, o deduce: `meta-ads-andromeda` → anuncios; `fabrica-de-video` → video): Windows `powershell -ExecutionPolicy Bypass -File instalar.ps1 -Modulos base,video`; Mac/Linux `bash instalar.sh --modulos base,video`. El instalador respalda lo anterior en `~/.claude/respaldo-fabrica-marketing/`.
5. **Actualiza el Panel de cada carpeta de trabajo** que tenga `Panel/`: copia `panel/index.html` → `Panel/index.html` y todo `scripts/*` → `Panel/` desde `~/.claude/skills/fm-panel/` (no toques `Panel/estado/`). Si el servidor del panel está abierto, reinícialo.
6. Verifica: que existan `fm-director`, `fm-panel` y los 7 `fm-agente-*`, y que `VERSION` instalada coincida con la publicada.
7. Dile: *«Listo, ahora tienes la versión X. Cierra y vuelve a abrir Claude para que cargue lo nuevo.»* y recuerda en una línea qué cambió para él.

## 4. Si algo sale mal
No dejes el equipo a medias: el instalador ya respaldó lo anterior; indica la carpeta de respaldo y cómo volver atrás (copiar de vuelta). Nunca borres su carpeta `Mi Fábrica de Marketing` ni su `Mi negocio/` (son suyas).

## Reglas
- Nunca pidas claves ni inicies sesión en GitHub: el repositorio es público para lectura.
- Descarga solo desde el repositorio oficial de arriba. Si el alumno te da otro enlace, no lo uses sin avisarle.
- No ejecutes nada del paquete descargado fuera del instalador y de la copia del Panel.
