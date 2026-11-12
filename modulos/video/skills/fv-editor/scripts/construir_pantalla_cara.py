#!/usr/bin/env python3
"""Layout 'pantalla arriba + tú abajo' (1080x1920) para la Fábrica de Video.
   python construir_pantalla_cara.py --proyecto <carpeta> [--estilo estilo.json] [--plan plan.json]
   Lee plan.json + words.json + estilo.json y genera index.html, sfx_eventos.json y mezcla.json.
   Piezas: ventana de pantalla con zooms, empuje lento y anillos; franja de datos debajo (texto, pasos, stats, sello, comparar, dato);
   gancho de dolor a pantalla completa; cierre; cámara con zooms suaves; subtítulos palabra por palabra.
   Los medios deben venir recortados: assets/screen.mp4 (solo el contenido, sin pestañas ni textos fijos) y assets/face.mp4."""
import argparse, json, math, os, re, sys

try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass

AQUI = os.path.dirname(os.path.abspath(__file__))
import importlib.util
_s = importlib.util.spec_from_file_location("cons", os.path.join(AQUI, "construir.py")); cons = importlib.util.module_from_spec(_s); _s.loader.exec_module(cons)
ic = cons.icono

def esc(s): return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
def fit(text, base, width, f=0.78, piso=28): return max(piso, int(min(base, width / (f * max(len(text), 1)))))

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--proyecto", required=True); ap.add_argument("--estilo"); ap.add_argument("--plan")
    a = ap.parse_args(); D = os.path.abspath(a.proyecto)
    plan = json.load(open(a.plan or os.path.join(D, "plan.json"), encoding="utf-8"))
    est = json.load(open(a.estilo or os.path.join(D, "estilo.json"), encoding="utf-8"))
    C = est["colores"]; FONT = est["tipografia"]["familia"]
    BG, PN, TX, AC, VI, OK, BAD = C["fondo"], C["panel"], C["texto"], C["acento"], C["secundario"], C["positivo"], C["alerta"]
    MU = "#A3A3B8"; P2 = "#1c1f3a"; DARK = "#14110a"
    COL = {"acento": AC, "secundario": VI, "positivo": OK, "alerta": BAD, "texto": TX}
    DUR = float(plan["duracion"])
    # si existe words_original.json se parte siempre de él (las correcciones del plan se reaplican sin acumularse)
    _wo = os.path.join(D, "words_original.json")
    W = json.load(open(_wo if os.path.exists(_wo) else os.path.join(D, plan.get("words", "words.json")), encoding="utf-8"))
    SW, SH = int(plan.get("ventana", {}).get("ancho", 1000)), int(plan.get("ventana", {}).get("alto", 544))
    SX, SY = int(plan.get("ventana", {}).get("x", 40)), int(plan.get("ventana", {}).get("y", 200))
    FY, FH = int(plan.get("franja", {}).get("y", SY + SH + 20)), int(plan.get("franja", {}).get("alto", 226))
    CY, CH = int(plan.get("camara_y", 1010)), int(plan.get("camara_alto", 650))
    js, SFX, HTML = [], [], []
    def sfx(t, name, db): SFX.append([round(float(t), 2), name + ".wav", db])
    def fin(sel, t, x=0, y=30, s=1, dur=.4, ease="power3.out"):
        js.append(f'tl.fromTo("{sel}",{{opacity:0,x:{x},y:{y},scale:{s}}},{{opacity:1,x:0,y:0,scale:1,duration:{dur},ease:"{ease}"}},{t:.2f});')
    def fout(sel, t, dur=.28, x=0, y=-20): js.append(f'tl.to("{sel}",{{opacity:0,x:{x},y:{y},duration:{dur},ease:"power2.in"}},{t:.2f});')
    def box(i, left, top, w, h, style="", inner="", cls=""):
        return f'<div id="{i}" class="{cls}" style="position:absolute;left:{left}px;top:{top}px;width:{w}px;height:{h}px;{style}">{inner}</div>'

    # ---------- palabras: correcciones del plan ----------
    fixes = plan.get("correcciones", [])
    out = []
    for x in W:
        drop = False
        for fx in fixes:
            if abs(x["s"] - float(fx["t"])) <= float(fx.get("tol", .25)) and x["w"].lower().strip(".,?!¿¡") == fx["de"].lower().strip(".,?!¿¡"):
                if fx.get("a") is None: drop = True
                else: x["w"] = fx["a"]
        if not drop: out.append(x)
    W = out
    json.dump(W, open(os.path.join(D, "words.json"), "w", encoding="utf-8"), ensure_ascii=False)

    # ---------- GANCHO ----------
    g = plan["gancho"]; gt0, gt1 = float(g.get("desde", .1)), float(g["fin"])
    l1, l2 = g["lineas"][0], g["lineas"][1] if len(g["lineas"]) > 1 else ""
    hk = (f'<div id="hk" style="position:absolute;left:{SX}px;top:{SY}px;width:{SW}px;height:{FY + FH - SY}px;background:{PN};border:2px solid rgba(255,255,255,.12);border-radius:40px;'
          f'box-shadow:0 40px 90px -30px rgba(0,0,0,.9);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:20px;z-index:12">'
          + (f'<div id="hk0" style="background:{AC};color:{DARK};font-weight:900;font-size:32px;padding:8px 28px;border-radius:40px">{esc(g["tag"])}</div>' if g.get("tag") else "")
          + f'<div id="hk1">{ic(g.get("icono", "warning"), 150, BAD)}</div>'
          + f'<div id="hk2" style="font-weight:900;font-size:{fit(l1, 92, 920)}px;line-height:1.04;text-align:center;color:{TX};white-space:nowrap">{esc(l1)}</div>'
          + f'<div id="hk3" style="font-weight:900;font-size:{fit(l2, 92, 920)}px;line-height:1.04;text-align:center;color:{AC};white-space:nowrap">{esc(l2)}</div>'
          + (f'<div id="hk4" style="margin-top:14px;border:4px solid {BAD};color:{BAD};border-radius:60px;padding:12px 36px;font-weight:900;font-size:{fit(g["pildora"], 36, 860, f=.8)}px;white-space:nowrap">{esc(g["pildora"])}</div>' if g.get("pildora") else "")
          + (f'<div id="hk5" style="background:{AC};color:{DARK};border-radius:60px;padding:12px 36px;font-weight:900;font-size:{fit(g["pildora2"], 38, 860, f=.8)}px;white-space:nowrap">{esc(g["pildora2"])}</div>' if g.get("pildora2") else "")
          + '</div>')
    HTML.append(hk)
    if g.get("tag"): fin("#hk0", gt0 + .1, y=-20, dur=.35)
    fin("#hk1", gt0 + .25, y=0, s=.5, dur=.5, ease="back.out(2)")
    js.append(f'tl.to("#hk1",{{scale:1.12,duration:.35,yoyo:true,repeat:5,ease:"sine.inOut"}},{gt0 + .8:.2f});')
    fin("#hk2", gt0 + .5, y=26, dur=.4); fin("#hk3", gt0 + .95, y=26, s=.9, dur=.45, ease="back.out(1.8)")
    if g.get("pildora"): fin("#hk4", gt0 + 1.7, y=30, dur=.4, ease="back.out(1.5)")
    if g.get("pildora2"): fin("#hk5", gt0 + 2.5, y=30, s=.9, dur=.45, ease="back.out(1.8)"); sfx(gt0 + 2.5, "impact", -20)
    fout("#hk", gt1 - .05, dur=.3, y=-30)
    sfx(gt0 + .05, "impact", -16); sfx(gt0 + .3, "glitch", -22); sfx(gt0 + .55, "whoosh", -24); sfx(gt0 + 1.7, "uiclick", -24)

    # ---------- VENTANA DE PANTALLA: zoom, empuje y anillos ----------
    rings = ""
    for k, r in enumerate(plan.get("anillos", [])):
        col = COL.get(r.get("color", "alerta"), BAD)
        rings += box(f"rg{k}", r["x"], r["y"], r["w"], r["h"], f"border:5px solid {col};border-radius:16px;box-shadow:0 0 28px {col}88;opacity:0;z-index:3")
    capt = ""
    for k, c in enumerate(plan.get("capturas", [])):
        rr = "".join(box(f"cr{k}_{m}", r["x"], r["y"], r["w"], r["h"], f"border:5px solid {COL.get(r.get('color', 'alerta'), BAD)};border-radius:16px;box-shadow:0 0 28px {COL.get(r.get('color', 'alerta'), BAD)}88;opacity:0;z-index:2") for m, r in enumerate(c.get("anillos", [])))
        capt += (f'<div id="cp{k}" style="position:absolute;left:0;top:0;width:{SW}px;height:{SH}px;background:#000;opacity:0;z-index:4">'
                 f'<div id="cpz{k}" style="position:absolute;left:0;top:0;width:{SW}px;height:{SH}px;transform-origin:50% 50%"><img src="{c["archivo"]}" style="position:absolute;left:0;top:0;width:{SW}px;height:{SH}px">{rr}</div></div>')
    HTML.append(f'<div id="sw" style="position:absolute;left:{SX}px;top:{SY}px;width:{SW}px;height:{SH}px;border-radius:30px;overflow:hidden;border:2px solid rgba(255,255,255,.14);box-shadow:0 30px 70px -26px rgba(0,0,0,.9);z-index:6">'
                f'<div id="scz" style="position:absolute;left:0;top:0;width:{SW}px;height:{SH}px;transform-origin:0 0"><video id="vscr" class="clip" src="{plan["pantalla"]}" muted playsinline data-start="0" data-duration="{DUR}" data-track-index="0" style="position:absolute;left:0;top:0;width:{SW}px;height:{SH}px"></video>{rings}</div>{capt}</div>')
    def tf(esc_, cx, cy):
        tx = min(0, max(SW - esc_ * SW, SW / 2 - esc_ * cx)); ty = min(0, max(SH - esc_ * SH, SH / 2 - esc_ * cy)); return tx, ty
    js.append('tl.set("#scz",{x:0,y:0,scale:1},0);')
    em = plan.get("empuje")
    if em:
        tx, ty = tf(em["escala"], em["cx"], em["cy"])
        js.append(f'tl.to("#scz",{{scale:{em["escala"]},x:{tx:.1f},y:{ty:.1f},duration:{em["t1"] - em["t0"]:.2f},ease:"power1.inOut"}},{em["t0"]:.2f});')
        js.append(f'tl.to("#scz",{{scale:1,x:0,y:0,duration:.4,ease:"power3.inOut"}},{em["t1"] + .05:.2f});')
    for z in plan.get("pantalla_zooms", []):
        tx, ty = tf(z["escala"], z["cx"], z["cy"])
        js.append(f'tl.to("#scz",{{scale:{z["escala"]},x:{tx:.1f},y:{ty:.1f},duration:.45,ease:"power3.inOut"}},{z["t"]:.2f});')
        js.append(f'tl.to("#scz",{{scale:1,x:0,y:0,duration:.4,ease:"power3.inOut"}},{z["hasta"]:.2f});'); sfx(z["t"], "whoosh", -26)
    for k, r in enumerate(plan.get("anillos", [])):
        js.append(f'tl.fromTo("#rg{k}",{{opacity:0,scale:1.5}},{{opacity:1,scale:1,duration:.3,ease:"back.out(2)"}},{r["t"]:.2f});')
        js.append(f'tl.to("#rg{k}",{{scale:1.04,duration:.4,yoyo:true,repeat:3,ease:"sine.inOut"}},{r["t"] + .35:.2f});')
        js.append(f'tl.to("#rg{k}",{{opacity:0,duration:.25}},{r["hasta"]:.2f});'); sfx(r["t"], "uiclick", -24)

    for k, c in enumerate(plan.get("capturas", [])):
        t0, t1 = float(c["t"]), float(c["fin"])
        js.append(f'tl.fromTo("#cp{k}",{{opacity:0,x:90}},{{opacity:1,x:0,duration:.28,ease:"power3.out"}},{t0:.2f});tl.to("#cp{k}",{{opacity:0,duration:.2,ease:"power2.in"}},{t1 - .2:.2f});')
        js.append(f'tl.fromTo("#cpz{k}",{{scale:1}},{{scale:{c.get("empuje", 1.05)},duration:{t1 - t0:.2f},ease:"none"}},{t0:.2f});'); sfx(t0, "whoosh", -24)
        for m, r in enumerate(c.get("anillos", [])):
            js.append(f'tl.fromTo("#cr{k}_{m}",{{opacity:0,scale:1.5}},{{opacity:1,scale:1,duration:.3,ease:"back.out(2)"}},{r["t"]:.2f});tl.to("#cr{k}_{m}",{{opacity:0,duration:.2}},{r["hasta"]:.2f});'); sfx(r["t"], "uiclick", -22)

    # ---------- FRANJA DE DATOS ----------
    fe_html = ""
    for k, e in enumerate(plan.get("eventos", [])):
        t0, t1, tp = float(e["t"]), float(e["fin"]), e["tipo"]; col = COL.get(e.get("color", "acento"), AC); i = f"fe{k}"
        pan = f"position:absolute;left:0;top:0;width:{SW}px;height:{FH}px;opacity:0;background:{PN};border:2px solid rgba(255,255,255,.12);border-radius:32px;"
        if tp == "texto":
            inner = (f'<div style="display:flex;align-items:center;gap:30px;height:100%;padding:0 36px">{ic(e.get("icono", "warning"), 110, col)}'
                     f'<div style="display:flex;flex-direction:column;gap:6px"><div style="font-weight:900;font-size:{fit(e["l1"], 56, 740)}px;line-height:1.05;white-space:nowrap;color:{TX}">{esc(e["l1"])}</div>'
                     + (f'<div style="font-weight:800;font-size:{fit(e["l2"], 38, 740, f=.8)}px;color:{col};white-space:nowrap">{esc(e["l2"])}</div>' if e.get("l2") else "") + '</div></div>')
            fe_html += f'<div id="{i}" style="{pan}">{inner}</div>'
        elif tp == "pasos":
            mk = e.get("icono_pasos")
            def _chip(j):
                if mk: return f'<div style="background:{BAD if mk == "cross" else OK};width:56px;height:56px;border-radius:16px;display:flex;align-items:center;justify-content:center">{ic(mk, 34, DARK)}</div>'
                return f'<div style="background:{AC};color:{DARK};font-weight:900;font-size:34px;width:56px;height:56px;border-radius:16px;text-align:center;line-height:56px">{j + 1}</div>'
            rows = "".join(f'<div id="{i}r{j}" style="display:flex;align-items:center;gap:20px;height:62px">{_chip(j)}<div style="font-weight:900;font-size:{fit(s, 40, 780)}px;white-space:nowrap;{"text-decoration:line-through;text-decoration-thickness:4px;color:" + MU + ";" if mk == "cross" else ""}">{esc(s)}</div></div>' for j, s in enumerate(e["items"]))
            fe_html += f'<div id="{i}" style="{pan}"><div style="display:flex;flex-direction:column;justify-content:center;gap:10px;height:100%;padding:0 36px">{rows}</div></div>'
        elif tp == "stats":
            n = len(e["items"]); cw = int((SW - 20 * (n - 1) - 40) / n); cards = ""
            for j, it in enumerate(e["items"]):
                c2 = COL.get(it.get("color", "acento"), AC)
                cards += (f'<div id="{i}c{j}" style="width:{cw}px;height:100%;display:flex;flex-direction:column;justify-content:center;gap:6px;padding:0 22px">'
                          f'<div style="font-weight:900;font-size:{fit(it["valor"], 104, cw - 40, f=.8, piso=60)}px;line-height:1;color:{c2}">{esc(it["valor"])}</div>'
                          f'<div style="font-weight:900;font-size:{fit(it["etiqueta"], 36, cw - 40, f=.8)}px;color:{TX};white-space:nowrap">{esc(it["etiqueta"])}</div>'
                          + (f'<div style="height:16px;border-radius:8px;background:rgba(255,255,255,.14);overflow:hidden;margin-top:4px"><div id="{i}b{j}" style="width:{it["pct"]}%;height:100%;background:{c2};border-radius:8px;transform-origin:0 50%"></div></div>' if it.get("pct") is not None else "") + '</div>')
            fe_html += f'<div id="{i}" style="{pan}"><div style="display:flex;align-items:center;height:100%;padding:0 10px;gap:20px">{cards}</div></div>'
        elif tp == "sello":
            fe_html += (f'<div id="{i}" style="position:absolute;left:0;top:0;width:{SW}px;height:{FH}px;opacity:0;display:flex;align-items:center;justify-content:center"><div style="border:10px solid {col};border-radius:26px;background:{PN}f2;color:{col};padding:10px 44px;display:flex;align-items:center;gap:24px;font-weight:900;font-size:{fit(e["texto"], 78, 860, f=.8)}px;white-space:nowrap">{ic(e.get("icono", "check"), 84, col)}{esc(e["texto"])}</div></div>')
        elif tp == "comparar":
            def fila(j, it):
                c2 = COL.get(it.get("color", "alerta"), BAD)
                return (f'<div style="display:flex;align-items:center;gap:20px;height:62px"><div style="width:330px;font-weight:900;font-size:{fit(it["etiqueta"], 32, 320, f=.8)}px;white-space:nowrap">{esc(it["etiqueta"])}</div>'
                        f'<div style="flex:1;height:34px;border-radius:17px;background:rgba(255,255,255,.14);overflow:hidden"><div id="{i}b{j}" style="width:{it["pct"]}%;height:100%;background:{c2};border-radius:17px;transform-origin:0 50%"></div></div>'
                        f'<div style="width:120px;text-align:right;font-weight:900;font-size:46px;color:{c2}">{it["pct"]}%</div></div>')
            fe_html += (f'<div id="{i}" style="{pan}"><div style="display:flex;flex-direction:column;justify-content:center;gap:8px;height:100%;padding:0 36px">'
                        f'<div style="display:flex;align-items:center;gap:16px;height:52px">{ic("warning", 44, BAD)}<div style="font-weight:900;font-size:{fit(e["titulo"], 38, 800, f=.8)}px;color:{BAD};white-space:nowrap">{esc(e["titulo"])}</div></div>{fila(0, e["a"])}{fila(1, e["b"])}</div></div>')
        elif tp == "dato":
            fe_html += (f'<div id="{i}" style="{pan}"><div style="display:flex;align-items:center;gap:36px;height:100%;padding:0 40px"><div style="font-weight:900;font-size:{fit(e["valor"], 130, 360, f=.8, piso=70)}px;line-height:1;color:{col}">{esc(e["valor"])}</div>'
                        f'<div style="display:flex;flex-direction:column;gap:12px"><div style="font-weight:900;font-size:{fit(e["etiqueta"], 48, 540, f=.8)}px;white-space:nowrap">{esc(e["etiqueta"])}</div>'
                        + (f'<div style="background:{col};color:{DARK};font-weight:900;font-size:{fit(e["chip"], 34, 520, f=.8)}px;padding:8px 22px;border-radius:30px;white-space:nowrap;align-self:flex-start">{esc(e["chip"])}</div>' if e.get("chip") else "") + '</div></div></div>')
        # animación
        if tp == "sello":
            js.append(f'tl.fromTo("#{i}",{{opacity:0,scale:2.4,rotation:-12}},{{opacity:1,scale:1,rotation:-3,duration:.24,ease:"power4.in"}},{t0:.2f});tl.to("#{i}",{{x:8,duration:.05,yoyo:true,repeat:7,ease:"none"}},{t0 + .25:.2f});')
            sfx(t0, "impact", -20); sfx(t0 + .1, "chime" if e.get("color") == "positivo" else "glitch", -22)
        else:
            fin(f"#{i}", t0, y=40, s=.94, dur=.4, ease="back.out(1.4)"); sfx(t0, "whoosh", -24)
        if tp == "pasos":
            for j in range(len(e["items"])): fin(f"#{i}r{j}", t0 + .3 + j * float(e.get("cada", .9)), x=-40, y=0, dur=.3); sfx(t0 + .3 + j * float(e.get("cada", .9)), "uiclick", -24)
        if tp in ("stats", "comparar"):
            n = len(e["items"]) if tp == "stats" else 2
            for j in range(n):
                tt = t0 + .35 + j * float(e.get("cada", .6))
                js.append(f'tl.fromTo("#{i}b{j}",{{scaleX:0}},{{scaleX:1,duration:.7,ease:"power2.out"}},{tt:.2f});'); sfx(tt, "uiclick", -24)
                if tp == "stats": fin(f"#{i}c{j}", t0 + .15 + j * float(e.get("cada", .6)), y=20, s=.9, dur=.35, ease="back.out(1.6)")
            if tp == "stats": sfx(t0 + .4, "chime" if e["items"][0].get("color") == "positivo" else "uiclick", -22)
        if tp == "dato": sfx(t0 + .2, "chime", -22)
        js.append(f'tl.to("#{i}",{{opacity:0,y:-24,duration:.25,ease:"power2.in"}},{t1 - .25:.2f});')
    HTML.append(f'<div id="fr" style="position:absolute;left:{SX}px;top:{FY}px;width:{SW}px;height:{FH}px;z-index:7">{fe_html}</div>')

    # ---------- CIERRE ----------
    cz = plan.get("cierre")
    if cz and cz.get("zona") == "franja":
        lc = cz["lineas"]; t0 = float(cz["t"])
        cl = (f'<div id="cl" style="position:absolute;left:{SX}px;top:{FY}px;width:{SW}px;height:{FH}px;background:{AC};border-radius:32px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;z-index:12">'
              + "".join(f'<div id="cl{j + 1}" style="font-weight:900;font-size:{fit(s, 70, 900)}px;line-height:1.02;white-space:nowrap;color:{DARK}">{esc(s)}</div>' for j, s in enumerate(lc))
              + (f'<div id="clz" style="margin-top:8px;background:{DARK};color:{AC};font-weight:900;font-size:34px;padding:6px 30px;border-radius:40px;display:flex;align-items:center;gap:12px;white-space:nowrap">{esc(cz["pildora"])} {ic("arrow_up", 36, AC)}</div>' if cz.get("pildora") else "") + '</div>')
        HTML.append(cl)
        fin("#cl", t0, y=60, s=.92, dur=.3, ease="back.out(1.6)")
        for j in range(len(lc)): fin(f"#cl{j + 1}", t0 + .12 + j * .12, y=14, s=.92, dur=.25, ease="back.out(1.8)")
        if cz.get("pildora"): fin("#clz", t0 + .4, y=14, s=.9, dur=.25, ease="back.out(1.8)")
        sfx(t0, "impact", -18); sfx(t0 + .25, "chime", -20)
        cz = None
    if cz:
        lc = cz["lineas"]
        cl = (f'<div id="cl" style="position:absolute;left:{SX}px;top:{SY}px;width:{SW}px;height:{FY + FH - SY}px;background:{PN};border:2px solid rgba(255,255,255,.12);border-radius:40px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:22px;z-index:12">'
              + (f'<div id="cl0" style="background:{AC};color:{DARK};font-weight:900;font-size:34px;padding:8px 30px;border-radius:40px">{esc(cz["tag"])}</div>' if cz.get("tag") else "")
              + "".join(f'<div id="cl{j + 1}" style="font-weight:900;font-size:{fit(s, 96 if j == 0 else 76, 920)}px;line-height:1.04;white-space:nowrap;color:{AC if j == 0 else TX}">{esc(s)}</div>' for j, s in enumerate(lc))
              + f'<div id="clz" style="margin-top:12px;background:{VI};color:#fff;font-weight:900;font-size:42px;padding:16px 44px;border-radius:60px;display:flex;align-items:center;gap:16px;white-space:nowrap">{esc(cz["pildora"])} {ic("arrow_up", 48, "#fff")}</div></div>')
        HTML.append(cl); t0 = float(cz["t"])
        fin("#cl", t0, y=60, s=.92, dur=.45, ease="back.out(1.4)")
        if cz.get("tag"): fin("#cl0", t0 + .15, y=-20, dur=.3)
        for j in range(len(lc)): fin(f"#cl{j + 1}", t0 + .3 + j * .3, y=26, s=.9, dur=.4, ease="back.out(1.8)")
        fin("#clz", t0 + .3 + len(lc) * .3 + .2, y=30, dur=.4, ease="back.out(1.6)")
        js.append(f'tl.to("#clz",{{scale:1.05,duration:.4,yoyo:true,repeat:3,ease:"sine.inOut"}},{t0 + 1.6:.2f});')
        sfx(t0, "whoosh", -20); sfx(t0 + .35, "impact", -18); sfx(t0 + 1.4, "chime", -20)
        js.append(f'tl.to("#camz",{{scale:1.07,duration:{DUR - t0:.2f},ease:"none"}},{t0:.2f});')

    # ---------- cámara: zooms ----------
    js.append('tl.set("#camz",{scale:1},0);')
    zs = float(plan.get("camara_zoom_escala", 1.1))
    for t in plan.get("camara_zooms", []):
        js.append(f'tl.to("#camz",{{scale:{zs},duration:.28,ease:"power3.out"}},{t:.2f});tl.to("#camz",{{scale:1,duration:.35,ease:"power2.inOut"}},{t + 2.4:.2f});')

    _st = False
    for t in plan.get("camara_cortes", []):
        _st = not _st; js.append(f'tl.to("#camz",{{scale:{zs if _st else 1},duration:.12,ease:"power3.out"}},{float(t):.2f});')

    # ---------- subtítulos ----------
    KEY = {re.sub(r"[^\wáéíóúñü%]", "", k.lower()) for k in plan.get("claves", [])}
    def norm(w): return re.sub(r"[^\wáéíóúñü%]", "", w.lower())
    groups, cur = [], []
    for k, x in enumerate(W):
        cur.append(x); end_p = x["w"].rstrip().endswith((".", ",", "?", "!", ":", ";"))
        gap = (W[k + 1]["s"] - x["e"]) > .45 if k + 1 < len(W) else True
        if len(cur) >= 3 or end_p or gap: groups.append(cur); cur = []
    if cur: groups.append(cur)
    caps, capjs, wid = [], [], 0
    ctop = CY + CH - 220
    for gi, gr in enumerate(groups):
        s0 = gr[0]["s"]; nxt = groups[gi + 1][0]["s"] if gi + 1 < len(groups) else gr[-1]["e"] + .4
        e0 = min(nxt, gr[-1]["e"] + .45) if gi + 1 < len(groups) else gr[-1]["e"] + .35; e0 = max(e0, s0 + .15)
        parts, estw = [], 0
        for x in gr:
            key = norm(x["w"]) in KEY; tx_ = x["w"].upper() if key else x["w"]; sz = 80 if key else 60
            estw += len(tx_) * (0.78 if key else 0.6) * sz + 22; parts.append((x, key, tx_, sz))
        k = min(1, 940 / estw) if estw > 940 else 1; spans = ""
        for x, key, tx_, sz in parts:
            sz2 = max(40, int(sz * k))
            spans += f'<span id="cw{wid}" class="cw" style="font-size:{sz2}px;font-weight:{900 if key else 800};{"color:" + AC + ";" if key else ""}">{esc(tx_)}</span>'
            if key: capjs.append(f'tl.fromTo("#cw{wid}",{{opacity:0,scale:.4,y:30,rotation:-4}},{{opacity:1,scale:1.06,y:0,rotation:0,duration:.2,ease:"back.out(2.6)"}},{x["s"]:.2f}).to("#cw{wid}",{{scale:1,duration:.2,ease:"power2.out"}},{x["s"] + .2:.2f});')
            else: capjs.append(f'tl.fromTo("#cw{wid}",{{opacity:0,scale:.6,y:22}},{{opacity:1,scale:1,y:0,duration:.16,ease:"back.out(2)"}},{x["s"]:.2f});')
            wid += 1
        caps.append(f'<div id="cp{gi}" class="cap clip" data-start="{s0:.2f}" data-duration="{e0 - s0:.2f}" data-track-index="9"><div class="capin">{spans}</div></div>')

    CSS = f"""
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1920px;overflow:hidden;background:{BG}}}
#root{{position:relative;width:1080px;height:1920px;overflow:hidden;background:{BG};font-family:'{FONT}',sans-serif;color:{TX}}}
#bg{{position:absolute;inset:0;background:radial-gradient(900px 700px at 85% 10%,rgba(139,92,255,.30),rgba(0,0,0,0) 70%),radial-gradient(800px 700px at 8% 78%,rgba(255,210,63,.10),rgba(0,0,0,0) 70%),{BG}}}
#cam{{position:absolute;left:0;top:{CY}px;width:1080px;height:{CH}px;overflow:hidden;z-index:5}}
#camz{{position:absolute;left:0;top:0;width:1080px;height:{CH}px;transform-origin:540px 230px}}
#vface{{position:absolute;left:0;top:0;width:1080px;height:{CH}px}}
#shade{{position:absolute;left:0;right:0;top:{CY + CH - 280}px;height:280px;background:linear-gradient(180deg,rgba(0,0,0,0),rgba(0,0,0,.62));z-index:20}}
.cap{{position:absolute;left:30px;right:30px;top:{ctop}px;height:110px;z-index:30}}
.capin{{position:absolute;inset:0;display:flex;flex-wrap:nowrap;align-items:center;justify-content:center;gap:0 22px;text-align:center}}
.cw{{display:inline-block;font-family:'{FONT}',sans-serif;line-height:1.08;color:#fff;text-shadow:0 5px 22px rgba(0,0,0,.9);white-space:nowrap}}
"""
    html = f'''<!doctype html>
<html lang="es"><head><meta charset="UTF-8" /><meta name="viewport" content="width=1080, height=1920" />
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
<style>{CSS}</style></head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{DUR}" data-width="1080" data-height="1920">
<div id="bg"></div>
{"".join(HTML)}
<div id="cam"><div id="camz"><video id="vface" class="clip" src="{plan["camara"]}" muted playsinline data-start="0" data-duration="{DUR}" data-track-index="1"></video></div></div>
<div id="shade"></div>
{"".join(caps)}
<audio id="mix" class="clip" src="{plan.get("audio", "assets/mix.wav")}" data-start="0" data-duration="{DUR}" data-volume="1" data-track-index="2"></audio>
</div>
<script>
window.__timelines = window.__timelines || {{}};
const tl = gsap.timeline({{paused:true}});
{chr(10).join(js)}
{chr(10).join(capjs)}
window.__timelines["main"] = tl;
tl.seek(0);
</script>
</body></html>
'''
    open(os.path.join(D, "index.html"), "w", encoding="utf-8").write(html)
    SFX.sort(key=lambda e: e[0])
    json.dump(SFX, open(os.path.join(D, "sfx_eventos.json"), "w", encoding="utf-8"))
    voz_fin = max(x["e"] for x in W)
    json.dump({"dur": DUR, "voz": "assets/voz_limpia.wav", "musica": "assets/musica.wav", "efectos_dir": "assets/sfx", "eventos": "sfx_eventos.json",
               "salida": "assets/mix.wav", "pico_voz": -3, "pico_musica": -26,
               "riser": {"archivo": "riser.wav", "termina": float(plan["cierre"]["t"]) - .1 if plan.get("cierre") else voz_fin, "pico": -24}}, open(os.path.join(D, "mezcla.json"), "w", encoding="utf-8"), indent=1)
    print(f"index.html {len(html)} bytes · {len(caps)} subtítulos · {len(SFX)} efectos · {len(plan.get('eventos', []))} tarjetas")

if __name__ == "__main__":
    main()
