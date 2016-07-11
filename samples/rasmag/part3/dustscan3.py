#!/usr/bin/python

import smbus
import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(31, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(29, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(38, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(40, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(37, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(33, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(35, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(36, GPIO.IN)

i2c = smbus.SMBus(1)
address = 0x68
GPIO.output(12, GPIO.LOW)

sw1 = 0b1
GPIO.output(31, GPIO.LOW)
GPIO.output(29, GPIO.LOW)
GPIO.output(38, GPIO.LOW)
GPIO.output(40, GPIO.LOW)
GPIO.output(37, GPIO.HIGH)
GPIO.output(33, GPIO.HIGH)
GPIO.output(35, GPIO.LOW)
time.sleep(0.5)

GPIO.output(31, GPIO.LOW)
GPIO.output(29, GPIO.LOW)
GPIO.output(38, GPIO.HIGH)
GPIO.output(40, GPIO.LOW)
GPIO.output(37, GPIO.LOW)
GPIO.output(33, GPIO.HIGH)
GPIO.output(35, GPIO.LOW)
time.sleep(0.5)

GPIO.output(31, GPIO.HIGH)
GPIO.output(29, GPIO.LOW)
GPIO.output(38, GPIO.LOW)
GPIO.output(40, GPIO.HIGH)
GPIO.output(37, GPIO.HIGH)
GPIO.output(33, GPIO.HIGH)
GPIO.output(35, GPIO.HIGH)
time.sleep(0.5)

while sw1 == 0b1:
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
  if dustscan > 1.252:
   GPIO.output(31, GPIO.LOW)
   GPIO.output(29, GPIO.HIGH)
   GPIO.output(38, GPIO.HIGH)
   GPIO.output(40, GPIO.LOW)
   GPIO.output(37, GPIO.LOW)
   GPIO.output(33, GPIO.LOW)
   GPIO.output(35, GPIO.LOW)
   time.sleep(1)
  else:
   GPIO.output(31, GPIO.HIGH)
   GPIO.output(29, GPIO.HIGH)
   GPIO.output(38, GPIO.HIGH)
   GPIO.output(40, GPIO.HIGH)
   GPIO.output(37, GPIO.HIGH)
   GPIO.output(33, GPIO.HIGH)
   GPIO.output(35, GPIO.LOW)
   time.sleep(0.3)
   GPIO.output(31, GPIO.HIGH)
   GPIO.output(29, GPIO.HIGH)
   GPIO.output(38, GPIO.HIGH)
   GPIO.output(40, GPIO.LOW)
   GPIO.output(37, GPIO.HIGH)
   GPIO.output(33, GPIO.HIGH)
   GPIO.output(35, GPIO.HIGH)
   time.sleep(0.3)
   GPIO.output(31, GPIO.LOW)
   GPIO.output(29, GPIO.HIGH)
   GPIO.output(38, GPIO.HIGH)
   GPIO.output(40, GPIO.HIGH)
   GPIO.output(37, GPIO.HIGH)
   GPIO.output(33, GPIO.HIGH)
   GPIO.output(35, GPIO.HIGH)
   time.sleep(0.3)
  sw1 = GPIO.input(36)

GPIO.output(31, False)
GPIO.output(29, False)
GPIO.output(38, False)
GPIO.output(40, False)
GPIO.output(37, False)
GPIO.output(33, False)
GPIO.output(35, False)
time.sleep(1)
GPIO.cleanup()
os.system("/sbin/shutdown -h now")
