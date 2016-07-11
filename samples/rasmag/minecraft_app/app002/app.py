#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mcpi import minecraft 
# ↑mcpiモジュールの利用

# メイン関数
def main():
  # Minecraftアプリと通信開始
  mc = minecraft.Minecraft.create()
  # チャットメッセージを投稿
  mc.postToChat("Python and Minecraft")

# 起動用処理
if __name__ == "__main__":
  main()

