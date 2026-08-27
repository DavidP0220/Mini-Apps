---
name: feedback-no-mezclar-canales-entre-proyectos
description: Nunca mezclar contenido/documentos de un canal de YouTube (proyecto) dentro del repo o carpeta de otro canal distinto — solo se comparten habilidades técnicas y aprendizajes de mejora entre ellos.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 941c322e-c3a7-48e6-8c32-b396c142026c
  modified: 2026-08-25T21:00:31.048Z
---

Nunca commitear ni mezclar documentos/contenido de un canal (ej. Human Chronicles) dentro del repositorio git o carpeta de proyecto de otro canal distinto (ej. Mindset Mechanics), aunque físicamente vivan en carpetas cercanas en el disco del usuario.

**Por qué:** el usuario corrigió esto explícitamente el 2026-08-25 después de que se commiteara `PROYECTO HUMAN CHRONICLES/` dentro del repo `mindset-mechanics` (a su vez, una sesión anterior ya había añadido ese mismo contenido a una lista blanca del `.gitignore` — el error se repitió una vez). Cada canal/proyecto tiene su propio repo/espacio; mezclarlos ensucia el historial y el contexto de cada uno.

**Cómo aplicarlo:** entre proyectos distintos (Mindset Mechanics, Human Chronicles, y cualquier otro canal futuro) lo único que se puede reutilizar o compartir es:
- Habilidades técnicas (ej. patrones de código robustos, fixes de bugs genéricos, buenas prácticas de automatización).
- Información de mejoras generales (ej. hallazgos de investigación sobre el algoritmo, YPP, buenas prácticas de miniaturas/títulos que apliquen en general).

Nunca compartir: documentos de estrategia, guiones, biblias de estilo, datos de cuenta, o cualquier archivo de contenido propio de un canal dentro del repo/carpeta de otro. Si se encuentra contenido de un canal viviendo dentro del repo de otro, sacarlo (destrackear, no necesariamente borrar del disco) y avisar.

Ver también: [[project_human_chronicles_canal]], [[project_mindset_mechanics_scope]].
