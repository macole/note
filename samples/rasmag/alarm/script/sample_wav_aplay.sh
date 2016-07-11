#! /bin/sh
# ディレクトリの指定
d=/usr/share/sounds/alsa
# /usr/share/sounds/alsaにある
# 各ファイルについて繰り返し処理
for f in `ls ${d}`; do
  # aplayコマンドでオーディオファイル再生
  aplay "$d/$f"
  # オーディオファイル再生後、1秒休止
  sleep 1
done
