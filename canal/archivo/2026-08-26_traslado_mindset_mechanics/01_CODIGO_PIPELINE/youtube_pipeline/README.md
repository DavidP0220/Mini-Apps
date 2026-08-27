# YouTube Pipeline

Esqueleto de automatización para producir videos para varios canales de
YouTube en paralelo. Cada canal es independiente: credenciales, carpeta de
salida y voz propias, para que si una cuenta tiene un problema no afecte a
las demás.

## Etapas

1. **research** (`pipeline/stages/research.py`) — analiza canales de
   referencia con la YouTube Data API: qué títulos, duraciones y horarios de
   publicación funcionan mejor. Requiere `YOUTUBE_API_KEY`.
2. **script_writer** (`pipeline/stages/script_writer.py`) — genera título,
   hook, guion, cierre-gancho y SEO a partir de un tema (y de los patrones
   detectados en la etapa 1). El tono es intenso y directo (nada de guiones
   planos), y el guion siempre termina con un `CIERRE_GANCHO`: un teaser de
   intriga hacia el siguiente video de la serie, para maximizar
   suscripción y retorno del espectador. El dramatismo va en el tono, no en
   inventar datos o prometer en el título algo que el video no cumple —
   YouTube penaliza el desajuste título/miniatura vs. contenido, y eso
   perjudicaría la meta de monetización. **Todos los videos del canal tienen
   un tope de 18 minutos** (`MAX_VIDEO_MINUTES` en `script_writer.py`): el
   guion se limita a ~2610 palabras (a 145 palabras/min de narración) y, si
   el tema da para más, se prioriza lo más fuerte y se deja el resto para el
   siguiente video (conectado por el `CIERRE_GANCHO`). Requiere
   `ANTHROPIC_API_KEY`.
3. **voice** (`pipeline/stages/voice.py`) — convierte el guion en audio con
   ElevenLabs. Requiere `ELEVENLABS_API_KEY` con suscripción activa.
4. **visuals** (`pipeline/stages/visuals.py`) — la miniatura siempre se
   genera con fondo degradado + texto (sin key, principio "simple gana").
   Las escenas del video intentan generarse como b-roll con IA
   (`generate_ai_scene_image`, requiere `GEMINI_API_KEY`); si esa etapa
   falla o no hay clave, cae de vuelta al mismo fondo degradado simple, así
   el pipeline nunca se rompe por esta clave.
5. **assembly** (`pipeline/stages/assembly.py`) — **funciona hoy sin
   ninguna key**: anima cada escena con una de 4 variantes de Ken Burns
   (zoom-in, zoom-out, paneo izq/der), las une con transición de crossfade,
   superpone subtítulos palabra por palabra sincronizados con la narración
   (si la etapa de voz devolvió `word_timings`), y las sincroniza con el
   audio. Exporta un .mp4 con moviepy (ffmpeg incluido vía
   `imageio-ffmpeg`, no hace falta instalarlo aparte).
6. **publish** (`pipeline/stages/publish.py`) — sube el video final a
   YouTube. Cada canal usa su propio token OAuth
   (`ChannelConfig.oauth_token_path`), completamente aislado de los demás.

`pipeline/orchestrator.py` conecta las 6 etapas: si a alguna le falta su API
key, no rompe el proceso — lo reporta como "pendiente de configurar" y sigue
con lo que sí puede ejecutar.

## Uso

```bash
pip install -r requirements.txt
```

### Probar que el ensamblado de video funciona (no necesita ninguna key)

```bash
python main.py demo
```

Genera 3 escenas, una miniatura y un video con zoom animado en
`output/demo/demo_video.mp4`.

### Correr el pipeline completo para un canal

1. Copia `config/channels.example.yaml` a `config/channels.yaml` y
   describe tus canales.
2. Copia `.env.example` a `.env` y rellena las claves que ya tengas
   (puedes dejar algunas vacías, esas etapas se saltan con instrucciones).
3. Ejecuta:

```bash
python main.py run --channel canal_ejemplo_1 --topic "3 curiosidades del imperio romano" --reference-channels UCxxxxxxx
```

## Próximos pasos sugeridos

- Conseguir `YOUTUBE_API_KEY` y `ANTHROPIC_API_KEY` para activar
  investigación de tendencias y generación automática de guion/título/SEO.
- Revisar la suscripción de ElevenLabs (https://elevenlabs.io/app/subscription)
  para activar la voz en off real.
- Cuando quieras miniaturas/escenas con imágenes generadas por IA en vez de
  fondos de degradado, extender `pipeline/stages/visuals.py`.
- Para publicar automáticamente, completar el flujo OAuth una vez por canal
  (se guarda el token y no hay que repetirlo).
