#!/usr/bin/env python3
"""Publica las mejoras del paquete en GitHub (solo para el autor; los alumnos no lo necesitan).

Qué hace, en orden:
  1. Comprueba que estás en el repositorio correcto (origin = pruebacursoads/fabrica-de-marketing-ia).
  2. Valida: sintaxis de los .py, que los .json se lean, y que no se cuele nada privado
     (claves/tokens, rutas de tu usuario de Windows, correos, teléfonos).
  3. Hace commit con un mensaje claro y lo sube a GitHub (rama main).
Si algo falla, NO sube nada y te dice qué corregir.

Uso:
  python publicar.py                         publica con mensaje automático
  python publicar.py -m "Qué mejoró"         publica con tu mensaje
  python publicar.py --version 1.1.1         además actualiza el archivo VERSION
  python publicar.py --simular               solo valida y muestra qué se publicaría
  python publicar.py --sin-push              solo guarda el commit en tu computadora
  python publicar.py --auto                  modo silencioso (lo usa el gancho de Claude Code al terminar cada respuesta)
Para pausar la publicación automática: define la variable de entorno FM_NO_PUBLICAR=1.
"""
import argparse, json, os, re, subprocess, sys

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

RAIZ = os.path.dirname(os.path.abspath(__file__))
REPO_ESPERADO = "pruebacursoads/fabrica-de-marketing-ia"
COAUTOR = "Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>"
# Lo que NO debe subirse nunca (se bloquea la publicación)
PRIVADO = [
    (re.compile(r"[A-Za-z]:\\Users\\[^\\\s\"']+", re.I), "ruta de usuario de Windows"),
    (re.compile(r"/Users/[A-Za-z0-9._-]+/|/home/[A-Za-z0-9._-]+/"), "ruta de usuario de Mac/Linux"),
    (re.compile(r"\bsk-[A-Za-z0-9_-]{20,}"), "clave tipo sk-…"),
    (re.compile(r"\bAIza[0-9A-Za-z_-]{30,}"), "clave de Google"),
    (re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}"), "token de GitHub"),
    (re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}"), "token de Slack"),
    (re.compile(r"(?i)\b(api[_-]?key|secret|password|token)\b\s*[:=]\s*['\"][^'\"\s]{10,}['\"]"), "clave o contraseña escrita en texto"),
    (re.compile(r"[A-Za-z0-9._%+-]+@(gmail|hotmail|outlook|yahoo|icloud)\.[a-z.]+", re.I), "correo personal"),
    (re.compile(r"(?<!\d)(\+?51 ?)?9\d{2}[ -]?\d{3}[ -]?\d{3}(?!\d)"), "posible teléfono"),
]
EXT_TEXTO = {".md", ".py", ".json", ".html", ".js", ".ps1", ".sh", ".bat", ".txt", ".yml", ".yaml", ".toml", ".css", ""}


def git(*args, check=True):
    r = subprocess.run(["git", *args], cwd=RAIZ, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if check and r.returncode != 0:
        raise RuntimeError((r.stderr or r.stdout).strip() or "git falló")
    return r.stdout.strip()


def hablar(auto, *msg):
    if not auto:
        print(*msg)
    else:
        print(*msg, file=sys.stderr)


def validar():
    """Devuelve la lista de problemas (vacía = todo bien)."""
    problemas = []
    archivos = git("ls-files", "--cached", "--others", "--exclude-standard").splitlines()
    for rel in archivos:
        ruta = os.path.join(RAIZ, rel)
        if not os.path.isfile(ruta) or rel.startswith(".git/"):
            continue
        ext = os.path.splitext(rel)[1].lower()
        if ext == ".py":
            try:
                compile(open(ruta, encoding="utf-8").read(), rel, "exec")
            except (SyntaxError, ValueError, OSError) as e:
                problemas.append("Error de sintaxis en %s: %s" % (rel, e))
        if ext == ".json":
            try:
                json.load(open(ruta, encoding="utf-8"))
            except (ValueError, OSError) as e:
                problemas.append("JSON inválido en %s: %s" % (rel, e))
        if ext in EXT_TEXTO and os.path.getsize(ruta) < 3_000_000 and os.path.basename(rel) != "publicar.py":
            try:
                texto = open(ruta, encoding="utf-8").read()
            except (UnicodeDecodeError, OSError):
                continue
            for n, linea in enumerate(texto.splitlines(), 1):
                for patron, que in PRIVADO:
                    if patron.search(linea):
                        problemas.append("%s:%d parece contener %s → %s" % (rel, n, que, linea.strip()[:80]))
                        break
    return problemas


def mensaje_auto(cambios):
    areas = {}
    for linea in cambios:
        ruta = linea[3:].strip().strip('"').replace("\\", "/")
        partes = ruta.split("/")
        clave = "/".join(partes[:3]) if partes[0] == "modulos" and len(partes) > 3 else partes[0]
        areas[clave] = areas.get(clave, 0) + 1
    resumen = ", ".join("%s (%d)" % (k, v) for k, v in sorted(areas.items(), key=lambda x: -x[1])[:4])
    return "Mejora automática: " + resumen


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-m", "--mensaje")
    ap.add_argument("--version")
    ap.add_argument("--sin-push", action="store_true")
    ap.add_argument("--auto", action="store_true")
    ap.add_argument("--simular", action="store_true", help="solo valida y muestra qué se publicaría; no guarda ni sube nada")
    args = ap.parse_args()
    auto = args.auto
    if os.environ.get("FM_NO_PUBLICAR") == "1":
        return 0
    if auto:
        try:
            sys.stdin.read()  # el gancho de Claude Code manda un JSON por stdin; no se usa
        except Exception:
            pass
    try:
        origen = git("remote", "get-url", "origin")
    except RuntimeError:
        hablar(auto, "No es un repositorio git con 'origin'. Nada que publicar.")
        return 0
    if REPO_ESPERADO not in origen.replace(".git", ""):
        hablar(auto, "El repositorio remoto (%s) no es el esperado; no publico." % origen)
        return 0
    if args.version:
        if not re.match(r"^\d+\.\d+\.\d+$", args.version):
            print("La versión debe verse así: 1.1.1")
            return 2
        open(os.path.join(RAIZ, "VERSION"), "w", encoding="utf-8", newline="\n").write(args.version + "\n")
    cambios = [c for c in git("status", "--porcelain").splitlines() if c.strip()]
    if not cambios:
        hablar(auto, "Sin cambios que publicar.")
        return 0
    problemas = validar()
    if problemas:
        print("NO publiqué nada. Corrige esto primero:\n - " + "\n - ".join(problemas[:15]), file=sys.stderr if auto else sys.stdout)
        return 0 if auto else 1
    if args.simular:
        lista = chr(10).join('  ' + c for c in cambios[:40])
        print('Validacion correcta. Se publicarian %d archivo(s):' % len(cambios))
        print(lista)
        return 0
    msg = (args.mensaje or mensaje_auto(cambios)).strip() + "\n\n" + COAUTOR
    try:
        git("add", "-A")
        git("commit", "-m", msg)
        corto = git("rev-parse", "--short", "HEAD")
        hablar(auto, "Guardado en tu repositorio local (%s): %d archivo(s)." % (corto, len(cambios)))
        if args.sin_push:
            return 0
        rama = git("branch", "--show-current") or "main"
        git("push", "origin", rama)
        hablar(auto, "Publicado en GitHub: https://github.com/%s (rama %s)" % (REPO_ESPERADO, rama))
    except RuntimeError as e:
        hablar(auto, "No pude subirlo a GitHub (queda guardado en tu computadora; se subirá en la próxima publicación): %s" % str(e)[:300])
        return 0 if auto else 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
