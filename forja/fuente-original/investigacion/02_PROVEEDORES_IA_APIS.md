# Proveedores de IA vía API (video, imagen, voz, música)

> Mantenido por el agente `higgsfield-tech-scout`. Última actualización con datos verificados: 2026-08-25
> (fuente: `informe_higgsfield.pdf`); **verificación fresca 2026-08-25 (misma fecha, segunda pasada
> con búsquedas web) confirmó la mayoría de datos y corrigió el matiz de Runway (ver abajo)**.
> Los precios de estos proveedores cambian con frecuencia — re-verificar antes de comprometer
> presupuesto real.

## Video

| Proveedor | Precio aprox. | Reventa / white-label | Nota clave |
|---|---|---|---|
| Runway Gen-4/4.5 | $0.05-$0.12/seg | **CORREGIDO 2026-08-25:** con acceso a la API SÍ puedes construir tu propio producto y exponerlo a end users — NO requiere forzosamente plan Enterprise. Requisito real: mostrar "Powered by Runway" con link a runway.com según sus Branding Guidelines. Prohibido es sub-licenciar/revender el servicio en sí (no la app construida encima) | Viable como base con plan API estándar + atribución visible; Enterprise da SSO, SLA y volumen negociado, no es requisito legal para operar |
| Kling AI | $0.03-$0.34/seg (vía agregador) | Permitido en planes pagos | Mejor relación calidad/precio |
| Luma Ray2 | $0.03-$0.14/seg aprox. | Sin info clara, contactar | Buena opción económica (Flash) |
| Google Veo 3.1 | $0.05 (Lite) a $0.75/seg (con audio) | Más flexible vía Google Cloud | Único con audio nativo sincronizado |
| OpenAI Sora 2 / Pro | $0.10-$0.70/seg | N/A | **CONFIRMADO 2026-08-25: shutdown en dos etapas — app/web ya cerró el 26-abr-2026, API cierra 24-sep-2026. Sora sigue existiendo solo como proyecto de investigación interno de "world models", sin API pública. No hay migración oficial a ningún sucesor — quien la usaba debe moverse a Veo 3.1, Kling o MiniMax ya.** |
| MiniMax / Hailuo | $0.19-$0.56/clip | Permitido | Muy barato, buena calidad viral |

## Imagen

| Proveedor | Precio aprox. | Nota |
|---|---|---|
| Flux (Black Forest Labs) | $0.014 (Klein) - $0.07 (Max) por imagen | Buena calidad/precio; línea económica se llama Klein |
| Ideogram | $0.02-$0.20 por imagen | Fuerte en texto dentro de imagen (miniaturas virales) |
| Midjourney | N/A | **SIN API oficial en 2026 — evitar, riesgo de baneo vía terceros** |

## Voz y música

| Proveedor | Precio aprox. | Nota |
|---|---|---|
| ElevenLabs | $0.05-$0.10/1000 caracteres; doblaje $0.33-$0.50/min; plan Scale $299/mes | Estándar de calidad del sector. **ToS confirmados 2026-08-25: reventa del servicio en sí solo vía "Authorized Reseller" con autorización previa por escrito de ElevenLabs. Sin esa autorización, puedes integrar sus voces en tu producto y cobrar por tu producto, pero NO puedes revender acceso al servicio de ElevenLabs como tal.** |
| Suno / Udio | Solo agregadores no oficiales | **ACTUALIZADO 2026-08-25: sigue sin API pública oficial. Suno abrió el 1-jul-2026 un formulario de intake para un grupo curado de "early partners" de cara a un futuro modelo "partner-powered" — no es aún un self-serve API. Udio sigue sin ninguna API pública. Warner Music (nov-2025) y Universal (Udio) ya cerraron acuerdos de licencia con estas plataformas, señal de que se están legalizando, pero para reventa vía terceros sigue siendo zona gris o de agregadores no oficiales.** |

## Agregadores (una sola API key para integrar todo)

- **Fal.ai** — pago por segundo de GPU, sin margen añadido, 30-50% más barato que Replicate,
  cubre Kling, MiniMax, Flux, Wan, y ahora también Veo (~$0.40/s) y Seedream. **Sigue siendo
  recomendado como motor principal** (confirmado 2026-08-25: rango real $0.02-$0.40 por output según
  modelo, GPU cruda H100 $1.89/h y A100 $0.99/h si se necesita cómputo directo).
- **Replicate** — catálogo enorme (50,000+ modelos), fácil de integrar, cobra con margen.
- **Segmind y ModelsLab** — precios muy bajos en imagen, planes de volumen (ej. ModelsLab
  $149/mes ilimitado).

### fal.ai — ToS de reventa verificados línea por línea (2026-08-25)

Se revisó el contrato completo (última actualización 03-mar-2026), no solo el resumen:

- **Prohibido explícitamente:** "resell, transfer, assign, or sublicense Customer's rights under
  these Terms to any third party" (sección 6(e)(xii)) — no puedes revender tu cuenta/acceso de fal.ai.
- **Prohibido exponer la API directamente:** "Client will not expose any of the Services APIs
  directly to any End Users" (sección 4(b)(ii)) — esto en realidad **encaja bien con el modelo de
  este proyecto**, porque el plan siempre fue construir un backend propio que llama a fal.ai
  internamente, nunca dar a los usuarios finales la API key ni un pass-through directo.
- **Indemnización a la inversa:** el cliente (nosotros) debe defender a fal.ai ante reclamos de
  terceros derivados de "Customer Input" o del "Customer Solution" (sección 17) — es decir, fal.ai
  no asume responsabilidad si un usuario final de nuestro producto reclama por derechos de autor;
  esa exposición legal es nuestra.
- **Conclusión:** fal.ai es viable como motor para este producto siempre que la arquitectura sea
  "backend propio llama a fal.ai, usuario final nunca toca la API directamente" — que es justamente
  el diseño ya planteado. No es un bloqueo, pero confirma que el producto necesita su propia
  cobertura legal/seguros ante reclamos de usuarios finales, no puede apoyarse en la de fal.ai.

## Notas operativas heredadas del pipeline actual (Mindset Mechanics)

El proyecto ya tiene experiencia real con proveedores similares en `recraft_ai/` y `video_express_ai/`.
La auditoría técnica del 2026-08-25 (`handoffs/REVISION_TECNICA_2026-08-25.md`) encontró y arregló
errores que aplican directo a cualquier integración nueva de estos proveedores:
- **429 (rate limit):** requiere reintento con backoff honrando `Retry-After`; nunca reintentar 5xx
  (puede cobrar la generación dos veces).
- **Telemetría nunca acoplada a llamadas de red opcionales** (ej. consultar créditos) — si esa llamada
  falla, la generación ya pagada no debe perder su registro.
- **Rutas de salida siempre absolutas/ancladas al módulo**, nunca relativas al directorio de trabajo
  (causó pérdida silenciosa de assets por `.gitignore` de lista blanca).

## Preguntas abiertas para la próxima ronda de investigación

- [x] ¿Sigue fal.ai siendo la opción más barata? — Sí, confirmado 2026-08-25, sigue siendo la
      opción recomendada, cobertura de modelos incluso creció (Veo, Seedream).
- [x] ¿Qué pasó con la migración de quienes usaban Sora 2? — No hay sucesor oficial ni migración
      guiada por OpenAI; el mercado se está moviendo por su cuenta a Veo 3.1/Kling/MiniMax.
- [x] ¿Hay ya vía oficial de reventa/API para Suno o Udio? — Todavía no self-serve; Suno abrió
      intake de partners el 1-jul-2026 pero sigue siendo acceso curado, no público.
- [ ] Costo real medido (no estimado) de generar 1 minuto de video terminado (imagen + animación +
      voz + música) con la combinación elegida — comparar contra el presupuesto de
      `05_PRESUPUESTO_Y_CRONOGRAMA.md`.
- [ ] Cuando Suno abra su API de partners más ampliamente, evaluar si califica el proyecto para
      acceso — revisar de nuevo en 1-2 meses.
- [ ] Verificar si fal.ai ofrece algún plan Enterprise con SLA distinto al pay-as-you-go que reduzca
      el riesgo de indemnización unilateral hacia el cliente (sección 17 de sus ToS).

## Fuentes

Documentación oficial de precios de fal.ai, Runway, ElevenLabs (citadas en `informe_higgsfield.pdf`, agosto 2026).
Verificación fresca 2026-08-25: [fal.ai Terms of Service](https://fal.ai/terms) (actualizado 03-mar-2026),
[fal.ai pricing — PricePerToken](https://pricepertoken.com/fal-ai-pricing), [OpenAI Help Center — Sora
discontinuation](https://help.openai.com/en/articles/20001152-what-to-know-about-the-sora-discontinuation),
[Apiyi — Sora-2 API shutdown Sept 24](https://help.apiyi.com/en/sora-2-api-shutdown-alternatives-2026-en.html),
[tunova.ai — ¿existe API oficial de Suno? (2026)](https://tunova.ai/guides/is-there-an-official-suno-api),
[ElevenLabs Terms of Service](https://elevenlabs.io/terms-of-use), [Runway Enterprise](https://runway.com/enterprise).
