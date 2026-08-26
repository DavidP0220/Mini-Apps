# LÉEME PRIMERO — Traslado del proyecto **Mindset Mechanics**

**Paquete maestro `TRASLADO_MINDSET_MECHANICS_COMPLETO_{{FECHA}}`**
Destino: una cuenta nueva de Claude (Max) que va a **continuar** este proyecto, no empezarlo.

---

## 0. Qué es este paquete y por qué está partido así

Es **todo** el proyecto Mindset Mechanics: la estrategia, el código del pipeline, los
handoffs con Kimi Code, la investigación, las memorias del agente, los agentes de
Claude Code y los assets generados.

No se ha omitido nada. La prueba está en tres archivos que acompañan a este:

| Archivo | Para qué sirve |
|---|---|
| `INVENTARIO_COMPLETO.md` | Lista de **todos** los archivos con ruta y tamaño. Si algo no está ahí, no está en el paquete. |
| `MANIFIESTO_SHA256.txt` | Huella de cada archivo. Se verifica con `sha256sum -c MANIFIESTO_SHA256.txt`. |
| `UNICOS_EN_ZIPS_INTERNOS.md` | Los **{{N_UNICOS}} archivos que solo vivían dentro de zips anidados** y que se habrían perdido si alguien hubiera copiado solo las carpetas. |

Cifras de este corte: **{{N_ARBOL}} archivos** en el árbol original ({{PESO}}) más
**{{N_DESEMP}} archivos** rescatados del interior de los zips anidados.

---

## 1. Cómo abrirlo (orden exacto)

Dentro de `paquetes/` hay varios zips. Cada uno guarda las rutas **tal cual estaban en el
proyecto original**, así que:

> **Extrae todos los zips de `paquetes/` en una misma carpeta.**
> Se ensamblan solos en el árbol original — no se pisan ni se duplican entre sí.

| Zip | Qué trae |
|---|---|
| `01_HANDOFFS_KIMI_CLAUDE.zip` | **El trabajo con Kimi-Claude completo**: handoffs, reportes diarios, revisiones técnicas, investigación diaria y el paquete `HANDOFF_KIMI_PACKAGE`. |
| `02_DOCUMENTACION_Y_MANUALES.zip` | Manuales, playbooks, biblia de estilo y los paquetes de conocimiento v1, v2 y v3 (tal cual, en `.zip`). |
| `03_PAQUETES_INTERNOS_DESEMPAQUETADOS.zip` | Esos mismos paquetes **ya abiertos**, para no tener que descomprimir zips dentro de zips. Aquí están los {{N_UNICOS}} archivos únicos. |
| `04_CODIGO_FUENTE_PIPELINE.zip` | Todo el código: `youtube_pipeline/`, `video_express_ai/`, `recraft_ai/`, `shorts_final/`, configs, requirements, logs. Ligero: se puede abrir entero sin problema. |
| `05_ASSETS_GENERADOS_parte_N_de_M.zip` | Las imágenes, voces en off y frames generados. Pesan y no comprimen, por eso van en volúmenes aparte y numerados. **No hacen falta para entender el proyecto**, pero son parte del historial y no se descartan. |

---

## 2. Orden de lectura para la cuenta que recibe esto

No leas el paquete entero de golpe. Este es el camino corto para poder trabajar el mismo día:

1. **`ESTADO_DEL_TRASLADO.md`** (aquí al lado) — dónde está parado el proyecto **hoy**, qué
   decisión está bloqueando la producción y qué falta por recibir.
2. **`ERRORES_QUE_NO_SE_DEBEN_REPETIR.md`**
   (en `03_PAQUETES_INTERNOS_DESEMPAQUETADOS` → `PAQUETE_..._2026-08-25_v3/`) — 26 errores
   con causa raíz y arreglo. Es el documento que más créditos y semanas ahorra. Léelo entero.
3. **`LEEME_PRIMERO.md` y `MANIFIESTO.md`** del mismo paquete v3 — el mapa del conocimiento,
   indexado por tema, fecha y severidad.
4. **`01_estrategia_y_estilo/SISTEMA_STORYBOARD_MINDSET_MECHANICS.md`** — el método de
   storyboard (esquema JSON + checklist de 15 puntos). Es la pieza más reutilizable de todo.
5. **`HANDOFF_2026-08-25_decision_tercera_via_resiliencia.md`** (en `01_HANDOFFS...`) — el
   pivote más importante del historial, con su razonamiento completo.
6. Los reportes del **2026-08-26** (`REVISION_TECNICA`, `REPORTE_..._storyboard`,
   `..._captacion`, `..._interaccion`, `INVESTIGACION_DIARIA`) — el último día registrado.
   Ahí está el estado real, ya verificado contra archivos, no asumido.
7. `04_CODIGO_FUENTE_PIPELINE` → empieza por `youtube_pipeline/README.md` y
   `youtube_pipeline/config/channels.example.yaml`.

---

## 3. Cómo se trabaja este proyecto (para no romper el método)

El sistema tiene cuatro roles y la separación entre ellos es lo que ha evitado quemar
presupuesto:

| Rol | Quién | Qué decide |
|---|---|---|
| Estratega | **Kimi Code** (otro LLM, vía handoffs en git) | Alcance, presupuesto, método |
| Ejecutor técnico | **Claude Code** | Genera, ensambla, reporta. Ejecuta sin improvisar |
| Storyboard Director | Subagente especializado | Convierte guion en storyboard técnico |
| Gate de calidad | **David** (humano) | Aprueba storyboard y piloto. Su veredicto manda |

Los handoffs con Kimi van completos en `01_HANDOFFS_KIMI_CLAUDE.zip` — **ese intercambio es
parte del proyecto, no un anexo**. Sin él se pierde el porqué de la mitad de las decisiones.

**Las tres reglas de arquitectura que no se negocian:**

1. Ningún video entra a generación **sin storyboard aprobado**.
2. El personaje se genera como **imagen en Recraft**, nunca desde texto en el generador de
   video. La consistencia se resuelve antes de animar, no después.
3. Prohibido sostener un frame congelado más de **4 segundos**. 3-4 sub-clips reales de
   10-18 s por escena, cada uno con plano distinto.

**Reglas de comunicación heredadas:** español siempre con David; el contenido del canal en
inglés · 1080p mínimo, nunca bajar el nivel · investigar en la web antes de parchar · no
mezclar canales/proyectos distintos en un mismo repo · nada se planifica sobre una fuente sin
verificar.

---

## 4. Los agentes de Claude Code que hay que instalar

En `03_PAQUETES_INTERNOS_DESEMPAQUETADOS` → `PAQUETE_..._2026-08-25_v3/05_agentes_claude_code/`
hay 8 agentes listos. Cópialos a `.claude/agents/` de la cuenta nueva:

`chief-technical-officer` · `storyboard-director` · `thumbnail-ctr-strategist` ·
`thumbnail-consistency-guardian` · `community-engagement-manager` · `growth-acquisition-lead` ·
`publish-readiness-coordinator` · `knowledge-archivist`

Y en `06_memoria_claude/` están las memorias del proyecto (alcance, política de idiomas,
calidad mínima 1080p, días de publicación, separación de canales). Adáptalas, no las borres.

---

## 5. Seguridad — ya revisado

Se barrió el paquete entero buscando claves (`sk-`, `AIza`, `ghp_`, `.env` reales,
credenciales): **cero resultados**. Solo viajan los `.env.example` con los nombres de las
variables y ningún valor. La cuenta que reciba esto tendrá que poner sus propias claves de
YouTube Data API, Anthropic, ElevenLabs, Gemini, Recraft y VideoExpress.

---

*Paquete armado con `tools/traslado/armar-traslado.sh`. Si llegan más partes del origen,
se vuelve a ejecutar el mismo script y se regenera todo — inventario y manifiesto incluidos.*
