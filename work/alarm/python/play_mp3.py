#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess # 必要なモジュールの指定
d = "/home/pi/Music" # ディレクトリの指定
f = "01.mp3"         # ファイルの指定
# コマンド文字列の生成
cmd = "/usr/bin/omxplayer -o local {0}/{1}".format(d, f)
# コマンド文字列を配列に変換してcallで実行
# ディレクトリ名に空白があると誤動作するので注意
subprocess.call(cmd.strip().split(" "))

