#!/usr/bin/env python3
"""Limpia la voz real del alumno (ruido de sala, graves, claridad, volumen parejo) -> WAV 48 kHz.
   python limpiar_voz.py entrada.(mp4|wav|mp3...) salida.wav [--nivel suave|normal|fuerte]
   suave: casi sin tocar · normal: ruido de sala + claridad (por defecto) · fuerte: oficinas, eco o micrófono de celular lejos."""
import argparse, re, subprocess, sys

try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass

CADENAS = {
    "suave": "highpass=f=70,afftdn=nr=8:nf=-30,acompressor=threshold=-24dB:ratio=2:attack=10:release=200:makeup=2,aresample=48000",
    "normal": "highpass=f=90,afftdn=nr=14:nf=-32,equalizer=f=250:t=q:w=1:g=-2,equalizer=f=3200:t=q:w=1:g=2.5,deesser=i=0.3,acompressor=threshold=-22dB:ratio=3:attack=8:release=160:makeup=3,aresample=48000",
    "fuerte": "highpass=f=100,afftdn=nr=22:nf=-28,equalizer=f=250:t=q:w=1:g=-3,equalizer=f=3000:t=q:w=1:g=3,deesser=i=0.4,acompressor=threshold=-24dB:ratio=4:attack=6:release=140:makeup=4,aresample=48000",
}

def medir(p):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", p, "-vn", "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True)
    i = re.findall(r"I:\s+(-?[\d.]+) LUFS", r.stderr); pk = re.findall(r"Peak:\s+(-?[\d.]+) dBFS", r.stderr)
    return (i[-1] if i else "?"), (pk[-1] if pk else "?")

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("entrada"); ap.add_argument("salida"); ap.add_argument("--nivel", default="normal", choices=list(CADENAS))
    a = ap.parse_args()
    antes = medir(a.entrada)
    r = subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", a.entrada, "-vn", "-af", CADENAS[a.nivel], "-ac", "2", a.salida], capture_output=True, text=True)
    if r.returncode: print("ERROR:", r.stderr[-800:]); sys.exit(1)
    despues = medir(a.salida)
    print(f"Voz limpiada ({a.nivel}) -> {a.salida}")
    print(f"  antes: {antes[0]} LUFS, pico {antes[1]} dB · después: {despues[0]} LUFS, pico {despues[1]} dB")
    print("  (la mezcla final se normaliza a -14 LUFS; esto solo limpia)")

if __name__ == "__main__":
    main()
