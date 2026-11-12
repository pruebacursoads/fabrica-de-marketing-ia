#!/usr/bin/env python3
"""Genera efectos de sonido y música propios (síntesis con numpy; sin derechos de autor de terceros).
   python generar_sonidos.py efectos <carpeta>                       -> click, whoosh, impact, riser, glitch, chime (WAV 48 kHz)
   python generar_sonidos.py musica <calma|energia> <segundos> <salida.wav>
   La música es sencilla (acordes suaves + ritmo ligero): sirve de fondo bajo la voz. Si el alumno tiene música propia con
   licencia, es mejor usar esa. No hay forma de 'escuchar' desde aquí: ajustar el volumen en la mezcla según el oído."""
import sys, os, wave
import numpy as np

try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass

SR = 48000
rng = np.random.default_rng(7)

def guardar(path, x, pico=0.9):
    x = np.asarray(x, dtype=float)
    m = np.max(np.abs(x))
    if m > 0: x = x / m * pico
    st = np.stack([x, x], axis=1)
    pcm = (np.clip(st, -1, 1) * 32767).astype("<i2")
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with wave.open(path, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())

def lp_variable(x, alpha):
    y = np.zeros_like(x); s = 0.0
    for i in range(len(x)):
        s += alpha[i] * (x[i] - s); y[i] = s
    return y

def click():
    t = np.arange(int(0.07 * SR)) / SR
    return np.sin(2 * np.pi * 2400 * t) * np.exp(-t * 95) + 0.5 * np.sin(2 * np.pi * 900 * t) * np.exp(-t * 60)

def whoosh():
    n = int(0.75 * SR); u = np.linspace(0, 1, n)
    y = lp_variable(rng.standard_normal(n), 0.02 + 0.5 * np.sin(np.pi * u) ** 2)
    return y * np.sin(np.pi * u) ** 1.5

def impact():
    n = int(1.0 * SR); t = np.arange(n) / SR
    f = 40 + 110 * np.exp(-t * 18)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 5.5) + 0.6 * rng.standard_normal(n) * np.exp(-t * 30)

def riser(dur=2.8):
    n = int(dur * SR); u = np.linspace(0, 1, n); t = u * dur
    ruido = lp_variable(rng.standard_normal(n), 0.03 + 0.45 * u ** 2)
    tono = np.sin(2 * np.pi * np.cumsum(200 + 1600 * u ** 2) / SR)
    return (0.8 * ruido + 0.35 * tono) * (u ** 1.6) * (1 - np.clip((u - 0.97) / 0.03, 0, 1))

def glitch():
    out = np.zeros(int(0.3 * SR)); pos = 0
    while pos < len(out) - 800:
        L = int(rng.uniform(0.012, 0.04) * SR)
        seg = np.sign(rng.standard_normal(L)) * rng.uniform(0.3, 1.0) if rng.random() < 0.5 else np.round(rng.standard_normal(L) * 3) / 3
        out[pos:pos + L] += seg[:len(out) - pos]
        pos += L + int(rng.uniform(0.005, 0.03) * SR)
    return out

def chime():
    n = int(0.6 * SR); t = np.arange(n) / SR
    a = np.sin(2 * np.pi * 880 * t) * np.exp(-t * 9)
    b = np.zeros(n); k = int(0.09 * SR)
    b[k:] = (np.sin(2 * np.pi * 1320 * t[:n - k]) * np.exp(-t[:n - k] * 8))
    return a + b

def efectos(carpeta):
    for nombre, fn in (("uiclick", click), ("whoosh", whoosh), ("impact", impact), ("riser", riser), ("glitch", glitch), ("chime", chime)):
        guardar(os.path.join(carpeta, nombre + ".wav"), fn())
        print(f"  {nombre}.wav")
    print(f"Efectos propios guardados en {carpeta}")

# ---------- música ----------
NOTAS = {"A2": 110.0, "C3": 130.81, "E3": 164.81, "G3": 196.0, "F2": 87.31, "A3": 220.0, "C4": 261.63, "E4": 329.63, "G4": 392.0,
         "D3": 146.83, "B2": 123.47, "F3": 174.61, "B3": 246.94, "D4": 293.66}

def env_nota(n, a=0.12, r=0.25):
    t = np.arange(n) / SR; e = np.ones(n)
    e *= np.clip(t / max(a, 1e-3), 0, 1); e *= np.clip((n / SR - t) / max(r, 1e-3), 0, 1)
    return e

def musica(mood, dur, salida):
    bpm = 72 if mood == "calma" else 108
    beat = 60 / bpm; barra = 4 * beat; n = int(dur * SR); y = np.zeros(n + int((2 * barra + 2.0) * SR))
    prog = [["A2", "E3", "G3", "C4"], ["F2", "A2", "C3", "E3"], ["C3", "G3", "E4", "G4"], ["G3", "D4", "B3", "F3"]] if mood == "calma" else \
           [["A2", "E3", "A3", "C4"], ["F2", "C3", "F3", "A3"], ["C3", "G3", "C4", "E4"], ["G3", "D4", "G4", "B3"]]
    nb = int(np.ceil(dur / barra)) + 1
    for b in range(nb):
        acorde = prog[b % 4]; i0 = int(b * barra * SR); L = int(barra * SR)
        t = np.arange(L) / SR; pad = np.zeros(L)
        for nota in acorde:
            f = NOTAS[nota]
            pad += np.sin(2 * np.pi * f * t) + 0.4 * np.sin(2 * np.pi * f * 2.003 * t) + 0.25 * np.sin(2 * np.pi * f * 0.997 * t)
        pad *= env_nota(L, 0.35 if mood == "calma" else 0.08, 0.4) * (0.10 if mood == "calma" else 0.07)
        y[i0:i0 + L] += pad
        # arpegio suave
        paso = beat / 2
        for k in range(8):
            f = NOTAS[acorde[(k * 3 + b) % 4]] * (2 if mood == "calma" else 1)
            j = i0 + int(k * paso * SR); m = int(0.5 * SR); tt = np.arange(m) / SR
            y[j:j + m] += (np.sin(2 * np.pi * f * tt) + 0.3 * np.sin(2 * np.pi * f * 2 * tt)) * np.exp(-tt * 6) * (0.06 if mood == "calma" else 0.05)
        # bajo y percusión suaves
        for k in range(4):
            j = i0 + int(k * beat * SR); m = int(0.25 * SR); tt = np.arange(m) / SR
            if mood == "energia" or k in (0, 2):
                y[j:j + m] += np.sin(2 * np.pi * np.cumsum(55 + 70 * np.exp(-tt * 30)) / SR) * np.exp(-tt * 14) * (0.35 if mood == "energia" else 0.22)
            h = j + int(beat / 2 * SR); mm = int(0.05 * SR)
            ruido = rng.standard_normal(mm); ruido = ruido - lp_variable(ruido, np.full(mm, 0.2))
            y[h:h + mm] += ruido * np.exp(-np.arange(mm) / SR * 90) * 0.05
        if mood == "energia":
            j = i0; m = int(barra * SR); tt = np.arange(m) / SR
            y[j:j + m] += np.sin(2 * np.pi * NOTAS[acorde[0]] / 2 * tt) * 0.18
    y = y[:n]
    y = lp_variable(y, np.full(n, 0.45 if mood == "calma" else 0.7))        # suaviza (más cálido)
    y += rng.standard_normal(n) * 0.0015                                  # aire muy ligero
    y *= np.clip(np.arange(n) / (1.0 * SR), 0, 1)                         # entrada suave 1 s
    guardar(salida, y, pico=0.6)
    print(f"Música '{mood}' de {dur:.0f} s ({bpm} BPM) guardada en {salida}")

if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "efectos": efectos(sys.argv[2])
    elif len(sys.argv) >= 5 and sys.argv[1] == "musica": musica(sys.argv[2], float(sys.argv[3]), sys.argv[4])
    else: print(__doc__); sys.exit(2)
