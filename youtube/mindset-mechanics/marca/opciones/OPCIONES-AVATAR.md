# Opciones de avatar — pendientes de decisión

**Generadas el 2026-08-26** con Cloudinary (Recraft V3 y Nano Banana 2).

> **Limitación del entorno:** el proxy de esta sesión bloquea `res.cloudinary.com`, así que las
> imágenes se generan pero no se pueden descargar ni revisar desde aquí. Las URLs de abajo hay que
> abrirlas manualmente. Por eso esta carpeta no contiene los archivos.

## El hallazgo que motiva esta revisión

Investigación de branding de canal:

> *"Los iconos de cara son mejores para creadores que salen en cámara. **Los logos son mejores para
> marcas, canales faceless y agencias.**"*

Factory Settings es faceless, y el avatar actual (`../avatar.png`) es el rostro del host. Contradice
la recomendación. El error de razonamiento: `PLAYBOOK_MONETIZACION.md` §5 dice que el host visible es
el activo diferencial, pero **eso aplica a miniaturas, no a la foto de perfil**. Se confundieron las
dos cosas.

## Las tres direcciones

| Opción | Concepto | URL |
|---|---|---|
| **A** | Rostro del host, versión de alto contraste | https://res.cloudinary.com/d9dmhela/image/upload/v1787791770/fs_avatar_A_rostro.png |
| **B** | Logo: cabeza de perfil con símbolo de encendido dentro | https://res.cloudinary.com/d9dmhela/image/upload/v1787791796/fs_avatar_B_logo.webp |
| **C** | Logo: silueta de cabeza con luz ámbar en la sien | https://res.cloudinary.com/d9dmhela/image/upload/v1787791819/fs_avatar_C_sien.webp |

## Recomendación: C

Razón de marca, no de gusto. La luz en la sien es la firma del host en los videos
(`FORMATO-DE-PRODUCCION.md` §2). Si el logo **es** esa misma luz, el avatar y el personaje son la
misma idea: el espectador reconoce el canal por el icono antes de leer el nombre.

- **B** usa un símbolo de encendido genérico, copiable por cualquiera.
- **A** tiene detalle que se pierde a 32 px, el tamaño al que YouTube muestra la foto de perfil en
  comentarios y feeds.

## Cómo evaluarlas

Abrir cada URL y **reducir la ventana hasta que la imagen se vea como un icono de comentario**. La que
siga siendo reconocible a ese tamaño gana. Es el único test que importa.

## Presupuesto de generación

| Proveedor | Estado |
|---|---|
| Cloudinary | **33 generaciones restantes** (Recraft 4 por imagen, Nano Banana premium 9) |
| vidIQ | 17 créditos — insuficiente, cada generación cuesta 22. Recarga el 18 de septiembre |

**Desbloqueo pendiente:** una API key de FLUX.2 o gpt-image eliminaría la dependencia del CDN
bloqueado y permitiría generar, revisar y montar las variantes en el banner dentro de la misma sesión.
