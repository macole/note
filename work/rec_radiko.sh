#!/bin/bash

# https://gist.github.com/matchy2/3956266 を若干修正

if [ $# -eq 2 ]; then
  channel=$1
  DURATION=`expr $2 \* 60`
  outdir="${XDG_CACHE_HOME}/radio/"
  outputprefix=${channel}
elif [ $# -eq 3 ]; then
  channel=$1
  DURATION=`expr $2 \* 60`
  outputprefix=$3
  outdir="${XDG_CACHE_HOME}/radio/"
elif [ $# -eq 4 ]; then
  channel=$1
  DURATION=`expr $2 \* 60`
  outputprefix=$3
  outdir=$4
else
  echo "usage : $0 channel_name duration(minutes) [filename_prefix [output_dir]]"
  echo "         channel_name list"
  echo "           TBS Radio: TBS"
  echo "           Nippon Cultural Broadcasting: QRR"
  echo "           Nippon Broadcasting: LFR"
  echo "           Radio Nippon: JORF"
  echo "           Inter FM: INT"
  echo "           Tokyo FM: FMT"
  echo "           J-WAVE: FMJ"
  echo "           bayfm 78.0MHz: BAYFM78"
  echo "           NACK5: NACK5"
  echo "           FM yokohama 84.7: YFM"
 exit 1
fi

#
# parameter setting
#
pid=$$
date=`date '+%Y-%m-%d-%H%M'`
playerurl=http://radiko.jp/player/swf/player_3.0.0.01.swf
playerfile="${outdir}/player.swf"
keyfile="${outdir}/authkey.png"
auth1_fms_file="${outdir}/auth1_fms_${pid}"
auth2_fms_file="${outdir}/auth2_fms_${pid}"
channel_file="${outdir}/${channel}.xml"
mkdir -p ${outdir}

#
# get player
#
if [ ! -f $playerfile ]; then
  wget -q -O $playerfile $playerurl

  if [ $? -ne 0 ]; then
    echo "failed get player"
    exit 1
  fi
fi

#
# get keydata (need swftool)
#
if [ ! -f $keyfile ]; then
  swfextract -b 14 $playerfile -o $keyfile

  if [ ! -f $keyfile ]; then
    echo "failed get keydata"
    exit 1
  fi
fi

if [ -f ${auth1_fms_file} ]; then
  rm -f ${auth1_fms_file}
fi

#
# access auth1_fms
#
wget -q \
     --header="pragma: no-cache" \
     --header="X-Radiko-App: pc_1" \
     --header="X-Radiko-App-Version: 2.0.1" \
     --header="X-Radiko-User: test-stream" \
     --header="X-Radiko-Device: pc" \
     --post-data='\r\n' \
     --no-check-certificate \
     --save-headers \
     -O ${auth1_fms_file} \
     https://radiko.jp/v2/api/auth1_fms

if [ $? -ne 0 ]; then
  echo "failed auth1 process"
  exit 1
fi

#
# get partial key
#
authtoken=`perl -ne 'print $1 if(/x-radiko-authtoken: ([\w-]+)/i)' ${auth1_fms_file}`
offset=`perl -ne 'print $1 if(/x-radiko-keyoffset: (\d+)/i)' ${auth1_fms_file}`
length=`perl -ne 'print $1 if(/x-radiko-keylength: (\d+)/i)' ${auth1_fms_file}`

partialkey=`dd if=$keyfile bs=1 skip=${offset} count=${length} 2> /dev/null | base64`

echo "authtoken: ${authtoken} \noffset: ${offset} length: ${length} \npartialkey: $partialkey"

rm -f ${auth1_fms_file}

if [ -f ${auth2_fms_file} ]; then
  rm -f ${auth2_fms_file}
fi

#
# access auth2_fms
#
wget -q \
     --header="pragma: no-cache" \
     --header="X-Radiko-App: pc_1" \
     --header="X-Radiko-App-Version: 2.0.1" \
     --header="X-Radiko-User: test-stream" \
     --header="X-Radiko-Device: pc" \
     --header="X-Radiko-Authtoken: ${authtoken}" \
     --header="X-Radiko-Partialkey: ${partialkey}" \
     --post-data='\r\n' \
     --no-check-certificate \
     -O ${auth2_fms_file} \
     https://radiko.jp/v2/api/auth2_fms

if [ $? -ne 0 -o ! -f ${auth2_fms_file} ]; then
  echo "failed auth2 process"
  exit 1
fi

echo "authentication success"

areaid=`perl -ne 'print $1 if(/^([^,]+),/i)' ${auth2_fms_file}`
echo "areaid: $areaid"

rm -f ${auth2_fms_file}

#
# get stream-url
#

if [ -f ${channel_file} ]; then
  rm -f ${channel_file}
fi

wget -q "http://radiko.jp/v2/station/stream/${channel}.xml" -O ${channel_file}

stream_url=`echo "cat /url/item[1]/text()" | xmllint --shell ${channel_file} | tail -2 | head -1`
url_parts=(`echo ${stream_url} | perl -pe 's!^(.*)://(.*?)/(.*)/(.*?)$/!$1://$2 $3 $4!'`)

rm -f ${channel_file}

#
# rtmpdump
#
rtmpdump -v -q \
         -r ${url_parts[0]} \
         --app ${url_parts[1]} \
         --playpath ${url_parts[2]} \
         -W $playerurl \
         -C S:"" -C S:"" -C S:"" -C S:$authtoken \
         --live \
         --stop ${DURATION} \
         --flv "${outdir}//${channel}_${date}"

# mp3 encode
#ffmpeg -loglevel quiet -y -i "${outdir}/${channel}_${date}" -acodec libmp3lame -ab 128k "${outdir}/${outputprefix}_${date}.mp3"

# ogg encode
#ffmpeg -loglevel quiet -y -i "${outdir}/${channel}_${date}" -acodec libvorbis -aq 3 "${outdir}/${outputprefix}_${date}.ogg"

# 再エンコしない (AAC) 場合
#ffmpeg -loglevel quiet -y -i "${outdir}/${channel}_${date}" -acodec copy "${outdir}/${outputprefix}_${date}.aac"
avconv -loglevel quiet -y -i "${outdir}/${channel}_${date}" -acodec copy "${outdir}/${outputprefix}_${date}.m4a"

if [ $? = 0 ]; then
  rm -f "${outdir}/${channel}_${date}"
fi
