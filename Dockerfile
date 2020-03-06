FROM registry.roqs.basf.net/base-images/ubuntu-python3-flaskrestplus:latest

ADD . .
EXPOSE 5000
RUN GIT_SSL_NO_VERIFY=1 pip3 install -r requirements.txt
RUN ls -la

COPY api.py api.py
