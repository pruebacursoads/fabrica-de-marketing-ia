#!/usr/bin/env bash
# Fábrica de Marketing con IA — instalador para Mac y Linux
# Uso:  bash instalar.sh
# Elegir niveles:   bash instalar.sh --modulos base,anuncios
# Probar sin tocar tu equipo:   bash instalar.sh --destino /ruta/de/prueba
# Niveles: base | anuncios | video  (por defecto: los tres)
set -euo pipefail

AQUI="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DESTINO="${HOME}/.claude"
MODULOS="base,anuncios,video"
while [ $# -gt 0 ]; do
  case "$1" in
    --destino) DESTINO="$2"; shift 2 ;;
    --modulos) MODULOS="$2"; shift 2 ;;
    *) echo "Opción desconocida: $1"; exit 1 ;;
  esac
done

D_SKILLS="$DESTINO/skills"
D_AGENTES="$DESTINO/agents"
VERSION="$(head -n1 "$AQUI/VERSION" 2>/dev/null || echo "")"
STAMP="$(date +%Y%m%d-%H%M%S)"
RESPALDO="$DESTINO/respaldo-fabrica-marketing/$STAMP"

echo
echo "Fábrica de Marketing con IA $VERSION"
echo "Niveles a instalar: $MODULOS"
echo "Skills en:  $D_SKILLS"
echo "Agentes en: $D_AGENTES"
echo

IFS=',' read -r -a LISTA <<< "$MODULOS"
for m in "${LISTA[@]}"; do
  m="$(echo "$m" | tr '[:upper:]' '[:lower:]' | xargs)"
  [ -d "$AQUI/modulos/$m/skills" ] || { echo "No existe el nivel '$m'. Usa: base, anuncios o video."; exit 1; }
done
case ",$MODULOS," in *,base,*) ;; *) echo "Aviso: sin el nivel 'base' no hay director ni panel. Se recomienda incluirlo." ;; esac

mkdir -p "$D_SKILLS" "$D_AGENTES"
N_SKILLS=0; N_AG=0; N_RESP=0

respaldar() { # $1 = ruta existente, $2 = etiqueta
  mkdir -p "$RESPALDO"
  mv "$1" "$RESPALDO/$2"
  N_RESP=$((N_RESP+1))
  echo "  Ya tenías '$2': la versión anterior quedó en $RESPALDO"
}

for m in "${LISTA[@]}"; do
  m="$(echo "$m" | tr '[:upper:]' '[:lower:]' | xargs)"
  echo "Nivel $m"
  for d in "$AQUI/modulos/$m/skills"/*/; do
    n="$(basename "$d")"
    [ -e "$D_SKILLS/$n" ] && respaldar "$D_SKILLS/$n" "skill-$n"
    cp -R "$d" "$D_SKILLS/$n"
    N_SKILLS=$((N_SKILLS+1))
    echo "  ✔ $n"
  done
  if [ -d "$AQUI/modulos/$m/ejemplos" ] && [ -d "$D_SKILLS/fabrica-de-video" ]; then
    rm -rf "$D_SKILLS/fabrica-de-video/ejemplos"
    cp -R "$AQUI/modulos/$m/ejemplos" "$D_SKILLS/fabrica-de-video/ejemplos"
  fi
done

case ",$MODULOS," in *,base,*)
  echo "Agentes del equipo"
  for f in "$AQUI"/agentes/fm-agente-*.md; do
    n="$(basename "$f")"
    [ -e "$D_AGENTES/$n" ] && respaldar "$D_AGENTES/$n" "agente-$n"
    cp "$f" "$D_AGENTES/$n"
    N_AG=$((N_AG+1))
    echo "  ✔ ${n%.md}"
  done ;;
esac

# Registro de la versión instalada (lo usa la skill fm-actualizar para avisar de novedades)
printf '{"version":"%s","modulos":"%s","fecha":"%s"}
' "$VERSION" "$MODULOS" "$(date +%Y-%m-%d)" > "$DESTINO/fabrica-de-marketing-ia.version.json"
echo
echo "Listo: $N_SKILLS skills y $N_AG agentes instalados ($N_RESP respaldados)."
echo
echo "Siguiente paso:"
echo "  1. Cierra y vuelve a abrir Claude (para que cargue las skills y los agentes)."
echo "  2. Crea una carpeta 'Mi Fábrica de Marketing' en Documentos y abre Claude dentro."
echo "  3. Escribe:  Quiero empezar"
echo
echo "Guía paso a paso: ver README.md"
