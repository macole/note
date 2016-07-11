#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mcpi import minecraft  # Minecraft用
from mcpi import block  # Minecraftブロック用
# ↑mcpiモジュールの利用

# 石壁の作成
def createWall():
  # プレーヤーが立っているタイルの位置を取得
  pos = mc.player.getTilePos()
  # posを基準として10x10の空間をSTONE（石）で埋める
  mc.setBlocks(pos.x+3, pos.y, pos.z,
               pos.x+3, pos.y+9, pos.z+9, block.STONE.id)

# メイン関数
def main():
  # グローバル変数
  global mc
  # Minecraftアプリと通信開始
  mc = minecraft.Minecraft.create()
  # チャットメッセージを投稿
  mc.postToChat("call createWall()")
  # 石壁の作成の実行
  createWall()

# 起動用処理
if __name__ == "__main__":
  main()
