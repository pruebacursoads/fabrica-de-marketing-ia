#!/usr/bin/env python3
"""Reporta el estado de un agente al Panel en vivo (solo librería estándar).

Uso (desde cualquier carpeta):
  python reportar.py --panel "Panel" agente estratega --estado trabajando --tarea "Armando calendario" --progreso 40 --log "Definí 3 pilares"
  python reportar.py --panel "Panel" agente estratega --estado listo --progreso 100 --archivo "Estrategia/calendario.md|Calendario"
  python reportar.py --panel "Panel" director --negocio "Mi negocio" --etapa 4 --estado-etapa en-curso --mensaje "Producción en paralelo" --log "Lancé 6 agentes"
  python reportar.py --panel "Panel" reiniciar

Cada agente escribe SOLO su propio archivo (estado/<id>.js): así varios agentes en paralelo no se pisan.
En Windows, si "python" no existe, usa "py -3".
"""
import argparse, json, os, re, sys
from datetime import datetime

ESTADOS = {"espera", "trabajando", "listo", "ajustando", "necesita-ayuda"}
ESTADOS_ETAPA = {"pendiente", "en-curso", "listo"}
IDS = ["estratega", "oferta", "imagenes", "carruseles", "video", "anuncios", "revisor"]


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


def main():
    p = argparse.ArgumentParser()
    aqui = os.path.dirname(os.path.abspath(__file__))
    # Si el script está dentro de Panel/ (junto a index.html), esa es la carpeta por defecto: así los agentes
    # solo ejecutan  python Panel/reportar.py agente <id> ...  desde cualquier lugar, sin --panel.
    por_defecto = aqui if os.path.exists(os.path.join(aqui, "index.html")) else "Panel"
    p.add_argument("--panel", default=por_defecto, help="carpeta del Panel (la que contiene index.html)")
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

    sub.add_parser("reiniciar")
    args = p.parse_args()
    est = os.path.join(args.panel, "estado")

    if args.cmd == "reiniciar":
        for i in IDS + ["director"]:
            f = os.path.join(est, i + ".js")
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


if __name__ == "__main__":
    sys.exit(main())
