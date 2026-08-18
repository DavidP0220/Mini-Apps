#!/usr/bin/env bash
# Instala y configura claude-code-router para usar modelos gratuitos de OpenRouter.
# Uso:  bash tools/router/setup-openrouter.sh sk-or-v1-...
set -euo pipefail

API_KEY="${1:-}"
if [ -z "$API_KEY" ]; then
  echo "Uso: bash tools/router/setup-openrouter.sh <OPENROUTER_API_KEY>" >&2
  exit 1
fi

echo "1/3 Instalando claude-code-router..."
npm install -g @musistudio/claude-code-router

DIR="$HOME/.claude-code-router"
mkdir -p "$DIR"
DESTINO="$DIR/config.json"
[ -f "$DESTINO" ] && cp "$DESTINO" "$DESTINO.bak" && echo "Config anterior respaldada en $DESTINO.bak"

echo "2/3 Escribiendo $DESTINO..."
sed "s|PON_AQUI_TU_OPENROUTER_API_KEY|$API_KEY|" \
  "$(dirname "$0")/config.ejemplo.json" > "$DESTINO"

echo "3/3 Listo."
echo
echo "Para trabajar GRATIS:   ccr code"
echo "Para volver a Claude:   claude"
echo "Cambiar de modelo dentro de la sesion:  /model openrouter,<id-del-modelo>"
