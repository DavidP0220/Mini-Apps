"""Etapa 1: Investigación de canales de referencia.

Busca qué títulos, duraciones y horarios de publicación están funcionando
en canales de un nicho dado, usando la YouTube Data API v3.

Requiere: YOUTUBE_API_KEY en el archivo .env
Consíguela en: https://console.cloud.google.com/apis/credentials
(habilita "YouTube Data API v3" en el proyecto)
"""
import os
from datetime import datetime

from ..models import TrendInsight

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")


def research_channel(channel_ref: str, max_videos: int = 10) -> list[TrendInsight]:
    """Trae los videos más recientes/populares de un canal de referencia
    y extrae patrones de título, duración y horario de publicación.

    `channel_ref` acepta tanto el ID interno (empieza con "UC...") como el
    @handle público del canal (ej. "@TomTalksMoney2k" o "TomTalksMoney2k"),
    que es como normalmente lo vas a identificar.
    """
    if not YOUTUBE_API_KEY:
        raise RuntimeError(
            "Falta YOUTUBE_API_KEY en .env. "
            "Sin esta clave no se puede consultar la YouTube Data API. "
            "Ver instrucciones en el README, sección 'Etapa 1'."
        )

    from googleapiclient.discovery import build

    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

    channel_id, uploads_playlist = _resolve_channel(youtube, channel_ref)
    video_ids = _get_recent_video_ids(youtube, uploads_playlist, max_videos)
    return _get_video_insights(youtube, channel_id, video_ids)


def _resolve_channel(youtube, channel_ref: str) -> tuple[str, str]:
    if channel_ref.startswith("UC"):
        resp = youtube.channels().list(part="contentDetails", id=channel_ref).execute()
    else:
        handle = channel_ref if channel_ref.startswith("@") else f"@{channel_ref}"
        resp = youtube.channels().list(part="contentDetails", forHandle=handle).execute()

    items = resp.get("items", [])
    if not items:
        raise ValueError(f"Canal no encontrado: {channel_ref}")
    channel_id = items[0]["id"]
    uploads_playlist = items[0]["contentDetails"]["relatedPlaylists"]["uploads"]
    return channel_id, uploads_playlist


def _get_recent_video_ids(youtube, playlist_id: str, max_videos: int) -> list[str]:
    resp = youtube.playlistItems().list(
        part="contentDetails",
        playlistId=playlist_id,
        maxResults=max_videos,
    ).execute()
    return [item["contentDetails"]["videoId"] for item in resp.get("items", [])]


def _get_video_insights(youtube, channel_id: str, video_ids: list[str]) -> list[TrendInsight]:
    if not video_ids:
        return []
    resp = youtube.videos().list(
        part="snippet,statistics,contentDetails", id=",".join(video_ids)
    ).execute()

    insights = []
    for item in resp.get("items", []):
        snippet = item["snippet"]
        stats = item["statistics"]
        published = datetime.fromisoformat(snippet["publishedAt"].replace("Z", "+00:00"))
        insights.append(
            TrendInsight(
                reference_channel=channel_id,
                video_title=snippet["title"],
                views=int(stats.get("viewCount", 0)),
                duration_seconds=_parse_iso8601_duration(item["contentDetails"]["duration"]),
                published_hour_utc=published.hour,
            )
        )
    return sorted(insights, key=lambda i: i.views, reverse=True)


def _parse_iso8601_duration(duration: str) -> int:
    """Convierte 'PT4M32S' -> 272 segundos, sin dependencias externas."""
    import re

    match = re.match(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", duration)
    if not match:
        return 0
    h, m, s = (int(x) if x else 0 for x in match.groups())
    return h * 3600 + m * 60 + s
