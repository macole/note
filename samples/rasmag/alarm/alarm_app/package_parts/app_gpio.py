#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

class AppGpio:
  # コンストラクタ
  def __init__(self, GPIO, buttons):
    self.GPIO = GPIO
    self.GPIO.setmode(GPIO.BCM)
    self.buttons = {}
    for button in buttons:
      self.buttons[button] = 0
      self.GPIO.setup(button, GPIO.IN)

  def cleanup(self):
    # GPIOの後片付け
    self.GPIO.cleanup()

  def get_button_input(self, button):
    value = self.buttons[button]
    v = GPIO.input(button)
    if v == GPIO.HIGH:
      self.buttons[button] = value + 1
      print str(button) + ":" + str(self.buttons[button])
      # チャタリング防止処置
      time.sleep(.5)
    return [v, self.buttons[button]]

# アプリ起動処理
if __name__ == "__main__":
  buttons = [11]
  app_gpio = AppGpio(GPIO, buttons)
  # スイッチが2回クリックされたら終了
  count = 0
  while count < 2:
    v, c = app_gpio.get_button_input(buttons[0])
    if c > count:
      count = c
    time.sleep(0.1)
  app_gpio.cleanup()

