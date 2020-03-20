FROM registry.roqs.basf.net/base-images/ubuntu:18.04

ENV http_proxy http://clientproxy.basf.net:8080
ENV https_proxy https://clientproxy.basf.net:8080

ADD ./app ./app
ADD ./database ./initial_database
#RUN ls -la

RUN chmod a+rw initial_database initial_database/*

RUN apt-get update && \
    apt-get install python3.6 -y && \
    apt-get install python3-pip -y && \
    apt-get install -y python-xlsxwriter && \
    pip3 install xlsxwriter && \
    pip3 install -r ./app/requirements.txt

EXPOSE 5000

ADD startup.sh /
RUN chmod +x /startup.sh
CMD ["/startup.sh"]
#CMD ["python3", "./app/manage.py", "runserver", "0.0.0.0:5000"]
