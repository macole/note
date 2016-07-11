#!/bin/sh
cd /home/pi/alarm_app/
python alarm_app.py &
python bottle_app.py &

