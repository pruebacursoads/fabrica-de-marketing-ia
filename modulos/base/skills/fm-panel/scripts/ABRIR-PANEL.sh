#!/bin/sh
# Abre tu Panel en vivo (con subida de archivos). Cópialo dentro de la carpeta Panel/.
cd "$(dirname "$0")" || exit 1
if command -v python3 >/dev/null 2>&1; then exec python3 servidor.py; fi
if command -v python >/dev/null 2>&1; then exec python servidor.py; fi
echo "No encuentro Python. Abre Panel/index.html para ver el Panel sin subida de archivos."
