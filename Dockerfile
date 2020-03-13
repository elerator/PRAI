FROM registry.roqs.basf.net/base-images/ubuntu:18.04

ENV http_proxy http://clientproxy.basf.net:8080
ENV https_proxy https://clientproxy.basf.net:8080

ADD ./app ./app
ADD ./database ./database
#RUN ls ./database
RUN chmod a+rw database database/*

RUN apt-get update && \
    apt-get install python3.6 -y && \
    apt-get install python3-pip -y && \
    pip3 install -r ./app/requirements.txt && \
    pip3 install --extra-index-url https://nexus.roqs.basf.net/repository/python/pypi basf_auth

#&& \ python3 ./app/manage.py shell -c "from users.models import Person; Person.objects.create_superuser('admin1', 'admin@example.com', 'adminpass')"

EXPOSE 5000

CMD ["python3", "./app/manage.py", "runserver", "0.0.0.0:5000"]
