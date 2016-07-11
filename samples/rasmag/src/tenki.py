#!/usr/bin/python
# -*- coding: utf-8 -*-

import feedparser

# 地域のRSSフィードURLに変更してください
RSS_URL="http://rss.weather.yahoo.co.jp/rss/days/4410.xml"

tenki_dic = feedparser.parse(RSS_URL)

# 最初のエントリーが今日の天気
today = tenki_dic.entries[0].title
# スペースで分解
tenki = today.split(" ")

# 4番目が天気
print tenki[4]
# 6番目は気温
print tenki[6]
