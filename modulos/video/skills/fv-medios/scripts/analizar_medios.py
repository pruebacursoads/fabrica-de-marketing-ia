#!/usr/bin/env python3
"""Analiza los archivos que entrega el alumno (clips de video, voz suelta, imágenes) y propone cómo unirlos.
   python analizar_medios.py <carpeta_o_archivos...> [--salida trabajo]
   Genera trabajo/medios.json y una hoja de fotogramas por clip (trabajo/hojas/*.jpg) para que Claude los mire."""
import argparse, json, os, re, subprocess, sys

try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass

VIDEO = {".mp4", ".mov", ".mkv", ".webm", ".avi", ".m4v"}
AUDIO = {".wav", ".mp3", ".m4a", ".aac", ".ogg", ".flac", ".opus"}
IMG = {".png", ".jpg", ".jpeg", ".webp"}

def probe(p):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", p], capture_output=True, text=True)
    try: return json.loads(r.stdout)
    except Exception: return None

def lufs(p):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", p, "-vn", "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True)
    i = re.findall(r"I:\s+(-?[\d.]+) LUFS", r.stderr); pk = re.findall(r"Peak:\s+(-?[\d.]+) dBFS", r.stderr)
    return (float(i[-1]) if i else None), (float(pk[-1]) if pk else None)

def hoja(p, dur, destino, n=6):
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    fps = max(n / max(dur, 0.5), 0.05)
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", p, "-vf", f"fps={fps:.4f},scale=270:-1,tile={n}x1", "-frames:v", "1", "-q:v", "4", destino], capture_output=True)

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("rutas", nargs="+"); ap.add_argument("--salida", default="trabajo")
    a = ap.parse_args()
    archivos = []
    for r in a.rutas:
        if os.path.isdir(r):
            for f in sorted(os.listdir(r)):
                if os.path.splitext(f)[1].lower() in VIDEO | AUDIO | IMG: archivos.append(os.path.join(r, f))
        elif os.path.exists(r): archivos.append(r)
        else: print(f"⚠ No existe: {r}")
    if not archivos: print("No encontré archivos de video, audio o imagen."); sys.exit(1)
    medios = []
    for p in archivos:
        ext = os.path.splitext(p)[1].lower()
        info = probe(p)
        if not info: print(f"⚠ No pude leer {p}"); continue
        v = next((s for s in info["streams"] if s["codec_type"] == "video"), None)
        au = next((s for s in info["streams"] if s["codec_type"] == "audio"), None)
        dur = float(info["format"].get("duration", 0) or 0)
        m = {"archivo": p, "nombre": os.path.basename(p), "duracion_s": round(dur, 2), "tiene_audio": bool(au), "tamano_mb": round(os.path.getsize(p) / 2**20, 1)}
        if ext in IMG: m["tipo"] = "imagen"
        elif v and ext in VIDEO and not (v.get("codec_name") in ("mjpeg", "png") and dur < 0.1):
            m["tipo"] = "video"
            w, h = int(v["width"]), int(v["height"])
            rot = 0
            for sd in v.get("side_data_list", []) or []:
                if "rotation" in sd: rot = int(sd["rotation"])
            if rot in (90, -90, 270, -270): w, h = h, w
            fr = v.get("avg_frame_rate", "0/1").split("/")
            fps = float(fr[0]) / float(fr[1]) if len(fr) == 2 and float(fr[1]) else 0
            m.update({"ancho": w, "alto": h, "fps": round(fps, 2), "orientacion": "vertical" if h > w else "horizontal" if w > h else "cuadrado", "rotacion": rot})
            if au:
                L, pk = lufs(p); m["lufs"] = L; m["pico_db"] = pk
            hoja(p, dur, os.path.join(a.salida, "hojas", os.path.splitext(m["nombre"])[0] + ".jpg"))
        elif au: m["tipo"] = "audio"; L, pk = lufs(p); m["lufs"] = L; m["pico_db"] = pk
        else: m["tipo"] = "desconocido"
        medios.append(m)
    os.makedirs(a.salida, exist_ok=True)
    videos = [m for m in medios if m["tipo"] == "video"]; audios = [m for m in medios if m["tipo"] == "audio"]
    avisos = []
    if len({m["orientacion"] for m in videos}) > 1: avisos.append("Hay clips verticales y horizontales mezclados: al unirlos hay que elegir 'cubrir' (recorta) o 'contener-difuminado' (fondo desenfocado).")
    fps_set = {round(m["fps"]) for m in videos if m.get("fps")}
    if len(fps_set) > 1: avisos.append(f"Los clips tienen distintos fotogramas por segundo ({sorted(fps_set)}): se igualan a 30 al unirlos.")
    if any(m.get("lufs") is not None and m["lufs"] < -23 for m in videos + audios): avisos.append("Algún audio está muy bajo (menos de -23 LUFS): se subirá al normalizar.")
    if any(m.get("pico_db") is not None and m["pico_db"] > -1 for m in videos + audios): avisos.append("Algún audio llega al límite (puede estar saturado): conviene revisarlo.")
    if any(m.get("ancho") and m["ancho"] < 720 for m in videos): avisos.append("Algún clip tiene menos de 720 px de ancho: se verá blando al llenar 1080x1920; evita hacer zoom fuerte.")
    if len(audios) == 1 and videos: ruta = "VOZ SEPARADA: la voz del alumno es el audio principal y los clips se usan como imagen (se mutean y se montan sobre la voz)."
    elif len(audios) == 0 and len(videos) == 1: ruta = "UN SOLO VIDEO CON AUDIO: se edita directamente (se pueden quitar silencios)."
    elif len(audios) == 0 and len(videos) > 1: ruta = "VARIOS CLIPS CON AUDIO PROPIO: se unen en el orden acordado y se igualan volumen y formato."
    elif len(audios) > 1: ruta = "VARIOS AUDIOS: hay que preguntar cuál es la voz principal y cuál (si alguno) es música."
    else: ruta = "Revisar manualmente."
    out = {"ruta_sugerida": ruta, "avisos": avisos, "medios": medios}
    json.dump(out, open(os.path.join(a.salida, "medios.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"\n{len(medios)} archivos analizados · {len(videos)} videos · {len(audios)} audios")
    for m in medios:
        if m["tipo"] == "video": print(f"  🎬 {m['nombre']}: {m['ancho']}x{m['alto']} {m['orientacion']} · {m['fps']} fps · {m['duracion_s']} s · audio: {'sí' if m['tiene_audio'] else 'no'}" + (f" · {m['lufs']} LUFS" if m.get('lufs') is not None else ""))
        elif m["tipo"] == "audio": print(f"  🎙 {m['nombre']}: {m['duracion_s']} s · {m.get('lufs')} LUFS")
        else: print(f"  📄 {m['nombre']} ({m['tipo']})")
    print("\nRuta sugerida:", ruta)
    for v_ in avisos: print("  ⚠ " + v_)
    print(f"\nHojas de fotogramas en {os.path.join(a.salida, 'hojas')} (mírelas para entender cada clip)")

if __name__ == "__main__":
    main()
