# Índice del proyecto — dónde está cada cosa

No se movió ni renombró ningún archivo (varios scripts tienen rutas absolutas
escritas a mano — mover carpetas los rompería). Esto es solo un mapa para
encontrar todo rápido. Se actualiza según el proyecto crece.

## Estrategia y contenido (leer primero)
- `PROYECTO MECHANICS OPTIMIZACIONES/PLAYBOOK_MONETIZACION.md` — cómo monetizar rápido: formato de títulos, ganchos, retención, miniaturas.
- `PROYECTO MECHANICS OPTIMIZACIONES/PLAYBOOK_MARCA_INTERACCION_VENTAS.md` — protocolo de interacción con la audiencia.
- `PROYECTO MECHANICS OPTIMIZACIONES/MANUAL_PRODUCCION.md` — cómo generar imagen+video consistentes (Recraft + VideoExpress), reglas de cámara.
- `ESTILO_MINDSET_MECHANICS.md` — ficha visual del personaje y estilo del canal.
- `RESILIENCE_SCENE_PLAN.md` — guion escena por escena del video actual en producción.

## Canal hermano: Human Chronicles (faceless, historia, en inglés)
Canal distinto, **cuenta de Google distinta y deliberadamente aislada**. No mezclar con Mindset Mechanics.
- `PROYECTO HUMAN CHRONICLES/ESTADO_CANAL.md` — **leer primero.** Estado real verificado, qué se hereda y qué no, y los pendientes que dependen de una acción humana.
- `PROYECTO HUMAN CHRONICLES/ESTILO_HUMAN_CHRONICLES.md` — manual de estilo faceless: voz narrativa, sistema visual sin personaje, uso de Recraft para escenas históricas, fuentes de archivo de dominio público, cumplimiento de la política de contenido no auténtico de YouTube.
- `PROYECTO HUMAN CHRONICLES/PLAYBOOK_MONETIZACION_HC.md` — monetización del nicho de historia (RPM real, camino a YPP desde cero, infoproductos).
- Agente propio: `history-visual-director` (reemplaza a `storyboard-director` y `thumbnail-consistency-guardian`, que asumen personaje fijo y **no aplican** a este canal).
- Handle correcto: **`@humanchronicles11`**. Cualquier documento que diga `HumanChronicles18` o `@HumanChroniclesHQ` está obsoleto.

## Código de producción (lo que genera/ensambla video)
- `video_express_ai/` — bot de VideoExpress.ai (Playwright): genera/anima escenas, sube imágenes, ensambla el video final.
  - `video_express_ai/outputs/` — **imágenes/pruebas ya generadas, ahora sí respaldadas en git** (los .mp4 pesados no, ver abajo).
  - `video_express_ai/logs/` — telemetría de cada generación (créditos gastados, timestamps).
  - `video_express_ai/refs/` — imágenes de referencia del personaje.
  - `video_express_ai/session.py` — lock de cuenta + cierre garantizado del navegador. **Ningún script nuevo debe abrir Playwright por su cuenta: usar `browser_page()`.**
- `recraft_ai/` — cliente de la API REST de Recraft (genera los stills). `generate_scene.py --credits` consulta el saldo sin gastar nada.
- `youtube_pipeline/` — pipeline genérico (voz TTS, ensamblaje) reutilizado por otros canales además de Mindset Mechanics. Renderiza a 1920x1080 (override con `PIPELINE_WIDTH`/`PIPELINE_HEIGHT`).
- `shorts_final/` — scripts y pruebas de los Shorts ya publicados.

## Coordinación entre sesiones/IAs
- `handoffs/` — toda la comunicación entre sesiones de Claude Code y Kimi (decisiones, reportes de QA, escalaciones). Es el historial real de qué se decidió y cuándo — revisar aquí antes de asumir el estado del proyecto.

## Paquetes de conocimiento (snapshots para portar el proyecto a otra cuenta/PC)
- `PAQUETE_CONOCIMIENTO_MINDSET_MECHANICS_2026-08-23_v2/` (y su .zip) — snapshot congelado al 23-ago. Para el estado actual, usar los archivos de arriba, no este paquete (queda desactualizado).
- `_ARCHIVO_HISTORICO/` — versiones viejas, solo para referencia histórica.

## Videos y archivos pesados (fuera de git — ver "Respaldo" abajo)
GitHub rechaza archivos de más de 100MB, así que los `.mp4` finales NO están en
este repo. Viven únicamente en:
1. El disco local de esta PC.
2. Las cuentas de Recraft AI y VideoExpress.ai — **ojo: ambas borran los archivos generados a los 60 días**, no son un respaldo permanente.

**Decidido con David 2026-08-25: sí, respaldar en Google Drive (mechanicsmindset02@gmail.com), pagar plan de más espacio si hace falta.** No hay conector MCP de Drive instalable en este entorno (registro consultado, vacío) — la vía es navegador (Claude Browser/Chrome, sesión ya logueada) subiendo a una carpeta dedicada en Drive. 15GB gratis alcanzan para 100+ videos finales de ~100MB antes de necesitar pagar, así que no es urgente pagar todavía.

Proceso (a completar / en curso):
1. Carpeta en Drive: `Mindset Mechanics - Respaldo` (crear si no existe).
2. Subir ahí: cada video final aprobado (.mp4), y opcionalmente un respaldo periódico de `video_express_ai/outputs/` completo (incluye lo que sí cabe en git más los .mp4 que no caben).
3. Git sigue siendo el respaldo principal de código/imágenes/docs (automático, cada commit). Drive es solo para los .mp4 pesados que git no acepta.

## Hallazgo técnico que condiciona toda la producción de imágenes (2026-08-25)
**Recraft V4.1 no ofrece ningún tamaño 16:9 exacto, y VideoExpress solo anima 16:9/9:16.**
Los tamaños de la API son una lista cerrada por familia de modelo
([Appendix oficial](https://www.recraft.ai/docs/api-reference/appendix)):
el más ancho de V4.1 es 1344x768 (1.750), fuera de la tolerancia. Solución
aplicada en `recraft_ai/recraft_client.py`: generar a 1344x768 y recortar el alto
a 1344x756 = 16:9 exacto. La alternativa es bajar a `recraftv3` @1820x1024
(16:9 nativo, y único modelo compatible con estilos propios `style_id`), pero eso
**cambia el look del personaje** — decisión de Kimi/David, no técnica.

## Otros
- `OTROS_PROYECTOS/` — proyectos ajenos a Mindset Mechanics que comparten esta PC (ComfyUI, etc.) — no tocar desde este proyecto.
- `kimi_token.txt` — token de la API de Kimi, excluido de git (`.gitignore`), nunca compartir ni commitear.
