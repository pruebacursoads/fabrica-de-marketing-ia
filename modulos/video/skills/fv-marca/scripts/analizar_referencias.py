#!/usr/bin/env python3
"""Analiza imágenes o videos de referencia del alumno: paleta de colores dominante y, en videos, ritmo de cortes.
   python analizar_referencias.py ref1.png ref2.mp4 ... [--salida referencias.json]
   Usa ffmpeg y numpy (no necesita otras librerías). Claude además debe MIRAR los fotogramas para describir el estilo
   (tipografía, posición de subtítulos, tipo de gráficos); aquí solo sale lo medible."""
import argparse, json, os, re, subprocess, sys, tempfile
import numpy as np

try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass

def duracion(p):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p], capture_output=True, text=True)
    try: return float(r.stdout.strip())
    except Exception: return 0.0

def pixeles(p, es_video):
    """Devuelve un arreglo (N,3) de píxeles RGB de fotogramas reducidos a 48x48."""
    vf = "fps=1/2,scale=48:48" if es_video else "scale=48:48"
    cmd = ["ffmpeg", "-v", "error", "-i", p, "-vf", vf, "-frames:v", "12" if es_video else "1", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"]
    r = subprocess.run(cmd, capture_output=True)
    d = np.frombuffer(r.stdout, dtype=np.uint8)
    return d[: (len(d) // 3) * 3].reshape(-1, 3).astype(float)

def kmeans(x, k=6, it=20, seed=1):
    rng = np.random.default_rng(seed)
    c = x[rng.choice(len(x), k, replace=False)]
    for _ in range(it):
        d = ((x[:, None, :] - c[None, :, :]) ** 2).sum(2)
        lab = d.argmin(1)
        for j in range(k):
            if (lab == j).any(): c[j] = x[lab == j].mean(0)
    return c, np.bincount(lab, minlength=k)

def hexa(c): return "#%02X%02X%02X" % tuple(int(round(v)) for v in c)
def sat(c):
    mx, mn = max(c), min(c)
    return 0 if mx == 0 else (mx - mn) / mx
def luma(c): return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]

def cortes_por_minuto(p):
    d = duracion(p)
    r = subprocess.run(["ffmpeg", "-v", "info", "-i", p, "-vf", "select='gt(scene,0.35)',showinfo", "-f", "null", "-"], capture_output=True, text=True)
    n = len(re.findall(r"pts_time:", r.stderr))
    return (n / d * 60 if d else 0), n, d

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("archivos", nargs="+"); ap.add_argument("--salida", default=None)
    a = ap.parse_args()
    todo, detalle = [], []
    for p in a.archivos:
        if not os.path.exists(p): print(f"⚠ No existe: {p}"); continue
        video = os.path.splitext(p)[1].lower() in (".mp4", ".mov", ".mkv", ".webm", ".avi", ".m4v")
        px = pixeles(p, video)
        if len(px) == 0: print(f"⚠ No pude leer: {p}"); continue
        todo.append(px)
        item = {"archivo": os.path.basename(p), "tipo": "video" if video else "imagen"}
        if video:
            cpm, n, d = cortes_por_minuto(p)
            item.update({"duracion_s": round(d, 1), "cortes": n, "cortes_por_minuto": round(cpm, 1),
                         "ritmo": "muy rápido" if cpm > 30 else "rápido" if cpm > 15 else "medio" if cpm > 6 else "pausado"})
        detalle.append(item)
    if not todo: print("No se pudo analizar nada."); sys.exit(1)
    x = np.vstack(todo)
    if len(x) > 6000: x = x[np.random.default_rng(0).choice(len(x), 6000, replace=False)]
    c, n = kmeans(x, 6)
    orden = np.argsort(-n)
    pal = [{"hex": hexa(c[i]), "porcentaje": round(100 * n[i] / n.sum(), 1)} for i in orden]
    cols = [c[i] for i in orden]
    oscuro = min(cols, key=luma); claro = max(cols, key=luma)
    vivo = max(cols, key=lambda v: sat(v) * (0.4 + luma(v) / 255))
    sugerencia = {"fondo": hexa(oscuro) if luma(oscuro) < 90 else hexa(claro), "acento": hexa(vivo),
                  "texto": "#FFFFFF" if luma(oscuro) < 90 else "#0F172A"}
    salida = {"paleta": pal, "sugerencia": sugerencia, "referencias": detalle}
    print("Paleta dominante (de más a menos presente):")
    for p_ in pal: print(f"  {p_['hex']}  {p_['porcentaje']}%")
    print(f"Sugerencia: fondo {sugerencia['fondo']} · acento {sugerencia['acento']} · texto {sugerencia['texto']}")
    for d_ in detalle:
        if d_["tipo"] == "video": print(f"  {d_['archivo']}: {d_['cortes_por_minuto']} cortes/min ({d_['ritmo']})")
    if a.salida:
        os.makedirs(os.path.dirname(os.path.abspath(a.salida)), exist_ok=True)
        json.dump(salida, open(a.salida, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(f"Guardado en {a.salida}")

if __name__ == "__main__":
    main()
