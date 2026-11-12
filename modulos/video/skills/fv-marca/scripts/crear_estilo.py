#!/usr/bin/env python3
"""Crea el archivo de estilo del alumno (estilo.json + Reglas-de-estilo.md) a partir de un estilo base y sus respuestas.
   python crear_estilo.py --preset oscuro-pro --nombre "Mi Marca" --handle @mimarca --acento #FF8800 --fuente Poppins --salida "Mi estilo"
   python crear_estilo.py --listar            (muestra los estilos base y las fuentes disponibles)
   Valida la fuente (debe venir incluida en HyperFrames) y avisa si el contraste de colores es débil."""
import argparse, json, os, re, sys

try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass

AQUI = os.path.dirname(os.path.abspath(__file__))
ESTILOS = os.path.join(AQUI, "..", "estilos")
# Fuentes que HyperFrames resuelve por nombre sin archivos extra
FUENTES = ["Montserrat", "Poppins", "Inter", "Outfit", "Nunito", "Oswald", "League Gothic", "Archivo Black", "Playfair Display",
           "EB Garamond", "Lato", "Roboto", "Open Sans", "Space Mono", "IBM Plex Mono", "JetBrains Mono", "Source Code Pro"]
PARES = {"Montserrat": "Montserrat (titulares y texto)", "Poppins": "Poppins (amigable)", "Inter": "Inter (limpia)",
         "Outfit": "Outfit (moderna)", "Nunito": "Nunito (cálida y redondeada)", "Playfair Display": "Playfair Display (elegante, para titulares)"}

def hex_rgb(h):
    h = h.lstrip("#")
    if len(h) == 3: h = "".join(c * 2 for c in h)
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))

def lum(h):
    def c(v):
        v /= 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = hex_rgb(h)
    return 0.2126 * c(r) + 0.7152 * c(g) + 0.0722 * c(b)

def contraste(a, b):
    la, lb = lum(a), lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)

def es_hex(v): return bool(re.fullmatch(r"#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})", v or ""))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--listar", action="store_true")
    ap.add_argument("--preset", default="oscuro-pro")
    ap.add_argument("--nombre"); ap.add_argument("--handle"); ap.add_argument("--eslogan")
    ap.add_argument("--fuente"); ap.add_argument("--acento"); ap.add_argument("--secundario"); ap.add_argument("--fondo"); ap.add_argument("--texto")
    ap.add_argument("--logo", help="ruta al logo (png con fondo transparente es lo ideal)")
    ap.add_argument("--cta"); ap.add_argument("--cta-sub"); ap.add_argument("--tono"); ap.add_argument("--mood", choices=["calma", "energia", "ninguna", "propia"])
    ap.add_argument("--mayusculas", choices=["si", "no"])
    ap.add_argument("--subtitulos-y", type=int)
    ap.add_argument("--salida", default="Mi estilo")
    a = ap.parse_args()
    presets = sorted(f[:-5] for f in os.listdir(ESTILOS) if f.endswith(".json"))
    if a.listar:
        print("Estilos base:", ", ".join(presets)); print("Fuentes disponibles:", ", ".join(FUENTES)); return
    ruta = os.path.join(ESTILOS, a.preset + ".json")
    if not os.path.exists(ruta):
        print(f"No existe el estilo base '{a.preset}'. Disponibles: {', '.join(presets)}"); sys.exit(2)
    e = json.load(open(ruta, encoding="utf-8"))
    avisos = []
    if a.nombre: e["nombre"] = a.nombre
    if a.handle: e["handle"] = a.handle if a.handle.startswith("@") else "@" + a.handle
    if a.eslogan is not None: e["eslogan"] = a.eslogan
    if a.fuente:
        f = next((x for x in FUENTES if x.lower() == a.fuente.lower()), None)
        if f: e["tipografia"]["familia"] = f
        else: avisos.append(f"La fuente '{a.fuente}' no viene incluida en HyperFrames; se mantiene {e['tipografia']['familia']}. Disponibles: {', '.join(FUENTES)}. (Si es imprescindible, hay que agregar el archivo de la fuente al proyecto.)")
    for campo, val in (("acento", a.acento), ("secundario", a.secundario), ("fondo", a.fondo), ("texto", a.texto)):
        if val:
            if es_hex(val): e["colores"][campo] = val.upper() if len(val) == 7 else val
            else: avisos.append(f"El color '{val}' para {campo} no es un código hexadecimal (ejemplo #FF8800); se ignora.")
    if a.logo:
        if os.path.exists(a.logo): e["logo"] = a.logo
        else: avisos.append(f"No encuentro el logo en {a.logo}; se usará el nombre escrito como marca.")
    if a.cta is not None: e["cta"]["texto"] = a.cta
    if a.cta_sub is not None: e["cta"]["sub"] = a.cta_sub
    if a.tono: e["tono"] = a.tono
    if a.mood: e["musica"]["mood"] = a.mood
    if a.mayusculas: e["tipografia"]["mayusculas"] = a.mayusculas == "si"
    if a.subtitulos_y: e["subtitulos"]["y"] = a.subtitulos_y
    c = e["colores"]
    for par, minimo, nombre in ((("texto", "fondo"), 4.5, "texto sobre fondo"), (("acento", "fondo"), 3.0, "acento sobre fondo"), (("texto", "panel"), 4.5, "texto sobre paneles")):
        r = contraste(c[par[0]], c[par[1]])
        if r < minimo: avisos.append(f"Contraste débil en {nombre}: {r:.1f}:1 (mínimo recomendado {minimo}:1). Elige un color más claro u oscuro.")
    os.makedirs(a.salida, exist_ok=True)
    json.dump(e, open(os.path.join(a.salida, "estilo.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    md = f"""# Reglas de estilo · {e['nombre']}

- **Marca:** {e['nombre']} ({e['handle']}) {('· ' + e['eslogan']) if e['eslogan'] else ''}
- **Tipografía:** {e['tipografia']['familia']} (títulos {e['tipografia']['peso_titulo']}, énfasis {e['tipografia']['peso_extra']}){' · mayúsculas' if e['tipografia']['mayusculas'] else ''}
- **Colores:** fondo `{c['fondo']}` · panel `{c['panel']}` · texto `{c['texto']}` · acento `{c['acento']}` · secundario `{c['secundario']}` · positivo `{c['positivo']}` · alerta `{c['alerta']}`
- **Subtítulos:** de {e['subtitulos']['palabras_por_grupo']} palabras, una palabra clave en el color de acento, a la altura y={e['subtitulos']['y']}
- **Tono:** {e['tono']}
- **Cierre (CTA):** {e['cta']['texto']} {('· ' + e['cta']['sub']) if e['cta']['sub'] else ''}
- **Música:** {e['musica']['mood']}
- **Reglas fijas:** ningún texto menor de 28 px · un gráfico por idea · un hueco, un gráfico a la vez · nada tapa la cara · zona segura de la red (nada importante bajo y=1540)
"""
    open(os.path.join(a.salida, "Reglas-de-estilo.md"), "w", encoding="utf-8").write(md)
    print(f"Estilo guardado en {os.path.join(a.salida, 'estilo.json')} (base: {e['preset']})")
    print(f"  Tipografía {e['tipografia']['familia']} · acento {c['acento']} · secundario {c['secundario']} · fondo {c['fondo']}")
    for v in avisos: print("  ⚠ " + v)

if __name__ == "__main__":
    main()
