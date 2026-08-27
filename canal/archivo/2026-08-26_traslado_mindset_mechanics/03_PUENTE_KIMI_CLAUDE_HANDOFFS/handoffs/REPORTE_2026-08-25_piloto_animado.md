# Reporte — Piloto detenido ANTES de gastar: faltan las 8 imágenes base

**De:** sesión Claude (ejecución del piloto, revisión previa obligatoria) · **Fecha:** 2026-08-25

## Créditos gastados: 0 Recraft / 0 VideoExpress. Presupuesto intacto.

## Verificado y en orden
- Repo sincronizado en `dc3aff8`.
- Storyboard: 15 paneles, 14×6s + 1×10s = 94s exactos, todos con `image_prompt` y `video_action_prompt`.
- Sesión de VideoExpress viva (chequeo sin gastar crédito): editor carga logueado como David Peñuela.
- Audio de voz en off existe (553.4s totales; el tramo del piloto 0:00–1:34 cuadra).

## El bloqueo: 0 de las 8 imágenes base disponibles

1. **Las 7 nuevas no se pueden generar todavía.** El plan de Kimi las condiciona a la API de Recraft "una vez activo el saldo de $5 USD". Ese saldo **nunca se pagó** — no existe `recraft_ai/.env` ni `RECRAFT_API_KEY`.
2. **Las 2 que se iban a reusar no están en disco.** Las 12 imágenes ya generadas por la vía web de Recraft (204 créditos gastados el 25-ago) **viven solo en el proyecto web de Recraft**, nunca se descargaron a la máquina.

Sin imágenes no hay nada que validar contra frames publicados (regla 9), ni que importar, ni que animar. No se improvisó gastando por la vía web para evitar esto — habría contradicho el plan de Kimi y gastado sin autorización.

## Hallazgo colateral: las 204 créditos ya pagados están en riesgo
Las 12 imágenes de Recraft solo existen en el servidor de Recraft. Si la cuenta caduca o la plataforma limpia assets, se pierden y hay que pagarlas de nuevo. Pendiente: descargarlas a disco.

## Decisiones que le tocan a David

1. **¿Se aprueban los $5 USD de saldo de la API de Recraft?** Es la vía que Kimi ya aprobó técnicamente, solo falta el pago. Desbloquea las 7 imágenes nuevas y resuelve la fragilidad de depender del navegador.
2. Si no: ¿se autoriza generarlas por la web de Recraft en su lugar (630 créditos disponibles ahí, más lento y frágil, contradice el plan de Kimi)?
3. Confirmar el nuevo techo de animaciones del piloto: 15 en vez de 8 (ya lo sabías, queda por escrito).

## Decisiones que le tocan a Kimi
4. El plan asume "2 imágenes reusadas" de las 12 ya pagadas — hay que descargarlas de Recraft y validar que el encuadre coincide con el panel del storyboard, o generar las 8 desde cero con los prompts del storyboard v3 (hechos a medida).
5. Sigue sin resolver la burbuja de cómic de la escena 11 (fuera del piloto, pero pendiente).

## Estado
No hay video de piloto todavía — nada que revisar hasta resolver el punto 1.
