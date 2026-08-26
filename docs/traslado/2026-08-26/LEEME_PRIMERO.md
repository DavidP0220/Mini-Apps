# LÉEME PRIMERO — Traslado del proyecto **Mindset Mechanics**

**Paquete maestro `TRASLADO_MINDSET_MECHANICS_COMPLETO_2026-08-26`**
Destino: una cuenta nueva de Claude (plan Max) que va a **continuar** este proyecto, no
empezarlo de cero.

> Este archivo explica **cómo se abre y se verifica el paquete**.
> El documento del proyecto en sí lo escribió David y está en
> `00_RAIZ_INDICES_DEL_AUTOR.zip` → **`LEEME_PRIMERO_TRASLADO.md`**.
> Ese es el que manda sobre alcance, exclusiones y credenciales. Léelo justo después de este.

---

## 1. Qué hay dentro

Todo el proyecto Mindset Mechanics: estrategia, código del pipeline, el historial completo de
handoffs con Kimi Code, la investigación, los storyboards, las memorias persistentes, los 8
agentes de Claude Code y las referencias visuales.

Cifras de este corte: **1377 archivos** (160M), más **246 archivos**
extraídos de los `.zip` que venían anidados dentro del árbol.

Cuatro archivos acompañan al paquete y son la prueba de que no falta nada:

| Archivo | Para qué sirve |
|---|---|
| `INVENTARIO_COMPLETO.md` | Lista de **todos** los archivos con ruta y tamaño. Si algo no está ahí, no está en el paquete. |
| `MANIFIESTO_SHA256.txt` | Huella de cada archivo. Se verifica con `sha256sum -c MANIFIESTO_SHA256.txt`. |
| `UNICOS_EN_ZIPS_INTERNOS.md` | Lo que solo existía dentro de zips anidados. En este corte: **0** — el árbol ya trae suelto todo lo que había dentro de los zips. |
| `ESTADO_DEL_TRASLADO.md` | Dónde está parado el proyecto y qué queda abierto. |

---

## 2. Cómo abrirlo

Dentro de `paquetes/` hay un zip por carpeta del proyecto. Cada uno guarda las rutas **tal cual
estaban en el origen**, así que:

> **Extrae todos los zips de `paquetes/` en una misma carpeta.**
> Se ensamblan solos en el árbol original — no se pisan ni se duplican entre sí.

| Zip | Qué trae |
|---|---|
| `00_RAIZ_INDICES_DEL_AUTOR` | `LEEME_PRIMERO_TRASLADO.md` e `INVENTARIO_ARCHIVOS.md`, escritos por David. **Empieza por aquí.** |
| `01_HANDOFFS_KIMI_CLAUDE_COMPLETO` | **El trabajo con Kimi-Claude completo**: los 27 archivos de `handoffs/` sin excepción, más `HANDOFF_KIMI_CODE.md`, el volcado de 522 KB `HANDOFF_KIMI_CODE_COMPLETO.txt`, `HANDOFF_KIMI_CODE.zip` y `HANDOFF_KIMI_PACKAGE/`. |
| `02_CODIGO_PIPELINE__DOCS_Y_CODIGO` | Todo el código: `recraft_ai/`, `video_express_ai/`, `youtube_pipeline/`, `shorts_final/`, configs, requirements, logs, manifiestos de subtítulos. **133 KB — se abre entero sin problema.** |
| `02_CODIGO_PIPELINE__ASSETS_parte_N` | Las imágenes, frames y voces en off que produjo ese código. |
| `03_DOCUMENTACION_Y_MANUALES__DOCS_Y_CODIGO` | Manuales, playbooks, biblia de estilo, investigaciones, `docs_raiz_repo/`, `PROY_MECH_OPT/` y los paquetes de conocimiento v1, v2 y v3. |
| `03_DOCUMENTACION_Y_MANUALES__ASSETS` | Las imágenes que acompañan a esa documentación. |
| `04_STORYBOARDS` | `storyboard_resilience_v3_piloto.json` (15 paneles, 94 s) y su versión en Markdown. |
| `05_MEDIA_REFERENCIA__ASSETS_parte_N` | Referencias de personaje, style-locks, badges, stills de Recraft, paneles de cómic y last-frames de las 12 escenas. |
| `06_MEMORIA_PERSISTENTE_CLAUDE` | `MEMORY.md` + 7 memorias del proyecto. **Reprodúcelas en la carpeta de memoria de la cuenta nueva.** |
| `07_AGENTES_CLAUDE_CODE` | Los 8 agentes + `settings.local.json`. **Cópialos a `.claude/agents/`.** |
| `ZZ_PAQUETES_INTERNOS_DESEMPAQUETADOS` | Los 6 `.zip` que venían anidados, ya abiertos, para no tener que descomprimir zips dentro de zips. |

---

## 3. Orden de lectura para la cuenta que recibe esto

1. **`LEEME_PRIMERO_TRASLADO.md`** (zip `00`) — el documento de David: alcance, qué se excluyó
   a propósito, credenciales que hay que rehacer, estado del proyecto.
2. **`ESTADO_DEL_TRASLADO.md`** (aquí al lado) — resumen operativo de dónde está el proyecto.
3. **`06_MEMORIA_PERSISTENTE_CLAUDE/MEMORY.md`** y sus archivos — cómo trabaja David y sus
   reglas duras.
4. **`03_.../docs_raiz_repo/CLAUDE.md`** — el protocolo de handoffs con Kimi Code:
   *"si no está en `handoffs/`, no existe"*.
5. **`ERRORES_QUE_NO_SE_DEBEN_REPETIR.md`**
   (`03_.../PROY_MECH_OPT/PAQUETE_CONOCIMIENTO_v3/`) — 26 errores con causa raíz y arreglo.
   Es el documento que más créditos y semanas ahorra. Léelo entero.
6. **`01_HANDOFFS.../handoffs/`** en orden cronológico — el historial real de decisiones.
   Los cinco archivos del **26-ago** son el último día registrado.
7. **`MANUAL_PRODUCCION.md`** + `SISTEMA_STORYBOARD_MINDSET_MECHANICS.md` +
   `ESTILO_MINDSET_MECHANICS.md` + `DICCIONARIO_VISUAL_MINDSET_MECHANICS.md` —
   **antes de generar una sola imagen.**
8. `02_CODIGO_PIPELINE/` cuando toque ejecutar. Empieza por `youtube_pipeline/README.md`.

---

## 4. Cómo se trabaja este proyecto (para no romper el método)

Cuatro roles, y la separación entre ellos es lo que ha evitado quemar presupuesto:

| Rol | Quién | Qué decide |
|---|---|---|
| Estratega | **Kimi Code** (otro LLM, vía handoffs en git) | Alcance, presupuesto, método |
| Ejecutor técnico | **Claude Code** | Genera, ensambla, reporta. Ejecuta sin improvisar |
| Storyboard Director | Subagente especializado | Convierte el guion en storyboard técnico |
| Gate de calidad | **David** (humano) | Aprueba storyboard y piloto. Su veredicto manda |

El intercambio con Kimi va completo en el zip `01` — **es parte del proyecto, no un anexo**.
Sin él se pierde el porqué de la mitad de las decisiones.

**Las tres reglas de arquitectura que no se negocian:**

1. Ningún video entra a generación **sin storyboard aprobado**.
2. El personaje se genera como **imagen en Recraft**, nunca desde texto en el generador de
   video. La consistencia se resuelve antes de animar, no después.
3. Prohibido sostener un frame congelado más de **4 segundos**. 3-4 sub-clips reales de
   10-18 s por escena, cada uno con plano distinto.

**Reglas de comunicación heredadas:** español siempre con David; el contenido del canal en
inglés · 1080p mínimo, nunca bajar el nivel · investigar en la web antes de parchar · **no
mezclar canales ni proyectos distintos** · nada se planifica sobre una fuente sin verificar ·
nada se ejecuta sin autorización explícita cuando cuesta créditos.

---

## 5. Verificar que no se perdió nada al copiar

```bash
# en la carpeta donde extrajiste TODOS los zips de paquetes/
sha256sum -c MANIFIESTO_SHA256.txt
```

Si algo sale `FAILED` o no aparece, se vuelve a sacar del zip que lo contiene según
`INVENTARIO_COMPLETO.md`.

---

## 6. Seguridad — ya revisado

Se barrió el paquete entero buscando claves (`sk-`, `AIza`, `ghp_`, `xoxb-`, claves privadas,
`.env` reales, `auth_state.json`, archivos con `token`/`secret`/`credential` en el nombre):
**cero resultados**. Solo viajan los `.env.example` con los nombres de las variables y ningún
valor. Las credenciales hay que rehacerlas en el PC nuevo — la lista está en el §5 del
`LEEME_PRIMERO_TRASLADO.md` de David.

---

*Paquete armado con `tools/traslado/armar-traslado.sh`. Se puede regenerar entero —
inventario y manifiesto incluidos — volviendo a ejecutar el script.*
