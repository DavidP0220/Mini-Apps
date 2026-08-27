# HANDOFF — Integración: deadline YPP feb-2027 + rescate de material local
**De: Kimi Code → Claude Code y David · Fecha: 2026-08-25**
**Integra: INVESTIGACION_DIARIA_2026-08-25.md + REVISION_TECNICA_2026-08-25.md. Ambos documentos: EXCELENTE nivel, quedan adoptados como insumo oficial.**

---

## 1. 🚨 ESTRATÉGICO: YouTube duplica requisitos YPP el 1-feb-2027

Hallazgo de la investigación diaria: para canales fuera del programa, las horas pasan de 4.000 a **8.000** (Shorts: 10M→20M). Los 1.000 subs no cambian.

**Mi posición oficial:**
1. **VERIFICAR ANTES DE ACTUAR** (el propio investigador lo pide, y tiene razón): David o Claude abren YouTube Studio → Monetización y confirman el aviso oficial. Regla del proyecto: nada se comunica ni se planifica sobre fuente no verificada.
2. **Si se confirma:** la fecha límite estratégica del canal pasa a ser **31 de enero de 2027**. La matemática no cambia (los 1.000 subs siguen siendo el cuello de botella — playbook §7), pero las 4.000h dejan de ser el objetivo fácil: hay que entrar al YPP ANTES de la duplicación. Esto REFUERZA la cadencia de 1 largo cada 4-5 días y la prioridad absoluta de largos sobre Shorts. No hay que cambiar estrategia — hay que ejecutarla más rápido.
3. Queda registrado en mi ronda diaria: verificación de este dato es prioridad esta semana.

## 2. 🔴 TÉCNICO URGENTE: rescate de material local (60 días de margen)

La revisión técnica encontró que outputs/logs generados desde la raíz del proyecto caían en carpetas no trackeadas por git (fallo YA corregido en código). **Acción requerida:**

```
Busca en la raíz del proyecto local de David carpetas outputs/ y/o logs/ sueltas
(fuera de video_express_ai/ y recraft_ai/). Si existen y tienen material generado
(imágenes, videos, logs JSONL): muévelas a su módulo correspondiente o súbelas al
repo (respetando .gitignore para mp4/mp3 pesados — esos respáldalos en Drive local).
Recraft y VideoExpress borran originales a los 60 días: esto es rescate, no limpieza.
Reporta qué encontraste en el próximo REPORTE.
```

## 3. Adopciones de la investigación diaria (entran en vigor)

1. **Test & Compare (A/B nativo de YouTube):** se adopta. A partir del próximo video publicado, preparar 2-3 variantes de título (de las fórmulas del playbook §1) y 2 miniaturas por video. Responsable de las variantes de título: Kimi (las entrego en el handoff de publicación de cada video).
2. **Números en miniaturas:** se añade a la biblia de miniaturas — probar "3 SEÑALES"/estilo con número como variante B en Test & Compare.
3. **Quality CTR:** confirma la regla existente — prohibido clickbait que el contenido no pague. Ya estaba en el playbook; ahora además sabemos que el algoritmo lo castiga activamente. Se mantiene.

## 4. Reconocimiento formal

Las rutinas diarias de Claude (investigación + revisión técnica) están produciendo exactamente el estándar que pide el proyecto: hallazgos con fuentes, fiabilidad explícita, fixes verificados, y escalación de decisiones que no les corresponden. **Mantener esa rutina diaria.** La mía (8 AM) revisará siempre sus reportes del día anterior.

---

## Prompt de activación para Claude Code

```
git pull. Nuevo: handoffs/HANDOFF_2026-08-25_integracion_investigacion_ypp_y_backup.md.
Acciones: (1) rescate de outputs/logs sueltos en raíz local — urgente, ventana 60 días; (2) pídele a David verificar en YouTube Studio → Monetización el aviso de cambio de requisitos YPP feb-2027 y reporta lo que diga; (3) registra Test & Compare como paso del checklist de publicación. El piloto de Resiliencia sigue igual: esperando ejecución del mapeo (HANDOFF_2026-08-25_mapeo_piloto_stills.md) y gate de David.
```
