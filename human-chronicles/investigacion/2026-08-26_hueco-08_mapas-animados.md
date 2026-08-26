# HUECO #8 — Mapa animado como formato

**Ronda 01 · 2026-08-26 · estado previo: 🔴 SIN PROBAR (ni herramienta ni coste conocidos)**
**Estado ahora: 🟢 HERRAMIENTAS IDENTIFICADAS CON PLAN GRATUITO — falta producir uno**

`ESTILO_HUMAN_CHRONICLES.md` §3.3 lo llama el plano estrella del nicho y no se sabía con qué se
hacía. Ahora sí, y sale gratis para empezar.

---

## 1. Por qué importa más de lo que parecía

El hueco #10 encontró que **Kings and Generals** construyó su audiencia precisamente sobre mapas
de batalla animados y superposiciones estratégicas. El mapa animado no es un adorno del nicho:
es el elemento que la referencia del sector usa como columna vertebral. Y encaja con dos reglas
ya escritas del canal:

- **Regla de los 4 segundos** (`ERRORES_A_EVITAR.md` #14): un mapa animado es movimiento real
  sostenido — resuelve exactamente el problema del frame congelado que hizo rechazar un video.
- **Ancla de marca faceless**: un estilo de mapa consistente es tan reconocible como un personaje,
  y no exige consistencia facial.

## 2. Las opciones, todas con plan gratuito

| Herramienta | Plan gratis | Fuerte en | Nota |
|---|---|---|---|
| **Animaps** | 12 créditos/mes, sin tarjeta | 30 tipos de animación, base de +67.000 localizaciones, soporta datos históricos; exporta MP4/GIF | La más completa para historia. **Primera a probar** |
| **Mapimator** | sí | Rutas, viajes, regiones; export MP4/GIF/**4K** | Señalada específicamente para mapas de batalla |
| **Google Earth Studio** | gratuito | Sobrevuelos sobre imagen satelital 3D | Geografía real, no cartografía histórica. Complemento, no base |
| After Effects + GeoLayers | de pago | Control total | Solo si algún día hace falta. No ahora |

Ambas de arriba corren en navegador, sin instalar nada y sin conocimientos de motion graphics.

## 3. Plan de prueba (coste 0, no toca el bloqueo de créditos de Recraft)

12 créditos/mes de Animaps dan de sobra para el video 1. La prueba:

1. Un solo mapa del bloque de **contexto** (0:45-2:00 de la estructura de `ESTILO_HUMAN_CHRONICLES.md` §5).
2. Exportar a MP4 y **medirlo con `ffprobe`** — resolución, duración real y fps.
   Obligatorio por `ERRORES_A_EVITAR.md` #15: se planifica sobre el dato medido, nunca sobre lo
   que promete la herramienta. Ya hubo un storyboard entero en riesgo por saltarse esto.
3. Verificar **1080p mínimo y 16:9 exacto** antes de meterlo en el montaje
   (`ERRORES_A_EVITAR.md` #10 y regla global de calidad).
4. Fijar el estilo de mapa (paleta, grosor de línea, tipografía de etiquetas) y anotarlo en
   `ESTILO_HUMAN_CHRONICLES.md` §3.3 como parte del canon del canal.

**Lo que hay que verificar en los términos antes de publicar nada:** que el plan gratuito permita
**uso comercial** del MP4 exportado. Es la misma trampa de licencia del hueco #1 y del hueco de
imagen: gratis no siempre significa comercialmente usable. Verificar en la web de cada herramienta,
no asumir.

## Fuentes

- [Animaps — AI Map Animation Generator](https://animaps.ai/)
- [Animate Your Map — Free AI Map Animation Maker — Animaps](https://animaps.ai/map-animation-maker)
- [Mapimator — Online Map Animation Tool](https://mapimator.com/)
- [How to Make Animated Maps for YouTube Videos — Moshion](https://moshion.app/resources/how-to-make-animated-maps-for-youtube)
- [How History Animators Make Their Maps — YouTube](https://www.youtube.com/watch?v=a0RfM0lOnew)
