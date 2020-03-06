FROM registry.roqs.basf.net/base-images/ubuntu:latest

ENV http_proxy http://clientproxy.basf.net:8080
ENV https_proxy https://clientproxy.basf.net:8080

RUN apt-get install python3.6 -y && \
    apt-get install python3-pip -y

ADD . .
EXPOSE 5000

RUN pip3 install -r requirements.txt
RUN ls -la
CMD ["python3", "./manage.py", "runserver", "0.0.0.0:5000"]
