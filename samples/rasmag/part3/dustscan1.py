#!/usr/bin/python

import smbus
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
i2c = smbus.SMBus(1)
address = 0x68
GPIO.output(12, GPIO.LOW)

try:
 while 1:
  GPIO.output(12, GPIO.HIGH)
  time.sleep(0.00028)
  temp = i2c.read_i2c_block_data(address,0x00,12)
  GPIO.output(12, GPIO.LOW)
  sign = temp[0] & 0b10000000
  if sign == 0:
   i2cout = ((temp[0] << 8) + temp[1]) * 0.001
  else:
   i2cout_p = ((temp[0] ^ 0b11111111) << 8) + (temp[1] ^ 0b11111111) + 1
   i2cout = i2cout_p * (-0.001)
  print temp
  dustscan = 3.3 + i2cout
  print dustscan
  time.sleep(1)
except KeyboardInterrupt:
 GPIO.cleanup()
