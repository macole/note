#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mcpi import minecraft  # Minecraft用
from mcpi import block  # Minecraftブロック用
import RPi.GPIO as GPIO  # GPIO用
import sys  # argv用
import time  # sleep用

# ゲーム開始後に警告となる秒数
GAME_ALARM_TIME = 20
# ゲームオーバーとなる秒数
GAME_OVER_TIME = 30
# GPIO スイッチ
buttons = [11, 9, 10, 22]
# GPIO LED
leds = [25, 24, 23]

# 迷路ゾーンのサイズ
SIZE_MAZE_X = 20
SIZE_MAZE_Y = 2
SIZE_MAZE_Z = 20

# 迷路ゾーンのデータセーブ用のファイル名
MAZE_DATA_FILE = "maze.txt"

# 迷路ゾーンの作成
def crateMazeZone(pos):
  # posより1つ低い高さ、xとzは1ずらした位置から
  # 22x3x22をSTONE（石）で敷き詰める
  mc.setBlocks(pos.x+1, pos.y-1, pos.z+1,
               pos.x+2+SIZE_MAZE_X, pos.y+SIZE_MAZE_Y-1, pos.z+2+SIZE_MAZE_Z, block.STONE.id)
  # posと同じ高さ、xとzは2ずらした位置から
  # 20x2x20をDIRT（土）で埋める
  mc.setBlocks(pos.x+2, pos.y, pos.z+2,
               pos.x+1+SIZE_MAZE_X, pos.y+SIZE_MAZE_Y-1, pos.z+1+SIZE_MAZE_Z, block.DIRT.id)
  # posより2つ高い高さ、xとzは1ずらした位置から
  # 22x122をGLASS（ガラス）で埋める
  mc.setBlocks(pos.x+1, pos.y+2, pos.z+1,
               pos.x+2+SIZE_MAZE_X, pos.y+SIZE_MAZE_Y, pos.z+2+SIZE_MAZE_Z, block.GLASS.id)

# セーブ
# 処理に時間がかかるので進行状況がわかるように
# printでコンソール画面へ取得値を出力
def save(pos):
  print "create list"
  yxz = [[[None for z in range(SIZE_MAZE_Z+2)] for x in range(SIZE_MAZE_X+2)] for y in range(SIZE_MAZE_Y+2)]
  # セーブするブロック情報を変数yxzへ設定
  print "getBlocks"
  for i in range(len(yxz)):
    for j in range(len(yxz[i])):
      for k in range(len(yxz[i][j])):
        yxz[i][j][k] = mc.getBlock(pos.x+1+j, pos.y-1+i, pos.z+1+k)
        print "(i, j, k, yxz[i][j][k]: " + str(i) + ", " + str(j) + ", " + str(k) + ", " + str(yxz[i][j][k])
  # セーブデータの文字列を生成
  print "create list text"
  txt = createListText(yxz)
  # データをファイルへ書き出し
  print "save"
  with open(MAZE_DATA_FILE, mode = "w") as fh:
    fh.write(txt)
    fh.flush()
  print "done"

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

# ロード
def load(pos):
  print "load"
  # ロードするブロック情報のPythonソースコードを取得
  lines = ""
  with open(MAZE_DATA_FILE, mode = "r") as fh:
    for line in fh:
      lines += line
  # ブロック情報をPythonのリストへ変換
  yxz = eval(lines)
  # ブロック情報から迷路を復元
  print "setBlocks"
  for i in range(len(yxz)):
    for j in range(len(yxz[i])):
      for k in range(len(yxz[i][j])):
         mc.setBlock(pos.x+1+j, pos.y-1+i, pos.z+1+k, yxz[i][j][k])
         print "(i, j, k, yxz[i][j][k]: " + str(i) + ", " + str(j) + ", " + str(k) + ", " + str(yxz[i][j][k])
  print "done"

# メイン処理
def main(ip, port):
  # グローバル変数
  global mc
  # GPIO設定
  GPIO.setmode(GPIO.BCM)
  for button in buttons:
    # スイッチはGPIO.INモード
    GPIO.setup(button, GPIO.IN)
  for led in leds:
    # LEDはGPIO.OUTモード
    GPIO.setup(led, GPIO.OUT)
    # 初期の出力はGPIO.LOWで消灯
    GPIO.output(led, GPIO.LOW)

  # Minecraftアプリと通信開始
  mc = minecraft.Minecraft.create(ip, port)
  # 基準値の初期化
  pos_zero = mc.player.getTilePos()
  # ゲーム開始判定用変数vの初期化
  # プレーヤーの下にあるブロック値を設定
  v = mc.getBlock(pos_zero.x, pos_zero.y-1, pos_zero.z)

  # アプリ開始
  running = True
  game_running = False
  while running:
    # スイッチ監視
    for button in buttons:
      v = GPIO.input(button)
      if v == GPIO.HIGH:
        print str(button)
        # アプリ終了
        if button == buttons[0]:
          running = False
        # 迷路ゾーンの作成
        elif button == buttons[1]:
          mc.postToChat("call crateMazeZone()")
          # 基準値の設定
          pos_zero = mc.player.getTilePos()
          # 迷路ゾーン作成関数呼び出し
          crateMazeZone(pos_zero)
        # 迷路のセーブ
        elif button == buttons[2]:
          mc.postToChat("call save()")
          save(pos_zero)
        # 迷路のロード
        elif button == buttons[3]:
          mc.postToChat("call load()")
          load(pos_zero)
        # チャタリング防止処置
        time.sleep(0.5)
    # ゲーム開始判定
    pos = mc.player.getTilePos()
    v = mc.getBlock(pos.x, pos.y-1, pos.z)
    if game_running==False and v == block.MELON.id:
      start_time = time.time()
      mc.postToChat("Start!")
      # 黄緑色LEDを点灯
      GPIO.output(leds[0], GPIO.HIGH)
      game_running = True
    # ゲーム終了判定
    if game_running and (v == block.DIAMOND_BLOCK.id):
      score = time.time() - start_time
      mc.postToChat("Goal! " + str(score))
      print("Goal! " + str(score))
      game_running = False
      # LED消灯
      for led in leds:
        GPIO.output(led, GPIO.LOW)
    # 経過時間のチェック
    if game_running:
      current_score = time.time() - start_time
      if current_score > GAME_OVER_TIME:
        score = 0
        game_running = False
        # LED消灯
        for led in leds:
          GPIO.output(led, GPIO.LOW)
        # 赤色LEDを点灯
        GPIO.output(leds[2], GPIO.HIGH)
        mc.postToChat("Game over!")
        time.sleep(5)
        # 5秒経過したら赤色LED消灯
        GPIO.output(leds[2], GPIO.LOW)
      elif current_score > GAME_ALARM_TIME:
        # LED消灯
        for led in leds:
          GPIO.output(led, GPIO.LOW)
        # 黄色LEDを点灯
        GPIO.output(leds[1], GPIO.HIGH)
    time.sleep(0.1)
  # 終了処理
  GPIO.cleanup()

# アプリ起動処理
if __name__ == "__main__":
  ip = sys.argv[1]
  port = 4711
  main(ip, port)
