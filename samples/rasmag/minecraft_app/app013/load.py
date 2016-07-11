#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mcpi import minecraft  # Minecraft用
from mcpi import block  # Minecraftブロック用
import sys  # コマンドパラメータ取得用

# sample.txtの迷路情報から迷路を復元
def loadMazeZone():
  lines = ""
  with open("sample.txt", mode = "r") as fh:
    for line in fh:
      lines += line
  yxz = eval(lines)
  pos = mc.player.getTilePos()
  print "setBlocks"
  for i in range(len(yxz)):
    print "i:" + str(i)
    for j in range(len(yxz[i])):
      print "j:" + str(j)
      for k in range(len(yxz[i][j])):
         mc.setBlock(pos.x+1+j, pos.y-1+i, pos.z+1+k, yxz[i][j][k])

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
  # チャットメッセージを投稿
  mc.postToChat("call loadMazeZone()")
  # 迷路ゾーンのロード実行
  loadMazeZone()

# 起動用処理
if __name__ == "__main__":
  main()

