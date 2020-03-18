FROM registry.roqs.basf.net/base-images/ubuntu:18.04

ENV http_proxy http://clientproxy.basf.net:8080
ENV https_proxy https://clientproxy.basf.net:8080

ADD ./app ./app
ADD ./database ./database1
#RUN ls -la
RUN find . -print | grep -i '.*[.]sqlite3'
