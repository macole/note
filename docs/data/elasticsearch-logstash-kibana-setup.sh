#!/usr/bin/env bash

echo 'Elasticsearch/logstash/kibana Auto setup script for logcol[01-02].zeolite'
echo "Copyright GYAO Corporation `date +%Y`"
echo "Author: Bungo Tamari"

sudo yum install -y java
sudo rpm --import https://packages.elastic.co/GPG-KEY-elasticsearch

cat << EOS |sudo tee /etc/yum.repos.d/elasticsearch.repo
[elasticsearch-2.x]
name=Elasticsearch repository for 2.x packages
baseurl=https://packages.elastic.co/elasticsearch/2.x/centos
gpgcheck=1
gpgkey=https://packages.elastic.co/GPG-KEY-elasticsearch
enabled=1
EOS

sudo yum install -y elasticsearch
sudo systemctl daemon-reload
sudo systemctl enable elasticsearch.service
sudo systemctl start elasticsearch.service

sudo mv /etc/elasticsearch/elasticsearch.yml /etc/elasticsearch/elasticsearch.yml.orig && \
cat << EOS |sudo tee  /etc/elasticsearch/elasticsearch.yml
network.host: 0.0.0.0
http.port: 9200
node.name: ${HOSTNAME}
cluster.name: log_collector
discovery.zen.ping.multicast.enabled: false
discovery.zen.ping.unicast.hosts: [host1,host2] # please change here
# http.cors.enabled: true # kibana4.5 is not work on ES2.3 so please comment out here
EOS

sudo -u elasticsearch /usr/share/elasticsearch/bin/plugin install mobz/elasticsearch-head
sudo -u elasticsearch /usr/share/elasticsearch/bin/plugin install royrusso/elasticsearch-HQ
sudo -u elasticsearch /usr/share/elasticsearch/bin/plugin install polyfractal/elasticsearch-inquisitor
sudo systemctl daemon-reload
sudo /etc/init.d/elasticsearch restart
sudo /etc/init.d/elasticsearch status
sudo /sbin/chkconfig --add elasticsearch


## logstash

cat << EOS |sudo tee /etc/yum.repos.d/logstash.repo
[logstash-2.3]
name=Logstash repository for 2.3.x packages
baseurl=http://packages.elastic.co/logstash/2.3/centos
gpgcheck=1
gpgkey=http://packages.elastic.co/GPG-KEY-elasticsearch
enabled=1
EOS

sudo yum install -y logstash

### kibana


cat << EOS |sudo tee /etc/yum.repos.d/kibana.repo
[kibana-4.5]
name=Kibana repository for 4.5.x packages
baseurl=http://packages.elastic.co/kibana/4.5/centos
gpgcheck=1
gpgkey=http://packages.elastic.co/GPG-KEY-elasticsearch
enabled=1
EOS

sudo yum install -y kibana
sudo chkconfig --add kibana
sudo /bin/systemctl daemon-reload
sudo /bin/systemctl enable kibana.service
sudo /etc/init.d/kibana restart

echo 'please check'
echo "http://${HOSTNAME}:9200/_plugin/head/"
echo "http://${HOSTNAME}:5601"