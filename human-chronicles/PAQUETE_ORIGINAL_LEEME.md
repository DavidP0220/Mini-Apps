# LÉEME PRIMERO — Paquete de conocimiento de Human Chronicles

**Fecha del paquete: 2026-08-26.**

## Qué es esto

Todo el conocimiento del proyecto **Human Chronicles** (`@humanchronicles11`): un canal de YouTube
de historia y civilizaciones, en inglés, formato **faceless** (sin personaje ni host), operado por
un equipo de agentes de Claude con el objetivo único de llevarlo a **monetización**.

Es el segundo canal del sistema. El primero es **Mindset Mechanics** (canal con personaje animado,
nicho de desarrollo personal, cuenta y repositorio separados). **Los canales no se mezclan**: lo
único que cruza entre ellos son habilidades y aprendizajes técnicos — que es exactamente lo que
contiene este paquete.

**Estado honesto del canal a la fecha: 0 videos publicados, 0 avances de producción.** Lo que hay
aquí es infraestructura de método y memoria, no contenido producido. Léelo sabiendo eso.

## En qué orden leerlo

1. **`documentos_canal/PERFIL_DEL_PROYECTO.md`** — empieza aquí, siempre. Es el cuadro completo:
   nombre, el porqué, el para qué, todas las habilidades aprendidas y todos los huecos que faltan.
   Si solo vas a leer un archivo, que sea este.
2. **`documentos_canal/ERRORES_A_EVITAR.md`** — 20 lecciones fechadas y con fuente. Cada una costó
   créditos, tiempo o un video reprobado. **Se lee entero antes de tocar nada.**
3. **`documentos_canal/ESTADO_CANAL.md`** — fuente única de verdad de los datos del canal. Si un
   dato no está confirmado ahí, no está confirmado.
4. **`documentos_canal/TABLERO_MONETIZACION.md`** — el marcador hacia la monetización y el
   historial de decisiones. Enseña el formato de tablero, que es media metodología.
5. **`documentos_canal/ESTILO_HUMAN_CHRONICLES.md`** y **`PLAYBOOK_MONETIZACION_HC.md`** — la
   biblia creativa y la estrategia de ingreso.
6. **`agentes_exclusivos_hc/`** y **`agentes_multicanal/`** — el equipo. Ver abajo.
7. **`herencia_mindset_mechanics/`** — de dónde vienen las lecciones heredadas.
8. **`memoria_claude/`** y **`tarea_programada/`** — reglas permanentes y automatización diaria.

## Qué hay en cada carpeta

| Carpeta | Contenido |
|---|---|
| `documentos_canal/` | Los 6 documentos del canal (incluido el `PERFIL_DEL_PROYECTO.md` nuevo) |
| `agentes_exclusivos_hc/` | **5 agentes exclusivos de Human Chronicles**: `research-analyst`, `production-lead`, `growth-monetization`, `program-director` (audita y es el único que escribe el tablero) y `history-visual-director` |
| `agentes_multicanal/` | **4 agentes compartidos** entre canales, ya adaptados para distinguir en cuál trabajan: `community-engagement-manager`, `growth-acquisition-lead`, `publish-readiness-coordinator`, `knowledge-archivist`. **Al invocarlos hay que decirles explícitamente en qué canal trabajan** |
| `herencia_mindset_mechanics/` | Solo lo indispensable del otro canal: `MANUAL_PRODUCCION.md` (pipeline Recraft → VideoExpress; su §3 es el banco de movimientos de cámara que HC hereda tal cual), `PLAYBOOK_MONETIZACION.md` (base transversal que el playbook de HC complementa), `POLITICA_IDIOMAS.md` y `check_video_specs.py` |
| `memoria_claude/` | Reglas permanentes del usuario (español siempre, 1080p mínimo, no mezclar canales, días de publicación, Recraft para imágenes) |
| `tarea_programada/` | La tarea diaria que invoca al director del programa cada mañana |

**Nota sobre la herencia:** este paquete **no** duplica el paquete completo de Mindset Mechanics.
`ERRORES_A_EVITAR.md` cita por nombre cada handoff y reporte de origen de las lecciones heredadas
(`REPORTE_2026-08-23c_QA_fallido_escalado.md`, `REPORTE_2026-08-25_revision_tecnica_y_mejoras.md`,
`REVISION_TECNICA_2026-08-25.md`, etc.). Si necesitas la evidencia original completa, está en
`PAQUETE_CONOCIMIENTO_MINDSET_MECHANICS_2026-08-23_v2` / `..._2026-08-25_v3`. Aquí se copiaron
únicamente los dos documentos sin los cuales alguien nuevo no entendería el método.

## Si vas a aplicar esto a OTRO canal o nicho

Esta es la distinción que más te va a servir.

**Específico de Human Chronicles — NO lo copies tal cual:** el nicho de historia; el idioma inglés
y la audiencia EE.UU./UK/CA/AU; la paleta sepia y las cartelas de nombre + año; la estructura de
video de 8-12 min con cold open y tres actos; las 6 fórmulas de título del nicho; el RPM de $5-$12;
las fuentes de archivo histórico de dominio público; la regla de no generar rostros IA de personas
históricas reales.

**Método general — esto es lo reutilizable, y es el 80% del valor:**
- Un `ESTADO_CANAL.md` donde cada dato dice si está confirmado, decidido o pendiente.
- Un `ERRORES_A_EVITAR.md` de **solo append** con campo `Estado:` (una entrada equivocada no se
  edita: se añade otra y la vieja pasa a `SUPERADA POR #N`).
- Un `TABLERO_MONETIZACION.md` de **solo append**, entradas nuevas arriba, con entregable real,
  bloqueo con responsable y próxima acción fechada. Prohibido "estoy investigando" sin entregable.
- Un equipo de agentes con **separación entre quien ejecuta y quien audita**; solo el director
  escribe en el tablero, y verifica en disco antes de dar algo por hecho.
- Una tarea programada diaria para que el canal avance sin depender de la memoria del humano.
- **Aislamiento de cuenta por canal**: cuenta Google propia, tokens propios, sesión de navegador
  propia, repositorio propio. Un strike en un canal no debe poder arrastrar a otro.
- `git check-ignore -v` al crear cualquier carpeta que deba respaldarse (un `.gitignore` de lista
  blanca ignora carpetas nuevas sin avisar).
- **Ejecutar primero, documentar después** — nunca al revés.
- El QA técnico es necesario pero **no suficiente**: la aprobación final es del humano, viendo el
  render, no una descripción del render.
- Gates de presupuesto literales: ni un crédito fuera del lote autorizado.
- Un **ancla de marca elegida conscientemente** (personaje, voz, paleta o estructura) fijada con una
  imagen de referencia. En un canal faceless, la referencia es de **estilo**, no de personaje.
- Medir con `ffprobe` un caso real antes de planificar duraciones sobre cualquier herramienta.
- Cumplimiento de la política de contenido no auténtico de YouTube: tesis original por video, sin
  plantilla repetida entre videos, fuentes citadas, voz sintética de calidad, ritmo sostenible.
  **La consistencia importa; la clonación mata.**

## Lo que este sistema todavía NO sabe hacer

Está en `PERFIL_DEL_PROYECTO.md` §5, y conviene leerlo antes de confiar en el resto. En corto: no
se ha probado **ninguna herramienta de voz** (siendo la voz el ancla del canal), no hay proceso
probado para filtrar archivo de dominio público a escala, no hay forma de detectar riesgo de
desmonetización antes del aviso de YouTube, el infoproducto v0 no existe, el repositorio no tiene
remoto, y **no hay una sola métrica real** porque el canal no tiene videos.
