# coding: utf-8
Encoding.default_external = 'UTF-8'
##
# 追記部分
STDOUT.sync = true

begin

  5.times {
    print "HELLO WORLD!"
    sleep(0.5)
  }

  raise "ERROR"

rescue => ex
  print ex.class
  print ex.message
  print ex.backtrace
end
