# HUECO #2 — Evaluar y filtrar archivo histórico de dominio público en volumen

**Ronda 01 · 2026-08-26 · estado previo: 🔴 SIN PROCESO PROBADO (solo una lista de 6 fuentes)**
**Estado ahora: 🟡 PROCESO DISEÑADO Y HERRAMIENTA ESCRITA — sin ejecutar (ver §4, límite real)**

El problema no era encontrar archivo, era que **verificar licencia ítem por ítem no escala a 2
videos/semana**. La solución es no verificar a mano lo que una API ya responde.

---

## 1. Las fuentes, reordenadas por coste de verificación

La lista de 6 fuentes de `ESTILO_HUMAN_CHRONICLES.md` §4 es correcta pero está ordenada por tamaño,
no por lo que de verdad cuesta usarla. Reordenada por **cuánto trabajo humano exige cada ítem**:

| Nivel | Fuente | Por qué | Verificación por ítem |
|---|---|---|---|
| **1 — sin fricción** | Gobierno federal EE.UU. (NASA, NARA, CDC) | Obra del gobierno federal = dominio público por ley | Ninguna |
| **1 — sin fricción** | Wikimedia Commons | Cada archivo lleva su licencia en metadatos legibles por API | Automática |
| **2 — API con campo de derechos** | Library of Congress | Cada ítem tiene campo **"Rights Advisory"**; muchas colecciones sin restricción conocida | Leer un campo |
| **2 — API con campo de derechos** | Internet Archive (Moving Image Archive, +2,5 M ítems; **Prelinger** dentro) | `licenseurl` / `rights` consultables por `advancedsearch.php` | Leer un campo |
| **3 — caso por caso** | American Archive of Public Broadcasting (~113.000 ítems digitalizados en la LoC) | Streaming sí, reutilización no siempre | Manual |
| **4 — NO es dominio público** | AP Archive, Periscope Films, PublicDomainFootage | Son **stock licenciable**, no dominio público. Están en la lista original y conviene decirlo claro | Contrato |

> **Corrección a la documentación previa:** `ESTILO_HUMAN_CHRONICLES.md` §4 lista AP Archive,
> Periscope y PublicDomainFootage junto a la LoC y el Internet Archive. Las notas ya avisaban
> ("licenciable", "stock, no siempre libre"), pero conviene el titular: **tres de las seis fuentes
> de la lista original no son gratuitas ni de dominio público.** El fondo realmente libre y a
> escala son la LoC, el Internet Archive, Wikimedia y el gobierno de EE.UU.

**Si el subnicho es civilizaciones antiguas** (recomendación del hueco #10), este problema casi
desaparece: no hay metraje fílmico de la Antigüedad que reclamar. El material es arte, mapas y
documentos, mayoritariamente dominio público por antigüedad y sobre todo en Wikimedia Commons —
nivel 1. **Es una razón más para ese subnicho.**

## 2. El proceso repetible (lo que faltaba)

Para cada video, cuatro pasos:

1. **Buscar por API, no por navegador** — una consulta por término del guion contra Wikimedia
   Commons + LoC + Internet Archive, pidiendo ya los campos de licencia.
2. **Filtrar automáticamente** — descartar todo ítem sin licencia legible o con licencia no
   comercial. Lo que la API no pueda afirmar, **no entra**. Nada de "seguramente es libre".
3. **Generar `sources_<video>.md`** con una fila por ítem: título, URL de origen, licencia, fecha
   de descarga. Es el registro de procedencia ya obligatorio (`ESTILO_HUMAN_CHRONICLES.md` §4).
4. **Revisión humana solo de los supervivientes**, y solo sobre la advertencia que ninguna API
   resuelve: **dominio público del contenedor ≠ dominio público del contenido** (música con
   derechos, obra de arte protegida, personas identificables). Eso sigue siendo ojo humano — pero
   sobre 10 ítems ya filtrados, no sobre 200.

Los pasos 1-3 son mecánicos: los hace la herramienta. El paso 4 es el único que cuesta tiempo, y
es donde debe estar el tiempo.

## 3. La herramienta

`human-chronicles/tools/buscar-archivo.mjs` — consulta las tres APIs, filtra por licencia y escribe
el `sources_<video>.md`. Uso:

```bash
node human-chronicles/tools/buscar-archivo.mjs "Constantinople 1453" --video video-01
```

## 4. Límite real de esta ronda (honesto, por `ERRORES_A_EVITAR.md` #20)

**La herramienta está escrita pero NO se ha ejecutado nunca.** El entorno remoto donde se hizo esta
investigación **bloquea `archive.org`, `www.loc.gov` y `commons.wikimedia.org`** en el proxy de red
(error 403 en CONNECT, comprobado el 2026-08-26). No se pudo probar ni una consulta.

Por tanto: el proceso está diseñado, el código está escrito contra la forma documentada de esas
APIs, y **la primera ejecución en la máquina de David es el paso de validación**. Hasta que eso
ocurra, este hueco es 🟡, no 🟢. La pregunta del hueco original —*"¿cuánto tarda de verdad?"*—
**sigue sin respuesta medida**, y solo se puede responder cronometrando la primera corrida real.

## Fuentes

- [Online Resources for Moving Image Material — Library of Congress](https://www.loc.gov/rr/mopic/onlinesources.html)
- [A/V Materials in the Public Domain — NYU Libraries](https://guides.nyu.edu/video/PD-CC)
- [Film Footage (free) — Penn State Library Guides](https://guides.libraries.psu.edu/filmarchives)
- [How to Find Archival Footage: Historical Video Clips — Coverr](https://coverr.co/blog/where-to-find-archival-footage)
- [American Archive of Public Broadcasting — Wikipedia](https://en.wikipedia.org/wiki/American_Archive_of_Public_Broadcasting)
- [LOC Public Domain Archive — loc.getarchive.net](https://loc.getarchive.net/)
