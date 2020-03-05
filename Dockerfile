FROM registry.roqs.basf.net/base-images/ubuntu-python3-flaskrestplus:latest

ENV APP_ROOT /src
ENV CONFIG_ROOT /config


RUN mkdir ${CONFIG_ROOT}
COPY /app/requirements.txt ${CONFIG_ROOT}/requirements.txt
RUN pip install -r ${CONFIG_ROOT}/requirements.txt

RUN mkdir ${APP_ROOT}
WORKDIR ${APP_ROOT}

ADD /app/ ${APP_ROOT}

COPY api.py api.py
