#!/usr/bin/env python3
"""Revisión de calidad antes de renderizar: choques de texto, errores de HyperFrames y fotogramas de los momentos clave.
   python revisar.py <proyecto> [--preparar] [--sin-choques] [--sin-fotogramas]
   --preparar     instala puppeteer-core (una sola vez) para el auditor de choques
   Salida: resumen en pantalla y fotogramas PNG que Claude debe MIRAR (rostro libre, nada cortado, nada pisado)."""
import argparse, glob, json, os, shutil, subprocess, sys, time

try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass

AQUI = os.path.dirname(os.path.abspath(__file__))
WIN = os.name == "nt"
RUIDO = {"nested_structure_needs_subcomposition", "composition_file_too_large", "timeline_track_too_dense", "line_unread", "craft_line_unread"}

def sh(cmd, cwd=None, salida=None):
    if salida:
        with open(salida, "w", encoding="utf-8", errors="replace") as f, open(salida + ".err", "w", encoding="utf-8", errors="replace") as e:
            return subprocess.run(cmd, cwd=cwd, stdout=f, stderr=e, shell=WIN).returncode
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace", shell=WIN)

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("proyecto"); ap.add_argument("--preparar", action="store_true")
    ap.add_argument("--sin-choques", action="store_true"); ap.add_argument("--sin-fotogramas", action="store_true")
    a = ap.parse_args(); D = os.path.abspath(a.proyecto)
    if not os.path.exists(os.path.join(D, "index.html")): print("No existe index.html: ejecuta construir.py primero."); sys.exit(1)
    if a.preparar or not os.path.isdir(os.path.join(AQUI, "node_modules", "puppeteer-core")):
        if not a.sin_choques:
            print("Instalando puppeteer-core (auditor de choques, una sola vez)...")
            r = sh("npm install --no-audit --no-fund puppeteer-core" if WIN else ["npm", "install", "--no-audit", "--no-fund", "puppeteer-core"], cwd=AQUI)
            print("  listo" if r.returncode == 0 else "  ⚠ no se pudo instalar: " + (r.stderr or "")[-300:])
    problemas = 0
    # 1) choques
    if not a.sin_choques and os.path.isdir(os.path.join(AQUI, "node_modules", "puppeteer-core")):
        r = sh(f'node "{os.path.join(AQUI, "auditar_choques.cjs")}" "{os.path.join(D, "index.html")}" 0.1 0.5 0.5' if WIN else ["node", os.path.join(AQUI, "auditar_choques.cjs"), os.path.join(D, "index.html"), "0.1", "0.5", "0.5"])
        lineas = [l for l in (r.stdout or "").splitlines() if "AUDIT" in l or "CHOQUES" in l or "choque" in l or "fuera" in l or "panel" in l]
        print("\n== Choques de texto ==")
        for l in lineas[:25]: print("  " + l)
        if r.returncode != 0: problemas += 1
    elif not a.sin_choques: print("\n== Choques de texto ==\n  ⚠ auditor no instalado (usa --preparar)")
    # 2) hyperframes check
    print("\n== HyperFrames check ==")
    jf = os.path.join(D, "check.json")
    sh("npx --yes hyperframes check --json" if WIN else ["npx", "--yes", "hyperframes", "check", "--json"], cwd=D, salida=jf)
    try:
        j = json.load(open(jf, encoding="utf-8", errors="replace"))
        for sec in ("lint", "runtime", "layout"):
            v = j.get(sec, {})
            cuenta = {}
            for f in v.get("findings", []):
                if f.get("code") in RUIDO: continue
                cuenta[f["code"]] = cuenta.get(f["code"], 0) + 1
            err = [f for f in v.get("findings", []) if f.get("severity") == "error"]
            print(f"  {sec}: {'OK' if v.get('ok', True) else 'REVISAR'}" + (" · " + ", ".join(f"{k}×{n}" for k, n in cuenta.items()) if cuenta else ""))
            for f in err[:5]: print("    ✗ " + (f.get("message", "")[:160])); problemas += 1
    except Exception as ex:
        print("  ⚠ no pude leer el resultado:", ex)
    # 3) fotogramas
    if not a.sin_fotogramas:
        try: plan = json.load(open(os.path.join(D, "plan.json"), encoding="utf-8"))
        except Exception: plan = {"duracion": 30, "eventos": []}
        ts = [0.3]
        g = plan.get("gancho")
        if g: ts.append(min(float(g.get("fin", 4)) - 0.5, 2.5))
        for e in plan.get("eventos", []): ts.append(float(e["t"]) + 0.9)
        if plan.get("cierre"): ts.append(float(plan["cierre"]["t"]) + 0.9)
        ts.append(float(plan["duracion"]) - 0.3)
        ts = sorted({round(t, 1) for t in ts if 0 <= t < float(plan["duracion"])})
        if len(ts) > 12: ts = ts[:1] + ts[1:-1][:: max(1, len(ts) // 10)] + ts[-1:]
        print(f"\n== Fotogramas ({len(ts)}) ==")
        sh(("npx --yes hyperframes snapshot . --at " + ",".join(map(str, ts))) if WIN else ["npx", "--yes", "hyperframes", "snapshot", ".", "--at", ",".join(map(str, ts))], cwd=D, salida=os.path.join(D, "snap.out"))
        base = os.path.join(D, ".hyperframes", "artifacts", "snapshots")
        if os.path.isdir(base):
            ult = sorted(glob.glob(os.path.join(base, "*")), key=os.path.getmtime)[-1]
            for p in sorted(glob.glob(os.path.join(ult, "frame-*.png"))): print("  " + p)
            print("  👀 MIRA estos fotogramas: rostro libre, nada cortado, nada pisado, texto legible.")
    print("\n" + ("✅ Revisión sin problemas graves." if problemas == 0 else f"⚠ {problemas} cosa(s) por corregir antes de renderizar."))
    sys.exit(0 if problemas == 0 else 1)

if __name__ == "__main__":
    main()
