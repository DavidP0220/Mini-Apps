# CANAL — sistema multiagente para monetizar

Este directorio es un proyecto **autocontenido**: el motor de mini-apps del repositorio no lo
toca y él no toca el motor. Está montado así a propósito, para poder moverlo entero a un
repositorio propio del canal en cuanto exista (decisión D-10, que aplica la regla de no mezclar
canales, error E-06).

---

## Cómo se llama esto de verdad

No son "3 súper agentes". El nombre técnico de lo que hay montado aquí es:

> **Un sistema multiagente con orquestador jerárquico y memoria institucional versionada.**

Cuatro piezas, cada una con su nombre propio:

| Pieza | Nombre técnico | Qué es aquí |
|---|---|---|
| El jefe | **Orquestador** (patrón *supervisor/worker*) | `jefe-monetizacion`: no investiga, reparte, revisa, rechaza y presiona |
| Los especialistas | **Subagentes especializados** | Cuatro, cada uno con un solo oficio y su propio contexto limpio |
| La memoria | **Base de conocimiento versionada** (*memoria institucional*) | `base-conocimiento/` + `archivo/`: en git, con historial, imposible de perder |
| La disciplina | **Ciclo operativo con métrica norte** (*north-star metric*) | Una ronda por día, y cada ronda mueve un número o explica por escrito por qué no |

Por qué esto es mejor que "tres agentes muy buenos": un agente muy bueno **olvida** al cerrar la
sesión. Aquí lo que se aprende queda escrito en el repositorio, con fecha y fuente — así que la
ronda 60 arranca sabiendo todo lo de las 59 anteriores, y ningún error del catálogo se puede
repetir por descuido. La inteligencia no está solo en el modelo: está en la memoria y en el
proceso que la obliga a usarse.

---

## Los cinco agentes

| Agente | Oficio | Se le pide… |
|---|---|---|
| **`jefe-monetizacion`** | Orquestador. Único KPI: monetizar | Abrir y cerrar cada ronda, priorizar, revisar, rechazar lo flojo, mantener `ESTADO.md` |
| **`investigador-nicho`** | Inteligencia externa | Qué está funcionando **ahora**: títulos, formatos, canales que rompen, cambios de algoritmo, palancas de ingreso |
| **`analista-datos`** | La verdad medida | Los números propios y de la competencia, la distancia real al objetivo, qué repetir y qué matar |
| **`arqueologo-memoria`** | Archivo y forense | Rescatar y verificar lo viejo, mantener el catálogo de errores, garantizar que nada se borre |
| **`director-storyboard`** | Producción | Guion → storyboard panel a panel → cronología de producción, **antes** de generar un solo fotograma |

Viven en `.claude/agents/`. Se lanzan con la herramienta Agent, o con el comando `/ronda-diaria`.

---

## Mapa del directorio

```
canal/
  ESTADO.md              ← el tablero vivo. Empieza SIEMPRE por aquí
  README.md              ← este archivo
  base-conocimiento/     ← lo que sabemos, con fuente y fecha
    00-INDICE.md           punto de entrada
    01-hallazgos/          una ficha por hallazgo verificado
    02-errores/            ★ 14 errores ya pagados, con antídoto
    03-benchmarks/         qué funciona fuera, con números
    04-metricas/           serie histórica + umbrales de decisión
    05-decisiones/         qué se decidió, cuándo y por qué
    06-fuentes/            registro de fuentes consultadas
  archivo/               ← material fuente INMUTABLE (18 MB del proyecto anterior)
  bitacora/              ← diario de trabajo de cada agente, append-only
  storyboards/           ← plantilla de 12 campos + esquema JSON
  produccion/            ← el pipeline de 13 pasos y sus 3 gates
  puente-kimi/           ← handoffs y reportes con Kimi Code
  protocolos/            ← investigación · antiborrado · definición de "hecho"
```

---

## El ciclo diario

```
1. El jefe lee ESTADO.md, la bitácora y el handoff activo de Kimi
2. Reparte encargos a los especialistas (en paralelo cuando son independientes)
3. Cada especialista investiga/analiza y DEJA ESCRITO su resultado en el repositorio
4. El jefe revisa contra el catálogo de errores y contra la definición de "hecho"
     → rechaza lo que no cumple, diciendo exactamente qué falta, y lo relanza
5. El jefe cierra: actualiza ESTADO.md con números, deuda, bloqueante y las 3 acciones de mañana
6. Todo se commitea y se pushea. Lo que no está en el repositorio, no existe
```

Se dispara con **`/ronda-diaria`**. Y `/estado-canal` da la foto rápida sin lanzar nada.

---

## Las reglas que no se negocian

1. **Español** con David, siempre. El canal publica en inglés.
2. **Fuente y fecha** en todo dato externo. Sin fuente es opinión.
3. **Número con su tamaño de muestra.** Un CTR sobre 23 impresiones no dice nada.
4. **Nada se borra.** Lo superado se marca OBSOLETO con fecha y se queda.
5. **Investigación sin decisión es ruido.** Toda ficha cierra en adoptar / probar / descartar.
6. **La calidad solo sube.** Mínimo 1080p, verificado en el archivo de salida.
7. **Nada se genera sin storyboard aprobado.**
8. **Un agente no aprueba su propio trabajo.**
9. **Ni un peso ni un crédito** sin autorización explícita de David. Nada público se publica ni
   se edita sin su visto bueno.
10. **Dos fallos del mismo método = stop y escalada.** No hay tercera tanda.

---

## Por dónde empezar (si llegas nuevo a este directorio)
1. `ESTADO.md` — dónde estamos hoy y qué bloquea.
2. `base-conocimiento/02-errores/ERRORES-HISTORICOS.md` — lo que ya salió caro.
3. `base-conocimiento/05-decisiones/DECISIONES.md` — lo que ya está decidido y no se reabre.
4. `base-conocimiento/03-benchmarks/BENCHMARKS.md` — lo que sí funciona, con cifras.
5. `archivo/LEEME.md` — qué hay en el archivo histórico y qué falta.
