#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# armar-traslado.sh
#
# Toma la carpeta ya fusionada de un paquete de traslado (la que sale de
# extraer TODAS las partes en el mismo sitio) y produce un paquete maestro
# organizado, listo para entregarselo a otra cuenta de Claude:
#
#   TRASLADO_..._COMPLETO_<fecha>/
#     LEEME_PRIMERO.md            <- como se abre este paquete y por donde empezar
#     ESTADO_DEL_TRASLADO.md      <- donde esta el proyecto, que entro y que no
#     INVENTARIO_COMPLETO.md      <- TODOS los archivos, con ruta y tamano
#     MANIFIESTO_SHA256.txt       <- huella de cada archivo
#     UNICOS_EN_ZIPS_INTERNOS.md  <- lo que solo vivia dentro de zips anidados
#     paquetes/*.zip              <- una carpeta del origen por zip (o dos: docs / assets)
#
#   envios/                       <- el mismo paquete partido en volumenes para chat
#
# Los zips de paquetes/ guardan las rutas TAL CUAL estaban en el origen: si se
# extraen todos en una misma carpeta, se reconstruye el arbol original exacto.
#
# Uso:
#   bash tools/traslado/armar-traslado.sh <carpeta_fusionada> <carpeta_salida> [fecha] [nombre]
#
# Necesita: zip, unzip, sha256sum, find, awk. Corre en Linux/macOS (o Git Bash / WSL).
# ---------------------------------------------------------------------------
set -euo pipefail

SRC="${1:?falta la carpeta fusionada de origen}"
OUT="${2:?falta la carpeta de salida}"
FECHA="${3:-$(date +%F)}"
NOMBRE="${4:-TRASLADO_MINDSET_MECHANICS_COMPLETO_${FECHA}}"

SRC="$(cd "$SRC" && pwd)"
mkdir -p "$OUT"; OUT="$(cd "$OUT" && pwd)"

BASE="$OUT/$NOMBRE"
PAQ="$BASE/paquetes"
LIMITE_MB=20            # tamano objetivo por zip, para poder mandarlos por chat

rm -rf "$BASE" "$OUT/$NOMBRE.zip" "$OUT/envios"
mkdir -p "$PAQ"

# extensiones que pesan y no comprimen: se separan de lo legible
es_media() {
  case "${1,,}" in
    *.png|*.jpg|*.jpeg|*.gif|*.webp|*.bmp|*.tif|*.tiff|\
    *.mp3|*.wav|*.m4a|*.ogg|*.flac|\
    *.mp4|*.mov|*.webm|*.mkv|*.avi) return 0 ;;
    *) return 1 ;;
  esac
}

# zipea, desde $2, la lista de rutas que llega por stdin (una por linea)
zip_lista() { (cd "$2" && zip -q -X -@ "$1"); }

# parte una lista de rutas en grupos de <= LIMITE_MB y crea un zip por grupo.
#   $1 = raiz   $2 = archivo con la lista   $3 = prefijo del zip
# Si cabe en un solo grupo, el zip va sin sufijo de parte.
zip_por_volumenes() {
  local raiz="$1" lista="$2" prefijo="$3"
  [ -s "$lista" ] || return 0
  local grupos="$OUT/_grupos.tmp"; : > "$grupos"
  local g=0 acc=0 lim=$((LIMITE_MB*1024*1024)) f sz
  while IFS= read -r f; do
    sz=$(stat -c %s "$raiz/$f")
    if [ "$acc" -gt 0 ] && [ $((acc + sz)) -gt "$lim" ]; then g=$((g+1)); acc=0; fi
    acc=$((acc + sz))
    printf '%s\t%s\n' "$g" "$f" >> "$grupos"
  done < "$lista"
  local total=$((g+1)) gi n destino
  for gi in $(seq 0 "$g"); do
    n=$((gi+1))
    if [ "$total" -eq 1 ]; then destino="${prefijo}.zip"
    else destino="${prefijo}_parte_${n}_de_${total}.zip"; fi
    awk -F'\t' -v g="$gi" '$1==g {print $2}' "$grupos" | zip_lista "$destino" "$raiz"
    echo "     $(basename "$destino")"
  done
  rm -f "$grupos"
}

# --- 0. copia de trabajo y limpieza de duplicados ---------------------------
# El arbol de origen no se toca. Se trabaja sobre una copia, se le quitan los
# archivos repetidos (casi la mitad del peso lo eran) y se deja constancia de
# cada borrado en DUPLICADOS_ELIMINADOS.md.
echo "==> copia de trabajo"
TRABAJO="$OUT/_arbol_tmp"
rm -rf "$TRABAJO"; mkdir -p "$TRABAJO"
cp -a "$SRC/." "$TRABAJO/"

echo "==> quitando duplicados"
HERRAMIENTAS="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python3 "$HERRAMIENTAS/deduplicar.py" "$TRABAJO" \
  "$BASE/DUPLICADOS_ELIMINADOS.md" "$BASE/VERSIONES_DEL_MISMO_DOCUMENTO.md"

SRC="$TRABAJO"

# --- 0.bis. desempaquetar los zips anidados que hayan sobrevivido -----------
# Dentro del origen hay .zip con documentos que NO existen sueltos en el arbol.
# Se extraen aparte para que nadie tenga que abrir zips dentro de zips.
echo "==> abriendo los zips anidados que quedan"
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
  echo "     $nombre ($(find "$destino" -type f | wc -l) archivos)"
done < <(cd "$SRC" && find . -type f -iname '*.zip' | sed "s|^\./|$SRC/|")

# --- 1. un zip por carpeta del origen ---------------------------------------
# Regla: si la carpeta tiene media pesada, se parte en dos (__DOCS_Y_CODIGO y
# __ASSETS); si no, va entera en un solo zip. Asi cada tema queda separado y lo
# legible se puede abrir sin descargar los 100 MB de imagenes.
lista_txt="$OUT/_txt.tmp"; lista_bin="$OUT/_bin.tmp"

echo "==> armando un zip por carpeta"
# archivos sueltos en la raiz del origen (LEEME, inventario del autor, etc.)
: > "$lista_txt"
while IFS= read -r f; do echo "$f" >> "$lista_txt"; done \
  < <(cd "$SRC" && find . -maxdepth 1 -type f -printf '%P\n' | sort)
if [ -s "$lista_txt" ]; then
  echo "  00_RAIZ_INDICES_DEL_AUTOR"
  zip_por_volumenes "$SRC" "$lista_txt" "$PAQ/00_RAIZ_INDICES_DEL_AUTOR"
fi

while IFS= read -r dir; do
  : > "$lista_txt"; : > "$lista_bin"
  while IFS= read -r f; do
    if es_media "$f"; then echo "$f" >> "$lista_bin"; else echo "$f" >> "$lista_txt"; fi
  done < <(cd "$SRC" && find "$dir" -type f | sort)

  echo "  $dir"
  if [ -s "$lista_bin" ] && [ -s "$lista_txt" ]; then
    zip_por_volumenes "$SRC" "$lista_txt" "$PAQ/${dir}__DOCS_Y_CODIGO"
    zip_por_volumenes "$SRC" "$lista_bin" "$PAQ/${dir}__ASSETS"
  elif [ -s "$lista_bin" ]; then
    zip_por_volumenes "$SRC" "$lista_bin" "$PAQ/${dir}__ASSETS"
  else
    zip_por_volumenes "$SRC" "$lista_txt" "$PAQ/${dir}"
  fi
done < <(cd "$SRC" && find . -mindepth 1 -maxdepth 1 -type d -printf '%P\n' | sort)

(cd "$DESEMP" && find . -type f -printf '%P\n' | sort) > "$lista_txt"
if [ -s "$lista_txt" ]; then
  echo "  ZZ_PAQUETES_INTERNOS_DESEMPAQUETADOS"
  zip_por_volumenes "$DESEMP" "$lista_txt" "$PAQ/ZZ_PAQUETES_INTERNOS_DESEMPAQUETADOS"
fi

rm -f "$lista_txt" "$lista_bin"

# --- 2. inventario -----------------------------------------------------------
echo "==> inventario"
{
  echo "# INVENTARIO COMPLETO — $NOMBRE"
  echo
  echo "Todos los archivos que viajan en este traslado, con su ruta original y su"
  echo "tamano en bytes. Si algo no esta en esta lista, no esta en el paquete."
  echo
  echo "## A. Arbol original del paquete de traslado"
  echo
  echo '```'
  (cd "$SRC" && find . -type f -printf '%10s  %P\n' | sort -k2)
  echo '```'
  echo
  if [ -n "$(ls -A "$DESEMP")" ]; then
    echo "## B. Contenido de los zips internos que se conservaron"
    echo
    echo "Estos archivos vivian DENTRO de un .zip del arbol y ademas no existen"
    echo "sueltos, por eso se extraen aparte."
    echo
    echo '```'
    (cd "$DESEMP" && find . -type f -printf '%10s  %P\n' | sort -k2)
    echo '```'
  else
    echo "## B. Zips internos"
    echo
    echo "Ninguno. Todos los .zip anidados eran copias comprimidas de archivos que"
    echo "ya estaban sueltos en el arbol, asi que se eliminaron; el detalle esta en"
    echo "DUPLICADOS_ELIMINADOS.md. No hay que abrir zips dentro de zips."
  fi
} > "$BASE/INVENTARIO_COMPLETO.md"

# --- 3. manifiesto de huellas ------------------------------------------------
echo "==> manifiesto SHA-256"
{
  echo "# MANIFIESTO SHA-256 — $NOMBRE"
  echo "# Verificar con:  sha256sum -c MANIFIESTO_SHA256.txt"
  echo "# ---- arbol original ----"
  (cd "$SRC" && find . -type f -print0 | sort -z | xargs -0 sha256sum | sed 's|  \./|  |')
  echo "# ---- zips internos desempaquetados ----"
  (cd "$DESEMP" && find . -type f -print0 | sort -z | xargs -0 sha256sum | sed 's|  \./|  _DESEMPAQUETADOS/|')
} > "$BASE/MANIFIESTO_SHA256.txt"

# --- 4. que existe SOLO dentro de los zips internos --------------------------
# Este es el riesgo real de perder informacion: documentos que no existen
# sueltos en ninguna carpeta y solo viven dentro de un .zip anidado.
h_arbol="$OUT/_h_arbol.tmp"; h_desemp="$OUT/_h_desemp.tmp"
(cd "$SRC" && find . -type f -print0 | xargs -0 sha256sum) | awk '{print $1}' | sort -u > "$h_arbol"
(cd "$DESEMP" && find . -type f -print0 | xargs -0 sha256sum) | sed 's|  \./|  |' > "$h_desemp"
{
  echo "# Archivos que SOLO existen dentro de los zips internos"
  echo
  echo "Comparacion por huella SHA-256 del contenido: estos archivos no aparecen"
  echo "sueltos en ninguna parte del arbol original. Si alguien hubiera copiado"
  echo "solo las carpetas sin abrir los .zip, los habria perdido."
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

# --- 5. documentos de arranque ----------------------------------------------
PLANTILLAS="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/plantillas"
for doc in LEEME_PRIMERO.md ESTADO_DEL_TRASLADO.md; do
  sed -e "s/{{FECHA}}/$FECHA/g" \
      -e "s/{{N_ARBOL}}/$n_arbol/g" \
      -e "s/{{N_DESEMP}}/$n_desemp/g" \
      -e "s/{{N_UNICOS}}/$n_unicos/g" \
      -e "s/{{PESO}}/$peso/g" \
      "$PLANTILLAS/$doc" > "$BASE/$doc"
done

# --- 6. zip maestro ----------------------------------------------------------
echo "==> zip maestro"
(cd "$OUT" && zip -q -r -X "$NOMBRE.zip" "$NOMBRE")

# --- 7. envios: el mismo paquete partido en volumenes ------------------------
# El zip maestro pesa demasiado para mandarlo por chat. Estos volumenes son el
# MISMO paquete: se extraen todos en la misma carpeta y se reconstruye entero.
echo "==> volumenes de envio"
ENV_DIR="$OUT/envios"; mkdir -p "$ENV_DIR"
lista_env="$OUT/_env.tmp"
(cd "$OUT" && find "$NOMBRE" -type f | sort) > "$lista_env"
zip_por_volumenes "$OUT" "$lista_env" "$ENV_DIR/${NOMBRE}" >/dev/null
total_env=$(ls "$ENV_DIR"/*.zip | wc -l)
rm -f "$lista_env"

cat > "$ENV_DIR/COMO_UNIRLOS.txt" <<TXT
COMO USAR ESTAS $total_env PARTES
=================================

Son el mismo paquete completo ($NOMBRE),
partido en $total_env zips para poder mandarlos por chat.
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

rm -rf "$DESEMP" "$TRABAJO"

echo
echo "LISTO"
echo "  zip maestro                 : $OUT/$NOMBRE.zip"
echo "  archivos del arbol original : $n_arbol ($peso)"
echo "  archivos de zips internos   : $n_desemp (de ellos, $n_unicos unicos)"
echo
ls -la "$PAQ"
echo
echo "Envios en: $ENV_DIR"
ls -la "$ENV_DIR"
