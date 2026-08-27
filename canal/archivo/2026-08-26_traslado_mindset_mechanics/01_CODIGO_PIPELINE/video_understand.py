"""Analiza un video (URL o archivo local) sin tener que verlo entero a mano.

Combina tres piezas que ya estaban instaladas pero nunca conectadas
(ver LEEME-PRIMERO-HANDOFF.md §5.4): yt-dlp para bajar el video si hace
falta, faster-whisper para transcribir el audio con timestamps, y la
técnica de rejilla de frames con ffmpeg (probada a mano en la sesión del
2026-08-22) para poder "leer" subtítulos quemados y UI de un vistazo sin
tener que reproducir el video.

Salida: un transcript con timestamps (.txt y .srt) y una o más imágenes de
rejilla con frames muestreados — pensadas para que se lean con la
herramienta Read de Claude Code, no para el ojo humano directo.

Ejemplos:
  # Analizar un tutorial completo de un competidor
  python video_understand.py "https://youtube.com/watch?v=XXXX" --out-dir out/competidor1

  # Solo un tramo de un video ya descargado, mapeando subtítulos quemados
  # a timestamps exactos (banda inferior, igual que la técnica probada)
  python video_understand.py video.mp4 --start 140 --duration 60 \
      --subtitle-band 700:330 --no-transcript

  # Solo transcript, sin frames (más rápido)
  python video_understand.py video.mp4 --no-frames
"""
import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

# Antes estaban clavados a la instalacion WinGet de una maquina concreta, asi
# que el script solo corria en ese equipo (mismo fallo que ya se corrigio en
# video_express_bot.py). Ahora: variable de entorno > PATH > nombre pelado.
FFMPEG = os.getenv("FFMPEG") or shutil.which("ffmpeg") or "ffmpeg"
FFPROBE = os.getenv("FFPROBE") or shutil.which("ffprobe") or "ffprobe"

FRAMES_PER_GRID = 20  # 4x5, el tamaño que se probó legible de un vistazo


def _run(cmd: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, text=True)


def is_url(s: str) -> bool:
    return s.startswith("http://") or s.startswith("https://")


def download_video(url: str, out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"Descargando con yt-dlp: {url}")
    result = _run([
        sys.executable, "-m", "yt_dlp",
        "-f", "bv*[height<=1080]+ba/b[height<=1080]",
        "--merge-output-format", "mp4",
        "-o", str(out_dir / "%(id)s.%(ext)s"),
        "--print", "after_move:filepath",
        url,
    ])
    if result.returncode != 0:
        raise RuntimeError(f"yt-dlp falló:\n{result.stderr}")
    path = Path(result.stdout.strip().splitlines()[-1])
    print(f"Descargado: {path}")
    return path


def probe_duration(video_path: Path) -> float:
    result = _run([
        FFPROBE, "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", str(video_path),
    ])
    return float(result.stdout.strip())


def transcribe(video_path: Path, out_dir: Path, model_size: str,
                start: float, duration: float | None) -> Path:
    from faster_whisper import WhisperModel

    print(f"Transcribiendo con faster-whisper (modelo '{model_size}')...")
    model = WhisperModel(model_size, device="cpu", compute_type="int8")
    transcribe_kwargs = {"vad_filter": True}
    if duration:
        # Pasar clip_timestamps=None explícito (en vez de omitirlo) rompe
        # faster-whisper: su código interno espera indexar clip_timestamps[0]
        # incluso cuando no hay recorte, así que solo se agrega la key si
        # hay un recorte real que aplicar.
        transcribe_kwargs["clip_timestamps"] = [start, start + duration]
    segments, info = model.transcribe(str(video_path), **transcribe_kwargs)
    print(f"Idioma detectado: {info.language} (p={info.language_probability:.2f})")

    txt_path = out_dir / "transcript.txt"
    srt_path = out_dir / "transcript.srt"
    with open(txt_path, "w", encoding="utf-8") as txt_f, \
         open(srt_path, "w", encoding="utf-8") as srt_f:
        for i, seg in enumerate(segments, start=1):
            txt_f.write(f"[{_fmt_ts(seg.start)} -> {_fmt_ts(seg.end)}] {seg.text.strip()}\n")
            srt_f.write(f"{i}\n{_fmt_srt(seg.start)} --> {_fmt_srt(seg.end)}\n{seg.text.strip()}\n\n")

    print(f"Transcript: {txt_path}")
    return txt_path


def _fmt_ts(seconds: float) -> str:
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def _fmt_srt(seconds: float) -> str:
    ms = int((seconds - int(seconds)) * 1000)
    h, rem = divmod(int(seconds), 3600)
    m, s = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def make_frame_grids(
    video_path: Path, out_dir: Path, start: float, duration: float,
    interval: float, subtitle_band: str | None,
) -> list[Path]:
    """Muestrea 1 frame cada `interval` segundos y las pega en rejillas de
    4x5 (20 frames por imagen) para poder leer decenas de momentos del
    video de un vistazo. Con `subtitle_band` ("y:h") recorta esa franja
    en vez del frame completo — la técnica exacta usada para leer
    subtítulos quemados sin reproducir el video (ver handoff §7.2)."""
    total_frames = int(duration // interval)
    n_grids = max(1, -(-total_frames // FRAMES_PER_GRID))  # ceil
    grid_paths = []

    for g in range(n_grids):
        chunk_start = start + g * FRAMES_PER_GRID * interval
        chunk_frames = min(FRAMES_PER_GRID, total_frames - g * FRAMES_PER_GRID)
        if chunk_frames <= 0:
            break
        chunk_duration = chunk_frames * interval

        crop = f"crop=iw:{subtitle_band.split(':')[1]}:0:{subtitle_band.split(':')[0]}," if subtitle_band else ""
        vf = f"fps=1/{interval},{crop}scale=760:-2,tile=4x5:margin=6:padding=6:color=black"

        out_path = out_dir / f"grid_{g+1:02d}.png"
        cmd = [
            FFMPEG, "-y", "-ss", str(chunk_start), "-t", str(chunk_duration),
            "-i", str(video_path), "-vf", vf, "-frames:v", "1", str(out_path),
        ]
        result = _run(cmd)
        if result.returncode != 0 or not out_path.exists():
            print(f"Aviso: rejilla {g+1} falló:\n{result.stderr[-500:]}")
            continue
        grid_paths.append(out_path)
        first_ts = _fmt_ts(chunk_start)
        last_ts = _fmt_ts(chunk_start + chunk_duration)
        print(f"Rejilla {g+1}/{n_grids}: {out_path}  (cubre {first_ts} -> {last_ts})")

    return grid_paths


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("input", help="URL de video (yt-dlp) o ruta a archivo local")
    parser.add_argument("--out-dir", default=None, help="Carpeta de salida (default: video_understand_out/<nombre>)")
    parser.add_argument("--start", type=float, default=0.0, help="Segundo de inicio (default: 0)")
    parser.add_argument("--duration", type=float, default=None, help="Duración a procesar en segundos (default: todo el video)")
    parser.add_argument("--transcript", dest="transcript", action="store_true", default=True)
    parser.add_argument("--no-transcript", dest="transcript", action="store_false")
    parser.add_argument("--whisper-model", default="small", help="Tamaño del modelo faster-whisper (default: small)")
    parser.add_argument("--frames", dest="frames", action="store_true", default=True)
    parser.add_argument("--no-frames", dest="frames", action="store_false")
    parser.add_argument("--frame-interval", type=float, default=3.0, help="Segundos entre frames muestreados (default: 3)")
    parser.add_argument("--subtitle-band", default=None, help="Recorta solo una franja 'y:altura' en vez del frame completo (para leer subtítulos quemados)")
    args = parser.parse_args()

    if is_url(args.input):
        tmp_dir = Path(args.out_dir or "video_understand_out/_downloads")
        video_path = download_video(args.input, tmp_dir)
        default_name = video_path.stem
    else:
        video_path = Path(args.input)
        if not video_path.exists():
            print(f"No existe el archivo: {video_path}")
            sys.exit(1)
        default_name = video_path.stem

    out_dir = Path(args.out_dir or f"video_understand_out/{default_name}")
    out_dir.mkdir(parents=True, exist_ok=True)

    total_duration = probe_duration(video_path)
    duration = args.duration or (total_duration - args.start)
    print(f"Video: {video_path}  |  duración total: {_fmt_ts(total_duration)}  |  procesando: {_fmt_ts(args.start)} -> {_fmt_ts(args.start + duration)}")

    if args.transcript:
        transcribe(video_path, out_dir, args.whisper_model, args.start, args.duration)

    if args.frames:
        make_frame_grids(video_path, out_dir, args.start, duration, args.frame_interval, args.subtitle_band)

    print(f"\nListo. Todo en: {out_dir}")


if __name__ == "__main__":
    main()
