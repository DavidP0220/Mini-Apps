# Habilidades que faltan por aprender (para retroalimentar mejor este proyecto)

Esto es una lista honesta de huecos, no una crítica al trabajo hecho — el sistema actual cubre bien
investigación de mercado/técnica/legal y planeación, pero todavía no ha probado varias capacidades
que el proyecto va a necesitar pronto. Cada punto dice qué falta, por qué hace falta, y qué agente
o habilidad nueva lo resolvería.

## 1. Nadie ha ejecutado nada técnico todavía — todo es investigación y plan

Los 3 agentes actuales (`higgsfield-market-intel`, `higgsfield-tech-scout`,
`higgsfield-product-architect`) investigan y deciden, pero **ninguno construye código ni prueba
software real**. La Fase 2 del roadmap (prueba de colas largas en Lovable) es la primera vez que el
proyecto va a tocar una herramienta real, y ningún agente de este equipo tiene ese trabajo asignado
todavía. Falta un agente (o ampliar `higgsfield-product-architect`) que sepa ejecutar y documentar
resultados de experimentos técnicos reales, no solo planearlos.

## 2. Ninguna validación legal real, solo lectura de ToS por un agente

`higgsfield-tech-scout` leyó los términos de servicio de Runway/ElevenLabs/fal.ai y corrigió un
error real del informe original — pero sigue siendo lectura de un agente de IA, no asesoría legal.
El propio documento `04_LEGAL_RIESGOS.md` señala esto como pendiente: "definir con un abogado si el
modelo de negocio necesita algo más que leer los ToS". Falta esa consulta real, y falta un criterio
claro de cuándo un hallazgo de `higgsfield-tech-scout` es suficiente vs. cuándo exige a un humano
con licencia legal.

## 3. Sin agente ni proceso de modelado financiero real

Los precios propuestos (créditos ~$9/$29, margen 3x) están basados en el costo estimado de
generación de doc 02, no en un modelo financiero real con proyección de cashflow, punto de
equilibrio, o sensibilidad a distintos volúmenes de uso. Falta una habilidad de "modelar unit
economics con datos reales" una vez que la Fase 2 del roadmap arroje el costo real medido (no
estimado) de generar un video.

## 4. Sin agente de diseño/UX ni de marca del producto nuevo

El nicho está definido (mindset/motivación) pero no hay ningún trabajo hecho sobre cómo se ve o se
siente el producto: nombre final, identidad visual, tono de copy del landing, experiencia de primer
uso. `storyboard-director` y `thumbnail-consistency-guardian` existen para el canal de YouTube, pero
nadie cumple ese rol para este producto de software.

## 5. Sin agente de seguridad/manejo de secretos para un no-técnico manejando API keys reales

El roadmap ya instruye guardar claves en Bitwarden y nunca en texto plano, pero es una instrucción
puntual dentro de un documento, no una habilidad que se revise sistemáticamente a medida que se
añaden más proveedores (Stripe, fal.ai, y luego posiblemente ElevenLabs/Runway en Nivel 2). Falta
un chequeo recurrente tipo "auditoría de secretos" — el mismo tipo de trabajo que
`chief-technical-officer` ya hace para el pipeline de Mindset Mechanics, pero aplicado a este
proyecto nuevo.

## 6. Sin agente de crecimiento/adquisición para el producto (distinto del de YouTube)

`growth-acquisition-lead` existe para traer audiencia nueva al canal de YouTube, no para conseguir
los primeros usuarios de pago de este producto. Son audiencias relacionadas pero la conversión
"seguidor del canal → usuario de pago del producto" es una habilidad de growth distinta (onboarding,
prueba gratis, primeras 10-30 personas) que ningún agente cubre todavía.

## 7. Sin proceso de medir si el nicho elegido sigue siendo el correcto una vez haya usuarios reales

`01_COMPETENCIA_HIGGSFIELD.md` valida el nicho con investigación de mercado externa, pero no hay
ninguna habilidad de "medir con datos propios" (cuántos de los primeros usuarios de prueba realmente
pagan, qué feedback dan, qué tan seguido vuelven) una vez arranque el Nivel 1. Es el mismo tipo de
disciplina que `thumbnail-ctr-strategist` aplica al canal (medir rendimiento real, no intuición) pero
todavía no existe para este producto.

## 8. Ningún agente de este equipo ha sido puesto a prueba con un fallo real todavía

Todos los aprendizajes de `07_ERRORES_Y_LECCIONES.md` (heredados y propio) vienen de investigación o
de auditoría de infraestructura — ninguno viene todavía de "el producto falló en producción y
tuvimos que arreglarlo con usuarios reales esperando". Es una habilidad que este sistema no puede
fabricar por adelantado; solo se aprende ejecutando la Fase 2 en adelante y documentando lo que
salga mal ahí, con la misma disciplina que ya se aplicó a las lecciones heredadas.

## Cómo usar esta lista

No es una lista de "crear 8 agentes nuevos ya". Es la entrada para que quien reciba este paquete
(otra sesión de Claude, otro proyecto) sepa exactamente qué preguntar o construir cuando el Nivel 1
avance más allá de la investigación — y para que `higgsfield-product-architect` la revise antes de
proponer la siguiente fase de decisiones, en vez de asumir que la investigación actual ya cubre todo
lo que el producto va a necesitar.
