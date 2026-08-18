---
description: Muestra el gasto de tokens de la sesión y los conectores cargados
allowed-tools: Bash(node tools/token-report.mjs:*), Bash(node tools/contar-herramientas.mjs:*)
---

Consumo de tokens:

!`node tools/token-report.mjs`

Herramientas y conectores cargados:

!`node tools/contar-herramientas.mjs`

Resume en pocas líneas: cuánto se lleva gastado, si el reuso de caché está por
debajo del 70%, y si hay conectores MCP cargados que no se estén usando en este
proyecto. Da una recomendación concreta, sin repetir las tablas completas.
