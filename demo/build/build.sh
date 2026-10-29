#!/bin/bash
set -e
cd "$(dirname "$0")"

# Krishna reads at 148 wpm. 1.16x lands it at 172 wpm and the cut at 2:57.
TEMPO=1.16

# ---- narration: speed-corrected, concatenated, then silence under the end card ----
for i in 0 1 2 3 4 5 6 7 8; do
  ffmpeg -y -loglevel error -i vo/t$i.wav -af "atempo=$TEMPO" -ar 48000 -ac 2 \
    -c:a pcm_s16le vo/a$i.wav
done
ffmpeg -y -loglevel error -f lavfi -i anullsrc=r=48000:cl=stereo -t 3.0 \
  -c:a pcm_s16le vo/sil.wav

: > alist.txt
for i in 0 1 2 3 4 5 6 7 8; do echo "file 'vo/a$i.wav'" >> alist.txt; done
echo "file 'vo/sil.wav'" >> alist.txt
ffmpeg -y -loglevel error -f concat -safe 0 -i alist.txt -c copy audio.wav

# ---- video: stills held against the speed-corrected narration ----
cat > vlist.txt <<'EOF'
file 'cards/c0a.png'
duration 4.60
file 'cards/c0b.png'
duration 4.85
file 'cards/c1a.png'
duration 15.94
file 'cards/c1b.png'
duration 12.47
file 'cards/c2a.png'
duration 14.25
file 'cards/c2b.png'
duration 3.20
file 'cards/n1.png'
duration 3.06
file 'cards/n2.png'
duration 5.35
file 'cards/s3.png'
duration 25.59
file 'cards/s4.png'
duration 25.79
file 'cards/s5.png'
duration 26.48
file 'cards/n3.png'
duration 2.91
file 'cards/n4.png'
duration 2.91
file 'cards/n5.png'
duration 2.18
file 'cards/c7b.png'
duration 15.84
file 'cards/c7a.png'
duration 8.50
file 'cards/end.png'
duration 3.00
file 'cards/end.png'
EOF

ffmpeg -y -loglevel error -f concat -safe 0 -i vlist.txt \
  -vf "fps=30,format=yuv420p" -c:v libx264 -preset slow -crf 18 video.mp4

# ---- mux ----
ffmpeg -y -loglevel error -i video.mp4 -i audio.wav \
  -af "loudnorm=I=-16:TP=-1.5:LRA=11,aresample=48000" \
  -c:v copy -c:a aac -b:a 192k -ar 48000 -shortest \
  one-record-demo.mp4

echo "built:"
ffmpeg -i one-record-demo.mp4 2>&1 | grep -E "Duration|Stream"
