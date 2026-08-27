# ARCHIVO — material fuente inmutable

**Esto no se edita ni se borra jamás.** Se lee. Si hay que corregir algo de aquí, la corrección
vive fuera, en `../base-conocimiento/`, y apunta al original. Ver `../protocolos/PROTOCOLO_ANTIBORRADO.md`.

---

## `2026-08-26_traslado_mindset_mechanics/`

**Origen:** paquete de traslado completo del proyecto anterior (canal Mindset Mechanics),
entregado por David el 2026-08-27 como archivo comprimido. Generado el 2026-08-26 por la sesión
de trabajo anterior con el propósito explícito de no perder nada al cambiar de cuenta.

**Contiene (142 archivos, 18 MB):**

| Carpeta | Qué es |
|---|---|
| `00_LEEME_PRIMERO_INSTRUCCIONES.md` | El documento de traslado original. Empieza por aquí |
| `01_CODIGO_PIPELINE/` | Todo el código de producción: bot de animación, cliente de generación de imágenes, pipeline de voz y ensamblaje, scripts de formato corto, storyboards |
| `02_DOCUMENTOS_ESTRATEGIA_ESTILO/` | Playbooks de monetización y de marca, biblia de estilo visual, diccionario visual, planes de escena, guiones, y la investigación completa de 12 canales monetizados (187 KB) |
| `03_PUENTE_KIMI_CLAUDE_HANDOFFS/` | **Los 28 handoffs y reportes del puente con Kimi Code** (23-26 ago 2026). La memoria real de qué se decidió y por qué |
| `04_MEMORIA_PERSISTENTE_CLAUDE/` | La memoria acumulada de las sesiones anteriores: reglas duras del usuario, alcance del proyecto, preferencias |
| `05_CONFIGURACION_REPO/` | Configuración e instrucciones permanentes del repositorio anterior |
| `06_HISTORIAL_GIT_COMPLETO/` | Bundle con el **historial git completo** (8,1 MB): todos los commits y ramas, incluida una rama que quedó sin fusionar. Se restaura con `git clone <bundle> <destino>` |
| `07_INVENTARIO_MEDIA_PESADA_NO_INCLUIDA.txt` | Lista de los **671 archivos** de video/audio/imagen que no cabían: ruta exacta y tamaño de cada uno |

**Qué NO está aquí, y dónde está:** ~1,3 GB de video, audio e imágenes ya generados. No se
omitieron en silencio: están inventariados uno a uno en `07_INVENTARIO...txt`. Viven en el disco
de David. **Riesgo abierto (error E-10):** buena parte de ese material (~669 MB) no tiene copia
en ningún otro sitio, y las plataformas que lo generaron borran los originales a los 60 días.

## Cambios hechos al archivar (los únicos, y por qué)
Se renombraron los archivos de configuración de git que venían dentro del paquete
(`.gitignore` → `_gitignore_ARCHIVADO.txt`, `.gitattributes` → `_gitattributes_ARCHIVADO.txt`,
`.env.example` → `_env.example_ARCHIVADO.txt`). Su contenido está intacto: solo se les quitó el
nombre funcional para que no silencien archivos dentro del propio archivo (error E-11).
Ningún otro archivo se movió, se renombró ni se editó.

## Cómo se añade material nuevo
Carpeta nueva `<fecha>_<origen>/` con el material **íntegro**, más una sección en este mismo
documento diciendo de dónde vino, qué contiene y qué falta. Nunca se mezcla con material ya
archivado.
