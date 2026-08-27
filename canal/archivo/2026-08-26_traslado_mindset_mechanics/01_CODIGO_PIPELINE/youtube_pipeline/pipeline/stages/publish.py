"""Etapa 5: Publicación en YouTube.

IMPORTANTE — aislamiento entre canales:
Cada canal tiene su PROPIO archivo de token OAuth (ChannelConfig.oauth_token_path,
normalmente en channels/<nombre_canal>/token.json). Nunca se comparte un token
entre canales. Así, si una cuenta es suspendida o baneada, las credenciales y el
historial de subidas de las demás cuentas no se ven afectados: son procesos
completamente independientes.

Requiere por canal: un client_secret.json de Google Cloud Console con el scope
"https://www.googleapis.com/auth/youtube.upload" habilitado, y completar el
flujo OAuth una vez (se guarda el token en oauth_token_path para no repetirlo).
Guía: https://developers.google.com/youtube/v3/guides/uploading_a_video
"""
from pathlib import Path

from ..models import ChannelConfig, PublishResult

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]


def publish_video(
    channel: ChannelConfig,
    video_path: Path,
    title: str,
    description: str,
    tags: list[str],
    client_secret_path: Path,
    privacy_status: str = "private",
) -> PublishResult:
    if channel.oauth_token_path is None:
        raise RuntimeError(
            f"El canal '{channel.name}' no tiene oauth_token_path configurado. "
            "Cada canal necesita su propio archivo de token, aislado de los demás "
            "(ver config/channels.example.yaml)."
        )
    if not client_secret_path.exists():
        raise RuntimeError(
            f"No se encontró {client_secret_path}. Descárgalo desde Google Cloud "
            "Console (credenciales OAuth de escritorio) para el proyecto de este canal."
        )

    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaFileUpload

    creds = _load_or_create_credentials(channel.oauth_token_path, client_secret_path)
    youtube = build("youtube", "v3", credentials=creds)

    body = {
        "snippet": {"title": title, "description": description, "tags": tags},
        "status": {"privacyStatus": privacy_status},
    }
    media = MediaFileUpload(str(video_path), chunksize=-1, resumable=True)

    request = youtube.videos().insert(part="snippet,status", body=body, media_body=media)
    response = None
    while response is None:
        _, response = request.next_chunk()

    video_id = response["id"]
    return PublishResult(
        channel_name=channel.name,
        video_id=video_id,
        url=f"https://youtu.be/{video_id}",
        status=privacy_status,
    )


def _load_or_create_credentials(token_path: Path, client_secret_path: Path):
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow

    creds = None
    if token_path.exists():
        creds = Credentials.from_authorized_user_file(str(token_path), SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(str(client_secret_path), SCOPES)
            creds = flow.run_local_server(port=0)
        token_path.parent.mkdir(parents=True, exist_ok=True)
        token_path.write_text(creds.to_json())

    return creds
