#!/bin/sh
curl -s -L -o bootstrap-3.3.6-dist.zip \
  https://github.com/twbs/bootstrap/releases/download/v3.3.6/bootstrap-3.3.6-dist.zip
curl -s -L -o jquery-1.12.4.min.js \
  https://code.jquery.com/jquery-1.12.4.min.js
curl -s -L -o jquery-ui-1.11.4.zip \
  http://jqueryui.com/resources/download/jquery-ui-1.11.4.zip

unzip bootstrap-3.3.6-dist.zip
unzip jquery-ui-1.11.4.zip

