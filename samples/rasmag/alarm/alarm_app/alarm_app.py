#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json, os, signal, time, threading, pygame
import RPi.GPIO as GPIO
from package_parts import conf, app_gpio

# メイン処理
def app_run():
  # 現在時刻取得
  check_cnt = 0
  # メインループ
  running = True
  while running:
    # 現在時刻が指定時刻かチェック
    check_cnt = check_cnt + 1
    if check_cnt >= CHECK_INTERVAL:
      # チェック開始のためのカウントクリア
      check_cnt = 0
      # エントリーの一覧
      entries = []
      # エントリーの一覧をロード。\ は改行をエスケープ
      entries_file = \
        config.get('alarm', 'entries_json_path')
      with open(entries_file, 'r') as f:
        entries = json.load(f)
      current_time = get_current_time_str()
      for entry in entries:
        # 指定時刻なら該当するオーディオファイルを再生
        if current_time == entry['start_time']:
          # 再生中でなければ開始
          if pygame.mixer.music.get_busy() != True:
            pygame.mixer.music.load(entry['file_name'])
            pygame.mixer.music.play()
            # 再生開始時にスイッチクリック数はクリア
            app_gpio.buttons[button] = 0
    # スイッチクリックのチェック
    for button, value in app_gpio.buttons.items():
      v, c = app_gpio.get_button_input(button)
      if button == buttons[0] and v == GPIO.HIGH:
        if pygame.mixer.music.get_busy() == True:
          # 再生の停止
          pygame.mixer.music.stop()
        if c == 5: # クリック数が5回のとき
          # アプリ停止
          running = False
          # スイッチクリック数のクリア
          app_gpio.buttons[button] = 0
    # 繰り返しは最低 0.1秒休止
    time.sleep(0.1)
  app_gpio.cleanup()
  print('App quit')

# 現在時刻を「年-月-日 時:分」の文字列で取得
def get_current_time_str():
  now = time.ctime() # 現在時刻の取得
  parsed = time.strptime(now) # datetimeオブジェクト生成
  # datetimeオブジェクトから「年-月-日 時:分」の文字列生成
  return time.strftime("%Y-%m-%d %H:%M", parsed)

# アプリ起動処理 --------------------------
if __name__ == '__main__':
  # 初期化処理   --------------------------
  # 設定ファイルの読み込み
  config = conf.Conf('./config.ini')
  # アプリ用GPIO
  buttons = config.get_button_list()
  app_gpio = app_gpio.AppGpio(GPIO, buttons)
  # メインループ実行管理用
  running = False
  # 再生時刻チェックのインターバル用（0.1秒*200回 = 20秒毎）
  CHECK_INTERVAL = 200
  # pygame.mixierの初期化
  pygame.mixer.init()
  # 開始
  app_run()

