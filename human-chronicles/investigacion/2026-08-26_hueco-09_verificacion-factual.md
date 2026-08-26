# HUECO #9 — Verificación factual a escala

**Ronda 01 · 2026-08-26 · estado previo: 🟡 REGLA SIN PROCESO**
**Estado ahora: 🟡 PROCESO ESCRITO — el coste en tiempo sigue sin medir (solo se mide midiéndolo)**

La regla estaba escrita (2 fuentes independientes por dato duro, `ESTILO_HUMAN_CHRONICLES.md` §2)
pero no había ni plantilla, ni proceso, ni idea de cuánto tiempo añade por guion. En un canal de
historia, un error visible en comentarios destruye la autoridad más rápido que ninguna otra cosa.

---

## 1. El estándar profesional, y por qué el del canal está bien calibrado

- **Principio de independencia:** cada dato se contrasta con al menos **una fuente autorizada**;
  si no la hay, con **varias fuentes independientes no autorizadas**.
- El estándar periodístico más exigente pide **tres fuentes creíbles no relacionadas**.
- La verificación la hace idealmente **alguien distinto de quien escribió** el material.

La regla de dos fuentes independientes del canal queda **entre** el mínimo académico y el máximo
periodístico. Es razonable. **Lo que sí conviene apretar es el criterio de "independiente":** dos
webs que copian del mismo artículo de Wikipedia no son dos fuentes, son una. Esa es la trampa real
del trabajo con IA en historia, y la que hay que escribir en la regla.

### Precisión que se añade a la regla del canal
> Dos fuentes son independientes si **no derivan la una de la otra ni de un mismo tercero**. Un
> manual académico + un artículo de divulgación que lo cita **son una sola fuente**. Ante la duda,
> se busca una fuente primaria o una obra de referencia.

## 2. La separación autor / verificador, aplicada al equipo de agentes

El estándar dice que verifique alguien distinto del autor. El equipo ya tiene esa separación
montada (`PERFIL_DEL_PROYECTO.md` §4.B.5: quien ejecuta ≠ quien audita). Se aplica tal cual:

- `human-chronicles-production-lead` **escribe** el guion y **marca** los datos duros.
- `human-chronicles-research-analyst` **verifica** cada dato marcado, sin haber escrito el guion.
- `human-chronicles-program-director` comprueba que la tabla esté completa antes de dar paso a VO.

Esto no añade agentes: usa los que ya existen en el papel que ya tienen.

## 3. La plantilla (lo que faltaba)

Cada guion lleva al lado un `datos_<video>.md`:

| # | Dato duro (cita textual del guion) | Fuente 1 | Fuente 2 | ¿Independientes? | Veredicto |
|---|---|---|---|---|---|
| 1 | "In 1204, the fleet turns north" | | | sí/no | ✅ / ⚠️ disputado / ❌ |

Tres veredictos posibles, y ninguno es "más o menos":
- **✅ Confirmado** — dos fuentes independientes coinciden. Va al guion como afirmación.
- **⚠️ Disputado** — las fuentes no coinciden. **Va al guion diciéndolo**: *"los cronistas no
  coinciden en…"*. `ESTILO_HUMAN_CHRONICLES.md` §2 ya lo establece, y con razón: señalar la disputa
  **suma** credibilidad. Es de las mejores decisiones de la biblia de estilo.
- **❌ No verificado** — **se reescribe la frase o se cae del guion.** No se publica un dato duro
  sin verificar por bonito que quede.

**Nada pasa a grabación de voz con una fila sin veredicto.** Es un gate, no una recomendación.

## 4. El coste en tiempo: sin medir, y así se marca

La pregunta del hueco original era *"cuánto tiempo añade por guion"*. La investigación **no
encontró ese dato** — la literatura de documental habla de proceso y de principios, no de minutos
por guion, y señala que los documentalistas suelen trabajar con muchos menos recursos que un
periodista de investigación.

Así que se mide en casa: **al verificar el guion del video 1, se cronometra y se anota el resultado
aquí.** Es el mismo principio que `ERRORES_A_EVITAR.md` #15 (medir un caso real con `ffprobe` antes
de planificar): no se planifica sobre una estimación inventada.

Hipótesis de trabajo a validar, no dato: un guion de 8-12 min tiene del orden de 15-25 datos duros;
a ~4 min por dato con dos fuentes, salen 1-1,5 h por guion. **Si la medición real lo desmiente, manda
la medición.**

## Fuentes

- [The No-Spin Zone: How Journalistic Documentaries Check Their Facts — International Documentary Association](https://www.documentary.org/feature/no-spin-zone-how-journalistic-documentaries-check-their-facts)
- [Fact Checking — Documentary Film Research Methods, The New School](https://guides.library.newschool.edu/c.php?g=274403&p=2643950)
- [The TiJ Fact Checking Guide — How to Fact-Check](https://thetijproject.ca/guide/how-to-fact-check/)
- [The TiJ Fact Checking Guide — Fact-Checking As Part of the Editorial Process](https://thetijproject.ca/guide/the-editorial-process/)
- [How to Fact-Check History — Retro Report](https://retroreport.org/video/how-to-fact-check-history/)
- [The 12 Best Tools for Documentary Research and Pre-Production (2026) — Storyflow](https://storyflow.so/blog/best-documentary-research-tools-2026)
