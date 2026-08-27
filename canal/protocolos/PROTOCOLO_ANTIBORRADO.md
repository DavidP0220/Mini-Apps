# PROTOCOLO ANTIBORRADO — nada se pierde nunca

El encargo es explícito: *"quiero que tengamos todo guardado y bien documentado donde no se
borre nunca"*. Esto es cómo se cumple.

## Las cuatro reglas
1. **No se borra.** Lo que deja de ser válido se marca, no se elimina:
   `> **OBSOLETO desde YYYY-MM-DD** — reemplazado por <ruta>. Motivo: <una línea>.`
   al principio del documento o de la sección. Se queda donde está.
2. **Append-only en las series.** Métricas, decisiones, bitácora y fuentes **se añaden**. Una fila
   antigua no se corrige: se añade la nueva con su fecha. La historia del número es un dato.
3. **El archivo es inmutable.** Todo lo que entra en `canal/archivo/` se lee y nunca se edita.
   Si hay que corregir algo de ahí, la corrección vive fuera, en la base de conocimiento, y
   apunta al original.
4. **Lo que no cabe, se inventaría.** Un archivo que no puede entrar al repositorio (peso,
   permisos, licencia) se registra en un inventario con su ruta exacta, su tamaño y **en cuántos
   sitios distintos vive**. Nunca se omite en silencio.

## Cuántas copias
Un archivo que existe en **un solo sitio no está respaldado**. Tampoco lo está el que solo vive
en un servicio que borra a los 60 días. Mínimo: repositorio (para lo que cabe) + una copia en
almacenamiento propio en la nube (para lo pesado). Ver error E-10.

## Al archivar material nuevo
1. Se deposita **íntegro** en `canal/archivo/<fecha>_<origen>/`, sin reordenar ni renombrar.
2. Se escribe al lado un `LEEME.md`: de dónde vino, qué contiene, qué falta y por qué.
3. Si trae `.gitignore` o `.gitattributes` propios, **se renombran** (`_gitignore_ARCHIVADO.txt`)
   antes de commitear, o silenciarán archivos dentro del propio archivo (error E-11).
4. Se comprueba con `git status --ignored` que nada quedó fuera, y que el archivo aparece en el
   remoto — no basta con que el commit exista en local.

## Fechas
Tras un `git pull` **todos** los archivos quedan con la fecha del pull: la fecha del sistema de
archivos no es fiable. El orden cronológico real se lee siempre con
`git log --reverse --name-status -- <ruta>`.
