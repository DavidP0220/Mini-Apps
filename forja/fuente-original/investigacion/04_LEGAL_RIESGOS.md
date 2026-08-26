# Riesgos legales y de negocio

> Mantenido por el agente `higgsfield-tech-scout`. Última actualización con datos verificados: 2026-08-25
> (fuente: `informe_higgsfield.pdf`); **segunda pasada de verificación línea por línea 2026-08-25
> (misma fecha, con lectura directa de ToS via WebFetch) matizó y corrigió el hallazgo principal —
> ver sección actualizada abajo. Ningún hallazgo nuevo bloquea el proyecto, pero sí precisa
> exactamente qué modelo de arquitectura es legalmente viable con cada proveedor.**
> Este documento es el que más puede frenar el proyecto si se ignora —
> revisarlo antes de cualquier decisión que implique gastar dinero real o vender a un tercero.

## El hallazgo más importante de la validación: riesgo de reventa

Runway y ElevenLabs otorgan la propiedad de los outputs en sus planes de pago, pero sus términos de
servicio **prohíben explícitamente arrendar, alquilar o sublicenciar el servicio a terceros** — es
decir, **revender acceso al pipeline de generación puede violar sus contratos** si se hace sobre un
plan de consumidor en vez de un plan Enterprise/API comercial.

Además, los planes de consumidor **no incluyen indemnización**, lo cual es un riesgo si un usuario
final reclama por derechos de autor o uso de voz sin consentimiento.

**Antes de lanzar el modelo de reventa es indispensable leer y, si hace falta, negociar
directamente los términos comerciales con cada proveedor elegido** (Runway, ElevenLabs, Google
Cloud, Kling, fal.ai, Replicate).

### CORRECCIÓN IMPORTANTE tras leer los ToS línea por línea (2026-08-25)

El resumen original mezclaba dos cosas distintas: (1) revender el *acceso a la cuenta/API del
proveedor* y (2) construir un producto propio que *usa* la API del proveedor como backend y cobra
por ese producto. Son legalmente muy diferentes, y para este proyecto **la opción (2) es la que
aplica y SÍ es viable en los tres proveedores clave**, con matices:

- **Runway:** con plan de API estándar (no forzosamente Enterprise) puedes "integrar la
  funcionalidad de Runway en tus propias aplicaciones, productos y servicios y hacer esa
  funcionalidad disponible a end users como parte de tu aplicación" — es un derecho explícito del
  contrato de API. La única obligación real es mostrar "Powered by Runway" con link a runway.com
  según sus Branding Guidelines. Lo prohibido es sub-licenciar o revender el *servicio de Runway en
  sí* fuera de ese uso vía API (ej. no puedes vender acceso directo a la cuenta). **Esto corrige el
  dato anterior que decía que "reventa real requiere plan Enterprise" — no es así, Enterprise da
  SSO/SLA/volumen negociado, no es un requisito legal para poder operar.**
- **ElevenLabs:** confirmado que reventa del *servicio en sí* solo está permitida vía "Authorized
  Reseller" con autorización previa y por escrito de ElevenLabs. Sin esa autorización, sigue estando
  permitido integrar sus voces en un producto propio y cobrar por ese producto — lo que no puedes
  hacer es revender acceso al servicio de ElevenLabs como tal (ej. no puedes ser tú mismo un
  "reseller" de cuentas de ElevenLabs sin ese acuerdo).
- **fal.ai:** ToS (actualizados 03-mar-2026) prohíben explícitamente exponer las APIs de fal.ai
  directamente a end users, y prohíben revender/sublicenciar los derechos de la cuenta a terceros.
  Esto en la práctica **obliga** (no solo permite) a la arquitectura "backend propio intermediario",
  que es exactamente el diseño ya contemplado para este producto. **Punto crítico de indemnización:**
  el cliente (nosotros) debe defender a fal.ai ante reclamos de terceros derivados del "Customer
  Solution" — fal.ai no asume ninguna responsabilidad si un usuario final reclama por derechos de
  autor o contenido generado. Esto refuerza que el producto necesita su propio seguro/cobertura
  legal, no puede apoyarse en la de sus proveedores.

**Conclusión de la corrección:** el modelo de negocio planeado (backend propio que llama a las APIs,
cobra a usuarios finales por el producto terminado, nunca expone las API keys ni el acceso directo a
los proveedores) es legalmente viable con Runway, ElevenLabs y fal.ai tal como están redactados sus
ToS actuales. El riesgo real no es "¿se puede hacer esto?" sino "¿quién responde legalmente si un
usuario final reclama por contenido generado?" — la respuesta es: el proyecto, no los proveedores.

## Checklist de control de calidad antes de invertir dinero real

Este informe pasó por 3 rondas de investigación y 3 rondas de validación independiente. Los tres
validadores dieron veredicto "REVISAR" con correcciones, no con bloqueos críticos — todas las
correcciones ya están incorporadas en los documentos de esta carpeta. Antes de invertir dinero real:

- [ ] Elegiste el nicho específico de contenido (no competir de frente con Higgsfield en todo).
- [ ] Leíste los términos de servicio de reventa de al menos el proveedor de video e imagen elegido
      (Runway/Kling/fal.ai) antes de cobrar a un tercero.
- [ ] Confirmaste que NO estás dependiendo de la API de Sora 2 (cierra 24-sep-2026).
- [ ] Definiste el modelo de precios propio (créditos vs. suscripción) y el margen sobre el costo
      real de cada generación.
- [ ] Tienes un grupo de prueba real (tu audiencia) listo para el Nivel 1 antes de gastar en Nivel 2 o 3.
- [ ] Si vas a manejar voces clonadas o contenido de personas reales, revisaste el tema de
      consentimiento e indemnización con el proveedor de voz.

## Otros riesgos confirmados

- **Dependencia de un solo proveedor de IA:** si sube precios o cierra su API (precedente: Sora 2),
  el producto se rompe. Diseñar el backend para poder cambiar de proveedor sin rehacer todo.
- **Softr/Glide/Adalo insuficientes** para colas de generación de varios minutos — no son solo
  "más caros de lo esperado", son la herramienta equivocada para este caso de uso.

## Preguntas abiertas para la próxima ronda de investigación

- [x] Leer línea por línea los ToS de reventa de Runway, ElevenLabs y fal.ai — Hecho 2026-08-25, ver
      corrección arriba. Conclusión: el modelo "backend propio + cobro a usuario final" es viable en
      los tres; ningún ToS lo prohíbe cuando se hace así.
- [ ] No se encontró evidencia de cambios en política de indemnización desde agosto-2026 en ninguno
      de los tres proveedores — seguía igual en la revisión de esta pasada (fal.ai: indemnización es
      del cliente hacia fal.ai, no al revés; ElevenLabs/Runway: sin cambios detectados).
- [ ] Definir con un abogado (aunque sea consulta puntual, no retainer) si el modelo de negocio
      elegido específicamente (créditos vs. suscripción, con qué proveedores) necesita algo más
      que "leer los ToS" — esto sigue pendiente y sigue siendo orientación, no asesoría legal real.
      **Ahora es más urgente**: al confirmarse que el proyecto asume la indemnización frente a
      reclamos de usuarios finales (no los proveedores), conviene definir seguro de responsabilidad
      civil o cláusulas de exención en los propios términos de uso del producto antes de lanzar a
      un tercero real.
- [ ] Leer los ToS de Kling y Google Veo (Cloud) con el mismo nivel de detalle que se hizo aquí para
      Runway/ElevenLabs/fal.ai — no se hizo en esta pasada por alcance de tiempo.
- [ ] Confirmar si Runway exige plan Enterprise en la práctica para volumen alto (aunque el contrato
      estándar de API ya permite legalmente el modelo de reventa vía producto propio) — puede haber
      un límite de uso comercial no legal sino operativo (rate limits, SLA) que empuje a Enterprise
      de todas formas cuando el producto escale.

## Fuentes

Términos de servicio de Runway/ElevenLabs (citados en `informe_higgsfield.pdf`, agosto 2026).
Verificación fresca 2026-08-25 con lectura directa: [fal.ai Terms of Service](https://fal.ai/terms)
(actualizado 03-mar-2026), [ElevenLabs Terms of Service](https://elevenlabs.io/terms-of-use),
[Runway API FAQs](https://help.runwayml.com/hc/en-us/articles/21668552945171-Runway-API-FAQs),
[Runway Enterprise](https://runway.com/enterprise), [Terms.Law — Runway ML Commercial Rights &
Output Ownership 2026](https://terms.law/ai-output-rights/runway/).
