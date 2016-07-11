#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mcpi import minecraft  # Minecraft用
from mcpi import block  # Minecraftブロック用
# ↑mcpiモジュールの利用

# 溶岩の作成
def createLava():
  # プレーヤーが立っているタイルの位置を取得
  pos = mc.player.getTilePos()
  # posを基準として(x, y-1, z) - (x+10, y-11, z+10) の空間を
  # STONE（石）で埋める
  mc.setBlocks(pos.x, pos.y-1, pos.z,
               pos.x+10, pos.y-11, pos.z+10, block.STONE.id)
  # posを基準として(x+1, y-1, z+1) - (x+9, y-10, z+9) の空間を
  # LAVA（溶岩）で埋める
  mc.setBlocks(pos.x+1, pos.y-1, pos.z+1,
               pos.x+9, pos.y-10, pos.z+9, block.LAVA.id)
  # posを基準として(x, y, z) - (x+10, y, z+10) の空間を
  # AIR（空気）で埋める
  mc.setBlocks(pos.x, pos.y, pos.z,
               pos.x+10, pos.y, pos.z+10, block.AIR.id)

# メイン関数
def main():
  # グローバル変数
  global mc
  # Minecraftアプリと通信開始
  mc = minecraft.Minecraft.create()
  # チャットメッセージを投稿
  mc.postToChat("call createWall()")
  # 溶岩の作成の実行
  createLava()

# 起動用処理
if __name__ == "__main__":
  main()
