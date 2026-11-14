#!/usr/bin/env python3
"""Reporta al Panel en vivo (solo librería estándar). Versión 1.1.

Uso (desde la carpeta de trabajo, la que contiene Panel/):
  python Panel/reportar.py agente estratega --estado trabajando --tarea "Armando calendario" --progreso 40 --log "Definí 3 pilares"
  python Panel/reportar.py agente estratega --estado listo --progreso 100 --archivo "Estrategia/calendario.md|Calendario"
  python Panel/reportar.py director --negocio "Mi negocio" --etapa 4 --estado-etapa en-curso --mensaje "Producción en paralelo" --log "Lancé 6 agentes"
  python Panel/reportar.py guia video --desde guia-video.json --md "Entregables/2026-11-13-tema/video/05-guia-de-generacion.md"
  python Panel/reportar.py medios                     (re-escanea lo que el alumno subió o copió a las carpetas)
  python Panel/reportar.py revision --slot vid-clip-01 --estado ok --nota "Voz y ropa bien"
  python Panel/reportar.py reiniciar

Cada agente escribe SOLO sus propios archivos (estado/<id>.js, estado/guia-<id>.json): así varios agentes en paralelo no se pisan.
En Windows, si "python" no existe, usa "py -3".
"""
import argparse, json, os, re, sys
from datetime import datetime

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")  # evita errores con tildes en la consola de Windows
    except Exception:
        pass

ESTADOS = {"espera", "trabajando", "listo", "ajustando", "necesita-ayuda"}
ESTADOS_ETAPA = {"pendiente", "en-curso", "listo"}
IDS = ["estratega", "oferta", "imagenes", "carruseles", "video", "anuncios", "revisor"]
ESTADOS_REVISION = {"revisando", "ok", "repetir"}

EXT_IMG = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".avif"}
EXT_VID = {".mp4", ".mov", ".webm", ".m4v"}
EXT_AUD = {".mp3", ".wav", ".m4a", ".aac", ".ogg"}
EXT_DOC = {".pdf", ".md", ".txt", ".json", ".csv", ".docx", ".xlsx"}
EXT_OK = EXT_IMG | EXT_VID | EXT_AUD | EXT_DOC
# Carpetas de "material" que también se vigilan (fotos reales, logo, referencias, subidas libres)
CARPETAS_MATERIAL = ["Mi negocio/fotos-producto", "Mi negocio/logo", "Mi negocio/referencias", "Mi negocio/subidas"]
RE_ID = re.compile(r"^[a-z0-9][a-z0-9-]{0,48}$")


def ahora():
    return datetime.now().strftime("%H:%M:%S")


def leer(ruta, clave):
    """Lee el JSON guardado en un archivo de estado (o None)."""
    try:
        txt = open(ruta, encoding="utf-8").read()
    except OSError:
        return None
    m = re.search(clave + r"\s*=\s*(\{.*\})\s*;?\s*$", txt, re.S)
    if not m:
        return None
    try:
        return json.loads(m.group(1))
    except ValueError:
        return None


def escribir(ruta, js):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    tmp = ruta + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(js)
    os.replace(tmp, ruta)  # escritura atómica: la página nunca lee a medias


def tipo_de(ext):
    ext = ext.lower()
    if ext in EXT_IMG:
        return "imagen"
    if ext in EXT_VID:
        return "video"
    if ext in EXT_AUD:
        return "audio"
    return "doc"


def carpeta_panel(arg=None):
    if arg:
        return os.path.abspath(arg)
    aqui = os.path.dirname(os.path.abspath(__file__))
    return aqui if os.path.exists(os.path.join(aqui, "index.html")) else os.path.abspath("Panel")


# ------------------------------------------------------------------ guía de generación
def guias_fusionadas(est):
    """Todas las guías (una por agente) ordenadas."""
    secs = []
    try:
        nombres = sorted(os.listdir(est))
    except OSError:
        return secs
    for n in nombres:
        if n.startswith("guia-") and n.endswith(".json"):
            try:
                secs.append(json.load(open(os.path.join(est, n), encoding="utf-8")))
            except (OSError, ValueError):
                pass
    secs.sort(key=lambda s: (s.get("orden", 50), s.get("agente", "")))
    return secs


def validar_guia(d):
    errs = []
    if not isinstance(d, dict) or not isinstance(d.get("pasos"), list) or not d["pasos"]:
        return ["El JSON debe ser un objeto con una lista 'pasos' (al menos 1)."]
    vistos = set()
    for i, p in enumerate(d["pasos"], 1):
        if not isinstance(p, dict):
            errs.append("Paso %d: debe ser un objeto." % i)
            continue
        pid = p.get("id", "")
        if not RE_ID.match(str(pid)):
            errs.append("Paso %d: 'id' inválido (solo minúsculas, números y guiones; máx. 49): %r" % (i, pid))
        elif pid in vistos:
            errs.append("Paso %d: 'id' repetido: %s" % (i, pid))
        vistos.add(pid)
        if not p.get("titulo"):
            errs.append("Paso %d (%s): falta 'titulo'." % (i, pid))
        sal = str(p.get("salida") or "").replace("\\", "/")
        if sal:
            if sal.startswith("/") or ".." in sal.split("/") or re.match(r"^[A-Za-z]:", sal):
                errs.append("Paso %d (%s): 'salida' debe ser una ruta relativa sin '..'." % (i, pid))
            elif sal.split("/")[0] not in ("Entregables", "Mi negocio"):
                errs.append("Paso %d (%s): 'salida' debe empezar por Entregables/ o Mi negocio/." % (i, pid))
        if p.get("prompt") is not None and not isinstance(p["prompt"], str):
            errs.append("Paso %d (%s): 'prompt' debe ser texto." % (i, pid))
        if p.get("refs") is not None and not isinstance(p["refs"], list):
            errs.append("Paso %d (%s): 'refs' debe ser una lista." % (i, pid))
    return errs


def guia_a_md(sec):
    L = ["# %s" % sec.get("titulo", "Guía de generación"), ""]
    if sec.get("intro"):
        L += [sec["intro"], ""]
    L += ["> Esta misma guía aparece en tu Panel (pestaña **Guía de generación**), con botón de copiar y para subir tus archivos.", ""]
    for n, p in enumerate(sec.get("pasos", []), 1):
        L.append("## %d · %s" % (n, p.get("titulo", "")))
        meta = []
        if p.get("herramienta"):
            meta.append("[%s](%s)" % (p["herramienta"], p["enlace"]) if p.get("enlace") else p["herramienta"])
        for k in ("formato", "duracion"):
            if p.get(k):
                meta.append(str(p[k]))
        if meta:
            L.append("**Dónde / cómo:** " + " · ".join(meta))
        if p.get("pedir"):
            L += ["", p["pedir"]]
        if p.get("refs"):
            L += ["", "**Carga en este orden:**"]
            for i, r in enumerate(p["refs"], 1):
                extra = (" (" + r["archivo"] + ")") if r.get("archivo") else ""
                L.append("%d. %s%s" % (i, r.get("nombre", ""), extra))
        if p.get("prompt"):
            L += ["", "**Prompt (copiar y pegar)**" + ((" · " + p["palabras"]) if p.get("palabras") else ""), "", "```text", p["prompt"].strip(), "```"]
        if p.get("notas"):
            L += ["", p["notas"]]
        if p.get("revisar"):
            L += ["", "**Revisa al recibirlo:**"] + ["- " + x for x in p["revisar"]]
        if p.get("salida"):
            L += ["", "**Guárdalo como:** `%s`" % p["salida"]]
        L.append("")
    return "\n".join(L)


def escribir_guia_js(est):
    secs = guias_fusionadas(est)
    js = ('window.FM=window.FM||{};window.FM.guia=' +
          json.dumps({"secciones": secs, "actualizado": datetime.now().isoformat(timespec="seconds")}, ensure_ascii=False) + ";\n")
    escribir(os.path.join(est, "guia.js"), js)


def buscar_paso(est, slot):
    for s in guias_fusionadas(est):
        for p in s.get("pasos", []):
            if p.get("id") == slot:
                return p
    return None


# ------------------------------------------------------------------ medios (lo que el alumno subió)
def _info(raiz, fp):
    st = os.stat(fp)
    return {"archivo": os.path.relpath(fp, raiz).replace("\\", "/"), "tam": st.st_size,
            "mod": int(st.st_mtime), "tipo": tipo_de(os.path.splitext(fp)[1])}


def _lista_carpeta(raiz, carpeta):
    out = []
    if os.path.isdir(carpeta):
        for f in sorted(os.listdir(carpeta)):
            fp = os.path.join(carpeta, f)
            if os.path.isfile(fp) and not f.startswith(".") and os.path.splitext(f)[1].lower() in EXT_OK:
                out.append(_info(raiz, fp))
    return out


def escanear(panel):
    """Devuelve {slot: info | {archivos:[...]}, '_material': {carpeta: [info,...]}}."""
    panel = os.path.abspath(panel)
    raiz = os.path.dirname(panel)
    est = os.path.join(panel, "estado")
    medios = {}
    for sec in guias_fusionadas(est):
        for p in sec.get("pasos", []):
            salida = str(p.get("salida") or "").replace("\\", "/").strip("/")
            if not salida:
                continue
            if p.get("multiple"):
                medios[p["id"]] = {"archivos": _lista_carpeta(raiz, os.path.join(raiz, salida))}
                continue
            ruta = os.path.join(raiz, salida)
            carpeta, stem = os.path.dirname(ruta), os.path.splitext(os.path.basename(ruta))[0]
            mejor = None
            if os.path.isdir(carpeta):
                for f in os.listdir(carpeta):
                    n, e = os.path.splitext(f)
                    fp = os.path.join(carpeta, f)
                    if n == stem and e.lower() in EXT_OK and os.path.isfile(fp):
                        if mejor is None or os.path.getmtime(fp) > os.path.getmtime(mejor):
                            mejor = fp
            if mejor:
                medios[p["id"]] = _info(raiz, mejor)
    medios["_material"] = {c: _lista_carpeta(raiz, os.path.join(raiz, c)) for c in CARPETAS_MATERIAL}
    return medios


def escribir_medios(panel):
    """Reescribe estado/medios.js solo si cambió. Devuelve True si cambió."""
    panel = os.path.abspath(panel)
    ruta = os.path.join(panel, "estado", "medios.js")
    nuevo = escanear(panel)
    if leer(ruta, r"FM\.medios") == nuevo:
        return False
    escribir(ruta, "window.FM=window.FM||{};window.FM.medios=" + json.dumps(nuevo, ensure_ascii=False) + ";\n")
    return True


def aplanar(medios):
    """{ruta: (mod, tam, slot)} para vigilar cambios."""
    out = {}
    for slot, v in medios.items():
        if slot == "_material":
            for carpeta, lista in v.items():
                for i in lista:
                    out[i["archivo"]] = (i["mod"], i["tam"], "material")
        else:
            for i in (v.get("archivos") if "archivos" in v else [v]):
                out[i["archivo"]] = (i["mod"], i["tam"], slot)
    return out


# ------------------------------------------------------------------ principal
def main():
    p = argparse.ArgumentParser()
    p.add_argument("--panel", default=None, help="carpeta del Panel (la que contiene index.html)")
    sub = p.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("agente")
    a.add_argument("id", choices=IDS)
    a.add_argument("--estado", choices=sorted(ESTADOS))
    a.add_argument("--tarea")
    a.add_argument("--progreso", type=int)
    a.add_argument("--log")
    a.add_argument("--archivo", action="append", help="ruta relativa a la carpeta de trabajo, opcional '|Nombre visible'")

    d = sub.add_parser("director")
    d.add_argument("--negocio")
    d.add_argument("--etapa", type=int, choices=range(1, 7))
    d.add_argument("--estado-etapa", choices=sorted(ESTADOS_ETAPA), default="en-curso")
    d.add_argument("--mensaje")
    d.add_argument("--log")

    g = sub.add_parser("guia", help="publica la guía de generación (prompts, referencias, dónde subir) de un agente")
    g.add_argument("agente", choices=IDS)
    g.add_argument("--desde", required=True, help="JSON con titulo, intro, orden y pasos[]")
    g.add_argument("--md", help="además, escribe la misma guía como Markdown en esta ruta (relativa a la carpeta de trabajo)")

    sub.add_parser("medios", help="re-escanea lo subido y actualiza estado/medios.js")

    r = sub.add_parser("revision", help="muestra en el Panel el veredicto de Claude sobre un archivo recibido")
    r.add_argument("--slot", required=True)
    r.add_argument("--estado", choices=sorted(ESTADOS_REVISION), required=True)
    r.add_argument("--nota", default="")

    sub.add_parser("reiniciar")
    args = p.parse_args()
    panel = carpeta_panel(args.panel)
    est = os.path.join(panel, "estado")
    raiz = os.path.dirname(panel)

    if args.cmd == "reiniciar":
        borrar = [i + ".js" for i in IDS + ["director"]] + ["guia.js", "medios.js", "revisiones.js", "servidor.json"]
        try:
            borrar += [n for n in os.listdir(est) if n.startswith("guia-") and n.endswith(".json")]
        except OSError:
            pass
        for n in borrar:
            f = os.path.join(est, n)
            if os.path.exists(f):
                os.remove(f)
        escribir(os.path.join(est, "director.js"),
                 'window.FM=window.FM||{};window.FM.director=' +
                 json.dumps({"negocio": "", "etapas": ["pendiente"] * 6, "mensaje": "Listo para empezar", "log": []}, ensure_ascii=False) + ";\n")
        print("Panel reiniciado")
        return

    if args.cmd == "agente":
        ruta = os.path.join(est, args.id + ".js")
        dat = leer(ruta, r'agentes\["' + args.id + r'"\]') or {"estado": "espera", "tarea": "", "progreso": 0, "archivos": [], "log": []}
        if args.estado:
            dat["estado"] = args.estado
        if args.tarea is not None:
            dat["tarea"] = args.tarea
        if args.progreso is not None:
            dat["progreso"] = max(0, min(100, args.progreso))
        if args.estado == "listo" and args.progreso is None:
            dat["progreso"] = 100
        for f in args.archivo or []:
            ruta_rel, _, nombre = f.partition("|")
            ruta_rel = ruta_rel.replace("\\", "/")
            if not any(x["ruta"] == ruta_rel for x in dat["archivos"]):
                dat["archivos"].append({"ruta": ruta_rel, "nombre": nombre or os.path.basename(ruta_rel)})
        if args.log:
            dat["log"].append({"t": ahora(), "m": args.log})
            dat["log"] = dat["log"][-30:]
        dat["actualizado"] = datetime.now().isoformat(timespec="seconds")
        js = ('window.FM=window.FM||{};window.FM.agentes=window.FM.agentes||{};window.FM.agentes["%s"]=' % args.id
              + json.dumps(dat, ensure_ascii=False) + ";\n")
        escribir(ruta, js)
        print("ok", args.id, dat["estado"], dat["progreso"])
        return

    if args.cmd == "director":
        ruta = os.path.join(est, "director.js")
        dat = leer(ruta, r"FM\.director") or {"negocio": "", "etapas": ["pendiente"] * 6, "mensaje": "", "log": []}
        if args.negocio is not None:
            dat["negocio"] = args.negocio
        if args.etapa:
            for i in range(6):
                if i < args.etapa - 1:
                    dat["etapas"][i] = "listo"
            dat["etapas"][args.etapa - 1] = args.estado_etapa
        if args.mensaje is not None:
            dat["mensaje"] = args.mensaje
        if args.log:
            dat["log"].append({"t": ahora(), "ag": "Director", "m": args.log})
            dat["log"] = dat["log"][-40:]
        js = 'window.FM=window.FM||{};window.FM.director=' + json.dumps(dat, ensure_ascii=False) + ";\n"
        escribir(ruta, js)
        print("ok director", dat["etapas"])
        return

    if args.cmd == "guia":
        try:
            dat = json.load(open(args.desde, encoding="utf-8"))
        except (OSError, ValueError) as e:
            print("No pude leer %s: %s" % (args.desde, e))
            return 2
        errs = validar_guia(dat)
        if errs:
            print("La guía tiene errores:\n - " + "\n - ".join(errs))
            return 2
        dat["agente"] = args.agente
        escribir(os.path.join(est, "guia-%s.json" % args.agente), json.dumps(dat, ensure_ascii=False, indent=1))
        escribir_guia_js(est)
        escribir_medios(panel)
        if args.md:
            destino = os.path.join(raiz, args.md.replace("\\", "/"))
            os.makedirs(os.path.dirname(destino), exist_ok=True)
            with open(destino, "w", encoding="utf-8") as f:
                f.write(guia_a_md(dat))
            print("ok guía + Markdown:", args.md)
        else:
            print("ok guía de", args.agente, "con", len(dat["pasos"]), "pasos")
        return

    if args.cmd == "medios":
        cambio = escribir_medios(panel)
        m = escanear(panel)
        recibidos = [k for k in m if k != "_material" and (m[k].get("archivos") if "archivos" in m[k] else True)]
        print("medios actualizados" if cambio else "sin cambios", "· recibidos:", ", ".join(recibidos) or "ninguno")
        return

    if args.cmd == "revision":
        ruta = os.path.join(est, "revisiones.js")
        dat = leer(ruta, r"FM\.revisiones") or {}
        dat[args.slot] = {"estado": args.estado, "nota": args.nota, "t": ahora()}
        escribir(ruta, "window.FM=window.FM||{};window.FM.revisiones=" + json.dumps(dat, ensure_ascii=False) + ";\n")
        print("ok revisión", args.slot, args.estado)
        return


if __name__ == "__main__":
    sys.exit(main())
