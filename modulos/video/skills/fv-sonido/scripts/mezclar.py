#!/usr/bin/env python3
"""Mezcla la voz real + música (opcional) + efectos sincronizados. Música baja cuando hablas. Máster -14 LUFS, pico <= -1,5 dB.
   python mezclar.py config.json
   {
     "dur": 31.2,                              # duración total del video (s)
     "voz": "assets/voz_limpia.wav",           # la voz REAL (o el audio del video unido)
     "musica": "assets/musica.wav",            # opcional (null = sin música)
     "efectos_dir": "assets/sfx",              # carpeta con uiclick.wav, whoosh.wav, impact.wav, riser.wav, glitch.wav, chime.wav
     "eventos": "sfx_eventos.json",            # lo genera construir.py: [[tiempo, "uiclick.wav", -26], ...]  (o una lista directa)
     "salida": "assets/mix.wav",
     "pico_voz": -3, "pico_musica": -25,
     "riser": {"archivo": "riser.wav", "termina": 29.5, "pico": -24}     # opcional
   }
   Rutas relativas = relativas a la carpeta del JSON. Imprime el volumen final medido."""
import json, os, re, subprocess, sys

try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass

def pico(path):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", path, "-af", "volumedetect", "-f", "null", "-"], capture_output=True, text=True)
    m = re.search(r"max_volume:\s*(-?[\d.]+) dB", r.stderr)
    return float(m.group(1)) if m else -6.0

def dur(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path], capture_output=True, text=True)
    return float(r.stdout.strip())

def main():
    if len(sys.argv) < 2: print(__doc__); sys.exit(2)
    cp = os.path.abspath(sys.argv[1]); base = os.path.dirname(cp)
    cfg = json.load(open(cp, encoding="utf-8"))
    P = lambda p: p if os.path.isabs(p) else os.path.join(base, p)
    DUR = float(cfg["dur"]); voz = P(cfg["voz"]); mus = P(cfg["musica"]) if cfg.get("musica") else None
    sfx = P(cfg.get("efectos_dir", "assets/sfx")); salida = P(cfg.get("salida", "assets/mix.wav"))
    ev = cfg.get("eventos", [])
    if isinstance(ev, str): ev = json.load(open(P(ev), encoding="utf-8"))
    entradas, fl, etiquetas = [voz], [], ["[v]"]
    fl.append(f"[0:a]aresample=48000,aformat=channel_layouts=stereo,volume={cfg.get('pico_voz', -3) - pico(voz):.2f}dB,apad=whole_dur={DUR},atrim=0:{DUR},asplit=2[v][vsc]")
    idx = 1
    if mus:
        entradas.append(mus)
        fl.append(f"[{idx}:a]aresample=48000,aformat=channel_layouts=stereo,atrim=0:{DUR},volume={cfg.get('pico_musica', -25) - pico(mus):.2f}dB,afade=t=out:st={max(0, DUR - 2.4):.2f}:d=2.4[m0]")
        fl.append("[m0][vsc]sidechaincompress=threshold=0.015:ratio=10:attack=15:release=400:makeup=1[md]")
        etiquetas.append("[md]"); idx += 1
    rz = cfg.get("riser")
    if rz:
        rp = os.path.join(sfx, rz.get("archivo", "riser.wav"))
        if os.path.exists(rp):
            rd = dur(rp); fin = float(rz["termina"]); ini = max(0.2, fin - rd)
            entradas.append(rp)
            fl.append(f"[{idx}:a]aresample=48000,aformat=channel_layouts=stereo,atrim=0:{min(rd, fin - ini):.2f},volume={rz.get('pico', -24) - pico(rp):.2f}dB,adelay={int(ini * 1000)}|{int(ini * 1000)}[s{idx}]")
            etiquetas.append(f"[s{idx}]"); idx += 1
    cache = {}
    faltan = set()
    for t, nombre, pk in ev:
        p = os.path.join(sfx, nombre)
        if not os.path.exists(p): faltan.add(nombre); continue
        cache.setdefault(p, pico(p))
        ms = int(float(t) * 1000)
        entradas.append(p)
        fl.append(f"[{idx}:a]aresample=48000,aformat=channel_layouts=stereo,volume={pk - cache[p]:.2f}dB,adelay={ms}|{ms}[s{idx}]")
        etiquetas.append(f"[s{idx}]"); idx += 1
    if faltan: print("⚠ Faltan efectos en", sfx, ":", ", ".join(sorted(faltan)), "(ejecuta generar_sonidos.py efectos)")
    fl.append("".join(etiquetas) + f"amix=inputs={len(etiquetas)}:normalize=0:duration=longest,atrim=0:{DUR},loudnorm=I=-14:TP=-1.5:LRA=9[out]")
    cmd = ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error"]
    for e in entradas: cmd += ["-i", e]
    cmd += ["-filter_complex", ";".join(fl), "-map", "[out]", "-ar", "48000", "-ac", "2", salida]
    os.makedirs(os.path.dirname(salida), exist_ok=True)
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode: print("ERROR ffmpeg:", r.stderr[-1000:]); sys.exit(1)
    m = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", salida, "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True).stderr
    li = re.findall(r"I:\s+(-?[\d.]+) LUFS", m); tp = re.findall(r"Peak:\s+(-?[\d.]+) dBFS", m)
    print(f"Mezcla lista: {salida} · {len(etiquetas) - 1 - (1 if mus else 0)} efectos · {'con' if mus else 'sin'} música · {li[-1] if li else '?'} LUFS · pico {tp[-1] if tp else '?'} dBFS")

if __name__ == "__main__":
    main()
