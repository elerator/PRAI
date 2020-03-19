FROM registry.roqs.basf.net/base-images/ubuntu:18.04

ENV http_proxy http://clientproxy.basf.net:8080
ENV https_proxy https://clientproxy.basf.net:8080

ADD ./app ./app
#ADD ./database ./database1
#ADD ./database ./database
RUN ls -la
RUN ls /database

#RUN chmod a+rw database1 database1/*

RUN apt-get update && \
    apt-get install python3.6 -y && \
    apt-get install python3-pip -y && \
    apt-get install -y python-xlsxwriter && \
    pip3 install xlsxwriter && \
    pip3 install -r ./app/requirements.txt

#&& \ python3 ./app/manage.py shell -c "from users.models import Person; Person.objects.create_superuser('admin1', 'admin@example.com', 'adminpass')"

EXPOSE 5000

CMD ["python3", "./app/manage.py", "runserver", "0.0.0.0:5000"]
