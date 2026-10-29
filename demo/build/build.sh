#!/bin/bash
set -e
cd "$(dirname "$0")"

# ---- video track: stills held for the measured narration durations ----
cat > vlist.txt <<'EOF'
file 'cards/c1a.png'
duration 10.40
file 'cards/c1b.png'
duration 11.25
file 'cards/c2a.png'
duration 11.24
file 'cards/c2b.png'
duration 3.00
file 'cards/s3.png'
duration 15.86
file 'cards/s4.png'
duration 20.85
file 'cards/s5.png'
duration 21.08
file 'cards/n1.png'
duration 2.50
file 'cards/n2.png'
duration 5.90
file 'cards/n3.png'
duration 2.50
file 'cards/n4.png'
duration 2.50
file 'cards/n5.png'
duration 1.88
file 'cards/c7a.png'
duration 7.30
file 'cards/c7b.png'
duration 13.51
file 'cards/end.png'
duration 3.50
file 'cards/end.png'
EOF

ffmpeg -y -loglevel error -f concat -safe 0 -i vlist.txt \
  -vf "fps=30,format=yuv420p" -c:v libx264 -preset slow -crf 18 video.mp4

# ---- audio track: the seven narration takes, then silence under the end card ----
ffmpeg -y -loglevel error -f lavfi -i anullsrc=r=48000:cl=stereo -t 3.5 \
  -c:a pcm_s16le vo/sil.wav

cat > alist.txt <<'EOF'
file 'vo/s1.wav'
file 'vo/s2.wav'
file 'vo/s3.wav'
file 'vo/s4.wav'
file 'vo/s5.wav'
file 'vo/s6.wav'
file 'vo/s7.wav'
file 'vo/sil.wav'
EOF

ffmpeg -y -loglevel error -f concat -safe 0 -i alist.txt -c copy audio.wav

# ---- mux ----
ffmpeg -y -loglevel error -i video.mp4 -i audio.wav \
  -af "loudnorm=I=-16:TP=-1.5:LRA=11" \
  -c:v copy -c:a aac -b:a 192k -shortest \
  one-record-demo.mp4

echo "built:"
ffmpeg -i one-record-demo.mp4 2>&1 | grep -E "Duration|Stream"
