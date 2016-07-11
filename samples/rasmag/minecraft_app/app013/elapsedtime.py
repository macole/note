#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mcpi import minecraft  # Minecraft用
from mcpi import block  # Minecraftブロック用
import sys  # コマンドパラメータ取得用
import time # 時間計測用

def start():
  start_time = time.time()
  # ダイヤモンドブロックの上を通過で測定終了
  v = block.AIR.id
  while v != block.DIAMOND_BLOCK.id:
    time.sleep(0.2)
    pos = mc.player.getTilePos()
    v = mc.getBlock(pos.x, pos.y-1, pos.z)
  # 経過時間を算出
  elapsed_time = time.time() - start_time
  # 経過時間を出力。小さいほど成績が良い
  print str(elapsed_time)
  mc.postToChat(str(elapsed_time))

# メイン関数
def main():
  # グローバル変数
  global mc
  # ラズパイのIPアドレスは
  # コマンドパラメータの第１引数に指定
  ip = sys.argv[1]
  # Minecraftアプリとの通信で使うポート番号
  port = 4711
  # Minecraftアプリと通信開始
  mc = minecraft.Minecraft.create(ip, port)
  # メロンブロックの上を通過で測定開始
  v = block.AIR.id
  while v != block.MELON.id:
    time.sleep(0.2)
    pos = mc.player.getTilePos()
    v = mc.getBlock(pos.x, pos.y-1, pos.z)
  mc.postToChat("game start()")
  start()

# 起動用処理
if __name__ == "__main__":
  main()

