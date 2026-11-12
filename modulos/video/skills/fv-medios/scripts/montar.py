#!/usr/bin/env python3
"""Monta el video base a partir de un plan de montaje (clips + voz real). Salida: 1080x1920, 30 fps, listo para la edición.
   python montar.py montaje.json
   montaje.json
   {
     "salida": "assets/base.mp4", "ancho": 1080, "alto": 1920, "fps": 30,
     "encuadre": "cubrir" | "contener-difuminado",        # cubrir recorta; contener-difuminado pone el clip entero sobre un fondo desenfocado
     "audio": {"fuente": "clips" | "ruta/a/voz.wav" | null, "normalizar": true},
     "xfade": 0.0,                                         # segundos de fundido entre clips (0 = corte directo)
     "cola": 1.3,                                          # segundos que se congela el último fotograma (espacio para el cierre)
     "segmentos": [ {"archivo": "tomas/a.mp4", "ini": 0, "fin": 5.2}, {"archivo": "tomas/b.mp4", "ini": 1, "fin": 4} ]
   }
   Rutas relativas = relativas a la carpeta del JSON. Con voz separada, el video se alarga/recorta para durar lo que la voz + la cola."""
import json, os, subprocess, sys, tempfile, shutil

try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass

def sh(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print("ERROR ffmpeg:", " ".join(cmd[:6]), "...\n", r.stderr[-1200:]); sys.exit(1)
    return r

def dur(p):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p], capture_output=True, text=True)
    try: return float(r.stdout.strip())
    except Exception: return 0.0

def tiene_audio(p):
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries", "stream=index", "-of", "csv=p=0", p], capture_output=True, text=True)
    return bool(r.stdout.strip())

def filtro_video(cfg):
    W, H, fps = cfg["ancho"], cfg["alto"], cfg["fps"]
    if cfg["encuadre"] == "contener-difuminado":
        return (f"split[a][b];[a]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},boxblur=24:2[bg];"
                f"[b]scale={W}:{H}:force_original_aspect_ratio=decrease[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2,fps={fps},setsar=1,format=yuv420p")
    return f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={fps},setsar=1,format=yuv420p"

def main():
    if len(sys.argv) < 2: print(__doc__); sys.exit(2)
    ruta = os.path.abspath(sys.argv[1]); base = os.path.dirname(ruta)
    cfg = json.load(open(ruta, encoding="utf-8"))
    P = lambda p: p if os.path.isabs(p) else os.path.join(base, p)
    cfg.setdefault("ancho", 1080); cfg.setdefault("alto", 1920); cfg.setdefault("fps", 30); cfg.setdefault("encuadre", "cubrir")
    cfg.setdefault("xfade", 0.0); cfg.setdefault("cola", 1.3)
    au = cfg.get("audio") or {"fuente": None}
    fuente = au.get("fuente"); usa_clips = fuente == "clips"; voz = P(fuente) if fuente and fuente != "clips" else None
    salida = P(cfg.get("salida", "assets/base.mp4")); os.makedirs(os.path.dirname(salida), exist_ok=True)
    tmp = tempfile.mkdtemp(prefix="fv_montaje_")
    temps = []
    try:
        for i, s in enumerate(cfg["segmentos"]):
            f = P(s["archivo"])
            if not os.path.exists(f): print(f"No existe el clip: {f}"); sys.exit(1)
            ini = float(s.get("ini", 0)); fin = s.get("fin"); d = (float(fin) - ini) if fin is not None else dur(f) - ini
            out = os.path.join(tmp, f"s{i:03d}.mp4")
            cmd = ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-ss", f"{ini:.3f}", "-i", f]
            hay_a = tiene_audio(f)
            if usa_clips and not hay_a: cmd += ["-f", "lavfi", "-t", f"{d:.3f}", "-i", "anullsrc=r=48000:cl=stereo"]
            cmd += ["-t", f"{d:.3f}"]
            vf = filtro_video(cfg)
            if "[" in vf: cmd += ["-filter_complex", "[0:v]" + vf + "[v]", "-map", "[v]"]
            else: cmd += ["-vf", vf, "-map", "0:v"]
            if usa_clips:
                cmd += ["-map", "0:a" if hay_a else "1:a", "-af", "aresample=48000,aformat=channel_layouts=stereo" + (",loudnorm=I=-16:TP=-1.5:LRA=11" if au.get("normalizar", True) else ""), "-c:a", "aac", "-b:a", "160k"]
            else: cmd += ["-an"]
            cmd += ["-c:v", "libx264", "-preset", "veryfast", "-crf", "17", out]
            sh(cmd); temps.append((out, d)); print(f"  clip {i + 1}/{len(cfg['segmentos'])}: {os.path.basename(f)} {ini:.1f}-{ini + d:.1f} s")
        xf = float(cfg["xfade"])
        sin_cola = os.path.join(tmp, "unido.mp4")
        if xf <= 0 or len(temps) == 1:
            lista = os.path.join(tmp, "lista.txt")
            open(lista, "w", encoding="utf-8").write("".join(f"file '{t.replace(chr(92), '/')}'\n" for t, _ in temps))
            sh(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lista, "-c", "copy", sin_cola])
        else:
            cmd = ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error"]
            for t, _ in temps: cmd += ["-i", t]
            fc, prev, acc = [], "[0:v]", temps[0][1]
            aprev = "[0:a]"
            for i in range(1, len(temps)):
                off = acc - xf
                fc.append(f"{prev}[{i}:v]xfade=transition=fade:duration={xf}:offset={off:.3f}[v{i}]"); prev = f"[v{i}]"
                if usa_clips: fc.append(f"{aprev}[{i}:a]acrossfade=d={xf}[a{i}]"); aprev = f"[a{i}]"
                acc += temps[i][1] - xf
            cmd += ["-filter_complex", ";".join(fc), "-map", prev]
            if usa_clips: cmd += ["-map", aprev, "-c:a", "aac", "-b:a", "160k"]
            cmd += ["-c:v", "libx264", "-preset", "veryfast", "-crf", "17", sin_cola]
            sh(cmd)
        total_v = dur(sin_cola)
        # voz real separada: la voz manda la duración
        if voz:
            dv = dur(voz); objetivo = dv + float(cfg["cola"])
            extra = max(0.0, objetivo - total_v)
            vf = f"tpad=stop_mode=clone:stop_duration={extra:.3f}" if extra > 0.01 else "null"
            cmd = ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", sin_cola, "-i", voz, "-vf", vf, "-map", "0:v", "-map", "1:a",
                   "-af", "aresample=48000,apad", "-t", f"{objetivo:.3f}", "-c:v", "libx264", "-preset", "veryfast", "-crf", "17", "-c:a", "aac", "-b:a", "192k", salida]
            sh(cmd)
            print(f"Voz {dv:.1f} s + cola {cfg['cola']} s = {objetivo:.1f} s (los clips sumaban {total_v:.1f} s" + (f"; se extendió el último fotograma {extra:.1f} s" if extra > 0.01 else "; se recortó al largo de la voz") + ")")
        else:
            cola = float(cfg["cola"])
            if cola > 0:
                cmd = ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", sin_cola, "-vf", f"tpad=stop_mode=clone:stop_duration={cola}", "-c:v", "libx264", "-preset", "veryfast", "-crf", "17"]
                cmd += (["-af", f"apad=pad_dur={cola}", "-c:a", "aac", "-b:a", "192k"] if usa_clips else ["-an"]) + [salida]
                sh(cmd)
            else: shutil.copy(sin_cola, salida)
        print(f"Listo: {salida} · {dur(salida):.1f} s")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

if __name__ == "__main__":
    main()
