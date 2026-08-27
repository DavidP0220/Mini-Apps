#!/bin/bash
set -e
FFMPEG="/c/Users/David Peñuela/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe/ffmpeg-9.0-full_build/bin/ffmpeg.exe"
OUT="/c/Users/David Peñuela/Documents/CLAUDE AUTOMATIC/shorts_final"
GLITCH="/c/Users/David Peñuela/Downloads/The-300000-Year-Old-Glitch-Still-Running-In-Your-Brain.mp4"
PREDATOR="/c/Users/David Peñuela/Downloads/Your-DNA-Hates-Predator-Meat-The-Secret-Science-of-Evolution.mp4"
OMNI="/c/Users/David Peñuela/Downloads/The-Psychological-Secret-to-Solving-EVERYTHING-Unlock-Your-Master-Mind.mp4"

FILTER="split=2[bg][fg];[bg]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,gblur=sigma=20[bg];[fg]scale=1080:-2[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2"

process() {
  local src="$1" start="$2" dur="$3" outname="$4"
  echo "=== Processing $outname ==="
  "$FFMPEG" -y -ss "$start" -i "$src" -t "$dur" \
    -vf "$FILTER" \
    -c:v libx264 -preset medium -crf 18 -c:a aac -b:a 192k \
    "$OUT/$outname" 2>&1 | tail -3
}

process "$GLITCH" 167.93 20.57 "02_glitch_dive_reflex.mp4"
process "$GLITCH" 43.96 25.79 "03_glitch_uncalibrated_reframe.mp4"
process "$PREDATOR" 0.22 32.56 "04_predator_opening_hook.mp4"
process "$PREDATOR" 444.09 30.70 "05_predator_herbivore_focus.mp4"
process "$PREDATOR" 166.00 26.38 "06_predator_douglas_mawson.mp4"
process "$OMNI" 0.40 38.72 "07_omni_opening_hook.mp4"
process "$OMNI" 197.00 13.00 "08_omni_stay_calm.mp4"
process "$OMNI" 210.72 14.83 "09_omni_why_panic_kills.mp4"

echo "=== DONE ==="
ls -la "$OUT"
