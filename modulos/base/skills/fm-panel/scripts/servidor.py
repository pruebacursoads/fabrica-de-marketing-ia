#!/usr/bin/env python3
"""Servidor local del Panel (solo librería estándar, solo tu computadora).

Qué hace:
  - Abre el Panel en http://localhost:8765/Panel/index.html (cambia de puerto si está ocupado).
  - Deja que arrastres tus imágenes, clips y fotos a la pestaña "Guía de generación": se guardan solas
    en la carpeta correcta de tu computadora, con el nombre correcto (clip-01.mp4, REF-01.png...).
  - Vigila las carpetas: si copias un archivo a mano, el Panel también lo detecta.

Uso:   python Panel/servidor.py          (o doble clic en ABRIR-PANEL.bat)
Cierra la ventana o pulsa Ctrl+C para detenerlo.

Seguridad: solo escucha en 127.0.0.1 (nadie más en tu red lo ve), solo acepta subidas con la cabecera propia
del Panel, solo escribe dentro de Entregables/ y Mi negocio/, solo tipos de archivo conocidos (imagen, video,
audio, pdf, texto) y como máximo 1 GB por archivo.
"""
import argparse, http.server, json, os, re, socketserver, sys, threading, time, urllib.parse, webbrowser
from datetime import datetime

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")  # evita errores con tildes en la consola de Windows
    except Exception:
        pass
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import reportar  # noqa: E402

MAX_BYTES = 1024 * 1024 * 1024
PANEL = reportar.carpeta_panel()
RAIZ = os.path.dirname(PANEL)
EST = os.path.join(PANEL, "estado")
PERMITIDAS = ("Entregables", "Mi negocio")


def limpiar_nombre(nombre):
    nombre = os.path.basename(nombre.replace("\\", "/"))
    stem, ext = os.path.splitext(nombre)
    stem = re.sub(r"[^A-Za-z0-9._-]+", "-", stem).strip(".-") or "archivo"
    return stem[:80] + ext.lower()


def dentro(ruta, base):
    ruta, base = os.path.realpath(ruta), os.path.realpath(base)
    return ruta == base or ruta.startswith(base + os.sep)


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=RAIZ, **k)

    def log_message(self, *a):
        pass

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def _host_ok(self):
        return self.headers.get("Host", "").rsplit(":", 1)[0] in ("localhost", "127.0.0.1", "[::1]")

    def _json(self, codigo, obj, extra=None):
        cuerpo = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(codigo)
        for k, v in (extra or {}).items():
            self.send_header(k, v)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(cuerpo)))
        self.end_headers()
        self.wfile.write(cuerpo)

    # ---- GET: ping + archivos con soporte de Range (para poder adelantar los videos)
    def do_GET(self):
        if not self._host_ok():
            return self.send_error(403)
        ruta = urllib.parse.urlparse(self.path).path
        if ruta == "/api/ping":
            # CORS abierto SOLO aquí: permite que Panel/index.html abierto con doble clic detecte el servidor y pase solo a la versión con subida
            return self._json(200, {"ok": True, "raiz": os.path.basename(RAIZ)}, {"Access-Control-Allow-Origin": "*"})
        rango = self.headers.get("Range")
        fs = self.translate_path(self.path)
        if rango and os.path.isfile(fs):
            m = re.match(r"bytes=(\d*)-(\d*)", rango)
            if m:
                tam = os.path.getsize(fs)
                ini = int(m.group(1)) if m.group(1) else max(0, tam - int(m.group(2) or 0))
                fin = int(m.group(2)) if m.group(1) and m.group(2) else tam - 1
                fin = min(fin, tam - 1)
                if ini > fin:
                    self.send_response(416)
                    self.send_header("Content-Range", "bytes */%d" % tam)
                    self.end_headers()
                    return
                self.send_response(206)
                self.send_header("Content-Type", self.guess_type(fs))
                self.send_header("Accept-Ranges", "bytes")
                self.send_header("Content-Range", "bytes %d-%d/%d" % (ini, fin, tam))
                self.send_header("Content-Length", str(fin - ini + 1))
                self.end_headers()
                try:
                    with open(fs, "rb") as f:
                        f.seek(ini)
                        resto = fin - ini + 1
                        while resto > 0:
                            bloque = f.read(min(65536, resto))
                            if not bloque:
                                break
                            self.wfile.write(bloque)
                            resto -= len(bloque)
                except (BrokenPipeError, ConnectionResetError):
                    pass
                return
        try:
            super().do_GET()
        except (BrokenPipeError, ConnectionResetError):
            pass

    # ---- POST /api/subir?slot=<id>&nombre=<archivo>
    def do_POST(self):
        if not self._host_ok() or self.headers.get("X-FM") != "1":
            return self._json(403, {"ok": False, "error": "No permitido"})
        u = urllib.parse.urlparse(self.path)
        if u.path != "/api/subir":
            return self._json(404, {"ok": False, "error": "No existe"})
        q = urllib.parse.parse_qs(u.query)
        slot = q.get("slot", [""])[0]
        nombre = limpiar_nombre(q.get("nombre", ["archivo"])[0])
        ext = os.path.splitext(nombre)[1].lower()
        if ext not in reportar.EXT_OK:
            return self._json(400, {"ok": False, "error": "Tipo de archivo no permitido (%s)" % (ext or "sin extensión")})
        try:
            largo = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            largo = 0
        if largo <= 0:
            return self._json(411, {"ok": False, "error": "Archivo vacío"})
        if largo > MAX_BYTES:
            return self._json(413, {"ok": False, "error": "Archivo mayor a 1 GB"})

        paso = reportar.buscar_paso(EST, slot) if slot != "extra" else None
        if slot == "extra":
            carpeta, fname = os.path.join(RAIZ, "Mi negocio", "subidas"), nombre
        elif not paso or not paso.get("salida"):
            return self._json(404, {"ok": False, "error": "Ese paso no existe o no recibe archivos"})
        else:
            salida = paso["salida"].replace("\\", "/").strip("/")
            if paso.get("multiple"):
                carpeta, fname = os.path.join(RAIZ, salida), nombre
            else:
                carpeta = os.path.dirname(os.path.join(RAIZ, salida))
                fname = os.path.splitext(os.path.basename(salida))[0] + ext
        if not dentro(carpeta, RAIZ) or os.path.relpath(carpeta, RAIZ).replace("\\", "/").split("/")[0] not in PERMITIDAS:
            return self._json(400, {"ok": False, "error": "Carpeta de destino no permitida"})
        os.makedirs(carpeta, exist_ok=True)
        destino = os.path.join(carpeta, fname)
        tmp = destino + ".subiendo"
        recibido = 0
        try:
            with open(tmp, "wb") as f:
                while recibido < largo:
                    bloque = self.rfile.read(min(1 << 20, largo - recibido))
                    if not bloque:
                        break
                    f.write(bloque)
                    recibido += len(bloque)
            if recibido != largo:
                os.remove(tmp)
                return self._json(400, {"ok": False, "error": "La subida se cortó. Intenta de nuevo."})
            # Si ya había una versión (incluso con otra extensión), se archiva para poder comparar intentos.
            stem = os.path.splitext(fname)[0]
            if not (paso and paso.get("multiple")) and slot != "extra":
                for viejo in os.listdir(carpeta):
                    n, e = os.path.splitext(viejo)
                    if n == stem and e.lower() in reportar.EXT_OK and os.path.isfile(os.path.join(carpeta, viejo)):
                        ant = os.path.join(carpeta, "_anteriores")
                        os.makedirs(ant, exist_ok=True)
                        os.replace(os.path.join(carpeta, viejo), os.path.join(ant, "%s-%s%s" % (n, datetime.now().strftime("%H%M%S"), e)))
            elif os.path.exists(destino):
                n, e = os.path.splitext(fname)
                k = 2
                while os.path.exists(os.path.join(carpeta, "%s-%d%s" % (n, k, e))):
                    k += 1
                destino = os.path.join(carpeta, "%s-%d%s" % (n, k, e))
            os.replace(tmp, destino)
        except OSError as e:
            try:
                os.remove(tmp)
            except OSError:
                pass
            return self._json(500, {"ok": False, "error": "No pude guardar: %s" % e})
        reportar.escribir_medios(PANEL)
        rel = os.path.relpath(destino, RAIZ).replace("\\", "/")
        print("  ✔ Recibido:", rel, "(%.1f MB)" % (recibido / 1048576))
        return self._json(200, {"ok": True, "archivo": rel, "tam": recibido})


class Servidor(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True
    allow_reuse_address = True


def vigilar_carpetas():
    while True:
        try:
            reportar.escribir_medios(PANEL)
        except Exception:
            pass
        time.sleep(2)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--puerto", type=int, default=8765)
    ap.add_argument("--no-abrir", action="store_true", help="no abrir el navegador")
    args = ap.parse_args()
    if not os.path.exists(os.path.join(PANEL, "index.html")):
        print("No encuentro Panel/index.html junto a este script.")
        return 1
    srv, puerto = None, args.puerto
    for p in range(args.puerto, args.puerto + 20):
        try:
            srv = Servidor(("127.0.0.1", p), Handler)
            puerto = p
            break
        except OSError:
            continue
    if not srv:
        print("No encontré un puerto libre entre %d y %d." % (args.puerto, args.puerto + 19))
        return 1
    url = "http://localhost:%d/Panel/index.html" % puerto
    reportar.escribir(os.path.join(EST, "servidor.json"), json.dumps({"url": url, "puerto": puerto, "pid": os.getpid()}))
    threading.Thread(target=vigilar_carpetas, daemon=True).start()
    print("")
    print("  Panel en vivo listo:  " + url)
    print("  Carpeta de trabajo:   " + RAIZ)
    print("  Arrastra tus archivos a la pestaña 'Guía de generación'. Para detener: Ctrl+C o cierra esta ventana.")
    print("")
    if not args.no_abrir:
        try:
            webbrowser.open(url)
        except Exception:
            pass
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        try:
            os.remove(os.path.join(EST, "servidor.json"))
        except OSError:
            pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
