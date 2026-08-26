#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# armar-traslado.sh
#
# Toma la carpeta ya fusionada del paquete de traslado de Mindset Mechanics
# (la que sale de extraer todas las partes TRASLADO_MM_parte_N_de_7.zip en el
# mismo sitio) y produce UN paquete maestro organizado:
#
#   TRASLADO_MINDSET_MECHANICS_COMPLETO_<fecha>/
#     LEEME_PRIMERO.md            <- por donde empieza la otra cuenta de Claude
#     ESTADO_DEL_TRASLADO.md      <- que entro, que falta, como verificar
#     INVENTARIO_COMPLETO.md      <- TODOS los archivos, con ruta y tamano
#     MANIFIESTO_SHA256.txt       <- huella de cada archivo (prueba de que no falta nada)
#     paquetes/
#       01_HANDOFFS_KIMI_CLAUDE.zip
#       02_DOCUMENTACION_Y_MANUALES.zip
#       03_PAQUETES_INTERNOS_DESEMPAQUETADOS.zip
#       04_CODIGO_FUENTE_PIPELINE.zip
#       05_ASSETS_GENERADOS_parte_N_de_M.zip
#
# Los zips 01, 02, 04 y 05 guardan las rutas TAL CUAL estaban en el paquete
# original: si los extraes todos en la misma carpeta, reconstruyes el arbol
# original exacto, sin pisarse ni duplicarse.
#
# Uso:
#   bash tools/traslado/armar-traslado.sh <carpeta_fusionada> <carpeta_salida> [fecha]
#
# Se ejecuta en Linux/macOS (o Git Bash / WSL en Windows). Necesita: zip, unzip,
# sha256sum, find, awk.
# ---------------------------------------------------------------------------
set -euo pipefail

SRC="${1:?falta la carpeta fusionada de origen}"
OUT="${2:?falta la carpeta de salida}"
FECHA="${3:-$(date +%F)}"

SRC="$(cd "$SRC" && pwd)"
mkdir -p "$OUT"; OUT="$(cd "$OUT" && pwd)"

NOMBRE="TRASLADO_MINDSET_MECHANICS_COMPLETO_${FECHA}"
BASE="$OUT/$NOMBRE"
PAQ="$BASE/paquetes"
LIMITE_MB=20            # tamano maximo por zip de assets, para poder mandarlos por chat

rm -rf "$BASE" "$OUT/$NOMBRE.zip"
mkdir -p "$PAQ"

es_binario() {  # extensiones que pesan y no comprimen
  case "${1,,}" in
    *.png|*.jpg|*.jpeg|*.gif|*.webp|*.mp3|*.wav|*.m4a|*.mp4|*.mov|*.webm) return 0 ;;
    *) return 1 ;;
  esac
}

# --- 0. desempaquetar los zips anidados -------------------------------------
# Dentro del paquete original hay zips (PAQUETE_CONOCIMIENTO_*.zip,
# HANDOFF_KIMI_CODE.zip) con documentos que NO existen sueltos en el arbol.
# Se extraen aparte para que nadie tenga que abrir zips dentro de zips.
DESEMP="$OUT/_desempaquetados_tmp"
rm -rf "$DESEMP"; mkdir -p "$DESEMP"
while IFS= read -r z; do
  nombre="$(basename "$z" .zip)"
  destino="$DESEMP/$nombre"
  mkdir -p "$destino"
  unzip -o -q "$z" -d "$destino" 2>/dev/null || true
  # si el zip trae una unica carpeta raiz con el mismo nombre, se aplana
  if [ -d "$destino/$nombre" ] && [ "$(ls -A "$destino" | wc -l)" -eq 1 ]; then
    mv "$destino/$nombre" "$destino.__tmp" && rm -rf "$destino" && mv "$destino.__tmp" "$destino"
  fi
  echo "  desempaquetado: $nombre ($(find "$destino" -type f | wc -l) archivos)"
done < <(cd "$SRC" && find . -type f -iname '*.zip' | sed "s|^\./|$SRC/|")

# --- 1..4. zips tematicos, con rutas relativas al paquete original -----------
zip_desde_lista() {   # $1 = zip destino, $2 = raiz, resto = lista por stdin
  local destino="$1" raiz="$2"
  (cd "$raiz" && zip -q -X -@ "$destino")
}

echo "==> 01_HANDOFFS_KIMI_CLAUDE.zip"
(cd "$SRC" && find "01_HANDOFFS_KIMI_CLAUDE_COMPLETO" -type f 2>/dev/null | sort) \
  | zip_desde_lista "$PAQ/01_HANDOFFS_KIMI_CLAUDE.zip" "$SRC"

echo "==> 02_DOCUMENTACION_Y_MANUALES.zip"
(cd "$SRC" && find "03_DOCUMENTACION_Y_MANUALES" -type f 2>/dev/null | sort) \
  | zip_desde_lista "$PAQ/02_DOCUMENTACION_Y_MANUALES.zip" "$SRC"

echo "==> 03_PAQUETES_INTERNOS_DESEMPAQUETADOS.zip"
(cd "$DESEMP" && find . -type f | sed 's|^\./||' | sort) \
  | zip_desde_lista "$PAQ/03_PAQUETES_INTERNOS_DESEMPAQUETADOS.zip" "$DESEMP"

echo "==> 04_CODIGO_FUENTE_PIPELINE.zip"
lista_codigo="$OUT/_lista_codigo.txt"
: > "$lista_codigo"
while IFS= read -r f; do
  es_binario "$f" || echo "$f" >> "$lista_codigo"
done < <(cd "$SRC" && find "02_CODIGO_PIPELINE" -type f 2>/dev/null | sort)
[ -s "$lista_codigo" ] && zip_desde_lista "$PAQ/04_CODIGO_FUENTE_PIPELINE.zip" "$SRC" < "$lista_codigo"

# --- 5. assets pesados, partidos en volumenes independientes ----------------
echo "==> 05_ASSETS_GENERADOS_*.zip"
lista_assets="$OUT/_lista_assets.txt"
: > "$lista_assets"
while IFS= read -r f; do
  es_binario "$f" && echo "$f" >> "$lista_assets"
done < <(cd "$SRC" && find "02_CODIGO_PIPELINE" -type f 2>/dev/null | sort)

if [ -s "$lista_assets" ]; then
  # reparte los assets en grupos por tamano acumulado (<= LIMITE_MB por zip)
  grupos="$OUT/_grupos.txt"; : > "$grupos"
  g=0; acc=0; lim=$((LIMITE_MB*1024*1024))
  while IFS= read -r f; do
    sz=$(stat -c %s "$SRC/$f")
    if [ "$acc" -gt 0 ] && [ $((acc + sz)) -gt "$lim" ]; then g=$((g+1)); acc=0; fi
    acc=$((acc + sz))
    printf '%s\t%s\n' "$g" "$f" >> "$grupos"
  done < "$lista_assets"

  total_grupos=$((g+1))
  for gi in $(seq 0 "$g"); do
    n=$((gi+1))
    awk -F'\t' -v g="$gi" '$1==g {print $2}' "$grupos" \
      | zip_desde_lista "$PAQ/05_ASSETS_GENERADOS_parte_${n}_de_${total_grupos}.zip" "$SRC"
    echo "  parte ${n}/${total_grupos}"
  done
fi

# --- 6. inventario y manifiesto ---------------------------------------------
echo "==> inventario y manifiesto"
{
  echo "# INVENTARIO COMPLETO — Mindset Mechanics ($FECHA)"
  echo
  echo "Todos los archivos que viajan en este traslado, con su ruta original y su"
  echo "tamano. Si algo no esta en esta lista, no esta en el paquete."
  echo
  echo "## A. Arbol original del paquete de traslado"
  echo
  echo '```'
  (cd "$SRC" && find . -type f -printf '%10s  %P\n' | sort -k2)
  echo '```'
  echo
  echo "## B. Contenido de los zips internos, ya desempaquetado"
  echo
  echo "(estos archivos vivian DENTRO de los .zip listados arriba; varios no"
  echo "existen sueltos en el arbol, por eso se extraen aparte)"
  echo
  echo '```'
  (cd "$DESEMP" && find . -type f -printf '%10s  %P\n' | sort -k2)
  echo '```'
} > "$BASE/INVENTARIO_COMPLETO.md"

{
  echo "# MANIFIESTO SHA-256 — $NOMBRE"
  echo "# Verificar con:  sha256sum -c MANIFIESTO_SHA256.txt"
  echo "# ---- arbol original ----"
  (cd "$SRC" && find . -type f -print0 | sort -z | xargs -0 sha256sum | sed 's|  \./|  |')
  echo "# ---- zips internos desempaquetados ----"
  (cd "$DESEMP" && find . -type f -print0 | sort -z | xargs -0 sha256sum | sed 's|  \./|  _DESEMPAQUETADOS/|')
} > "$BASE/MANIFIESTO_SHA256.txt"

# --- 6.bis. que archivos existen SOLO dentro de los zips internos -----------
# Este es el riesgo real de perder informacion: hay documentos que no existen
# sueltos en el arbol y solo viven dentro de un .zip anidado.
h_arbol="$OUT/_h_arbol.txt"; h_desemp="$OUT/_h_desemp.txt"
(cd "$SRC" && find . -type f -print0 | xargs -0 sha256sum) | awk '{print $1}' | sort -u > "$h_arbol"
(cd "$DESEMP" && find . -type f -print0 | xargs -0 sha256sum) | sed 's|  \./|  |' > "$h_desemp"
{
  echo "# Archivos que SOLO existen dentro de los zips internos"
  echo
  echo "Comparacion por huella SHA-256 del contenido: estos archivos no aparecen"
  echo "sueltos en ninguna parte del arbol original. Si alguien hubiera copiado"
  echo "solo las carpetas y no hubiera abierto los .zip, los habria perdido."
  echo
  echo '```'
  awk 'NR==FNR{h[$1];next} !($1 in h){print $2}' "$h_arbol" "$h_desemp" | sort
  echo '```'
} > "$BASE/UNICOS_EN_ZIPS_INTERNOS.md"
n_unicos=$(awk 'NR==FNR{h[$1];next} !($1 in h){print $2}' "$h_arbol" "$h_desemp" | wc -l)
rm -f "$h_arbol" "$h_desemp"

n_arbol=$(cd "$SRC" && find . -type f | wc -l)
n_desemp=$(cd "$DESEMP" && find . -type f | wc -l)
peso=$(du -sh "$SRC" | cut -f1)

# --- 6.ter. documentos de arranque ------------------------------------------
PLANTILLAS="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/plantillas"
for doc in LEEME_PRIMERO.md ESTADO_DEL_TRASLADO.md; do
  sed -e "s/{{FECHA}}/$FECHA/g" \
      -e "s/{{N_ARBOL}}/$n_arbol/g" \
      -e "s/{{N_DESEMP}}/$n_desemp/g" \
      -e "s/{{N_UNICOS}}/$n_unicos/g" \
      -e "s/{{PESO}}/$peso/g" \
      "$PLANTILLAS/$doc" > "$BASE/$doc"
done

# --- 7. zip maestro ----------------------------------------------------------
echo "==> zip maestro"
(cd "$OUT" && zip -q -r -X "$NOMBRE.zip" "$NOMBRE")

# --- 8. envios: el mismo paquete partido en volumenes <= LIMITE_MB ----------
# El zip maestro pesa demasiado para mandarlo por chat. Estos volumenes son el
# MISMO paquete: se extraen todos en la misma carpeta y se reconstruye entero.
ENV_DIR="$OUT/envios"
rm -rf "$ENV_DIR"; mkdir -p "$ENV_DIR"
lista_env="$OUT/_lista_env.txt"
(cd "$OUT" && find "$NOMBRE" -type f | sort) > "$lista_env"
grupos_env="$OUT/_grupos_env.txt"; : > "$grupos_env"
g=0; acc=0; lim=$((LIMITE_MB*1024*1024))
while IFS= read -r f; do
  sz=$(stat -c %s "$OUT/$f")
  if [ "$acc" -gt 0 ] && [ $((acc + sz)) -gt "$lim" ]; then g=$((g+1)); acc=0; fi
  acc=$((acc + sz))
  printf '%s\t%s\n' "$g" "$f" >> "$grupos_env"
done < "$lista_env"
total_env=$((g+1))
for gi in $(seq 0 "$g"); do
  n=$((gi+1))
  awk -F'\t' -v g="$gi" '$1==g {print $2}' "$grupos_env" \
    | (cd "$OUT" && zip -q -X -@ "$ENV_DIR/${NOMBRE}_parte_${n}_de_${total_env}.zip")
done

cat > "$ENV_DIR/COMO_UNIRLOS.txt" <<TXT
COMO USAR ESTAS $total_env PARTES
=================================

Son el mismo paquete completo ($NOMBRE),
partido en $total_env zips para poder mandarlos por chat (cada uno pesa menos de ${LIMITE_MB} MB).
No falta nada: juntas suman exactamente el mismo contenido que el zip grande.

Pasos:
1. Descarga las $total_env partes (parte_1_de_$total_env hasta parte_${total_env}_de_$total_env).
2. Extrae CADA UNA en la MISMA carpeta destino (por ejemplo, tu Escritorio).
   Todas comparten la misma carpeta raiz interna ("$NOMBRE"),
   asi que al extraerlas en el mismo sitio se juntan solas en una sola carpeta
   completa: no se pisan ni se duplican entre si.
3. Entra en esa carpeta y abre LEEME_PRIMERO.md. Ahi esta todo explicado.
4. Para comprobar que no se perdio nada:  sha256sum -c MANIFIESTO_SHA256.txt
5. Esa carpeta completa es la que se le entrega a la otra cuenta de Claude Max.

Si tu Windows no extrae bien un .zip por separado: clic derecho -> Extraer todo,
uno por uno, apuntando siempre a la misma carpeta destino.
TXT

rm -f "$lista_env" "$grupos_env"

rm -rf "$DESEMP" "$lista_codigo" "$lista_assets" "$OUT/_grupos.txt"

echo
echo "LISTO: $OUT/$NOMBRE.zip"
echo "  archivos del arbol original : $n_arbol ($peso)"
echo "  archivos de zips internos   : $n_desemp"
ls -la "$PAQ"
echo
echo "Envios listos en: $ENV_DIR"
ls -la "$ENV_DIR"
