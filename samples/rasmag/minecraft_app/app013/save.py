#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mcpi import minecraft  # Minecraft用
from mcpi import block  # Minecraftブロック用
import sys  # コマンドパラメータ取得用

# 迷路情報をsample.txtへ保存
def saveMazeZone():
  pos = mc.player.getTilePos()
  print "create list"
  yxz = [[[None for z in range(22)] for x in range(22)] for y in range(4)]
  print "getBlocks"
  for i in range(len(yxz)):
    print "i:" + str(i)
    for j in range(len(yxz[i])):
      print "j:" + str(j)
      for k in range(len(yxz[i][j])):
        yxz[i][j][k] = mc.getBlock(pos.x+1+j, pos.y-1+i, pos.z+1+k)
  print "create list text"
  txt = createListText(yxz)
  print "start save"
  with open("sample.txt", mode = "w") as fh:
    fh.write(txt)
    fh.flush()

# yxzリストからPythonソースコードを生成
def createListText(yxz):
  t = "[\n"
  for i in range(len(yxz)):
    t += "  [\n"
    for j in range(len(yxz[i])):
      t += "    ["
      for k in range(len(yxz[i][j])):
        t += str(yxz[i][j][k])
        t += ","
      t += "],\n"
    t += "  ],\n"
  t += "]\n"
  return t

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
  mc.postToChat("call saveMazeZone()")
  # 迷路ゾーン保存の実行
  saveMazeZone()

# 起動用処理
if __name__ == "__main__":
  main()
