# Decisión de avatar — cerrada

**Abierta el 2026-08-26, cerrada el 2026-08-27.**

El bloqueo que dejó esta decisión abierta era del entorno: el proxy no dejaba descargar
`res.cloudinary.com`, así que las tres opciones se generaron pero nunca se pudieron mirar. Con la red
abierta se descargaron, se probaron y se decidió.

## El hallazgo que motivó la revisión

Investigación de branding de canal:

> *"Los iconos de cara son mejores para creadores que salen en cámara. **Los logos son mejores para
> marcas, canales faceless y agencias.**"*

Factory Settings es faceless y el avatar era el rostro del host. El error de razonamiento:
`PLAYBOOK_MONETIZACION.md` §5 dice que el host visible es el activo diferencial, pero **eso aplica a
miniaturas, no a la foto de perfil**. Se confundieron las dos cosas. El hallazgo era correcto.

## Resultado: gana el concepto de C, no la ejecución de C

`revision-circular.png` — las cinco variantes bajo el recorte que YouTube aplica de verdad: **círculo**,
sobre el gris del feed, a 32 / 48 / 88 px.

| Opción | Qué es | Veredicto |
|---|---|---|
| Rostro anterior | El avatar que estaba puesto | Marrón sobre oscuro, poco contraste. La luz de la sien queda en el borde y el círculo la recorta |
| **A** | Rostro del host, alto contraste | Legible, pero es una cara — el hallazgo dice logo. La mitad naranja se come la luz de la sien: se pierde la regla de un solo punto caliente |
| **B** | Logo, símbolo de encendido | El más legible de los tres, pero fondo blanco: prohibido por la biblia visual, y el símbolo de encendido es genérico y copiable |
| **C** | Logo, luz en la sien | **Concepto correcto, ejecución fallida.** El punto ámbar —la firma de la marca— es lo que peor sobrevive a 32 px: pequeño, en la coronilla y no en la sien, y un marco interior desperdicia el 15% del lienzo |
| **D → avatar final** | C regenerado y reencuadrado | Elegido |

La recomendación registrada el 26-ago era C, pero **no la sostenía el propio test que ese documento
define como decisivo**. C falla justo en el elemento que le da sentido. El concepto sí era el bueno.

## Lo que se hizo

1. **Regenerar** (Recraft V3, 4 créditos): fondo negro de marca a sangre y sin marco, cabeza de perfil
   en crema llenando el lienzo, punto ámbar grande con halo cálido. Resultado: `../logo-fuente-ia.png`.
2. **Reencuadrar con código** — `../generar-avatar.py`. El arte lo hace la IA, la geometría el código,
   que es el método que ya usa la marca para la tipografía. Normaliza el fondo a `#02060E` y recorta al
   cráneo: el punto ámbar pasa de **1,26% a 1,70% del lienzo** sin recortar el perfil.

`revision-DFE.png` documenta el reencuadre. Se probaron tres: el original (punto pequeño, mucho aire),
el intermedio (elegido) y uno cerrado que agrandaba más el punto pero cortaba el perfil y dejaba de
leerse como una cabeza.

Verificación final a los cuatro tamaños reales: `../preview-tamanos.png`.

## Salvedad registrada

El punto ámbar quedó en la **frente alta**, no estrictamente en la sien (que es a la altura del ojo,
delante de la oreja). Recraft no acertó la posición en la primera pasada. Se aceptó igual porque a
32 px la posición exacta no se distingue y lo que decide es que haya un solo punto caliente dentro del
cráneo, que sí se cumple.

Si se quiere perseguir la posición exacta quedan 29 generaciones. No es un bloqueo: el avatar actual
es publicable.

## Archivos de esta carpeta

Solo quedan como registro de la decisión, a 512 px. El avatar en uso es `../avatar.png`.

| Archivo | Qué es |
|---|---|
| `fs_avatar_A.png` `fs_avatar_B.png` `fs_avatar_C.png` | Las tres opciones descartadas |
| `avatar-rostro-anterior.png` | El avatar de rostro que estaba puesto antes |
| `revision-circular.png` | El test que decidió: recorte circular a 32/48/88 px |
| `revision-DFE.png` | Comparación de los tres reencuadres |

## Presupuesto

| Proveedor | Estado |
|---|---|
| Cloudinary | **29 generaciones restantes** de 50 (se gastaron 4 en la regeneración) |
| vidIQ | 17 créditos — insuficiente, cada generación cuesta 22. Recarga el 18 de septiembre |
