#!/usr/bin/env python3
"""Renderiza el video final con HyperFrames, eligiendo procesos según la memoria libre, y verifica el MP4.
   python render.py <proyecto> [--nombre FINAL.mp4] [--borrador] [--procesos N]
   --borrador   calidad rápida para probar (más liviana). Sin esa opción: calidad de entrega.
   Al final mide duración, tamaño, volumen (LUFS) y crea una versión ligera de 720p para ver rápido."""
import argparse, os, re, subprocess, sys, time

try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass

AQUI = os.path.dirname(os.path.abspath(__file__))
WIN = os.name == "nt"

def libre_gb():
    try:
        sys.path.insert(0, os.path.join(AQUI, "..", "..", "fv-diagnostico", "scripts"))
        import diagnostico
        return diagnostico.memoria()[1]
    except Exception:
        return 4.0

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("proyecto"); ap.add_argument("--nombre", default="FINAL.mp4")
    ap.add_argument("--borrador", action="store_true"); ap.add_argument("--procesos", type=int)
    a = ap.parse_args(); D = os.path.abspath(a.proyecto)
    if not os.path.exists(os.path.join(D, "index.html")): print("No existe index.html."); sys.exit(1)
    libre = libre_gb()
    if libre < 1.0:
        print(f"⛔ Solo hay {libre:.1f} GB libres: el render se cerraría solo. Cierra Chrome y otros programas (Claude y la terminal no) y vuelve a intentar."); sys.exit(2)
    n = a.procesos or (1 if libre < 4 else 2)
    os.makedirs(os.path.join(D, "renders"), exist_ok=True)
    salida = os.path.join("renders", a.nombre)
    cmd = f'npx --yes hyperframes render . -o "{salida}" --workers {n}' + (" -q draft" if a.borrador else "")
    print(f"Memoria libre {libre:.1f} GB -> {n} proceso(s) de render" + (" · borrador" if a.borrador else "") + ". Puede tardar varios minutos; no cierres esta ventana.")
    t0 = time.time()
    with open(os.path.join(D, "render.out"), "w", encoding="utf-8", errors="replace") as f, open(os.path.join(D, "render.err"), "w", encoding="utf-8", errors="replace") as e:
        r = subprocess.run(cmd if WIN else cmd.split(), cwd=D, stdout=f, stderr=e, shell=WIN)
    mp4 = os.path.join(D, salida)
    if r.returncode != 0 or not os.path.exists(mp4):
        cola = open(os.path.join(D, "render.out"), encoding="utf-8", errors="replace").read()[-600:]
        print("✗ El render falló. Últimas líneas:\n" + cola + "\nSi dice memoria o se cerró solo: cierra programas y repite con --procesos 1."); sys.exit(1)
    seg = time.time() - t0
    info = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "stream=codec_type,width,height,r_frame_rate:format=duration", "-of", "default=nw=1", mp4], capture_output=True, text=True).stdout
    dur = re.search(r"duration=([\d.]+)", info); w = re.search(r"width=(\d+)", info); h = re.search(r"height=(\d+)", info)
    m = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", mp4, "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True).stderr
    li = re.findall(r"I:\s+(-?[\d.]+) LUFS", m); tp = re.findall(r"Peak:\s+(-?[\d.]+) dBFS", m)
    print(f"\n✅ Render terminado en {seg / 60:.1f} min: {mp4}")
    print(f"   {w.group(1) if w else '?'}x{h.group(1) if h else '?'} · {float(dur.group(1)):.1f} s · {os.path.getsize(mp4) / 2**20:.1f} MB · {li[-1] if li else '?'} LUFS · pico {tp[-1] if tp else '?'} dBFS")
    prev = os.path.join(D, "renders", "VER-AQUI-" + os.path.splitext(a.nombre)[0] + ".mp4")
    subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", mp4, "-vf", "scale=720:1280", "-c:v", "libx264", "-crf", "24", "-preset", "fast", "-pix_fmt", "yuv420p", "-movflags", "+faststart", "-c:a", "aac", "-b:a", "128k", prev])
    if os.path.exists(prev): print(f"   Versión ligera (720p, {os.path.getsize(prev) / 2**20:.1f} MB) para ver rápido: {prev}")
    print("   Escúchalo completo y dame tus notas con el segundo exacto (por ejemplo: «en 0:12 el texto tapa»).")

if __name__ == "__main__":
    main()
