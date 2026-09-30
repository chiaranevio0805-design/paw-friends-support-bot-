#!/usr/bin/env bash
# Einmal pro neuer Session: ffmpeg, Whisper und die Untertitel-Schrift installieren.
set -e
pip install -q imageio-ffmpeg faster-whisper
FF=$(python3 -c "import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())")
command -v ffmpeg >/dev/null || ln -sf "$FF" /usr/local/bin/ffmpeg
mkdir -p /root/.fonts
[ -f /root/.fonts/Anton-Regular.ttf ] || curl -sSL -o /root/.fonts/Anton-Regular.ttf \
  https://raw.githubusercontent.com/google/fonts/main/ofl/anton/Anton-Regular.ttf
echo "setup ok"
