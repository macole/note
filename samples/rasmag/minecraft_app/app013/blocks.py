#!/usr/bin/env python
# -*- coding: utf-8 -*-
y = [None for y in range(4)]
print 'y  :' + str(y)
for i in range(len(y)):
  y[i] = i
print 'y  :' + str(y)

xz = [[None for z in range(3)] for x in range(2)]
print 'xz :' + str(xz)
for i in range(len(xz)):
  for j in range(len(xz[i])):
    xz[i][j] = 10*i + j
print 'xz :' + str(xz)

yxz = [[[None for z in range(3)] for x in range(2)] for y in range(4)]
for i in range(len(yxz)):
  for j in range(len(yxz[i])):
    for k in range(len(yxz[i][j])):
      yxz[i][j][k] = 100*i + 10*j + k
print 'yxz[0]:' + str(yxz[0])
print 'yxz[1]:' + str(yxz[1])
