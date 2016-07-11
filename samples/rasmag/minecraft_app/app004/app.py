#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mcpi import minecraft # Minecraft用
from mcpi import block # Minecraftブロック用
import random # 乱数生成用
import time # 処理休止用
# ↑ 必要なモジュールのインポート

# 宝用ブロックの配置用。値が 1のところに宝を
# 置くので、1を16個好きなところに記述できる。
# ここでは四角形にしている
d = [
0,1,1,1,1,0,
1,0,0,0,0,1,
1,0,0,0,0,1,
1,0,0,0,0,1,
1,0,0,0,0,1,
0,1,1,1,1,0,
]

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
  # 0から15のどれかを生成する乱数計算
  n = random.randint(0, 15)
  # ブロックを何個配置したかを保持する変数
  k = 0
  # 宝用ブロックとTNT爆弾ブロックの用意
  for j in range(6):
    for i in range(6):
      m = j*6+i
      b = d[m]
      if b == 1:
        # 宝用ブロックの用意
        mc.setBlock(i, 0, j, block.WOOL.id, m)
        # TNT爆弾ブロックの用意。kがnに一致するものだけ爆発
        if k == n:
          mc.setBlock(i, 1, j, block.TNT.id, 1)
        else:
          mc.setBlock(i, 1, j, block.TNT.id, 0)
        k = k + 1
      # 描画ができるよう、0.1秒間処理を休止
      time.sleep(0.1)
  # プレーヤーのスタート位置調整
  mc.player.setPos(3, 0, 3)

# 起動用処理
if __name__ == "__main__":
  main()

