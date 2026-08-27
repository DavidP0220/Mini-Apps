# PROTOCOLO DE INVESTIGACIÓN

Regla de oro: **investigación sin decisión es ruido.** Toda ficha termina en *adoptar* /
*probar con presupuesto X y medir Y* / *descartar porque Z*.

## Las cinco condiciones para que un hallazgo entre al repositorio
1. **Fuente + fecha de consulta.** URL completa. Sin fuente es opinión, no dato.
2. **Número, no adjetivo.** "Funciona bien" se rechaza; "14,7 % de CTR sobre 68 impresiones" se acepta.
3. **Tamaño de muestra.** Todo porcentaje va con el denominador al lado.
4. **Verificado en la fuente real**, no en un resumen de sesión anterior (error E-03).
5. **Recomendación cerrada**, con su coste y su forma de medirla.

## Plantilla de ficha
Se guarda en `canal/base-conocimiento/01-hallazgos/HALLAZGO-NNNN-<tema>.md`:

```markdown
# HALLAZGO-NNNN — <título en una línea>
**Fecha:** YYYY-MM-DD · **Agente:** <quién> · **Frente:** nicho | algoritmo | monetización | producción | guiones
**Estado:** propuesto | adoptado | en prueba | descartado | OBSOLETO desde YYYY-MM-DD

## Qué encontré
<Los hechos, con cifras y tamaño de muestra.>

## Por qué importa para nosotros
<Conexión directa con suscriptores, horas de visualización o ingresos. Si no la hay, no es un hallazgo.>

## Qué contradice o confirma
<Decisión D-NN o hallazgo previo. Si contradice algo vigente, se dice explícitamente.>

## Recomendación
- [ ] Adoptar ya — acción concreta:
- [ ] Probar — presupuesto: · métrica que lo juzga: · fecha de veredicto:
- [ ] Descartar — motivo:

## Fuentes
| URL | Fecha de consulta | Qué aportó |
|---|---|---|
```

## Numeración
Correlativa y **nunca se reutiliza**, ni siquiera si la ficha se descarta. Una ficha descartada
sigue siendo información: dice que ese camino ya se exploró.

## Coste cero por defecto
La investigación es web y datos: nunca gasta créditos ni dinero. Cualquier recomendación que
implique gasto va como propuesta con presupuesto, jamás ejecutada directamente.
