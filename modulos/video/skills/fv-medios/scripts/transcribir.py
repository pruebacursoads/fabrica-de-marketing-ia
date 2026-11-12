#!/usr/bin/env python3
"""Transcribe la voz con el segundo exacto de cada palabra (Whisper) -> words.json, transcripcion.txt, frases.txt
   python transcribir.py audio_o_video.ext [--salida .] [--modelo auto|base|small|medium] [--idioma es] [--prompt "marcas, siglas, nombres"]
   El prompt con el vocabulario del alumno mejora mucho nombres propios y siglas. `medium` corrige más palabras pero gasta ~4 GB de RAM."""
import argparse, json, os, subprocess, sys, tempfile

try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass

def ram_total_gb():
    try:
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "fv-diagnostico", "scripts"))
        import diagnostico
        return diagnostico.memoria()[0]
    except Exception:
        return 8.0

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("entrada")
    ap.add_argument("--salida", default="."); ap.add_argument("--modelo", default="auto"); ap.add_argument("--idioma", default="es"); ap.add_argument("--prompt", default="")
    a = ap.parse_args()
    modelo = a.modelo
    if modelo == "auto":
        gb = ram_total_gb(); modelo = "base" if gb < 8 else "small" if gb < 12 else "medium"
        print(f"Modelo automático según tu memoria ({gb:.1f} GB): {modelo}")
    wav = os.path.join(tempfile.gettempdir(), "fv_audio16k.wav")
    subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", a.entrada, "-vn", "-ac", "1", "-ar", "16000", wav], check=True)
    import whisper
    m = whisper.load_model(modelo)
    r = m.transcribe(wav, language=a.idioma, word_timestamps=True, initial_prompt=a.prompt or None)
    palabras = []
    for s in r["segments"]:
        for w in s["words"]:
            t = w["word"].strip()
            if t.startswith(".") and palabras: palabras[-1]["w"] += t; palabras[-1]["e"] = round(w["end"], 2)   # flow .google .com -> flow.google.com
            else: palabras.append({"w": t, "s": round(w["start"], 2), "e": round(w["end"], 2)})
    os.makedirs(a.salida, exist_ok=True)
    json.dump(palabras, open(os.path.join(a.salida, "words.json"), "w", encoding="utf-8"), ensure_ascii=False)
    open(os.path.join(a.salida, "transcripcion.txt"), "w", encoding="utf-8").write(r["text"].strip() + "\n")
    lineas, cur, t0 = [], [], None
    for w in palabras:
        if t0 is None: t0 = w["s"]
        cur.append(w["w"])
        if w["w"][-1:] in ".?!," and len(cur) >= 3:
            lineas.append(f"{t0:6.1f} - {w['e']:6.1f}  {' '.join(cur)}"); cur, t0 = [], None
    if cur: lineas.append(f"{t0:6.1f} - {palabras[-1]['e']:6.1f}  {' '.join(cur)}")
    open(os.path.join(a.salida, "frases.txt"), "w", encoding="utf-8").write("\n".join(lineas) + "\n")
    print(f"{len(palabras)} palabras · fin {palabras[-1]['e'] if palabras else 0} s · modelo {modelo}")
    print(f"Guardado: {os.path.join(a.salida, 'words.json')}, transcripcion.txt, frases.txt")
    print("Revisa la transcripción: confirma con el alumno las palabras dudosas (siglas, nombres, cifras).")

if __name__ == "__main__":
    main()
