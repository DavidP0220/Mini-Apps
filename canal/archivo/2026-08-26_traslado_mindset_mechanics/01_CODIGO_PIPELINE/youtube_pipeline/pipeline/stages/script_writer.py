"""Etapa 2: Generación de título, hook, guion y SEO.

Toma un tema + los patrones detectados en la etapa de investigación
(TrendInsight) y genera un VideoBrief listo para grabar.

Requiere: ANTHROPIC_API_KEY en el archivo .env
Consíguela en: https://console.anthropic.com/settings/keys
"""
import os
import re

from ..models import TrendInsight, VideoBrief

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# Restricción del canal: ningún video dura menos de 8 ni más de 18 minutos.
MIN_VIDEO_MINUTES = 8
MAX_VIDEO_MINUTES = 18
_WORDS_PER_MINUTE_NARRATION = 145  # ritmo promedio de narración hablada
MIN_SCRIPT_WORDS = MIN_VIDEO_MINUTES * _WORDS_PER_MINUTE_NARRATION
MAX_SCRIPT_WORDS = MAX_VIDEO_MINUTES * _WORDS_PER_MINUTE_NARRATION

SYSTEM_PROMPT = f"""Eres un guionista experto en YouTube especializado en canales \
que buscan maximizar retención y suscripción recurrente. Recibes un tema y \
ejemplos de qué títulos y formatos están funcionando en el nicho (de canales \
de referencia que ya monetizan bien). Generas contenido simple de producir \
(evita animaciones complejas o efectos costosos) pero con tono intenso: \
directo, dramático, con ganchos fuertes — NADA de guiones planos o neutros. \
Usa un lenguaje que genere urgencia y curiosidad (titulares con carga \
emocional, preguntas retóricas, revelaciones progresivas), sin inventar \
datos falsos ni prometer en el título/hook algo que el guion no cumple — \
el desajuste entre título/miniatura y contenido real es penalizado por \
YouTube y perjudica la monetización, así que el dramatismo va en el TONO, \
no en mentir sobre el contenido.

El guion SIEMPRE debe cerrar con un CIERRE_GANCHO: una frase o mini-teaser \
que deje una pregunta abierta o intriga concreta conectada con el próximo \
video de la serie, para que el espectador quede esperando la continuación \
y sea más probable que se suscriba y vuelva a ver el canal.

RESTRICCIÓN DE DURACIÓN (obligatoria): el canal solo publica videos de \
entre {MIN_VIDEO_MINUTES} y {MAX_VIDEO_MINUTES} minutos. El GUION completo (sin \
contar CIERRE_GANCHO) debe tener entre {MIN_SCRIPT_WORDS} y {MAX_SCRIPT_WORDS} \
palabras, calculado a un ritmo de narración de {_WORDS_PER_MINUTE_NARRATION} \
palabras por minuto. Si el tema no da para llegar al mínimo, profundiza más en \
cada punto (ejemplos concretos, contexto, cifras, matices) en vez de entregar \
un guion corto. Si da para más del máximo, prioriza los puntos más fuertes y \
deja el resto para un próximo video (conéctalo con el CIERRE_GANCHO).

Responde SIEMPRE en este formato exacto, sin texto adicional:

TITULO: <título de máx 70 caracteres, con gancho fuerte y alto CTR>
HOOK: <primeras 2-3 frases del guion, deben generar curiosidad, tensión o urgencia inmediata>
GUION:
ESCENA 1: <título corto de la escena, máx 6 palabras>
<párrafos de narración de esta escena, tono intenso y directo>

ESCENA 2: <título corto de la escena, máx 6 palabras>
<párrafos de narración de esta escena>

(continúa así, "ESCENA N: <título corto>" seguido de sus párrafos, tantas
escenas como el tema necesite — cada escena se convierte en una imagen del
video, así que el título debe resumir de qué habla esa parte)
CIERRE_GANCHO: <frase final de intriga hacia el próximo video de la serie>
SEO_KEYWORDS: <palabra1, palabra2, palabra3, ...>
SEO_DESCRIPCION: <descripción de 2-3 líneas para el cuadro de descripción>
"""


def write_brief(topic: str, insights: list[TrendInsight] | None = None) -> VideoBrief:
    if not ANTHROPIC_API_KEY:
        raise RuntimeError(
            "Falta ANTHROPIC_API_KEY en .env. "
            "Sin esta clave no se puede generar el guion automáticamente. "
            "Ver instrucciones en el README, sección 'Etapa 2'."
        )

    import anthropic

    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

    context = _build_context(topic, insights)
    response = client.messages.create(
        model="claude-sonnet-5",
        max_tokens=8192,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": context}],
    )
    text = next(block.text for block in response.content if block.type == "text")
    brief = parse_brief(text)
    brief.topic = topic
    return brief


def _top_insights_per_channel(insights: list[TrendInsight], per_channel: int = 2) -> list[TrendInsight]:
    """Toma los `per_channel` videos con más vistas de CADA canal de
    referencia, en vez de los primeros N de la lista combinada — así, con
    varios canales de referencia, el prompt ve patrones de todos ellos y no
    solo del primero (que domina la lista si se investigó primero).
    """
    by_channel: dict[str, list[TrendInsight]] = {}
    for insight in insights:
        by_channel.setdefault(insight.reference_channel, []).append(insight)

    selected = []
    for channel_insights in by_channel.values():
        top = sorted(channel_insights, key=lambda i: i.views, reverse=True)[:per_channel]
        selected.extend(top)
    return selected


def _build_context(topic: str, insights: list[TrendInsight] | None) -> str:
    lines = [f"Tema del video: {topic}"]
    if insights:
        lines.append("\nEjemplos de títulos que están funcionando en el nicho:")
        for insight in _top_insights_per_channel(insights):
            lines.append(
                f"- \"{insight.video_title}\" ({insight.views} vistas, "
                f"{insight.duration_seconds}s, publicado a las {insight.published_hour_utc}h UTC)"
            )
    return "\n".join(lines)


_SCENE_RE = re.compile(r"^ESCENA\s+\d+:\s*(.+)$", re.MULTILINE)


def split_scenes(script: str) -> list[tuple[str, str]]:
    """Divide el GUION en (título_escena, texto_escena) usando los marcadores
    'ESCENA N: <título>' que el SYSTEM_PROMPT le exige al modelo. Cada par se
    usa en la etapa de ensamblado para generar una imagen por escena.
    """
    matches = list(_SCENE_RE.finditer(script))
    if not matches:
        return []

    scenes = []
    for i, match in enumerate(matches):
        title = match.group(1).strip()
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(script)
        body = script[start:end].strip()
        scenes.append((title, body))
    return scenes


def parse_brief(text: str) -> VideoBrief:
    """Convierte el texto TITULO:/HOOK:/GUION:/... (de la respuesta de la API
    o de un archivo de guion editado a mano) de vuelta en un VideoBrief.
    """
    sections = {
        "TEMA": "",
        "TITULO": "",
        "HOOK": "",
        "GUION": "",
        "CIERRE_GANCHO": "",
        "SEO_KEYWORDS": "",
        "SEO_DESCRIPCION": "",
    }
    current = None
    for line in text.splitlines():
        matched = False
        for key in sections:
            if line.strip().startswith(f"{key}:"):
                sections[key] = line.split(":", 1)[1].strip()
                current = key
                matched = True
                break
        if not matched and current:
            sections[current] += "\n" + line

    keywords = [k.strip() for k in sections["SEO_KEYWORDS"].split(",") if k.strip()]
    return VideoBrief(
        topic=sections["TEMA"].strip(),
        title=sections["TITULO"].strip(),
        hook=sections["HOOK"].strip(),
        script=sections["GUION"].strip(),
        closing_hook=sections["CIERRE_GANCHO"].strip(),
        seo_keywords=keywords,
        seo_description=sections["SEO_DESCRIPCION"].strip(),
    )


def format_brief(brief: VideoBrief) -> str:
    """Serializa un VideoBrief al mismo formato de texto que parse_brief lee,
    para guardarlo en un archivo que el usuario pueda editar a mano antes de
    seguir con voz/video (ver `orchestrator.write_script` / `render_from_script`).
    """
    keywords = ", ".join(brief.seo_keywords)
    return (
        f"TEMA: {brief.topic}\n"
        f"TITULO: {brief.title}\n"
        f"HOOK: {brief.hook}\n"
        f"GUION:\n{brief.script}\n\n"
        f"CIERRE_GANCHO: {brief.closing_hook}\n"
        f"SEO_KEYWORDS: {keywords}\n"
        f"SEO_DESCRIPCION: {brief.seo_description}\n"
    )
