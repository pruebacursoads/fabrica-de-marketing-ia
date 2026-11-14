#!/usr/bin/env python3
"""Vigila en tiempo real lo que el alumno sube o copia (solo librería estándar).

Imprime UNA línea por cada archivo nuevo o cambiado, cuando ya terminó de copiarse:
    SUBIDA paso=vid-clip-01 archivo=Entregables/2026-11-13-tema/video/clips/clip-01.mp4 tam=18.2MB

Pensado para que Claude lo ejecute en segundo plano con la herramienta Monitor (cada línea llega como aviso)
y así revise cada archivo apenas aparece. Además mantiene al día estado/medios.js para el Panel.

Uso:  python Panel/vigilar.py            (queda corriendo; Ctrl+C para detener)
      python Panel/vigilar.py --una-vez  (lista lo que hay ahora y termina)
"""
import os, sys, time

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")  # evita errores con tildes en la consola de Windows
    except Exception:
        pass
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import reportar  # noqa: E402


def main():
    una_vez = "--una-vez" in sys.argv
    panel = reportar.carpeta_panel()
    previo = None if not una_vez else {}
    pendiente = {}
    print("VIGILANDO %s (revisa cada 2 s)" % os.path.dirname(panel), flush=True)
    while True:
        reportar.escribir_medios(panel)
        actual = reportar.aplanar(reportar.escanear(panel))
        if previo is None:
            previo = dict(actual)  # lo que ya existe al arrancar no se anuncia
        else:
            for ruta, sig in actual.items():
                if previo.get(ruta) == sig:
                    continue
                if pendiente.get(ruta) == sig:  # mismo tamaño y fecha en dos lecturas: ya terminó de copiarse
                    previo[ruta] = sig
                    pendiente.pop(ruta, None)
                    print("SUBIDA paso=%s archivo=%s tam=%.1fMB" % (sig[2], ruta, sig[1] / 1048576), flush=True)
                else:
                    pendiente[ruta] = sig
        if una_vez:
            for ruta, sig in sorted(actual.items()):
                print("HAY paso=%s archivo=%s tam=%.1fMB" % (sig[2], ruta, sig[1] / 1048576))
            return 0
        time.sleep(2)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        pass
