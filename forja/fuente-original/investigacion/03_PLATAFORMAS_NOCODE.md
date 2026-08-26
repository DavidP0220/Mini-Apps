# Cómo construirlo sin programar: 3 rutas posibles

> Mantenido por el agente `higgsfield-tech-scout`. Última actualización con datos verificados: 2026-08-25
> (fuente: `informe_higgsfield.pdf`); **segunda pasada de verificación 2026-08-25 no encontró
> competidor mejor posicionado que Lovable ni resolvió a fondo el manejo de colas largas — ver
> hallazgos abajo.**

## Ruta A — Bubble.io + APIs de IA + Stripe (versión "seria", para escalar)

Bubble es el builder no-code más probado para SaaS reales, con API Connector para conectar
Runway/ElevenLabs/fal.ai, e integración nativa con Stripe para suscripciones.

**Punto clave de la validación:** el API Connector tiene timeout corto (30-60 seg), insuficiente
para una generación de video que tarda minutos — hace falta implementar **Backend Workflows con
patrón webhook/callback** (la IA avisa a Bubble cuando termina) en vez de esperar la respuesta en
línea. Esto es arquitectura adicional real, no un simple "conectar y listo".

- Costo inicial: ~$29-$100/mes de Bubble + créditos de API.
- Costo mensual: $50-$150/mes de plataforma + variable según uso.
- Dificultad: media (3-6 semanas de curva de aprendizaje real).

## Ruta B — Lovable.dev / Base44 + Fal.ai + Stripe (MVP rápido para validar) — RECOMENDADA para empezar

Lovable genera apps completas por prompt (frontend + backend real sobre Supabase, sin lock-in),
con Stripe nativo (suscripciones, portal de cliente, pagos únicos) — **confirmado como viable a
nivel producción**, no solo MVP, aunque conviene auditar el código generado antes de lanzar.

Base44 (ahora de Wix, adquirida el 18 de junio de 2025 por ~$80M, con earn-outs hasta 2029) es aún
más "todo incluido". **Actualizado 2026-08-25:** "Base44 Payments powered by Wix" sí soporta pagos
recurrentes/suscripciones nativas para cobrar a terceros (confirmado en su propia documentación de
soporte), y su ARR pasó de $100M en marzo-2026 a ~$150M a mediados de mayo-2026 — señal de tracción
real, no solo promesa. Lo que sigue sin verificarse a fondo es el detalle operativo (tasas de
procesamiento exactas, soporte multi-moneda, límites de payout) para un modelo de reventa
específico — se recomienda una prueba real con una suscripción de bajo monto antes de comprometer
el modelo de negocio a esta vía.

- Costo inicial: ~$25/mes.
- Costo mensual: $25-$50/mes + variable de API.
- Dificultad: baja-media — la más amigable para alguien sin experiencia técnica.

## Ruta C — Licenciar una plataforma white-label ya existente

Contratar un plan de agencia/reseller de una herramienta ya construida (ej. ReelsBuilder AI, Wideo,
Viddyoze). Cero desarrollo, lanzamiento en días.

**Advertencia:** el rebranding completo del dashboard (dominio propio, marca 100% removida) es raro
y normalmente exige contrato Enterprise negociado directamente con el proveedor — la mayoría solo
permite tu logo en el video exportado, no una app con tu marca completa.

- Costo: desde ~$500/mes de retainer + créditos al costo (revendibles con margen).
- Dificultad: muy baja, pero es la opción menos escalable y menos "tuya" a largo plazo.

## Riesgos generales confirmados en la validación (aplican a las 3 rutas)

- **Softr, Glide y Adalo son insuficientes** para este caso de uso: ninguna maneja bien colas de
  trabajos de IA de varios minutos, y sus costos reales de planes altos (Softr Business $269/mes)
  son mayores a lo inicialmente estimado.
- **Dependencia de un solo proveedor de IA:** si un proveedor sube precios o cierra su API (como
  pasó con Sora 2), el producto se puede romper — diseñar el backend para poder cambiar de
  proveedor sin rehacer todo.
- **Riesgo legal de reventa** — ver [`04_LEGAL_RIESGOS.md`](04_LEGAL_RIESGOS.md).

## Recomendación de secuencia (del informe original)

Empezar en **Ruta B** con la propia audiencia como grupo de prueba (costo y riesgo mínimos), y
solo escalar a Ruta A (Bubble) cuando el MVP muestre que la gente realmente paga y usa el producto
de forma recurrente.

## Preguntas abiertas para la próxima ronda de investigación

- [x] ¿Sigue siendo Lovable la mejor opción? — Sí por ahora; no apareció un competidor claramente
      mejor posicionado en la búsqueda 2026-08-25. Diferencia clave frente a Bubble: Lovable genera
      código React/TypeScript real que sincroniza a GitHub sobre Supabase (sin lock-in), mientras
      Bubble no permite exportar código — vive encerrado en su plataforma.
- [x] Confirmar estado real de Base44/Wix para pagos recurrentes de terceros — Confirmado que sí
      soporta suscripciones recurrentes nativas ("Base44 Payments powered by Wix"), con tracción
      real (ARR de $100M a ~$150M entre marzo y mayo de 2026). Persiste duda operativa fina (tasas,
      multi-moneda, payouts) — ver nota en Ruta B arriba.
- [ ] **PENDIENTE, no resuelto en esta pasada:** auditar en la práctica (no solo documentación) cómo
      maneja Lovable/Supabase colas de trabajos de IA de varios minutos. La búsqueda web no encontró
      documentación técnica específica sobre esto en ninguna plataforma — es información que solo
      se obtiene construyendo un prototipo real con callback/webhook y midiendo. Sigue siendo el
      punto más débil sin verificar de toda la investigación no-code; recomendado como primer
      experimento técnico antes de comprometer la Ruta B en firme.
- [ ] Evaluar si conviene el patrón "Lovable/Supabase + Edge Functions + webhook de fal.ai" en vez
      de esperar respuesta síncrona — mismo patrón que ya se identificó como necesario en Bubble
      (Ruta A), aplica igual aquí.

## Fuentes

Documentación oficial de Bubble, Lovable y Wix/Base44 (citadas en `informe_higgsfield.pdf`, agosto 2026).
Verificación fresca 2026-08-25: [Lovable — Bubble vs Lovable comparison](https://lovable.dev/guides/bubble-vs-lovable-no-code-platform-comparison),
[Base44 Payments powered by Wix — Wix Support](https://support.wix.com/en/article/base44-payments-powered-by-wix-ensuring-your-business-is-ready-for-sales),
[Base44 Payments — recurring subscriptions, Wix Support](https://support.wix.com/en/article/base44-payments-creating-and-managing-subscriptions),
[Calcalistech — Base44 ARR growth 2026](https://www.calcalistech.com/ctechnews/article/j7bfdhkor).
