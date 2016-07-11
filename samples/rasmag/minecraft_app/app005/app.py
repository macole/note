#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mcpi import minecraft  # Minecraft用
from mcpi import block  # Minecraftブロック用
# ↑mcpiモジュールの利用

# フィールド整地
def clearBlock():
  # プレーヤーが立っているタイルの位置を取得
  pos = mc.player.getTilePos()
  # posを基準として1つ低い高さの100x100をGRASS（緑地）で敷き詰める
  mc.setBlocks(pos.x, pos.y-1, pos.z,
               pos.x+99, pos.y-1, pos.z+99, block.GRASS.id)
  # posを基準として100x100x100の空間をAIR（空気）で埋める
  mc.setBlocks(pos.x, pos.y, pos.z,
               pos.x+99, pos.y+99, pos.z+99, block.AIR.id)

# メイン関数
def main():
  # グローバル変数
  global mc
  # Minecraftアプリと通信開始
  mc = minecraft.Minecraft.create()
  # チャットメッセージを投稿
  mc.postToChat("call clearBlock()")
  # 整地の実行
  clearBlock()

# 起動用処理
if __name__ == "__main__":
  main()
