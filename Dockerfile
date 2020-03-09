FROM registry.roqs.basf.net/base-images/ubuntu:latest

ENV http_proxy http://clientproxy.basf.net:8080
ENV https_proxy https://clientproxy.basf.net:8080

ADD ./app ./app
ADD ./database ./database

RUN apt-get install python3.6 -y && \
    apt-get install python3-pip -y && \
    pip3 install -r ./app/requirements.txt

EXPOSE 5000

RUN ls -la
CMD ["python3", "./app/manage.py", "runserver", "0.0.0.0:5000"]
