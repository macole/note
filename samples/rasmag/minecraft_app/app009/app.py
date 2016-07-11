#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mcpi import minecraft  # Minecraft用
from mcpi import block  # Minecraftブロック用
import RPi.GPIO as GPIO  # GPIO用
import time  # sleep用

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

# 石壁の作成
def createWall():
  # プレーヤーが立っているタイルの位置を取得
  pos = mc.player.getTilePos()
  # posを基準として10x10の空間をSTONE（石）で埋める
  mc.setBlocks(pos.x+3, pos.y, pos.z,
               pos.x+3, pos.y+9, pos.z+9, block.STONE.id)

# 池の作成
def createPond():
  # プレーヤーが立っているタイルの位置を取得
  pos = mc.player.getTilePos()
  # posを基準として(x, y-1, z) - (x+10, y-11, z+10) の空間を
  # STONE（石）で埋める
  mc.setBlocks(pos.x, pos.y-1, pos.z,
               pos.x+10, pos.y-11, pos.z+10, block.STONE.id)
  # posを基準として(x+1, y-1, z+1) - (x+9, y-10, z+9) の空間を
  # WATER（水）で埋める
  mc.setBlocks(pos.x+1, pos.y-1, pos.z+1,
               pos.x+9, pos.y-10, pos.z+9, block.WATER.id)
  # posを基準として(x, y, z) - (x+10, y, z+10) の空間を
  # AIR（空気）で埋める
  mc.setBlocks(pos.x, pos.y, pos.z,
               pos.x+10, pos.y, pos.z+10, block.AIR.id)

# メイン処理
def main():
  # グローバル変数
  global mc
  # GPIOスイッチ
  buttons = [11, 9, 10, 22]
  # GPIO設定
  GPIO.setmode(GPIO.BCM)
  for button in buttons:
    GPIO.setup(button, GPIO.IN)

  # Minecraftアプリと通信開始
  mc = minecraft.Minecraft.create()

  # アプリ開始
  running = True
  while running:
    for button in buttons:
      v = GPIO.input(button)
      if v == GPIO.HIGH:
        print str(button)
        # アプリ終了
        if button == buttons[0]:
          running = False
        # 整地の実行
        elif button == buttons[1]:
          mc.postToChat("call clearBlock()")
          clearBlock()
        # 壁の作成を実行
        elif button == buttons[2]:
          mc.postToChat("call createWall()")
          createWall()
        # 池の作成を実行
        elif button == buttons[3]:
          mc.postToChat("call createPond()")
          createPond()
        # チャタリング防止処置
        time.sleep(0.5)
    time.sleep(0.1)

  GPIO.cleanup()

# アプリ起動処理
if __name__ == "__main__":
  main()
