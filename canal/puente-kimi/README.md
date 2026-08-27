# PUENTE CON KIMI CODE — protocolo

Kimi Code es el **estratega y decisor de alto nivel**. Los agentes de este repositorio son la
**ejecución**. La comunicación entre los dos lados ocurre **por archivos versionados en el
repositorio**, no por chat: así queda historial, fecha y autor de cada decisión.

Este protocolo no se reinventa: viene funcionando desde el proyecto anterior y su historial
completo está en `../archivo/2026-08-26_traslado_mindset_mechanics/03_PUENTE_KIMI_CLAUDE_HANDOFFS/`.

## Los dos tipos de archivo

| Archivo | Lo escribe | Qué es |
|---|---|---|
| `HANDOFF_YYYY-MM-DD_<tema>.md` | Kimi (o los agentes, para **pedir** una decisión) | **El plan activo.** El más reciente manda |
| `REPORTE_YYYY-MM-DD_<tema>.md` | Los agentes | Qué se hizo, qué falló, qué se gastó, qué bloquea |
| `NOTA_INVESTIGACION_YYYY-MM-DD_<tema>.md` | Cualquiera | Insumo de investigación. **No** es plan activo |

## Ciclo de trabajo
1. **Al abrir la ronda:** leer el `HANDOFF_*.md` más reciente. Ese es el plan activo.
   Si hay varios del mismo día, el orden real se lee con
   `git log --reverse --name-status -- canal/puente-kimi/`, **nunca** por la fecha del archivo
   (tras un `git pull` todas quedan con la fecha del pull).
2. **Ejecutar por lotes**, respetando los gates. **Nunca se contradice un handoff de Kimi sin
   consultarlo.** Las decisiones de alcance, estrategia y presupuesto son suyas.
3. **Al cerrar el lote:** escribir un `REPORTE_` y commitear. Los bugs se reportan siempre en el
   formato **síntoma → causa raíz → arreglo → verificación**, con el gasto consumido contra el
   presupuesto y los bloqueantes abiertos.
4. **Si la investigación contradice el plan activo:** no se ejecuta el cambio. Se propone en un
   `HANDOFF_` nuevo que diga **explícitamente qué reemplaza**.

## Cómo se pide una decisión a Kimi (importante)
Un handoff de petición se escribe con la pregunta **cerrada**, nunca abierta:

- Mal: *"¿qué hacemos con la producción?"*
- Bien: *"Opción A: <coste, riesgo, plazo>. Opción B: <coste, riesgo, plazo>. Recomiendo A por X.
  Necesito tu sí/no antes del <fecha> porque bloquea <qué>."*

Las opciones vienen ya evaluadas. El decisor decide, no investiga.

## Gates
Un gate es un punto donde la ejecución **se para** hasta tener autorización escrita. Mientras un
gate está cerrado se avanza solo en tareas de coste cero. Cruzar un gate sin autorización es el
error E-13 del catálogo.

## Qué está pre-autorizado y qué no
- **Pre-autorizado:** investigar, escribir documentos, commitear y pushear el trabajo del repo.
- **Requiere autorización explícita de David:** gastar dinero o créditos de pago, publicar o
  editar contenido público (videos, títulos, descripciones, comentarios, comunidad), tocar
  cuentas de terceros.
