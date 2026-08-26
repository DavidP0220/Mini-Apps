# Human Chronicles — Estado real del canal (fuente única de verdad)

**Última verificación documental: 2026-08-25.**
Este archivo existe para que ninguna sesión vuelva a asumir datos de memoria.
Si un dato no está confirmado aquí, **no está confirmado** — se verifica antes de usarlo.

---

## 1. Ficha del canal

| Campo | Valor | Estado |
|---|---|---|
| Nombre | Human Chronicles | Confirmado |
| Handle | `@humanchronicles11` | Confirmado (handle real, creado en YouTube) |
| Cuenta Google | `humanchronicleshq@gmail.com` | Confirmado — cuenta **nueva y aislada** |
| Idioma / audiencia | Inglés / EE.UU.-UK-CA-AU | Decidido |
| Nicho | Historia y civilizaciones | Decidido |
| Formato | **Faceless**: narración + imágenes, mapas y clips históricos. **Sin personaje/host animado** | Decidido |
| Descripción, handle y correo de contacto publicados en YouTube Studio | Sí | Confirmado |
| Foto de perfil y banner | **NO subidos** | 🔴 Pendiente (bloqueado por acción humana, ver §4) |
| Videos publicados | 0 | — |
| Suscriptores | Sin dato medido | Pendiente de verificar en YouTube Studio |

### ⚠️ Handle: corrección histórica
Documentación vieja del proyecto mencionaba `HumanChronicles18` y `@HumanChroniclesHQ`.
**Ninguno de los dos es válido.** El único correcto es **`@humanchronicles11`**.
Corregido el 2026-08-25 en `PROYECTO MECHANICS OPTIMIZACIONES/LEEME-PRIMERO-HANDOFF.md/.txt`.

### ⚠️ Aislamiento de cuentas (regla dura)
Human Chronicles vive en `humanchronicleshq@gmail.com`, **separado** de la cuenta
compartida `walterdpscpfcm@gmail.com` (que aloja otros canales) y de
`mechanicsmindset02@gmail.com` (Mindset Mechanics). El motivo es explícito: un strike
en un canal de una cuenta compartida puede arrastrar a los demás canales de esa cuenta.

Consecuencia operativa para cualquier agente o script:
1. **Verificar siempre el channel ID / la cuenta activa antes de tocar YouTube Studio.**
2. Nunca reutilizar tokens, sesiones ni `auth_state.json` de Mindset Mechanics para Human Chronicles.
3. Nunca abrir las dos cuentas en la misma sesión de navegador en paralelo (ya hubo
   conflictos de pestaña de Chrome entre sesiones concurrentes en este proyecto).

---

## 2. Qué NO se hereda de Mindset Mechanics

| Elemento de Mindset Mechanics | ¿Aplica a Human Chronicles? |
|---|---|
| Personaje fijo (gorra azul, hoodie gris, sin orejas/nariz) | **NO.** Canal faceless, sin host. |
| `ESTILO_MINDSET_MECHANICS.md` / `true_character_ref.jpg` | **NO.** Ver `ESTILO_HUMAN_CHRONICLES.md`. |
| `thumbnail-consistency-guardian` (consistencia de personaje) | **NO** en su forma actual. |
| `storyboard-director` (storyboard con personaje) | **NO** en su forma actual. |
| Fórmulas de título de psicología evolutiva | **NO** directamente — ver `PLAYBOOK_MONETIZACION_HC.md`. |
| Pipeline técnico (Recraft → VideoExpress → ensamblaje) | **SÍ**, la infraestructura se reutiliza. |
| Política de idiomas (`POLITICA_IDIOMAS.md`) | **SÍ** — canal en inglés, comunicación interna en español. |
| Calidad mínima 1080p | **SÍ**, regla global del proyecto. |
| Protocolo de handoffs y respaldo en git | **SÍ**, regla global. |

---

## 3. Infraestructura ya existente reutilizable

- `youtube_pipeline/` — ya es genérico y multi-canal (`youtube_pipeline/channels/<canal>/`).
  Human Chronicles debería vivir como un canal más ahí, **no** como un pipeline aparte.
- `recraft_ai/` — generación de imágenes vía API (no navegador). Reutilizable tal cual.
- `handoffs/` — mismo protocolo de coordinación entre sesiones.
- Agentes genéricos (`community-engagement-manager`, `growth-acquisition-lead`,
  `publish-readiness-coordinator`, `knowledge-archivist`): sus prompts hoy nombran
  explícitamente "Mindset Mechanics". Se les añadió una nota de alcance multi-canal
  el 2026-08-25 — **hay que decirles explícitamente en qué canal trabajan** al invocarlos.

---

## 4. Pendientes reales (nada de esto se puede simular)

| # | Pendiente | Depende de | Bloquea |
|---|---|---|---|
| 1 | Login confirmado en Recraft AI con la cuenta de pago | **David (acción humana)** | Generar avatar y banner |
| 2 | Generar foto de perfil (800×800 mín., se ve a 98×98) y banner (2048×1152) | Autorización explícita de gasto de créditos | Identidad visual del canal |
| 3 | Subirlos en YouTube Studio > Personalización de la cuenta `humanchronicleshq@gmail.com` | David (login) | Publicar el primer video con canal presentable |
| 4 | Definir subnicho concreto dentro de "historia" | Decisión creativa (David/Kimi) | Guion del video 1 |
| 5 | Verificar suscriptores/estado real en YouTube Studio | Acceso a la cuenta | Métricas base |

**Ninguno de estos pendientes se ha ejecutado. No inventar avances.**

---

## 5. Reglas de seguridad para este canal

1. **Nunca publicar nada** sin aprobación explícita de David.
2. **Nunca gastar créditos** de Recraft/VideoExpress para Human Chronicles sin autorización
   explícita — el presupuesto vigente del proyecto está asignado a Mindset Mechanics.
3. **Nunca tocar producción activa de Mindset Mechanics** desde una tarea de Human Chronicles.
4. Todo lo que se genere para este canal se respalda en git desde el primer día
   (Recraft y VideoExpress borran lo generado a los ~60 días).
