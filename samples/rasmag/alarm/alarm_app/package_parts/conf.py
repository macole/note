#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import ConfigParser
import codecs

class Conf:
  def __init__(self, file_name):
    self.config = ConfigParser.SafeConfigParser()
    self.config.readfp(codecs.open(file_name, 'r', 'utf8'))
  def get(self, section, key):
    return self.config.get(section, key)
  def get_button_list(self):
    v = self.config.get('button', 'button_gpios')
    return map(int, v.split(","))

# アプリ起動処理
if __name__ == '__main__':
  config = Conf('./config.ini')
  print '[alarm] entries_json_path: ' + config.get('alarm', 'entries_json_path')
  print '[button] button_gpios: ' + config.get('button', 'button_gpios')
