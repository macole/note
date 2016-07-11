#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import feedparser

import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI
import Adafruit_DHT

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Raspberry Pi software SPI
SCLK = 17
DIN  = 18
DC   = 27
RST  = 23
CS   = 22

SENSOR = Adafruit_DHT.AM2302 
SENSOR_PIN = 26

# 地域のRSSフィードURLに変更してください
RSS_URL="http://rss.weather.yahoo.co.jp/rss/days/4410.xml"

# LCD初期化
disp = LCD.PCD8544(DC, RST, SCLK, DIN, CS)
disp.begin(contrast=60)
disp.clear()
disp.display()

# PIL Images
image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))
draw = ImageDraw.Draw(image)

# 日本語フォントのロード
jpfont = ImageFont.truetype('/usr/share/fonts/truetype/takao-gothic/TakaoGothic.ttf',12, encoding="unic");

counter = 0
tenki=''
kion=''
while True:
	# 60分に1回、RSSから天気を取得
	if counter%60 == 0:
		tenki_dic = feedparser.parse(RSS_URL)
		today = tenki_dic.entries[0].title
		today_dic = today.split(" ")
		tenki=today_dic[4]
		kion=today_dic[6]
	# センサーを読み取る
	hum, temp = Adafruit_DHT.read_retry(SENSOR, SENSOR_PIN)
	current_temp = u'温度:{0:0.1f}℃'.format(temp)
	current_hum  = u'湿度:{0:0.1f}%'.format(hum)

	draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)
	draw.text((2,0), tenki, font=jpfont)
	draw.text((2,12), kion, font=jpfont)
	draw.text((2,24), current_temp, font=jpfont)
	draw.text((2,36), current_hum, font=jpfont)
	# 表示
	disp.image(image)
	disp.display()
	
	counter += 1
	# 60秒スリープ
	time.sleep(60.0)
