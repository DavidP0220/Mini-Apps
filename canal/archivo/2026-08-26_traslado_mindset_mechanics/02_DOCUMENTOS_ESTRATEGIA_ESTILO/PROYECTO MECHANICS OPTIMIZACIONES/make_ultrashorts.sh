#!/bin/bash
# Ultra-short batch v2 (12-18s) — built from the 2026-08-22 A/B finding:
# the winning variable is the first-2-seconds hook (concrete + visceral, no clinical
# jargon in the opening line), not the clip length. Cut points sit on silencedetect
# boundaries so no clip starts or ends mid-word.
set -e
FFMPEG="/c/Users/David Peñuela/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe/ffmpeg-9.0-full_build/bin/ffmpeg.exe"
OUT="/c/Users/David Peñuela/Documents/CLAUDE AUTOMATIC/shorts_final"
GLITCH="/c/Users/David Peñuela/Downloads/The-300000-Year-Old-Glitch-Still-Running-In-Your-Brain.mp4"
PREDATOR="/c/Users/David Peñuela/Downloads/Your-DNA-Hates-Predator-Meat-The-Secret-Science-of-Evolution.mp4"

FILTER="split=2[bg][fg];[bg]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,gblur=sigma=20[bg];[fg]scale=1080:-2[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2"

process() {
  local src="$1" start="$2" dur="$3" outname="$4"
  echo "=== $outname  (${start}s +${dur}s) ==="
  "$FFMPEG" -y -ss "$start" -i "$src" -t "$dur" \
    -vf "$FILTER" \
    -c:v libx264 -preset medium -crf 18 -c:a aac -b:a 192k \
    "$OUT/$outname" 2>&1 | tail -2
}

# 15 — replaces the failed 16s amygdala short (15% retention). Same source video,
#      same length class, but opens on "Your smoke detector..." instead of "Amygdala".
process "$GLITCH"   141.82 13.43 "15_glitch_smoke_detector.mp4"
# 16 — 300,000 years compressed into one 24-hour day; concrete numbers, zero jargon.
process "$GLITCH"   264.31 16.29 "16_glitch_24_hour_day.mp4"
# 17 — DDT made bald eagle eggshells crumble. Shock fact, no jargon.
process "$PREDATOR" 193.20 11.90 "17_predator_ddt_eagles.mp4"
# 18 — Mawson's team ate sled dog livers; skin peeled off in sheets. Most visceral
#      moment in the whole video and still unused (06_* is misnamed, it covers 166-192).
process "$PREDATOR" 210.80 14.53 "18_predator_mawson_livers.mp4"
# 19 — predators eat the sick and weak, so you eat everything that was wrong with the
#      prey. Ends at 270.18, exactly where the published trichinosis winner begins.
process "$PREDATOR" 253.00 17.18 "19_predator_cleanup_crew.mp4"

echo "=== DONE ==="
