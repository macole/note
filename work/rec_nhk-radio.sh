#!/bin/bash

# 下記を参考にしつつ作成
# https://gist.github.com/matchy2/3956266
# https://gist.github.com/saiten/1185755

if [ $# -eq 2 ]; then
  channel=$1
  duration=`expr $2 \* 60`
  outputprefix="NHK-${channel}"
  outdir="${XDG_CACHE_HOME}/radio/"
elif [ $# -eq 3 ]; then
  channel=$1
  duration=`expr $2 \* 60`
  outputprefix=$3
  outdir="${XDG_CACHE_HOME}/radio/"
elif [ $# -eq 4 ]; then
  channel=$1
  duration=`expr $2 \* 60`
  outputprefix=$3
  outdir=$4
else
  echo "usage : $0 channel_name duration(minuites) [filename_prefix [output_dir]]"
  echo "         channel_name list"
  echo "           NHK Radio #1: r1"
  echo "           NHK Radio #2: r2"
  echo "           NHK-FM: fm"
  exit 1
fi

#
# parameter setting
#
case ${channel} in
  r1) playpath='NetRadio_R1_flash@63346' ;;
  r2) playpath='NetRadio_R2_flash@63342' ;;
  fm) playpath='NetRadio_FM_flash@63343' ;;
  *) exit 1 ;;
esac
date=`date '+%Y-%m-%d-%H%M'`
playerurl="http://www3.nhk.or.jp/netradio/files/swf/rtmpe.swf"
rtmpurl="rtmpe://netradio-${channel}-flash.nhk.jp/live/${playpath}"
buffer=1000
mkdir -p ${outdir}


#
# rtmpdump
#
rtmpdump --quiet \
         --rtmp "${rtmpurl}" \
         --swfVfy ${playerurl} \
         --live \
         --buffer ${buffer} \
         --stop ${duration} \
         --flv - > "${outdir}/NHK-${channel}_${date}"

# mp3 encode
#ffmpeg -loglevel quiet -y -i "${outdir}/NHK-${channel}_${date}" -acodec libmp3lame -ab 128k "${outdir}/${outputprefix}_${date}.mp3"

# ogg encode
#ffmpeg -loglevel quiet -y -i "${outdir}/NHK-${channel}_${date}" -acodec libvorbis -aq 3 "${outdir}/${outputprefix}_${date}.ogg"

# dump stream (AAC)
#ffmpeg -loglevel quiet -y -i "${outdir}/NHK-${channel}_${date}" -acodec copy "${outdir}/${outputprefix}_${date}.aac"
avconv -loglevel quiet -y -i "${outdir}/NHK-${channel}_${date}" -acodec copy "${outdir}/${outputprefix}_${date}.m4a"

if [ $? = 0 ]; then
  rm -f "${outdir}/NHK-${channel}_${date}"
fi
