#!/usr/bin/env python3
"""Diagnóstico del equipo para la Fábrica de Video (Windows, Mac y Linux). No instala nada.
   python diagnostico.py [--json salida.json]
   Revisa memoria, disco, ffmpeg, Node, Python, Whisper y Chrome; recomienda modo normal o ligero
   y muestra los comandos de instalación para lo que falte."""
import argparse, ctypes, importlib.util, json, os, platform, re, shutil, subprocess, sys

try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass

SO = {"Windows": "windows", "Darwin": "mac"}.get(platform.system(), "linux")

def run(cmd, t=25):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=t, shell=isinstance(cmd, str))
        return r.returncode, (r.stdout or r.stderr).strip()
    except Exception as e:
        return -1, str(e)

def memoria():
    """(total_GB, libre_GB)"""
    try:
        if SO == "windows":
            class MS(ctypes.Structure):
                _fields_ = [("dwLength", ctypes.c_ulong), ("dwMemoryLoad", ctypes.c_ulong), ("ullTotalPhys", ctypes.c_ulonglong),
                            ("ullAvailPhys", ctypes.c_ulonglong), ("ullTotalPageFile", ctypes.c_ulonglong), ("ullAvailPageFile", ctypes.c_ulonglong),
                            ("ullTotalVirtual", ctypes.c_ulonglong), ("ullAvailVirtual", ctypes.c_ulonglong), ("sullAvailExtendedVirtual", ctypes.c_ulonglong)]
            m = MS(); m.dwLength = ctypes.sizeof(MS)
            ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(m))
            return m.ullTotalPhys / 2**30, m.ullAvailPhys / 2**30
        if SO == "mac":
            tot = int(run("sysctl -n hw.memsize")[1]) / 2**30
            vm = run("vm_stat")[1]
            page = int(re.search(r"page size of (\d+)", vm).group(1))
            libre = 0
            for k in ("Pages free", "Pages inactive", "Pages speculative"):
                mm = re.search(k + r":\s+(\d+)", vm)
                if mm: libre += int(mm.group(1))
            return tot, libre * page / 2**30
        d = {}
        for l in open("/proc/meminfo"):
            k, v = l.split(":"); d[k] = int(v.split()[0])
        return d["MemTotal"] / 2**20, d.get("MemAvailable", d["MemFree"]) / 2**20
    except Exception:
        return 0.0, 0.0

def version(cmd):
    c, o = run(cmd)
    return o.splitlines()[0] if c == 0 and o else None

def chrome():
    cand = [os.environ.get("CHROME_PATH"),
            r"C:\Program Files\Google\Chrome\Application\chrome.exe", r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
            os.path.join(os.environ.get("LOCALAPPDATA", ""), r"Google\Chrome\Application\chrome.exe"),
            r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe", r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
            "/usr/bin/google-chrome", "/usr/bin/chromium", "/usr/bin/chromium-browser"]
    return next((c for c in cand if c and os.path.exists(c)), None)

INSTALAR = {
    "ffmpeg": {"windows": "winget install --id Gyan.FFmpeg -e", "mac": "brew install ffmpeg", "linux": "sudo apt install ffmpeg"},
    "node": {"windows": "winget install OpenJS.NodeJS.LTS", "mac": "brew install node", "linux": "sudo apt install nodejs npm"},
    "python": {"windows": "winget install Python.Python.3.11", "mac": "brew install python@3.11", "linux": "sudo apt install python3 python3-pip"},
    "whisper": {"windows": "pip install openai-whisper", "mac": "pip3 install openai-whisper", "linux": "pip3 install openai-whisper"},
    "chrome": {"windows": "winget install Google.Chrome", "mac": "brew install --cask google-chrome", "linux": "sudo apt install chromium"},
}
PARA = {"ffmpeg": "cortar, unir, limpiar audio y medir volumen", "node": "motor de HyperFrames (el que arma el video)",
        "python": "ejecutar los scripts de la Fábrica", "whisper": "transcribir tu voz con el segundo de cada palabra",
        "chrome": "HyperFrames dibuja los fotogramas con Chrome y la revisión de choques también"}

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--json", default=None); a = ap.parse_args()
    tot, libre = memoria()
    disco = shutil.disk_usage(os.getcwd()).free / 2**30
    items = []
    def add(clave, ok, detalle, obligatorio=True):
        items.append({"item": clave, "ok": bool(ok), "detalle": detalle, "obligatorio": obligatorio,
                      "para": PARA.get(clave, ""), "instalar": None if ok else INSTALAR.get(clave, {}).get(SO)})
    ff = version(["ffmpeg", "-version"]) if shutil.which("ffmpeg") else None
    add("ffmpeg", ff and shutil.which("ffprobe"), ff or "no está en el PATH")
    nd = version(["node", "-v"]) if shutil.which("node") else None
    mayor = int(nd.lstrip("v").split(".")[0]) if nd and nd.startswith("v") else 0
    add("node", mayor >= 20, (nd + (" · se recomienda 22 o superior" if 0 < mayor < 22 else "")) if nd else "no instalado")
    add("python", sys.version_info >= (3, 10), f"Python {platform.python_version()}")
    w = importlib.util.find_spec("whisper") is not None
    add("whisper", w, "instalado" if w else "no instalado")
    ch = chrome()
    add("chrome", ch, ch or "no encuentro Chrome ni Edge")
    npx = shutil.which("npx")
    items.append({"item": "npx", "ok": bool(npx), "detalle": npx or "viene con Node.js", "obligatorio": True, "para": "ejecutar HyperFrames", "instalar": None if npx else INSTALAR["node"][SO]})
    modo = "normal"
    notas = []
    if tot < 8: modo = "ligero"; notas.append(f"Tu memoria total es {tot:.1f} GB: usa el modo ligero (transcripción pequeña, render a 720p, menos efectos).")
    elif tot < 12: modo = "ligero"; notas.append(f"Memoria total {tot:.1f} GB: modo ligero recomendado para videos de más de 1 minuto.")
    if libre < 2: notas.append(f"Solo hay {libre:.1f} GB libres ahora: cierra Chrome y otros programas antes de renderizar (con menos de 1 GB el render se cierra solo).")
    elif libre < 4: notas.append(f"Hay {libre:.1f} GB libres: usa 1 proceso de render, o cierra programas para ir más rápido.")
    if disco < 10: notas.append(f"Solo quedan {disco:.0f} GB de disco: libera al menos 10 GB.")
    faltan = [i["item"] for i in items if not i["ok"] and i["obligatorio"]]
    gestor = {"windows": "winget", "mac": "brew"}.get(SO)
    if gestor and not shutil.which(gestor):
        notas.append(f"No encuentro '{gestor}', el instalador de programas de tu sistema. " + ("En Mac, instala Homebrew desde brew.sh." if SO == "mac" else "Actualiza Windows o instala 'App Installer' desde Microsoft Store."))
    informe = {"sistema": f"{platform.system()} {platform.release()} · {platform.machine()}", "cpus": os.cpu_count(), "ram_total_gb": round(tot, 1),
               "ram_libre_gb": round(libre, 1), "disco_libre_gb": round(disco), "modo": modo, "listo": not faltan, "faltan": faltan, "notas": notas, "items": items}
    print(f"\nEquipo: {informe['sistema']} · {informe['cpus']} hilos · RAM {tot:.1f} GB ({libre:.1f} GB libres) · disco libre {disco:.0f} GB")
    for i in items:
        print(f"  {'✅' if i['ok'] else '❌'} {i['item']:<8} {i['detalle']}")
        if not i["ok"]:
            print(f"       sirve para: {i['para']}")
            if i["instalar"]: print(f"       instalar:   {i['instalar']}")
    print(f"\nModo recomendado: {modo.upper()}")
    for n in notas: print("  · " + n)
    print("\nTodo listo ✅" if not faltan else "\nFalta: " + ", ".join(faltan) + "  (después de instalar, cierra y abre la terminal y la app)")
    if a.json:
        os.makedirs(os.path.dirname(os.path.abspath(a.json)), exist_ok=True)
        json.dump(informe, open(a.json, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(f"Informe guardado en {a.json}")

if __name__ == "__main__":
    main()
