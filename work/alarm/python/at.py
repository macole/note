#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse # 引数解析用モジュール
import time # 休止に必要なモジュール

# 現在時刻を「年-月-日 時:分」の文字列で取得
def get_current_time_str():
  now = time.ctime() # 現在時刻の取得
  parsed = time.strptime(now) # datetimeオブジェクト生成
  # datetimeオブジェクトから「年-月-日 時:分」の文字列生成
  return time.strftime("%Y-%m-%d %H:%M", parsed)

# 時刻チェックの間隔（秒数指定）
INTERVAL=20
# コマンドパラメータの解析
parser = argparse.ArgumentParser(description=u"指定時刻に処理を実行するプログラム")
help_str = u"処理を開始する時刻 YYYY-mm-dd HH:MM 例：2015-01-01 01:00"
parser.add_argument("start_time", type=str, help=help_str)
args = parser.parse_args()
play_start_time = args.start_time # 処理を開始する時刻の指定

# 現在時刻が指定時刻になるまでチェック
current_time = get_current_time_str()
while current_time != play_start_time:
  time.sleep(INTERVAL)
  current_time = get_current_time_str()

# 現在時刻が指定時刻を越えるとwhileが終了するので処理を実行
#（ここではcurrent_timeの値を表示）
print current_time

