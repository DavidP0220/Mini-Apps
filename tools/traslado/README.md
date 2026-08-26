# tools/traslado — armado del paquete de traslado

Herramienta para empaquetar un proyecto entero (código, documentación, handoffs y assets)
en **un solo zip maestro organizado**, listo para entregárselo a otra cuenta de Claude que
va a continuar el trabajo.

Se creó para trasladar **Mindset Mechanics**, pero no tiene nada específico de ese proyecto
salvo los nombres de las tres carpetas de primer nivel que agrupa.

## Uso

```bash
bash tools/traslado/armar-traslado.sh <carpeta_fusionada> <carpeta_salida> [fecha]
```

- `<carpeta_fusionada>`: la carpeta que queda al extraer **todas** las partes del origen
  en el mismo sitio.
- `<carpeta_salida>`: dónde se escribe el resultado (usa el scratchpad de la sesión, no el repo).
- `[fecha]`: `AAAA-MM-DD`, por defecto la de hoy. Va en el nombre del paquete.

Requiere `zip`, `unzip`, `sha256sum` y `awk`. Corre en la sesión de Claude (Linux); en
Windows, con Git Bash o WSL.

## Qué produce

```
<salida>/
  TRASLADO_..._COMPLETO_<fecha>.zip        <- el zip maestro, todo dentro
  TRASLADO_..._COMPLETO_<fecha>/           <- el mismo contenido sin comprimir
    LEEME_PRIMERO.md                        por dónde empieza quien recibe
    ESTADO_DEL_TRASLADO.md                  dónde está el proyecto y qué falta
    INVENTARIO_COMPLETO.md                  todos los archivos, con ruta y tamaño
    MANIFIESTO_SHA256.txt                   huella de cada archivo
    UNICOS_EN_ZIPS_INTERNOS.md              lo que solo vivía dentro de zips anidados
    paquetes/*.zip                          el proyecto por temas
  envios/                                   el mismo paquete en volúmenes para mandar por chat
    ..._parte_N_de_M.zip
    COMO_UNIRLOS.txt
```

## Las tres decisiones de diseño que importan

1. **Los zips anidados se abren.** Dentro del origen había `.zip` con documentos que no
   existían sueltos en ninguna carpeta. Copiar solo el árbol los habría perdido. El script
   los extrae aparte y deja constancia de cuáles eran en `UNICOS_EN_ZIPS_INTERNOS.md`.
2. **Las rutas se conservan.** Cada zip de `paquetes/` guarda la ruta original del archivo,
   así que extraerlos todos en una misma carpeta reconstruye el árbol exacto de partida.
3. **Lo pesado se separa de lo legible.** El código y los documentos caben en unos pocos MB
   y se pueden abrir enteros; las imágenes y audios generados van en volúmenes numerados
   aparte. Nada se descarta, solo se ordena por peso.

`LEEME_PRIMERO.md` y `ESTADO_DEL_TRASLADO.md` salen de `plantillas/`, que sí son específicas
de Mindset Mechanics. Para otro proyecto, se reescriben esas dos y el resto sirve igual.
Los marcadores `{{FECHA}}`, `{{N_ARBOL}}`, `{{N_DESEMP}}`, `{{N_UNICOS}}` y `{{PESO}}` los
rellena el script con las cifras reales del corte.

## Verificar que no se perdió nada

```bash
sha256sum -c MANIFIESTO_SHA256.txt
```
