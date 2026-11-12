#!/usr/bin/env python3
"""Extrae los colores dominantes REALES de un logo/imagen (para el ADN de marca).

Uso:  python extraer_paleta.py logo.png [cantidad]
Requiere Pillow (pip install pillow). Ignora píxeles transparentes y casi blancos/negros de relleno.
Muestra HEX, porcentaje y luminancia, y el contraste contra blanco y contra casi negro.
"""
import sys

try:
    from PIL import Image
except ImportError:
    print("Falta Pillow: pip install pillow  (o mira la imagen y marca los HEX como ESTIMADO)")
    sys.exit(1)


def lum(rgb):
    def c(v):
        v /= 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = rgb
    return 0.2126 * c(r) + 0.7152 * c(g) + 0.0722 * c(b)


def contraste(a, b):
    la, lb = lum(a), lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    im = Image.open(sys.argv[1]).convert("RGBA")
    im.thumbnail((200, 200))
    px = [p[:3] for p in im.getdata() if p[3] > 200]
    if not px:
        print("La imagen no tiene píxeles opacos")
        return 1
    q = im.convert("RGB").quantize(colors=max(n * 2, 8), method=Image.Quantize.MEDIANCUT)
    pal = q.getpalette()
    cuentas = sorted(q.getcolors(), reverse=True)
    total = sum(c for c, _ in cuentas)
    visto = []
    print("HEX      %    contraste vs blanco / vs #1a1a1a")
    for cnt, idx in cuentas:
        rgb = tuple(pal[idx * 3: idx * 3 + 3])
        if any(sum(abs(a - b) for a, b in zip(rgb, v)) < 40 for v in visto):
            continue
        visto.append(rgb)
        print("#%02X%02X%02X  %4.1f%%   %.1f / %.1f" % (*rgb, 100 * cnt / total, contraste(rgb, (255, 255, 255)), contraste(rgb, (26, 26, 26))))
        if len(visto) >= n:
            break
    print("\nContraste mínimo recomendado para texto: 4.5. Si no llega, define un tono más oscuro/claro para texto.")


if __name__ == "__main__":
    sys.exit(main())
