# HUECO #1 — Voz narrativa sintética de calidad

**Ronda 01 · 2026-08-26 · estado previo: 🔴 SIN PROBAR (ninguna herramienta evaluada)**
**Estado ahora: 🟡 CANDIDATAS ELEGIDAS Y JUSTIFICADAS — falta la prueba de escucha (requiere a David)**

Es el hueco más grave del canal: la voz es el ancla de marca (`ESTILO_HUMAN_CHRONICLES.md` §2) y a la
vez el marcador que dispara la revisión por contenido no auténtico. Esta ronda no lo cierra —
ninguna investigación cierra una decisión de oído — pero lo deja listo para decidir en una sesión.

---

## 1. Lo primero: la política, porque condiciona la elección

**Las voces sintéticas NO están prohibidas ni son un problema de monetización por sí mismas.** Lo
que YouTube castiga, bajo la política de contenido no auténtico (renombrada desde "contenido
repetitivo" en 2026), es otra cosa:

- Narración de IA de baja calidad leyendo texto sobre metraje de stock, sin punto de vista propio.
- Guiones leídos literalmente de una fuente externa.
- Producción en masa con plantilla.

La formulación que mejor resume el criterio real: una locución de IA es monetizable cuando
**funciona como un departamento de producción de verdad** — narración dirigida, escrita para el
montaje y mezclada profesionalmente. No es la herramienta lo que se juzga, es el resultado.

### Declaración obligatoria y su régimen sancionador (dato nuevo, importante)
Hay que marcar la casilla **"Altered or synthetic content"** en YouTube Studio cuando haya voz
sintética, visuales generados por IA o alteraciones realistas. **No declararlo activa un sistema de
tres golpes: aviso → suspensión de monetización 90 días → expulsión permanente del YPP.**

Esto es más duro de lo que decía la documentación previa del canal (que solo señalaba que "la
etiqueta no penaliza el alcance", lo cual sigue siendo cierto). **Declarar es gratis; no declarar
puede costar el canal.** Regla del canal: ante la duda, se declara.

---

## 2. Las candidatas, ordenadas por lo que importa a este canal

Criterios, en este orden: (a) calidad de narración larga sostenida, (b) coste real, (c) licencia
comercial sin ambigüedad, (d) control sobre la variación prosódica (lo que separa "documental" de
"robot").

### Opción A — Chatterbox (Resemble AI) · **recomendada para probar primero**
- **Licencia MIT.** Comercial sin condiciones, sin cuota por carácter.
- 0,5B de parámetros, se ejecuta local. **Coste marginal por video: 0 €.**
- En el estudio de escucha ciega del propio fabricante, **65,3% de los oyentes prefirieron su voz
  Turbo frente a ElevenLabs** (24,5% a la inversa). Dato del fabricante — tratar como indicio
  fuerte, no como verdad neutral.
- Soporta clonación de voz, lo que permite fijar **una** voz de canal y no volver a tocarla.
- Riesgo: calidad y estabilidad en pasajes de 8-12 minutos sin cortes, no verificada aquí.

### Opción B — Kokoro-82M · **recomendada como caballo de batalla**
- **Licencia Apache 2.0.** Comercial sin condiciones.
- Corre en **2-3 GB de VRAM, incluso en CPU**. Es el modelo señalado específicamente *para
  narración*.
- Muy rápido y barato de operar → sirve para iterar el guion escuchándolo antes de fijar la toma
  buena.
- Riesgo: menos expresivo que Chatterbox. Puede ser justo el perfil "plano" que hay que evitar.

### Opción C — ElevenLabs · **referencia de calidad, pero cara**
- Modelo construido para entender la lógica y la emoción del texto y cómo cada frase conecta con la
  de al lado — que es exactamente lo que un documental necesita en pasajes largos.
- **Pro 99 $/mes, Scale 330 $/mes.** El consenso de 2026 es que "se puso caro" y está empujando a
  los creadores hacia alternativas.
- Uso sensato aquí: **no** como motor de producción, sino como **vara de medir**. Generar el mismo
  párrafo en ElevenLabs y en las opciones A/B y comparar.

### Opción D — Fish Audio S2 Pro · alternativa de pago barata
- ~5,5 $/mes con facturación anual, 200 min de audio/mes, uso comercial incluido.
- Señalada como "lo más cercano a la calidad de ElevenLabs" por precio.
- 200 min/mes ≈ 20 videos de 10 min. Suficiente de sobra para el ritmo del canal (2 largos/semana).

### Descartadas y por qué
- **XTTS v2** — licencia CPML, no comercial libre. Descartada por licencia.
- **F5-TTS** — CC-BY-NC 4.0, **no comercial**. Descartada por licencia.
- **PlayHT / LOVO** — buenas para long-form y voces de documental respectivamente, pero no aportan
  nada que A-D no cubran ya a mejor precio. Reserva.

> **Trampa de licencia a vigilar (vale para cualquier herramienta):** que un modelo sea libre no
> basta. Si se accede por una API alojada, **los términos de servicio de ese proveedor y de ese
> plan concreto** también tienen que permitir uso comercial. Se verifican las dos cosas.

---

## 3. Cómo se decide (protocolo de prueba — 1 sesión, coste 0)

`ERRORES_A_EVITAR.md` #2 manda: el QA técnico no aprueba nada, la aprobación es de David y viendo
(aquí, oyendo) el resultado real, no una descripción.

1. **Texto de prueba fijo:** los primeros 90 segundos del guion del video 1 — cold open + tesis.
   Tiene que ser texto real del canal, no una frase de demo. Precedente: `ERRORES_A_EVITAR.md` #17,
   validar contra una prueba aislada en vez de contra material real salió mal.
2. Generar **el mismo texto** en Chatterbox, Kokoro y (una sola vez, plan gratis o mínimo)
   ElevenLabs como referencia.
3. **Escucha ciega de David**, sin decirle cuál es cuál. Solo una pregunta: *¿cuál de estas tres
   suena a canal de documentales que verías 10 minutos seguidos?*
4. La ganadora se fija como **voz del canal** y se anota en `ESTADO_CANAL.md` como dato *decidido*.
   No se vuelve a tocar: la consistencia de voz **es** la marca en un canal faceless.

### Criterio de "alta calidad con variación real" (lo que faltaba definir)
No hay métrica automática fiable de monotonía. Lo que sí es verificable a oído, y se convierte en
checklist:
- [ ] ¿Hay **pausas** distintas entre frases, y no un silencio de duración idéntica?
- [ ] ¿Cambia la entonación al final de una pregunta y de una afirmación?
- [ ] ¿Hay énfasis en el nombre propio o la cifra, o pasa igual que el resto?
- [ ] A los 3 minutos seguidos, ¿sigue sonando a alguien contando algo, o a alguien leyendo?
- [ ] ¿Respira? (una narración sin respiraciones se detecta como sintética al instante)

Si falla la 4ª, la voz no sirve para este canal por buena que sea en una frase suelta.

## 4. Qué queda pendiente y de quién depende

| Pendiente | Responsable | Bloquea |
|---|---|---|
| Instalar Chatterbox y Kokoro en local (ambos gratis, sin cuenta de pago) | David (una vez) | Toda la prueba |
| Escucha ciega y elección de voz | **David** (decisión de oído, no la toma un agente) | El guion del video 1 y el canon del canal |
| Anotar la voz elegida en `ESTADO_CANAL.md` | `human-chronicles-program-director` | — |

**Ninguna de las 4 opciones exige gastar créditos ni autorización de presupuesto.** Este hueco se
puede cerrar sin desbloquear ninguno de los bloqueos 🔴 del tablero. Es, por tanto, **lo más útil
que se puede hacer hoy mismo**.

## Fuentes

- [Best Open-Source TTS 2026: Chatterbox 65.3% Beats ElevenLabs — FindSkill.ai](https://findskill.ai/blog/best-open-source-tts-2026/)
- [Kokoro vs XTTS vs Chatterbox: Best Local TTS in 2026? — Local AI Master](https://localaimaster.com/blog/kokoro-vs-xtts-vs-chatterbox)
- [Best Local TTS Models 2026: 8 Open-Source Voices Tested — Local AI Master](https://localaimaster.com/blog/best-local-tts-models)
- [Best Open-Source Text to Speech in 2026: 8 Free Models Ranked — TextToLab](https://texttolab.com/blog/open-source-text-to-speech)
- [14 Best ElevenLabs Alternatives in 2026 (Tested & Compared) — Fliki](https://fliki.ai/blog/elevenlabs-alternatives)
- [Best AI Voice Generators in 2026 (Tested by a Creator) — Feisworld Media](https://www.feisworld.com/blog/best-ai-voice-generators)
- [Is AI-Generated Voice Content Still Monetizable on YouTube? (2026) — Beverly Boy](https://beverlyboy.com/film-technology/youtube-in-2026-is-ai-generated-voice-content-still-monetizable/)
- [Using AI Voices for YouTube Monetization (2026 Policy) — Fluxnote](https://fluxnote.io/guides/using-ai-voices-for-youtube-monetization)
- [YouTube AI Monetization Policy 2026 — Rules, Disclosure, Tips — Vexub](https://vexub.com/blog/ai-generated-video-monetization-policies)
- [YouTube Monetization with AI Content 2026 — Miraflow](https://miraflow.ai/blog/youtube-monetization-ai-content-2026-allowed-demonetized)
