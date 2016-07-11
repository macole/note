#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame # オーディオ再生に必要なモジュール
import time # 休止に必要なモジュール
INTERVAL = 10
d = "/home/pi/Music" # ディレクトリの指定
f = "01.mp3"         # ファイルの指定
# ファイルパスの生成
path = "{0}/{1}".format(d, f)
# pygame.mixierの初期化
pygame.mixer.init()
# オーディオファイルのロード
pygame.mixer.music.load(path)
# 再生
pygame.mixer.music.play()
# 再生中は継続。INTERVAL秒ごとにチェック
while pygame.mixer.music.get_busy() == True:
  time.sleep(INTERVAL)
  continue

