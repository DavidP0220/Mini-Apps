# FACTORY SETTINGS — identidad del canal

**Cerrado el 2026-08-26.** Sustituye a `NOMBRE-Y-MARCA.md`, que proponía *Mental Mechanics* — una
variación del nombre viejo y por tanto descartada.

---

## 1. El nombre

```
Factory Settings
```
Handle: `@factorysettings` (alternativas si estuviera tomado: `@factorysettingsyt`, `@thefactorysettings`)

**Por qué.** El nombre no sale del nicho, sale de la tesis: *estás corriendo la configuración de
fábrica de hace 200.000 años y nadie te mandó la actualización.* Los cuarenta canales del nicho se
llaman "X Psychology". Este no suena a ninguno, se entiende sin explicación y da una imagen de marca
obvia y potente.

## 2. Eslogan

```
Your brain shipped in 200,000 BC. Nobody sent the update.
```

## 3. Descripción del canal

```
Factory Settings explains the machinery behind the things you do every day and
quietly feel bad about.

Why you forget a name ten seconds after hearing it. Why silence makes you reach for
the radio. Why you apologize when someone else walks into you. Why you rehearse
conversations that will never happen.

None of it means something is wrong with you. Your brain shipped with settings
written for a world that stopped existing 200,000 years ago, and nobody ever sent
the update.

Every video takes one specific behavior, names the mechanism behind it, and traces
it back to where it came from - using real research, cited by researcher and decade.
No motivation. No life advice. Just the explanation nobody gave you.

New video every 4 days.

For education and information only. Not a substitute for professional psychological
or medical advice.
```

## 4. Palabras clave

```
psychology explained, human behavior, why we do what we do, psychology of people who,
evolutionary psychology, cognitive psychology, behavioral science, psychology facts,
hidden psychology, self understanding, factory settings, animated documentary
```

## 5. Ajustes que mueven el RPM

| Ajuste | Valor | Por qué |
|---|---|---|
| País | **Estados Unidos** | Multiplicador geográfico: 67% de diferencia medida |
| Categoría de cada video | **Educación** | $6,00 contra $4,50 de Lifestyle. Nunca Entretenimiento |
| Idioma | Inglés (EE.UU.) | — |
| Uso de IA | **Sí** | Obligatorio |
| Hecho para niños | **No** | Un canal "para niños" pierde comentarios y personalización |

## 6. Paleta

| Uso | Color |
|---|---|
| Fondo | `#02060E` azul casi negro |
| Acento / brillo | `#FF8A1F` ámbar incandescente |
| Texto principal | `#FFF3E0` crema |
| Luz de contorno | azul frío, contrapunto del ámbar |

Regla: **un solo punto caliente por imagen**, sobre fondo casi negro. Es lo que hace que el avatar se
lea a 32 px y que las miniaturas destaquen en un feed saturado.

## 7. Archivos

| Archivo | Medida | Dónde va |
|---|---|---|
| `marca/avatar.png` | 800 × 800 | Foto de perfil |
| `marca/banner.png` | 2560 × 1440 | Banner del canal |
| `marca/preview-tamanos.png` | — | Verificación a 32/48/88/160 px |
| `marca/logo-fuente-ia.png` | 1024 × 1024 | Arte del logo generado con IA — insumo del avatar |
| `marca/personaje.png` | — | Host canónico — insumo del banner |
| `marca/generar-avatar.py` | — | Regenera el avatar desde `logo-fuente-ia.png` |
| `marca/generar-marca.mjs` | — | Regenera el banner desde `personaje.png` |
| `marca/generar-preview.mjs` | — | Regenera la verificación de tamaños |

**Método.** El arte lo genera la IA; la geometría y la tipografía las monta el código. Los generadores
de imagen destrozan el texto y no encuadran para iconos pequeños, así que esas dos cosas se hacen
aparte y se pueden cambiar sin regenerar el arte.

**Avatar: un logo, no un rostro.** Los canales faceless se marcan con logo; los iconos de cara son para
creadores que salen en cámara. El avatar es una cabeza de perfil en crema sobre negro con **la luz
ámbar en la sien** — la misma firma que lleva el host en los videos (`FORMATO-DE-PRODUCCION.md` §2), de
modo que el icono y el personaje son la misma idea.

YouTube muestra la foto de perfil recortada **en círculo** y a **32 px** en comentarios y feeds. Ese
recorte, no el cuadrado, es el que decide: `marca/opciones/revision-circular.png` compara las variantes
bajo él. El reencuadre de `generar-avatar.py` existe para que el punto ámbar sobreviva a ese tamaño.
Historial completo de la decisión en `marca/opciones/OPCIONES-AVATAR.md`.

**Banner:** texto y símbolo dentro de la zona segura móvil (1546 × 423 centrada), lo único visible en
teléfono. Usa el rostro del host, que ahí sí funciona porque hay espacio. Incluye la promesa de
cadencia, que es de las pocas cosas que mueven la suscripción en la visita al canal.
