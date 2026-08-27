"""CLI del pipeline de automatización de canales de YouTube.

Comandos:
  python main.py demo                          Corre un ensamblado real de
                                                 principio a fin con assets
                                                 generados localmente (no
                                                 necesita ninguna API key).
  python main.py run --channel NOMBRE --topic "..."
                                                 Corre el pipeline completo
                                                 para un canal definido en
                                                 config/channels.yaml.
"""
import argparse
import sys
import wave
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

from pipeline.models import ChannelConfig, VisualAsset
from pipeline.stages import assembly, visuals

ROOT = Path(__file__).parent


def cmd_demo(_args):
    demo_dir = ROOT / "output" / "demo"
    demo_dir.mkdir(parents=True, exist_ok=True)

    print("1/4 Generando escenas de ejemplo (sin API keys)...")
    scenes_specs = [
        ("Bienvenidos al canal", (20, 24, 40), (60, 30, 90), 4.0),
        ("Hoy hablamos de automatización", (30, 20, 60), (80, 40, 20), 4.0),
        ("Suscríbete para más contenido", (40, 20, 20), (90, 70, 20), 4.0),
    ]
    scenes: list[VisualAsset] = []
    for i, (text, top, bottom, duration) in enumerate(scenes_specs):
        asset = visuals.make_scene_image(
            text, demo_dir / f"scene_{i}.png", top, bottom, duration
        )
        scenes.append(asset)
    print(f"    -> {len(scenes)} escenas creadas en {demo_dir}")

    print("2/4 Generando miniatura...")
    thumbnail = visuals.make_thumbnail(
        "Automatiza tu canal de YouTube", demo_dir / "thumbnail.png"
    )
    print(f"    -> {thumbnail.image_path}")

    print("3/4 Generando pista de audio silenciosa de ejemplo (placeholder de voz)...")
    total_duration = sum(s.duration_seconds for s in scenes)
    audio_path = demo_dir / "voiceover_placeholder.wav"
    _write_silence(audio_path, total_duration)
    print(f"    -> {audio_path} ({total_duration:.1f}s)")

    print("4/4 Ensamblando video con efecto Ken Burns...")
    result = assembly.render_video(scenes, demo_dir / "demo_video.mp4", audio_path)
    print(f"    -> Video listo: {result.video_path} ({result.duration_seconds:.1f}s)")
    print("\nDemo completa. Abre la carpeta output/demo para ver el video y la miniatura.")


def _load_channel(name: str) -> tuple[ChannelConfig, dict]:
    import yaml

    channels_path = ROOT / "config" / "channels.yaml"
    if not channels_path.exists():
        print(
            f"No existe {channels_path}. Copia config/channels.example.yaml "
            "a config/channels.yaml y complétalo primero."
        )
        sys.exit(1)

    data = yaml.safe_load(channels_path.read_text(encoding="utf-8"))
    match = next((c for c in data["channels"] if c["name"] == name), None)
    if match is None:
        print(f"Canal '{name}' no encontrado en {channels_path}.")
        sys.exit(1)

    channel = ChannelConfig(
        name=match["name"],
        niche=match["niche"],
        language=match.get("language", "es"),
        elevenlabs_voice_id=match.get("elevenlabs_voice_id") or None,
        oauth_token_path=Path(match["oauth_token_path"]) if match.get("oauth_token_path") else None,
        output_dir=Path(match.get("output_dir", "output")),
    )
    return channel, match


def _print_report(report):
    print("\n=== Reporte del pipeline ===")
    print(f"Etapas completadas: {', '.join(report.completed_stages) or '(ninguna)'}")
    if report.skipped_stages:
        print("Etapas pendientes de configuración:")
        for stage, reason in report.skipped_stages.items():
            print(f"  - {stage}: {reason}")
    if report.video_path:
        print(f"Video: {report.video_path}")
    if report.thumbnail_path:
        print(f"Miniatura: {report.thumbnail_path}")


def cmd_run(args):
    from pipeline import orchestrator

    channel, match = _load_channel(args.channel)
    reference_channels = args.reference_channels or match.get("reference_channels", [])
    report = orchestrator.run_pipeline(channel, args.topic, reference_channels)
    _print_report(report)


def cmd_write_script(args):
    from pipeline import orchestrator

    channel, match = _load_channel(args.channel)
    reference_channels = args.reference_channels or match.get("reference_channels", [])
    brief, script_path = orchestrator.write_script(channel, args.topic, reference_channels)

    print(f"\nGuion generado: {script_path}")
    print(f"Titulo: {brief.title}")
    print(
        "\nEdita el archivo si quieres (título, guion, cierre, SEO) y despúes corre:\n"
        f'  python main.py render --channel {args.channel} --script-file "{script_path}"'
    )


def cmd_render(args):
    from pipeline import orchestrator

    channel, _match = _load_channel(args.channel)
    script_path = Path(args.script_file)
    if not script_path.exists():
        print(f"No existe el archivo de guion: {script_path}")
        sys.exit(1)

    report = orchestrator.render_from_script(channel, script_path)
    _print_report(report)


def _write_silence(path: Path, duration_seconds: float, sample_rate: int = 44100):
    n_frames = int(duration_seconds * sample_rate)
    with wave.open(str(path), "w") as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(b"\x00\x00" * n_frames)


def main():
    parser = argparse.ArgumentParser(description="Pipeline de automatización de YouTube")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("demo", help="Corre un ensamblado de video real sin necesitar API keys")

    run_parser = sub.add_parser("run", help="Corre el pipeline completo para un canal, sin pausas")
    run_parser.add_argument("--channel", required=True, help="Nombre del canal en channels.yaml")
    run_parser.add_argument("--topic", required=True, help="Tema del video a generar")
    run_parser.add_argument(
        "--reference-channels", nargs="*", default=[], help="IDs de canales de YouTube a investigar"
    )

    write_script_parser = sub.add_parser(
        "write-script",
        help="Genera solo el guion (research + guion) y lo guarda en un archivo editable",
    )
    write_script_parser.add_argument("--channel", required=True, help="Nombre del canal en channels.yaml")
    write_script_parser.add_argument("--topic", required=True, help="Tema del video a generar")
    write_script_parser.add_argument(
        "--reference-channels", nargs="*", default=[], help="IDs de canales de YouTube a investigar"
    )

    render_parser = sub.add_parser(
        "render",
        help="Retoma un archivo de guion (de write-script, editado o no) y termina voz/video",
    )
    render_parser.add_argument("--channel", required=True, help="Nombre del canal en channels.yaml")
    render_parser.add_argument("--script-file", required=True, help="Ruta al archivo de guion")

    args = parser.parse_args()
    {
        "demo": cmd_demo,
        "run": cmd_run,
        "write-script": cmd_write_script,
        "render": cmd_render,
    }[args.command](args)


if __name__ == "__main__":
    main()
