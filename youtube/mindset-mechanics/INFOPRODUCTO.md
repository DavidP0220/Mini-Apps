# Infoproducto en inglés — Factory Settings, manual de campo

**Montado el 2026-08-27.** Vive en `apps/factory-settings-manual/` de este mismo repositorio.

---

## 1. Por qué existe

Los dos documentos de estrategia coinciden sin haberse coordinado:

- `ALCANCES-DEL-PAQUETE.md` §5.3 y §7.4: *"La única vía de ingreso real dentro de la ventana de 30
  días sigue siendo el infoproducto en inglés."*
- `PLAN-MES-01.md` §8: los 8 videos del mes **no** monetizan el canal. Faltan 989 suscriptores
  ≈ 36.000 vistas de largos.
- `PLAYBOOK_MARCA_INTERACCION_VENTAS.md` §4.2 propone exactamente esto: *"un mini-ebook o PDF tipo
  'Guía de bolsillo: por qué tu cerebro hace esto' que empaquete 8-10 de los mecanismos evolutivos ya
  cubiertos en los videos — contenido que YA existe en los guiones, solo hay que compilarlo."*

No depende de ningún umbral: ni de los 1.000 suscriptores ni de las 4.000 horas del YPP. Y es lo único
del proyecto que se puede terminar entero dentro de este repositorio.

## 2. Qué es

Una mini-app PWA instalable, no un PDF. Mismo motor que el resto del repositorio: el contenido es un
solo `content.json`, así que corregir una frase no obliga a regenerar nada.

| | |
|---|---|
| Título | **Factory Settings** |
| Subtítulo | *The field manual for a brain that shipped in 200,000 BC* |
| Capítulos | 10 — introducción, los 8 mecanismos, y el cierre |
| Secciones | 51 |
| Idioma | Inglés (el canal es US/inglés; el resto del repositorio sigue en castellano) |
| Tema | Oscuro por defecto, acento ámbar `#FF8A1F` — la paleta de la marca |
| Iconos | Generados desde `marca/avatar.png` |

Cada capítulo de mecanismo tiene la misma estructura: qué haces, qué está corriendo por debajo, una
tabla de investigación con **investigador y década**, el replanteo citable, y un quiz.

## 3. Los 8 capítulos son los 8 videos

| Capítulo | Video del plan |
|---|---|
| The blank under pressure | #1 · 29 ago |
| The reach for noise | #2 · 2 sep |
| The phone you turn back over | #3 · 6 sep |
| The arithmetic you did not agree to do | #4 · 10 sep |
| The forty-minute task | #5 · 14 sep |
| The empty room | #6 · 18 sep |
| The argument in the shower | #7 · 22 sep |
| Sorry when it was not you | #8 · 25 sep |

Esto no es casualidad, es la palanca: cada video que se publica es el anuncio natural del capítulo
que le corresponde, y el manual da algo que entregar antes de tener nada que vender.

El capítulo de cierre añade lo que ningún video suelto puede dar: **los ocho son la misma forma**, un
sistema sesgado por una asimetría de coste entre dos errores posibles. Esa tabla es la razón de comprar
el manual entero en vez de ver los videos por separado.

## 4. Cómo publicarlo

El repositorio ya lo explica en `README.md` §"Publicar gratis en GitHub Pages". Una vez activado
Pages (Settings → Pages), la app queda en:

```
https://davidp0220.github.io/Mini-Apps/apps/factory-settings-manual/
```

Dónde va el link, según `PLAYBOOK_MARCA_INTERACCION_VENTAS.md` §4.2:

1. Primera línea de la descripción de **cada** video.
2. Sección "Acerca de" del canal.
3. Comentario fijado, cuando el video empiece a moverse.

## 5. Lo que falta decidir

| # | Asunto |
|---|---|
| 1 | **Precio y pasarela.** Ahora mismo es una URL abierta. Sirve como imán de correos o como producto de pago; esa decisión no es técnica y no la he tomado |
| 2 | **Captura de correos.** No la lleva. Es la diferencia entre un regalo y una lista, y el motor no tiene formularios |
| 3 | Activar GitHub Pages en Settings — es un clic manual, no se puede hacer desde aquí |

## 6. Una corrección de fuente

`PLAN-MES-01.md` §5 atribuye al video #7 la *"teoría del rango social de la ansiedad (Leary &
Kowalski)"*. Esas dos cosas no van juntas: la teoría del rango social es de **Gilbert**, mientras que
Leary & Kowalski (1990) son los de la **teoría de la autopresentación** de la ansiedad social.

En el manual he puesto la atribución correcta —autopresentación, Leary & Kowalski, 1990— porque la
promesa del canal es investigación real citada por investigador y década, y una cita cruzada es
justo el tipo de error que un espectador del nicho detecta. **Conviene arreglarlo también en el guion
del video #7 antes de grabarlo.**
