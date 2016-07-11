#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import route, run, redirect, request, static_file, HTTPResponse
from package_parts import conf
import json, os, signal

# ルート（/static/index.htmlへリダイレクト）
@route('/')
def webroot():
  redirect("/static/index.html")

# 静的ファイル
@route('/static/<filepath:path>')
def server_static(filepath):
  return static_file(filepath, root=document_root)

# エントリーの一覧取得
@route('/entries')
def get_entries():
  # エントリーの一覧
  entries = []
  # エントリーの一覧をファイルから取得
  entries_file = config.get('alarm', 'entries_json_path')
  with open(entries_file, 'r') as f:
    entries = json.load(f)
  # JSONデータにして返却
  r = HTTPResponse(status=200, body=json.dumps(entries))
  r.set_header('Content-Type', 'application/json')
  return r

# エントリーの更新
@route('/entry/<id:int>', method='POST')
def post_entry(id):
  if request.is_xhr: # XMLHttpRequestのリクエストのみ対応 
    # idは/entry/<id:int>から取得。残りはJSONデータから取得
    entry_id = id
    start_time = request.json['start_time']
    file_name = request.json['file_name']
    # エントリーの一覧
    entries = []
    # エントリーの一覧をファイルから取得
    entries_file = config.get('alarm', 'entries_json_path')
    with open(entries_file, 'r') as f:
      entries = json.load(f)
    # 各エントリーについて、idのものを取得して更新
    for entry in entries:
      for k, v in entry.items():
        if k == 'id' and entry_id == int(v):
          entry['start_time'] = start_time
          entry['file_name'] = file_name
          # ファイルへ反映
          with open(entries_file, 'w') as f:
            json.dump(entries, f, indent=2)
    # エントリーの一覧を返却
    return get_entries()
  else:
    r = HTTPResponse(status=400)
    return r

# アプリ停止用
@route('/server/stop')
def post_server_stop():
  print 'bottle app stop'
  # Bottleアプリの終了
  os.kill(os.getpid(), signal.SIGTERM)

# アプリ起動処理 --------------------------
if __name__ == '__main__':
  # 初期化処理   --------------------------
  # 設定ファイルの読み込み
  config = conf.Conf('./config.ini')
  host = config.get('bottle', 'host')
  port = config.get('bottle', 'port')
  BASE_DIR = os.path.abspath(os.path.dirname(__file__))
  document_root = BASE_DIR + '/' + config.get('bottle', 'document_root')
  # Bottle Webサーバ開始
  run(host=host, port=port, debug=True, reloader=True)

