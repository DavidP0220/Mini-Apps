# Errores y lecciones — registro vivo

> Mantenido por el agente `higgsfield-product-architect` (con aportes de los otros dos agentes
> cuando encuentren algo relevante). Formato: síntoma → causa → fix → cómo evitarlo la próxima vez.
> Nunca se borra una entrada, aunque el error ya esté arreglado — es la memoria de qué NO volver a hacer.

## Heredado del pipeline de producción existente (aplica directo a este producto nuevo)

Fuente: `handoffs/REVISION_TECNICA_2026-08-25.md` — auditoría técnica real del pipeline
`video_express_ai/` + `recraft_ai/` que usa proveedores de IA muy similares a los que este producto
nuevo va a integrar. Estas lecciones son directamente aplicables al backend que se construya aquí:

### 1. Rutas relativas + `.gitignore` de lista blanca = pérdida silenciosa de datos
**Síntoma:** archivos generados (imágenes, videos, logs) nunca aparecían en git, sin ningún error visible.
**Causa:** `OUTPUT_DIR`/`LOG_DIR` definidos como rutas relativas al directorio de trabajo, no al
módulo; un `.gitignore` de lista blanca (`/*` + excepciones) ignoraba esas carpetas sin avisar.
**Fix:** anclar rutas por defecto a `Path(__file__).resolve().parent`, permitir que variables de
entorno absolutas tengan prioridad.
**Cómo evitarlo aquí:** cualquier ruta de almacenamiento en el backend nuevo (media, logs,
telemetría) debe ser absoluta o anclada al módulo desde el día uno — nunca relativa al cwd.

### 2. Rate limits (429) sin manejo = generación perdida o cobrada dos veces
**Síntoma:** un 429 de la API abortaba la generación sin más.
**Causa:** no había reintento ni backoff.
**Fix:** backoff exponencial honrando `Retry-After`; **solo reintentar 429**, nunca 5xx (un 5xx pudo
ejecutarse del lado del proveedor — reintentarlo cobra dos veces).
**Cómo evitarlo aquí:** todo cliente de API de IA que se integre a este producto (fal.ai, Runway,
Kling, ElevenLabs) necesita esta misma lógica desde el primer prototipo, no como mejora posterior —
es la diferencia entre un crédito perdido ocasional y un problema de facturación con usuarios reales.

### 3. Telemetría acoplada a llamadas de red opcionales
**Síntoma:** si una llamada secundaria (ej. consultar créditos restantes) fallaba, se perdía el
registro de una generación que sí se pagó y sí se ejecutó.
**Causa:** la telemetría dependía del éxito de esa llamada opcional en vez de degradar con gracia.
**Fix:** la llamada opcional degrada a `null`/`None` y el evento principal se registra igual.
**Cómo evitarlo aquí:** en un producto que cobra a usuarios reales por crédito, perder el registro
de un consumo pagado es un problema de negocio, no solo técnico — diseñar la telemetría para que
nunca dependa de una llamada que no sea la generación en sí misma.

### 4. Configuración clavada a una sola máquina
**Síntoma:** un script fallaba con `FileNotFoundError` opaco en cualquier equipo que no fuera el
original.
**Causa:** ruta absoluta de un ejecutable (`ffprobe`) hardcodeada.
**Fix:** `os.getenv(...) or shutil.which(...) or "default"`, con mensajes de error explícitos.
**Cómo evitarlo aquí:** si este producto se va a operar desde más de un equipo/entorno (dev local,
CI, producción en la nube), ninguna ruta de herramienta externa puede estar hardcodeada — es un
error que se paga caro justo cuando se intenta escalar de MVP a producción real.

## Errores propios de este proyecto (Higgsfield-alternativa)

### 1. La propia carpeta de este proyecto estuvo ignorada por git desde su creación
**Síntoma:** el 2026-08-26, al armar el paquete de conocimiento para entregar, `git status` y
`git log` no mostraban absolutamente nada de `PROYECTO HIGGSFIELD ALTERNATIVA/` — ni como
untracked, ni commiteado. Todo el trabajo de investigación de los 3 agentes (docs 01-07) llevaba
desde su creación el día anterior viviendo solo en disco local, sin ningún respaldo en git.
**Causa raíz:** el `.gitignore` de la raíz del repo es una **lista blanca** (`/*` + excepciones
explícitas, ver `handoffs/REVISION_TECNICA_2026-08-25.md` sección 1.1 para el mismo patrón de bug
encontrado el día anterior en `video_express_ai/`). Al crear la carpeta nueva nadie añadió la
excepción correspondiente — mismo síntoma exacto que ya se había documentado 24 horas antes en
otro módulo del proyecto, y aun así se repitió aquí.
**Fix:** añadidas las líneas `!/PROYECTO HIGGSFIELD ALTERNATIVA` y
`!/PROYECTO HIGGSFIELD ALTERNATIVA/**` al `.gitignore` de la raíz.
**Cómo evitarlo la próxima vez:** en este repo específico (lista blanca), **toda carpeta nueva de
primer nivel se verifica con `git check-ignore -v <carpeta>/<archivo>` inmediatamente después de
crearla**, antes de escribir ningún contenido dentro — no después, no "cuando se acuerde alguien".
Un `.gitignore` de lista blanca hace que el error por omisión sea la norma, no la excepción: cada
carpeta nueva nace ignorada hasta que se demuestra lo contrario.
