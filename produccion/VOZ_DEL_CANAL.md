# La voz del canal — decision permanente

Una sola voz para todos los videos, de aqui en adelante. Cambiar de voz entre
videos rompe la identidad del canal: el espectador que vuelve reconoce la voz
antes que la miniatura.

## Las 9 voces masculinas de en-US en Edge TTS

Lista viva del servicio, consultada el 2026-08-30. Las etiquetas son de
Microsoft, no mias.

| Voz | Categoria | Personalidad |
|---|---|---|
| **ChristopherNeural** | News, Novel | **Reliable, Authority** |
| GuyNeural | News, Novel | Passion |
| EricNeural | News, Novel | Rational |
| SteffanNeural | News, Novel | Rational |
| RogerNeural | News, Novel | Lively |
| AndrewNeural | Conversation | Warm, Confident, Authentic, Honest |
| BrianNeural | Conversation | Approachable, Casual, Sincere |
| AndrewMultilingualNeural | Conversation | igual que Andrew |
| BrianMultilingualNeural | Conversation | igual que Brian |

## El hallazgo

**Andrew, la que usamos en el video 5, es una voz de conversacion, no de
narracion.** Esta en la familia `Conversation, Copilot` — pensada para
asistentes. Por eso lee ligera y rapida: a 175 wpm, fuera del rango del nicho.

La familia correcta para psicologia evolutiva es **News, Novel**. Y dentro de
esa familia, la unica que Microsoft etiqueta como **Authority** es
**Christopher**.

## Los 3 finalistas

1. **ChristopherNeural** — la mas grave y con autoridad. Recomendada.
2. **GuyNeural** — News/Novel con `Passion`. Mas energia, menos peso.
3. **EricNeural** — News/Novel, `Rational`. Neutra y seria, mas plana.

## La prueba antes de decidir

**Nadie decide una voz leyendo una tabla.** Se generan las tres diciendo
exactamente el mismo texto — el hook del video 7, que es donde se gana o se
pierde la audiencia — y se escuchan seguidas.

Se juzga con tres preguntas, en este orden:

1. **¿Suena a documental o suena a asistente de telefono?**
2. **¿La voz sostiene una frase larga sin volverse monotona?**
3. **¿La escucharias 15 minutos seguidos?**

La tercera es la unica que importa de verdad. Es literalmente lo que decide el
tiempo de reproduccion.

## Comando de la prueba

```bash
TEXTO="Right before you speak in public, your body does something you never asked it to do. Your chest tightens. Your hands go cold. Something starts scanning the room, not for danger, for faces. You have felt it in a meeting. It shows up in children before they can explain it, and in people who have never failed at anything. Impostor syndrome. That is the name we gave it."

for V in ChristopherNeural GuyNeural EricNeural AndrewNeural; do
  edge-tts --voice en-US-$V --rate=-15% --text "$TEXTO" --write-media prueba_$V.mp3
  ffprobe -v error -show_entries format=duration -of csv=p=0 prueba_$V.mp3
done
```

Se incluye Andrew a proposito, para comparar contra lo que ya conocemos.
Las cuatro se generan con `--rate=-15%` para oirlas al ritmo del nicho.

## Decision — CERRADA

- **Voz del canal: `en-US-AndrewNeural`**
- **Decidida por David el 2026-08-30.** No se reabre.
- **Rate: `-15%` por defecto**, hasta que la medicion del nicho diga otro numero.

**Todos los videos, de aqui en adelante, con esta voz.** El espectador que
vuelve reconoce la voz antes que la miniatura.

### Lo que hay que vigilar con esta voz

Andrew pertenece a la familia `Conversation, Copilot`, no a `News, Novel`. En
la practica eso significa **una sola cosa que corregir siempre**: lee rapido.
En el video 5 salio a **175 wpm**, muy por encima del rango del nicho
(148-159).

**Regla fija: ningun audio de este canal se genera sin `--rate`.**

```bash
edge-tts --voice en-US-AndrewNeural --rate=-15% \
         --file NARRACION.txt --write-media VOZ.mp3
ffprobe -v error -show_entries format=duration -of csv=p=0 VOZ.mp3
```

Y despues de generar, **siempre** se mide:

```
palabras del guion / duracion en segundos x 60 = wpm real
```

Si el resultado sale fuera de 148-159, se ajusta el `--rate` y se vuelve a
generar. Es gratis y toma minutos. Publicar con la voz acelerada cuesta
retencion.
