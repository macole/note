#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mcpi import minecraft  # Minecraft用
import sys  # コマンドパラメータ取得用

# メイン関数
def main():
  # ラズパイのIPアドレスは
  # コマンドパラメータの第１引数に指定
  ip = sys.argv[1]
  # Minecraftアプリとの通信で使うポート番号
  port = 4711
  # Minecraftアプリと通信開始
  mc = minecraft.Minecraft.create(ip, port)
  # チャットメッセージを投稿
  mc.postToChat("app012")

# 起動用処理
if __name__ == "__main__":
  main()

