# MÉTRICAS — serie histórica

**Append-only.** Cada captura añade una fila con su fecha. No se reescribe una fila anterior
aunque el dato haya cambiado: se añade la nueva. La historia de los números es un dato en sí.

Lo mantiene el agente `analista-datos`.

---

## 1. Canal nuevo (el que vamos a crear)

*Sin datos todavía. La primera fila entra el día que se publique el primer video.*

| Fecha | Suscriptores | Horas públicas | Vistas | Videos publicados | Nota |
|---|---|---|---|---|---|
| — | — | — | — | — | pendiente de crear el canal |

**Objetivo del Programa de Socios:** 1.000 suscriptores **y** 4.000 horas de visualización
pública en 12 meses (vía formato largo), o 10 millones de vistas de formato corto en 90 días.
La vía elegida es la de formato largo — ver `../05-decisiones/DECISIONES.md`, decisión D-01.

---

## 2. Datos heredados del canal anterior (referencia, no es este canal)

Punto de partida documentado del proyecto previo, útil como línea base de lo que produce cada
formato. Capturado a mano en YouTube Studio → Cobertura → "Desde la publicación".

**Estado del canal al 2026-08-22:** 7 suscriptores, 246 vistas, ≈6,8 horas.

| Captura | Video | Publicado | Impresiones | CTR | Veredicto de entonces |
|---|---|---|---|---|---|
| 2026-08-26 | The Psychological Secret to Solving EVERYTHING | 19-jul-2026 | 526 | 4,4 % | Normal, no tocar |
| 2026-08-26 | The 300000 Year Old Glitch | 07-ago-2026 | 108 | 13,0 % | Muy bueno, no tocar |
| 2026-08-26 | The Psychology of Discipline | 19-ago-2026 | 23 | sin datos suficientes | **Ruido**, esperar más impresiones |
| 2026-08-26 | Your DNA Hates Predator Meat | 28-jul-2026 | 68 | 14,7 % | Muy bueno, no tocar |

**Dato comparativo de formato (2026-08-22):**
95 vistas de formato corto → 8 minutos vistos → **0 suscriptores**.
146 vistas de formato largo → 398 minutos vistos → **4 suscriptores**.

**Conclusión que sigue vigente:** con 3-7 % de CTR de referencia para canales pequeños del nicho,
ninguna de esas miniaturas estaba fallando. El cuello de botella era **pocas impresiones**, es
decir poco volumen publicado — no mal CTR. Ver error E-04.

---

## 3. Umbrales de decisión (para no repetir E-04)

| Métrica | Muestra mínima para concluir | Qué se hace por debajo |
|---|---|---|
| CTR de miniatura | ~500 impresiones | Nada. Se espera y se vuelve a medir |
| Retención media | 100 vistas | Nada |
| Efecto de un cambio de título | 2 semanas o 1.000 impresiones | Nada, y no se cambia otra cosa a la vez |

Regla que acompaña: **nunca se cambia lo que ya funciona.**

---

## 4. Cómo se capturan

1. YouTube Studio → cada video → pestaña **Cobertura** → periodo **"Desde la publicación"**:
   impresiones, CTR, vistas, duración media de visualización.
2. Studio → Analytics → Descripción general: suscriptores y horas públicas acumuladas.
3. Alternativa sin abrir Studio: conector de **vidIQ** (estadísticas de canal y de video), que
   además permite comparar contra competidores con el mismo criterio.

**Cadencia:** cada 1-2 semanas, y **siempre a los 10 días** de publicar un video nuevo.
