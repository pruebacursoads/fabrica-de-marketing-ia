#!/usr/bin/env python3
"""Motor de edición de la Fábrica de Video: plan.json + estilo.json + words.json  ->  index.html (HyperFrames) + sfx_eventos.json
   python construir.py --proyecto <carpeta> [--estilo ruta/estilo.json] [--plan plan.json] [--validar]
   Lee de la carpeta del proyecto: plan.json, words.json (transcripción con tiempos), assets/base.mp4 (video montado) y estilo.json.
   Qué dibuja: subtítulos palabra por palabra con palabra clave, gancho, tarjetas con icono, datos grandes, sellos, listas, titulares,
   etiquetas, tarjeta de nombre, capítulos con barra de progreso, zooms de cámara y cierre. Todo con el estilo del alumno.
   Reglas que valida: un hueco = un gráfico a la vez, nada sobre la banda de subtítulos, nada sobre la zona del rostro, texto >= 28 px."""
import argparse, json, os, re, shutil, sys

try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass

W, H = 1080, 1920
BASE = {"arriba": (170, 440), "medio": (640, 420), "abajo": (1420, 110)}   # (y, alto) por defecto

# ---------------- iconos (trazo redondeado, color por currentColor) ----------------
_I = {
 "check": '<polyline points="22,54 42,74 80,28" stroke-width="12"/>',
 "cross": '<path d="M24 24L76 76M76 24L24 76" stroke-width="12"/>',
 "warning": '<path d="M50 12 L92 86 H8 Z"/><path d="M50 40V60M50 72V74"/>',
 "star": '<path d="M50 8 L61 38 L92 38 L67 57 L77 88 L50 69 L23 88 L33 57 L8 38 L39 38 Z"/>',
 "rocket": '<path d="M50 8 C66 22 70 44 62 66 H38 C30 44 34 22 50 8 Z"/><path d="M38 62 L22 78 L38 74 M62 62 L78 78 L62 74"/><circle cx="50" cy="38" r="6"/><path d="M44 72 L50 92 L56 72"/>',
 "chart": '<path d="M10 90H92"/><rect x="16" y="56" width="14" height="34" rx="3" fill="currentColor" stroke="none"/><rect x="36" y="40" width="14" height="50" rx="3" fill="currentColor" stroke="none"/><rect x="56" y="48" width="14" height="42" rx="3" fill="currentColor" stroke="none"/><rect x="76" y="18" width="14" height="72" rx="3" fill="currentColor" stroke="none"/>',
 "trend": '<path d="M10 78 L36 50 L52 62 L90 22 M68 22 H90 V44"/>',
 "megaphone": '<path d="M18 42 L58 24 V76 L18 58 Z" fill="currentColor" fill-opacity=".18"/><rect x="8" y="42" width="10" height="16" rx="2"/><path d="M26 60 l6 22 h10 l-5 -18"/><path d="M68 38 q10 12 0 24"/><path d="M76 28 q18 22 0 44"/>',
 "chip": '<rect x="26" y="26" width="48" height="48" rx="8" fill="currentColor" fill-opacity=".18"/><path d="M38 14v12M50 14v12M62 14v12M38 74v12M50 74v12M62 74v12M14 38h12M14 50h12M14 62h12M74 38h12M74 50h12M74 62h12"/>',
 "lock": '<path d="M34 44 V30 a16 16 0 0 1 32 0 V44"/><rect x="22" y="44" width="56" height="44" rx="9" fill="currentColor" fill-opacity=".18"/><circle cx="50" cy="66" r="5" fill="currentColor"/>',
 "unlock": '<path d="M34 44 V30 a16 16 0 0 1 30 -6"/><rect x="22" y="44" width="56" height="44" rx="9" fill="currentColor" fill-opacity=".18"/><circle cx="50" cy="66" r="5" fill="currentColor"/>',
 "shield": '<path d="M50 8 L86 22 V50 C86 74 70 88 50 94 C30 88 14 74 14 50 V22 Z"/><polyline points="34,52 46,64 68,38" stroke-width="8"/>',
 "user": '<circle cx="50" cy="32" r="16"/><path d="M16 90 C16 64 32 56 50 56 C68 56 84 64 84 90"/>',
 "building": '<rect x="22" y="12" width="56" height="78" rx="4"/><path d="M36 30h8M56 30h8M36 46h8M56 46h8M36 62h8M56 62h8"/><path d="M42 90V76h16v14"/>',
 "store": '<path d="M12 36 L20 14 H80 L88 36 Z" fill="currentColor" fill-opacity=".2"/><path d="M12 36 q8 12 19 0 q9 12 19 0 q9 12 19 0 q9 12 19 0"/><rect x="18" y="44" width="64" height="44" rx="3"/><rect x="42" y="60" width="16" height="28"/>',
 "phone": '<rect x="28" y="8" width="44" height="84" rx="9"/><path d="M44 80 H56"/>',
 "camera": '<rect x="10" y="26" width="58" height="48" rx="9"/><path d="M68 42 L90 30 V70 L68 58"/><circle cx="39" cy="50" r="9"/>',
 "mic": '<rect x="36" y="10" width="28" height="48" rx="14"/><path d="M22 46 a28 28 0 0 0 56 0M50 74 V90M34 90 H66"/>',
 "globe": '<circle cx="50" cy="50" r="38"/><path d="M12 50H88M50 12C34 30 34 70 50 88M50 12C66 30 66 70 50 88"/>',
 "heart": '<path d="M50 86 C20 62 10 44 10 30 C10 18 20 10 31 10 C40 10 47 15 50 22 C53 15 60 10 69 10 C80 10 90 18 90 30 C90 44 80 62 50 86 Z"/>',
 "cart": '<path d="M10 14 H24 L34 62 H78 L88 28 H28"/><circle cx="40" cy="78" r="6"/><circle cx="72" cy="78" r="6"/>',
 "money": '<circle cx="50" cy="50" r="38"/><path d="M50 26V74M62 36 C58 30 40 30 40 42 C40 54 60 50 60 62 C60 74 42 72 38 64"/>',
 "clock": '<circle cx="50" cy="50" r="38"/><path d="M50 26V50L68 60"/>',
 "bulb": '<path d="M50 8 C30 8 20 24 24 40 C27 50 36 56 36 66 H64 C64 56 73 50 76 40 C80 24 70 8 50 8 Z"/><path d="M38 76 H62 M42 86 H58"/>',
 "target": '<circle cx="50" cy="50" r="38"/><circle cx="50" cy="50" r="24"/><circle cx="50" cy="50" r="9" fill="currentColor"/>',
 "calendar": '<rect x="12" y="20" width="76" height="68" rx="9"/><path d="M12 40H88M32 10V28M68 10V28"/>',
 "play": '<circle cx="50" cy="50" r="38"/><path d="M42 34 L68 50 L42 66 Z" fill="currentColor"/>',
 "link": '<path d="M40 60 a14 14 0 0 1 0 -20 l12 -12 a14 14 0 0 1 20 20 l-6 6"/><path d="M60 40 a14 14 0 0 1 0 20 l-12 12 a14 14 0 0 1 -20 -20 l6 -6"/>',
 "gear": '<circle cx="50" cy="50" r="14"/><path d="M50 10v14M50 76v14M10 50h14M76 50h14M22 22l10 10M68 68l10 10M78 22L68 32M32 68L22 78"/>',
 "spark": '<path d="M50 8 L58 42 L92 50 L58 58 L50 92 L42 58 L8 50 L42 42 Z" fill="currentColor" stroke="none"/>',
 "arrow_up": '<path d="M50 88V16M22 42L50 14l28 28" stroke-width="9"/>',
 "arrow_right": '<path d="M12 50H84M58 22L86 50L58 78" stroke-width="9"/>',
 "question": '<circle cx="50" cy="50" r="38"/><path d="M38 40 C38 28 62 28 62 42 C62 54 50 54 50 66M50 76V78"/>',
 "thumb": '<path d="M30 46 V86 H14 V46 Z"/><path d="M30 50 L46 14 C58 14 60 24 56 34 H84 C90 34 92 40 90 46 L82 80 C80 84 76 86 72 86 H30"/>',
}
def icono(nombre, size, color="currentColor"):
    return f'<svg viewBox="0 0 100 100" width="{size}" height="{size}" fill="none" stroke="{color}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" style="color:{color}">{_I.get(nombre, _I["spark"])}</svg>'

# ---------------- utilidades ----------------
AVISOS, ERRORES = [], []
def esc(s): return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
def jl(o): return json.dumps(o, ensure_ascii=False, separators=(",", ":"))

def ajustar(texto, base, ancho, piso=28, mayus=True, etiqueta=""):
    """Tamaño de letra que cabe en `ancho` px (peso 800)."""
    f = 0.84 if mayus else 0.68
    n = max((len(l) for l in re.sub(r"\*", "", texto).split("\n")), default=1)
    fs = int(min(base, ancho / (f * max(n, 1))))
    if fs < piso:
        AVISOS.append(f"El texto '{texto[:30]}' ({etiqueta}) es demasiado largo para caber a {piso} px; acórtalo o divídelo con \\n.")
        fs = piso
    return fs

def marcar(texto, col_clave):
    """*palabra* -> palabra en color de acento"""
    partes = re.split(r"(\*[^*]+\*)", esc(texto))
    return "".join(f'<span style="color:{col_clave}">{p[1:-1]}</span>' if p.startswith("*") and p.endswith("*") and len(p) > 2 else p for p in partes).replace("\n", "<br>")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--proyecto", required=True); ap.add_argument("--estilo"); ap.add_argument("--plan"); ap.add_argument("--validar", action="store_true")
    a = ap.parse_args()
    D = os.path.abspath(a.proyecto)
    estilo = json.load(open(a.estilo or os.path.join(D, "estilo.json"), encoding="utf-8"))
    plan = json.load(open(a.plan or os.path.join(D, "plan.json"), encoding="utf-8"))
    words = json.load(open(os.path.join(D, plan.get("words", "words.json")), encoding="utf-8")) if os.path.exists(os.path.join(D, plan.get("words", "words.json"))) else []
    COL = estilo["colores"]; TIPO = estilo["tipografia"]; SUB = estilo["subtitulos"]; GR = estilo.get("estilo_grafico", {"radio": 30, "vidrio": True})
    MAY = bool(TIPO.get("mayusculas", True))
    def color(v):
        if not v: return COL["texto"]
        return COL.get(v, v)
    DUR = float(plan["duracion"])
    VIDEO = plan.get("video", "assets/base.mp4"); AUDIO = plan.get("audio", "assets/mix.wav")
    ROSTRO_Y = int(plan.get("rostro_y", 760)); ZOOM_MAX = min(float(plan.get("zoom_max", 1.15)), 1.2)
    Z = {k: list(v) for k, v in BASE.items()}
    for k, v in (plan.get("zonas") or {}).items(): Z[k] = [int(v["y"]), int(v["h"])]
    SUB_Y = int(plan.get("subtitulos_y", SUB.get("y", 1180))); SUB_H = 210
    ROSTRO = plan.get("rostro")   # {"y1":..,"y2":..} zona que ningún gráfico debe tapar
    logo = None
    if estilo.get("logo") and os.path.exists(estilo["logo"]):
        ext = os.path.splitext(estilo["logo"])[1]; os.makedirs(os.path.join(D, "assets"), exist_ok=True)
        shutil.copy(estilo["logo"], os.path.join(D, "assets", "logo" + ext)); logo = "assets/logo" + ext
    for rel in (VIDEO,):
        if not os.path.exists(os.path.join(D, rel)): AVISOS.append(f"Todavía no existe {rel} (hay que montarlo antes de renderizar).")

    html_gfx, js, sfx = [], [], []
    def sfx_add(t, n, pk): sfx.append([round(float(t), 2), n, pk])
    cajas = []   # (id, pos, t0, t1, y, h, solapa) para validar
    acento, sec = color("acento"), color("secundario")
    panel_css = f"background:{COL['panel']}ee;" if GR.get("vidrio", True) else f"background:{COL['panel']};"
    radio = int(GR.get("radio", 30))

    # --- gancho
    g = plan.get("gancho")
    if g:
        lineas = g["lineas"]; y0 = int(g.get("y", Z["arriba"][0])); fin = float(g.get("fin", 4.0)); cas = float(g.get("cascada", 0.45))
        items, alto = [], 28
        if logo and g.get("logo", True): items.append(f'<img src="{logo}" style="height:96px;max-width:420px;object-fit:contain;display:block;margin:0 auto 6px">'); alto += 104
        if g.get("tag"):
            items.append(f'<div class="chipt" style="background:{acento};color:{COL["fondo"]}">{esc(g["tag"])}</div>'); alto += 70
        for i, l in enumerate(lineas):
            fs = ajustar(l["t"], int(l.get("tam", 80)), 900, mayus=MAY, etiqueta="gancho")
            items.append(f'<div id="gl{i}" class="big" style="font-size:{fs}px;color:{color(l.get("color"))};text-align:center;margin-top:6px">{marcar(l["t"], acento)}</div>'); alto += int(fs * 1.12) + 6
        html_gfx.append(f'<div id="gancho" class="panel" style="left:60px;top:{y0}px;width:960px;height:{alto}px;padding:14px 30px 0">{"".join(items)}</div>')
        cajas.append(("gancho", "gancho", 0.0, fin, y0, alto, False))
        for i in range(len(lineas)):
            js.append(f'tl.fromTo("#gl{i}",{{opacity:0,y:24,scale:.92}},{{opacity:1,y:0,scale:1,duration:.35,ease:"back.out(1.8)"}},{0.15 + i * cas:.2f});')
        js.append(f'tl.fromTo("#gancho",{{opacity:1}},{{opacity:1,duration:.01}},0);tl.to("#gancho",{{opacity:0,y:-30,duration:.3,ease:"power2.in"}},{fin:.2f});')
        sfx_add(0.0, "impact.wav", -18)

    # --- eventos
    for i, e in enumerate(plan.get("eventos", [])):
        tipo = e["tipo"]; t0 = float(e["t"]); dur = float(e.get("dur", 2.5)); t1 = min(t0 + dur, DUR)
        pos = e.get("pos", "abajo" if tipo in ("etiqueta", "nombre") else "arriba"); zy, zh = Z[pos]
        eid = f"ev{i}"; col = color(e.get("color", "acento"))
        x_in = {"x": -80, "y": 0} if e.get("entrada") == "izquierda" else {"x": 80, "y": 0} if e.get("entrada") == "derecha" else {"y": 40}
        ease = "back.out(1.5)"
        if tipo == "tarjeta":
            h = 200; tfs = ajustar(e["titulo"], 60, 740, mayus=MAY, etiqueta="tarjeta")
            sub = f'<div class="mono" style="position:absolute;left:176px;top:{34 + int(tfs * 1.12) + 6}px;font-size:30px;color:{COL["texto"]}cc;white-space:nowrap">{esc(e["sub"])}</div>' if e.get("sub") else ""
            ty = (h - int(tfs * 1.12)) // 2 if not e.get("sub") else 30
            html_gfx.append(f'<div id="{eid}" class="card" style="left:60px;top:{zy}px;width:960px;height:{h}px;{panel_css}border-radius:{radio}px"><div class="ic" style="left:34px;top:45px">{icono(e.get("icono", "spark"), 110, col)}</div><div class="big abs" style="left:176px;top:{ty}px;font-size:{tfs}px">{marcar(e["titulo"], col)}</div>{sub}</div>')
            cajas.append((eid, pos, t0, t1, zy, h, e.get("solapa", False))); sfx_add(t0, "uiclick.wav", -26)
        elif tipo == "dato":
            h = 260; vfs = ajustar(e["valor"], 150, 840, mayus=MAY, etiqueta="dato"); lfs = ajustar(e["etiqueta"], 44, 840, mayus=MAY, etiqueta="dato")
            html_gfx.append(f'<div id="{eid}" class="card col" style="left:100px;top:{zy}px;width:880px;height:{h}px;{panel_css}border-radius:{radio}px"><div class="big" style="font-size:{vfs}px;color:{col};font-weight:{TIPO.get("peso_extra", 900)}">{esc(e["valor"])}</div><div class="big" style="font-size:{lfs}px;margin-top:6px">{marcar(e["etiqueta"], col)}</div></div>')
            cajas.append((eid, pos, t0, t1, zy, h, e.get("solapa", False))); sfx_add(t0, "uiclick.wav", -24)
        elif tipo == "sello":
            h = 170; fs = ajustar(e["texto"], 88, 820, mayus=MAY, etiqueta="sello")
            html_gfx.append(f'<div id="{eid}" class="sello" style="left:90px;top:{zy}px;width:900px;height:{h}px;border-color:{col};color:{col}"><span class="big" style="font-size:{fs}px;font-weight:{TIPO.get("peso_extra", 900)}">{esc(e["texto"])}</span></div>')
            cajas.append((eid, pos, t0, t1, zy, h, e.get("solapa", False))); sfx_add(t0, "impact.wav", -18)
            js.append(f'tl.fromTo("#{eid}",{{opacity:0,scale:2.4,rotation:-14,filter:"blur(10px)"}},{{opacity:1,scale:1,rotation:-4,filter:"blur(0px)",duration:.22,ease:"power4.in"}},{t0:.2f});tl.to("#{eid}",{{x:10,duration:.05,yoyo:true,repeat:7,ease:"none"}},{t0 + .22:.2f});tl.to("#{eid}",{{opacity:0,y:-30,duration:.26,ease:"power2.in"}},{t1 - .26:.2f});')
            continue
        elif tipo == "lista":
            its = e["items"][:5]; n = len(its); cada = float(e.get("cada", 0.6)); tit = e.get("titulo")
            h = (70 if tit else 0) + n * 88 + 36
            filas = "".join(f'<div id="{eid}r{j}" class="fila" style="top:{(70 if tit else 0) + 22 + j * 88}px"><span style="color:{COL["positivo"]}">{icono("check", 46)}</span><span class="big" style="font-size:{ajustar(x, 46, 800, mayus=MAY, etiqueta="lista")}px">{marcar(x, col)}</span></div>' for j, x in enumerate(its))
            tt = f'<div class="big abs" style="left:34px;top:16px;font-size:{ajustar(tit, 44, 880, mayus=MAY, etiqueta="lista")}px;color:{col}">{esc(tit)}</div>' if tit else ""
            html_gfx.append(f'<div id="{eid}" class="card" style="left:60px;top:{zy}px;width:960px;height:{h}px;{panel_css}border-radius:{radio}px">{tt}{filas}</div>')
            cajas.append((eid, pos, t0, t1, zy, h, e.get("solapa", False))); sfx_add(t0, "uiclick.wav", -26)
            for j in range(n):
                js.append(f'tl.fromTo("#{eid}r{j}",{{opacity:0,x:-40}},{{opacity:1,x:0,duration:.35,ease:"power3.out"}},{t0 + .3 + j * cada:.2f});')
                if j: sfx_add(t0 + .3 + j * cada, "uiclick.wav", -28)
        elif tipo == "titular":
            lin = e["texto"].split("\n")[:3]; h = int(len(lin) * 120 + 40)
            fs = min(ajustar(l, 100, 960, mayus=MAY, etiqueta="titular") for l in lin)
            ls = "".join(f'<div class="big" style="font-size:{fs}px;text-align:center;font-weight:{TIPO.get("peso_extra", 900)};text-shadow:0 6px 30px rgba(0,0,0,.65)">{marcar(l, acento)}</div>' for l in lin)
            html_gfx.append(f'<div id="{eid}" class="titular" style="left:50px;top:{zy}px;width:980px;height:{h}px">{ls}</div>')
            cajas.append((eid, pos, t0, t1, zy, h, e.get("solapa", False))); sfx_add(t0, "whoosh.wav", -24)
        elif tipo in ("etiqueta", "nombre"):
            h = 110
            if tipo == "nombre":
                txt1, txt2 = e.get("texto", estilo["nombre"]), e.get("sub", estilo.get("handle", "")); ic = None
            else:
                txt1, txt2, ic = e["texto"], e.get("sub"), e.get("icono")
            fs = 34 if txt2 is None else 36
            ancho = int(min(980, max(520, (0.84 if MAY else 0.7) * fs * len(txt1) + (170 if ic else 90)))); left = (W - ancho) // 2
            icon_html = f'<span style="color:{col};flex:none">{icono(ic, 56)}</span>' if ic else ""
            sub_html = f'<div class="mono" style="font-size:28px;color:{COL["texto"]}cc;white-space:nowrap">{esc(txt2)}</div>' if txt2 else ""
            html_gfx.append(f'<div id="{eid}" class="pill" style="left:{left}px;top:{zy}px;width:{ancho}px;height:{h}px;border-color:{col};{panel_css}"><div class="col" style="align-items:flex-start;gap:0">{icon_html and ""}<div class="big" style="font-size:{fs}px;font-weight:{TIPO.get("peso_extra", 900)}">{esc(txt1)}</div>{sub_html}</div></div>' if ic is None else
                            f'<div id="{eid}" class="pill" style="left:{left}px;top:{zy}px;width:{ancho}px;height:{h}px;border-color:{col};{panel_css}">{icon_html}<div class="col" style="align-items:flex-start;gap:0"><div class="big" style="font-size:{fs}px;font-weight:{TIPO.get("peso_extra", 900)}">{esc(txt1)}</div>{sub_html}</div></div>')
            cajas.append((eid, pos, t0, t1, zy, h, e.get("solapa", False))); sfx_add(t0, "uiclick.wav", -26)
        else:
            ERRORES.append(f"Evento {i}: tipo desconocido '{tipo}' (usa tarjeta, dato, sello, lista, titular, etiqueta, nombre)."); continue
        fr = {"opacity": 0, "scale": .92, "filter": "blur(8px)"}; fr.update(x_in)
        js.append(f'tl.fromTo("#{eid}",{jl(fr)},{{opacity:1,x:0,y:0,scale:1,filter:"blur(0px)",duration:.42,ease:"{ease}"}},{t0:.2f});tl.to("#{eid}",{{opacity:0,y:-30,scale:.95,filter:"blur(6px)",duration:.28,ease:"power2.in"}},{t1 - .28:.2f});')

    # --- capítulos y barra de progreso
    caps = plan.get("capitulos") or []
    if caps:
        barras = []
        for j, c in enumerate(caps):
            t0 = float(c["t"]); t1 = float(caps[j + 1]["t"]) if j + 1 < len(caps) else DUR
            ct = ajustar(c["texto"], 38, 700, mayus=MAY, etiqueta="capítulo")
            html_gfx.append(f'<div id="cap{j}" class="chap"><span class="cb" style="background:{acento};color:{COL["fondo"]}">{esc(c["badge"])}</span><span class="ct" style="font-size:{ct}px">{esc(c["texto"])}</span></div>')
            js.append(f'tl.fromTo("#cap{j}",{{opacity:0,x:-50}},{{opacity:1,x:0,duration:.4,ease:"power4.out"}},{t0:.2f});' + (f'tl.to("#cap{j}",{{opacity:0,x:50,duration:.25,ease:"power2.in"}},{t1 - .25:.2f});' if j + 1 < len(caps) else ""))
            barras.append(f'<div class="seg"><i id="pg{j}" style="background:{acento}"></i></div>')
            js.append(f'tl.fromTo("#pg{j}",{{scaleX:0}},{{scaleX:1,duration:{max(t1 - t0, .1):.2f},ease:"none"}},{t0:.2f});')
            if j: sfx_add(t0, "whoosh.wav", -26)
        html_gfx.append(f'<div class="pbar">{"".join(barras)}</div>')
        cajas.append(("capitulos", "capitulos", 0.0, DUR, 150, 130, False))

    # --- cierre
    c = plan.get("cierre")
    if c:
        t0 = float(c["t"]); cta = estilo["cta"]; y0 = int(c.get("y", 1240))
        l1 = c.get("texto", cta["texto"]); l2 = c.get("sub", cta.get("sub", "")); l3 = c.get("handle", estilo.get("handle", ""))
        f1 = ajustar(l1, 56, 820, mayus=MAY, etiqueta="cierre"); alto = 40 + int(f1 * 1.12) + (44 if l2 else 0) + (44 if l3 else 0) + (104 if logo else 0)
        lg = f'<img src="{logo}" style="height:84px;max-width:360px;object-fit:contain;display:block;margin:0 auto 6px">' if logo else ""
        html_gfx.append(f'<div id="cierre" class="cierre" style="left:90px;top:{y0}px;width:900px;height:{alto}px;background:{acento};color:{COL["fondo"]}">{lg}<div class="big" style="font-size:{f1}px;font-weight:{TIPO.get("peso_extra", 900)}">{esc(l1)}</div>' + (f'<div class="mono" style="font-size:30px;color:{COL["fondo"]};margin-top:4px">{esc(l2)}</div>' if l2 else "") + (f'<div class="mono" style="font-size:30px;color:{COL["fondo"]}">{esc(l3)}</div>' if l3 else "") + '</div>')
        js.append(f'tl.fromTo("#cierre",{{opacity:0,y:60,scale:.88}},{{opacity:1,y:0,scale:1,duration:.5,ease:"back.out(1.8)"}},{t0:.2f});tl.to("#cierre",{{scale:1.03,duration:.5,yoyo:true,repeat:3,ease:"sine.inOut"}},{t0 + .6:.2f});')
        cajas.append(("cierre", "cierre", t0, DUR, y0, alto, False)); sfx_add(t0, "chime.wav", -22)

    # --- zooms de cámara
    zooms = plan.get("zooms")
    if zooms is None and plan.get("zooms_auto", True) and words:
        zooms, ult, alt = [], 1.0, False
        for k, w in enumerate(words[:-1]):
            if w["w"][-1:] in ".?!" and words[k + 1]["s"] - w["e"] > 0.2 and words[k + 1]["s"] > 1.5 and words[k + 1]["s"] - ult > 3.6 and words[k + 1]["s"] < DUR - 2:
                alt = not alt; zooms.append({"t": round(words[k + 1]["s"] - .05, 2), "escala": round(min(ZOOM_MAX, 1.12), 2) if alt else 1.0}); ult = words[k + 1]["s"]
    zooms = zooms or []
    def cam(s):
        x = 540 - s * 540; y = ROSTRO_Y - s * ROSTRO_Y
        return round(max(W * (1 - s), min(0, x))), round(max(H * (1 - s), min(0, y)))
    cur = (0, 0, 1.0); zj = ['tl.set("#cam",{x:0,y:0,scale:1,transformOrigin:"0 0"},0);']
    for z in zooms:
        s = min(float(z["escala"]), ZOOM_MAX); x, y = cam(s)
        zj.append(f'tl.fromTo("#cam",{{x:{cur[0]},y:{cur[1]},scale:{cur[2]}}},{{x:{x},y:{y},scale:{s},duration:.22,ease:"power4.out"}},{float(z["t"]):.2f});'); cur = (x, y, s)
        if s > 1.0: sfx_add(float(z["t"]) - .02, "whoosh.wav", -28)

    # --- subtítulos
    cap_html = []
    if words and plan.get("subtitulos", True):
        ppg = int(SUB.get("palabras_por_grupo", 3)); claves = [k.lower() for k in plan.get("claves", [])]
        sin = plan.get("sin_subtitulos", [])
        def limpia(w): return re.sub(r"^[¿¡\"'(]+|[,.;:?!\"')]+$", "", w).upper() if MAY else re.sub(r"^[¿¡\"'(]+|[,.;:?!\"')]+$", "", w)
        grupos, cur_g = [], []
        for i, w in enumerate(words):
            cur_g.append(i); texto = " ".join(limpia(words[j]["w"]) for j in cur_g)
            gap = (words[i + 1]["s"] - w["e"]) if i + 1 < len(words) else 9
            if w["w"][-1:] in ".,?!" or len(cur_g) >= ppg or len(texto) >= 19 or gap > 0.3: grupos.append(cur_g); cur_g = []
        if cur_g: grupos.append(cur_g)
        tam = int(SUB.get("tam", 64)); tamk = int(SUB.get("tam_clave", 92)); colk = color(SUB.get("color_clave", "acento"))
        for gi, gg in enumerate(grupos):
            a0, b0 = gg[0], gg[-1]; t_ini = words[a0]["s"]
            if any(s[0] <= t_ini <= s[1] for s in sin): continue
            k = next((j for j in gg if limpia(words[j]["w"]).lower() in claves), None)
            if k is None: k = max(gg, key=lambda j: len(limpia(words[j]["w"])))
            start = max(0.0, t_ini - 0.04); nxt = (words[grupos[gi + 1][0]]["s"] - 0.04) if gi + 1 < len(grupos) else DUR
            end = min(nxt, words[b0]["e"] + 0.45); dur = max(0.3, end - start)
            def sp(j):
                tx = limpia(words[j]["w"])
                if j != k: return f'<span id="cw{j}" class="cw">{esc(tx)}</span>'
                fs = max(54, min(tamk, int(900 / (0.84 * max(len(tx), 1)))))
                return f'<span id="cw{j}" class="cw key" style="font-size:{fs}px;color:{colk}">{esc(tx)}</span>'
            cap_html.append(f'<div id="cp{gi}" class="cap clip" data-start="{start:.2f}" data-duration="{dur:.2f}" data-track-index="9"><div class="capin">{"".join(sp(j) for j in gg)}</div></div>')
            for j in gg:
                tj = max(0.0, words[j]["s"] - .03)
                if j == k: js.append(f'tl.fromTo("#cw{j}",{{opacity:0,scale:.4,y:30,rotation:-4}},{{opacity:1,scale:1.06,y:0,rotation:0,duration:.2,ease:"back.out(2.6)"}},{tj:.2f}).to("#cw{j}",{{scale:1,duration:.2,ease:"power2.out"}},{tj + .2:.2f});')
                else: js.append(f'tl.fromTo("#cw{j}",{{opacity:0,scale:.6,y:22}},{{opacity:1,scale:1,y:0,duration:.16,ease:"back.out(2)"}},{tj:.2f});')
    elif not words:
        AVISOS.append("No hay words.json: el video saldrá sin subtítulos (ejecuta transcribir.py).")

    # --- validaciones (las reglas de calidad)
    for i, (id1, p1, a1, b1, y1, h1, s1) in enumerate(cajas):
        if y1 < 150 and id1 not in ("capitulos",): AVISOS.append(f"'{id1}' queda sobre y<150, donde la red social pone su interfaz.")
        if y1 + h1 > 1540 and id1 not in ("cierre",): AVISOS.append(f"'{id1}' llega a y={y1 + h1}, debajo de la zona segura (1540).")
        if ROSTRO and not (y1 + h1 < ROSTRO["y1"] or y1 > ROSTRO["y2"]) and id1 not in ("capitulos",):
            ERRORES.append(f"'{id1}' (y {y1}-{y1 + h1}) tapa el rostro (y {ROSTRO['y1']}-{ROSTRO['y2']}). Muévelo o acórtalo.")
        if not (y1 + h1 < SUB_Y or y1 > SUB_Y + SUB_H) and id1 not in ("cierre",) and cap_html:
            ERRORES.append(f"'{id1}' (y {y1}-{y1 + h1}) pisa la banda de subtítulos (y {SUB_Y}-{SUB_Y + SUB_H}).")
        for (id2, p2, a2, b2, y2, h2, s2) in cajas[i + 1:]:
            if id1 == "capitulos" or id2 == "capitulos": continue
            if min(b1, b2) - max(a1, a2) > 0.12 and not (y1 + h1 <= y2 or y2 + h2 <= y1) and not (s1 or s2):
                ERRORES.append(f"'{id1}' y '{id2}' se pisan en pantalla entre {max(a1, a2):.1f} y {min(b1, b2):.1f} s (mismo hueco). Un hueco = un gráfico a la vez: mueve uno o acórtalo.")
    for e in ERRORES: print("✗ " + e)
    for w_ in AVISOS: print("⚠ " + w_)
    if ERRORES:
        print(f"\n{len(ERRORES)} error(es) de composición: corrige el plan y vuelve a ejecutar."); sys.exit(1)
    if a.validar: print("Plan válido ✓"); return

    # --- salida
    fam = TIPO["familia"]; pt = TIPO.get("peso_titulo", 800); pe = TIPO.get("peso_extra", 900)
    css = """
*{margin:0;padding:0;box-sizing:border-box}
html,body{margin:0;width:1080px;height:1920px;overflow:hidden;background:%(bg)s}
#root{position:relative;width:1080px;height:1920px;overflow:hidden;background:%(bg)s;font-family:'%(fam)s',sans-serif;color:%(tx)s}
#cam{position:absolute;left:0;top:0;width:1080px;height:1920px;transform-origin:0 0}
#vid{position:absolute;left:0;top:0;width:1080px;height:1920px;object-fit:cover}
#shade{position:absolute;left:0;right:0;top:%(sy0)spx;height:700px;background:linear-gradient(180deg,rgba(0,0,0,0),%(shade)s);z-index:50}
.big{font-family:'%(fam)s',sans-serif;font-weight:%(pt)s;line-height:1.08;letter-spacing:-.01em;white-space:nowrap;position:relative;%(up)s}
.mono{font-family:'%(fam)s',sans-serif;font-weight:700;white-space:nowrap}
.abs{position:absolute}
#gfx{position:absolute;inset:0;z-index:60}
.card,.panel,.pill,.cierre,.sello,.titular{position:absolute}
.card{border:2px solid rgba(255,255,255,.18);box-shadow:0 30px 70px -26px rgba(0,0,0,.85);opacity:0}
.panel{border-radius:%(r)spx;border:2px solid rgba(255,255,255,.2);background:%(panel)s;box-shadow:0 30px 70px -26px rgba(0,0,0,.85)}
.col{display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}
.ic{position:absolute}
.chipt{display:inline-block;font-weight:900;font-size:30px;padding:8px 22px;border-radius:14px;margin:0 auto 8px;display:table}
.fila{position:absolute;left:34px;display:flex;align-items:center;gap:20px;opacity:0}
.sello{border:10px solid;border-radius:22px;display:flex;align-items:center;justify-content:center;background:%(panel)sf0;opacity:0}
.pill{border:3px solid;border-radius:30px;display:flex;align-items:center;gap:18px;padding:0 26px;opacity:0}
.titular{opacity:0;background:rgba(0,0,0,.52);border-radius:28px;padding-top:12px}
.cierre{border-radius:30px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:14px 20px;box-shadow:0 0 70px -10px rgba(0,0,0,.6);opacity:0}
.chap{position:absolute;left:40px;top:160px;display:flex;align-items:center;gap:18px;opacity:0}
.cb{font-weight:900;font-size:30px;padding:0 20px;height:62px;display:flex;align-items:center;border-radius:14px;white-space:nowrap;font-family:'%(fam)s',sans-serif}
.ct{font-weight:800;color:%(tx)s;white-space:nowrap;font-family:'%(fam)s',sans-serif;text-shadow:0 3px 14px rgba(0,0,0,.7)}
.pbar{position:absolute;left:40px;top:238px;width:1000px;display:flex;gap:12px}
.seg{flex:1;height:8px;border-radius:4px;background:rgba(255,255,255,.22);overflow:hidden}
.seg i{display:block;height:100%%;width:100%%;transform-origin:0 50%%;transform:scaleX(0)}
.cap{position:absolute;left:30px;right:30px;top:%(suby)spx;height:%(subh)spx;z-index:100}
.capin{position:absolute;inset:0;display:flex;flex-wrap:wrap;align-items:center;justify-content:center;align-content:center;gap:0 22px;text-align:center}
.cw{display:inline-block;font-family:'%(fam)s',sans-serif;font-weight:%(pt)s;font-size:%(tam)spx;line-height:1.08;color:#fff;text-shadow:0 5px 22px rgba(0,0,0,.9);letter-spacing:-.01em;will-change:transform;%(up)s}
.cw.key{font-weight:%(pe)s;text-shadow:0 0 36px rgba(255,255,255,.18),0 5px 22px rgba(0,0,0,.9)}
""" % dict(bg=COL["fondo"], tx=COL["texto"], fam=fam, pt=pt, pe=pe, panel=COL["panel"], r=radio, sy0=max(SUB_Y - 120, 900), shade="rgba(0,0,0,.62)",
           up="text-transform:uppercase;" if MAY else "", suby=SUB_Y, subh=SUB_H, tam=int(SUB.get("tam", 64)))
    runtime = r'''
const tl = gsap.timeline({paused:true});
''' + "\n".join(zj) + "\n" + "\n".join(js) + "\n" + "\n".join(f"" for _ in range(0)) + '''
window.__timelines["main"] = tl;
tl.seek(0);
'''
    audio_tag = f'<audio id="mix" class="clip" src="{AUDIO}" data-start="0" data-duration="{DUR}" data-volume="1" data-track-index="2"></audio>' if AUDIO else ""
    html = f'''<!doctype html>
<html lang="es"><head><meta charset="UTF-8" /><meta name="viewport" content="width=1080, height=1920" />
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
<style>{css}</style></head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{DUR}" data-width="1080" data-height="1920">
<div id="cam"><video id="vid" class="clip" src="{VIDEO}" muted playsinline data-start="0" data-duration="{DUR}" data-track-index="0"></video></div>
<div id="shade"></div>
<div id="gfx">{"".join(html_gfx)}</div>
{"".join(cap_html)}
{audio_tag}
</div>
<script>{runtime}</script>
</body></html>
'''
    open(os.path.join(D, "index.html"), "w", encoding="utf-8").write(html)
    sfx.sort(key=lambda x: x[0])
    json.dump(sfx, open(os.path.join(D, "sfx_eventos.json"), "w", encoding="utf-8"))
    print(f"\nindex.html listo · {len(plan.get('eventos', []))} eventos · {len(cap_html)} grupos de subtítulos · {len(zooms)} zooms · {len(sfx)} efectos de sonido")
    print("Siguiente: mezclar.py (audio) -> revisar.py (choques y fotogramas) -> render.py")

if __name__ == "__main__":
    main()
