# PUENTE CON KIMI CODE — protocolo

Kimi Code es el **estratega y decisor de alto nivel**. Los agentes de este repositorio son la
**ejecución**.

## ⚠️ Cómo funciona el puente DE VERDAD (corregido 2026-08-27)

La primera versión de este documento decía que la comunicación era por commits al repositorio.
**Era incorrecto.** Verificado contra las reglas del repositorio `DavidP0220/mindset-mechanics`,
que es donde Kimi trabaja:

> **Kimi no tiene cuenta de Google, ni acceso a disco, ni acceso a git.**

Es decir, el puente es **asimétrico** y solo una dirección está automatizada:

| Dirección | Cómo funciona | ¿Automático? |
|---|---|---|
| **Kimi → Claude** | Kimi deja el archivo en una carpeta de Drive sincronizada en el PC de David (`kimi-buzon`). David escribe *"sincroniza"* y Claude la copia a `handoffs/` | Sí, si Claude corre **en el PC de David** |
| **Claude → Kimi** | Claude escribe el handoff, le dice a David el **nombre exacto del archivo**, y **David lo arrastra a mano al chat de Kimi** | **No. Nunca lo fue.** El puente es David |

**Y una limitación más, de esta sesión:** cuando Claude corre en la nube (como ahora) tampoco
puede leer el buzón de Drive, porque ese es un disco del PC de David. En sesiones en la nube,
**las dos direcciones son manuales**.

### Consecuencia práctica
Un handoff escrito y commiteado **no llega a Kimi por sí solo**. El trabajo no está entregado
hasta que David lo arrastra al chat de Kimi. Por eso cada handoff se cierra avisando a David
del nombre exacto del archivo — nunca se da por entregado sin ese aviso.

### Propuesta para quitar a David de cartero (pendiente de su decisión)
El repositorio `DavidP0220/Mini-Apps` es **público**, así que cualquier archivo suyo es legible
desde una URL de tipo `raw.githubusercontent.com`. Si Kimi Code puede abrir enlaces, publicar
ahí los handoffs haría automática la dirección Claude → Kimi.
**Contrapartida que David debe sopesar:** eso hace públicos los documentos de estrategia del
proyecto. Hoy viven en un repositorio privado. No se hace sin su visto bueno explícito.

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
