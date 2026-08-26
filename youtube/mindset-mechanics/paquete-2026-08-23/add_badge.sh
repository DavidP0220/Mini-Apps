#!/bin/bash
# Burn the SUBSCRIBE badge into the final seconds of each ultra-short.
# Rationale (2026-08-22 data): Shorts = 95 views / 0 subscribers, but 83.8% average
# retention on the best one, i.e. viewers reach the end and are never asked.
# Badge sits at y=1330, inside the blurred padding below the 656..1263 video band,
# so it covers no captions and stays clear of the Shorts UI action rail.
set -e
FFMPEG="/c/Users/David Peñuela/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe/ffmpeg-9.0-full_build/bin/ffmpeg.exe"
FFPROBE="/c/Users/David Peñuela/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe/ffmpeg-9.0-full_build/bin/ffprobe.exe"
DIR="/c/Users/David Peñuela/Documents/CLAUDE AUTOMATIC/shorts_final"
BADGE="$DIR/subscribe_badge_shorts.png"
HOLD=3.5   # seconds the badge stays on screen, at the very end

for name in "$@"; do
  src="$DIR/$name.mp4"
  dur=$("$FFPROBE" -v error -show_entries format=duration -of csv=p=0 "$src")
  start=$(awk -v d="$dur" -v h="$HOLD" 'BEGIN{printf "%.2f", (d-h<0?0:d-h)}')
  echo "=== $name  dur=${dur}s  badge from ${start}s ==="
  "$FFMPEG" -y -i "$src" -loop 1 -i "$BADGE" \
    -filter_complex "[1:v]format=rgba,fade=in:st=${start}:d=0.4:alpha=1[b];[0:v][b]overlay=210:1330:enable='gte(t,${start})'" \
    -c:v libx264 -preset medium -crf 18 -c:a copy -shortest \
    "$DIR/${name}_badged.mp4" 2>&1 | tail -1
done
echo "=== DONE ==="
