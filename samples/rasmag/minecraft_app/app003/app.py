#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mcpi import minecraft # Minecraft用
from mcpi import block # Minecraftブロック用
import random # 乱数生成用
import time # 処理休止用
# ↑ 必要なモジュールのインポート

def main():
  # Minecraftアプリと通信接続
  mc = minecraft.Minecraft.create()
  # フィールド整地
  # (0,0,0) - (20,20,20) で決まる立方体の範囲を空気で
  # 敷き詰める。また、(0,-1,0) - (20,-20,20) で決まる
  # 立方体の範囲を石で敷き詰める
  x0 =  0
  y0 =  0
  z0 =  0
  x1 = 20
  y1 = 20
  z1 = 20
  mc.setBlocks(x0, y0, z0, x1, y1, z1, block.AIR.id)
  mc.setBlocks(0, -1, 0, x1, -y1, z1, block.STONE.id)
  # 0,1,2,3,4のどれかを生成する乱数計算
  n = random.randint(0, 4)
  # 宝用ブロックとTNT爆弾ブロックの用意
  x0 = 3 
  y0 = 0
  z0 = 3 
  vx = 1
  vy = 0
  vz = 0
  for i in range(5):
    # 宝用ブロックの用意
    x1 = x0 + vx
    y1 = y0 + vy
    z1 = z0 + vz
    mc.setBlock(x1, y1, z1, block.WOOL.id, i)
    # TNT爆弾ブロックの用意。nに一致するものだけ爆発
    if i == n:
      mc.setBlock(x1, y1+1, z1, block.TNT.id, 1)
    else:
      mc.setBlock(x1, y1+1, z1, block.TNT.id, 0)
    x0 = x1
    y0 = y1
    z0 = z1
    # 描画ができるよう、0.1秒間処理を休止
    time.sleep(0.1)
  # プレーヤーのスタート位置調整
  mc.player.setPos(1, 0, 10)

# 起動用処理
if __name__ == "__main__":
  main()
