#!/usr/bin/env python3
"""Detecta silencios en un video con voz y genera un montaje.json que solo conserva lo hablado (cortes limpios).
   python quitar_silencios.py video.mp4 [--umbral -35] [--min 0.45] [--margen 0.12] [--salida montaje.json] [--destino assets/base.mp4]
   Luego: python montar.py montaje.json"""
import argparse, json, os, re, subprocess, sys

try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("video")
    ap.add_argument("--umbral", type=float, default=-35.0, help="dB bajo los que se considera silencio")
    ap.add_argument("--min", type=float, default=0.45, help="duración mínima de silencio a cortar (s)")
    ap.add_argument("--margen", type=float, default=0.12, help="respiro que se deja a cada lado (s)")
    ap.add_argument("--salida", default="montaje.json"); ap.add_argument("--destino", default="assets/base.mp4")
    a = ap.parse_args()
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", a.video, "-af", f"silencedetect=noise={a.umbral}dB:d={a.min}", "-f", "null", "-"], capture_output=True, text=True)
    total = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", a.video], capture_output=True, text=True).stdout.strip())
    ini = [float(x) for x in re.findall(r"silence_start: (-?[\d.]+)", r.stderr)]
    fin = [float(x) for x in re.findall(r"silence_end: (-?[\d.]+)", r.stderr)]
    sil = list(zip(ini, fin + [total] * (len(ini) - len(fin))))
    keep, t = [], 0.0
    for s, e in sil:
        a0, b0 = t, max(t, s + a.margen)
        if b0 - a0 > 0.2: keep.append([round(a0, 3), round(min(b0, total), 3)])
        t = max(0.0, e - a.margen)
    if total - t > 0.2: keep.append([round(t, 3), round(total, 3)])
    keep = [k for k in keep if k[1] - k[0] > 0.2]
    ahorro = total - sum(b - a_ for a_, b in keep)
    m = {"salida": a.destino, "encuadre": "cubrir", "audio": {"fuente": "clips", "normalizar": False}, "xfade": 0.0, "cola": 1.3,
         "segmentos": [{"archivo": os.path.abspath(a.video), "ini": k[0], "fin": k[1]} for k in keep]}
    json.dump(m, open(a.salida, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{len(sil)} silencios · se conservan {len(keep)} tramos · se ahorran {ahorro:.1f} s de {total:.1f} s ({100 * ahorro / total:.0f} %)")
    print(f"Montaje guardado en {a.salida}. Ejecuta: python montar.py {a.salida}")
    if len(keep) > 40: print("⚠ Muchos cortes: sube --min o baja --umbral para un ritmo más natural.")

if __name__ == "__main__":
    main()
