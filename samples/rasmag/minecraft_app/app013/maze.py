#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mcpi import minecraft  # Minecraft用
from mcpi import block  # Minecraftブロック用
import sys  # コマンドパラメータ取得用

# 迷路ゾーン作成
def createMazeZone():
  # プレーヤーが立っているタイルの位置を取得
  pos = mc.player.getTilePos()
  # posより1つ低い高さ、xとzは1ずらした位置から
  # 22x3x22をSTONE（石）で敷き詰める
  mc.setBlocks(pos.x+1, pos.y-1, pos.z+1,
               pos.x+22, pos.y+1, pos.z+22, block.STONE.id)
  # posと同じ高さ、xとzは2ずらした位置から
  # 20x2x20をDIRT（土）で埋める
  mc.setBlocks(pos.x+2, pos.y, pos.z+2,
               pos.x+21, pos.y+1, pos.z+21, block.DIRT.id)
  # posより2つ高い高さ、xとzは1ずらした位置から
  # 22x122をGLASS（ガラス）で埋める
  mc.setBlocks(pos.x+1, pos.y+2, pos.z+1,
               pos.x+22, pos.y+2, pos.z+22, block.GLASS.id)

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
  mc.postToChat("call createMazeZone()")
  # 迷路ゾーン作成の実行
  createMazeZone()

# 起動用処理
if __name__ == "__main__":
  main()


