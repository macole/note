#!/bin/bash

#
# mmsなストリーミングのasxファイルを読み込み、ストリームをdumpする
#   1. asxファイルをダウンロード
#   2. asxファイルのなかからURL(mms://~)を取得
#   3. mplayerでdump
#

if [ $# -eq 1 ]; then
  url=$1
  outdir="${XDG_CACHE_HOME}/radio/"
elif [ $# -eq 2 ]; then
  url=$1
  outdir=$2
else
  echo "usage : $0 url [outputdir]"
  exit 1
fi

#
# parameter setting
#
pid=$$
tmpdir="${XDG_CACHE_HOME}/radio/"
asxfile="${tmpdir}/${url##*/}"
mkdir -p ${tmpdir}
mkdir -p ${outdir}


#
# get asx file
#
if [ ! -f ${asxfile} ]; then
  wget -q -O ${asxfile} ${url}

  if [ $? -ne 0 ]; then
    echo "failed to get ${url}"
    exit 1
  fi
fi

#
# parse asx file
#
mmsurl=`nkf -w ${asxfile} | gawk '/href=/ {print $0}' | sed -e 's/.*\(mms\:\/\/[^">]\+\).*/\1/'`

# 出力ファイル名はasxファイルのファイル名に合わせる
outputfile="${asxfile%.*}.${mmsurl##*.}"

#
# dump
#
mplayer ${mmsurl} -dumpstream -dumpfile ${outputfile}


if [ $? = 0 ]; then
  rm -f ${asxfile}
fi
