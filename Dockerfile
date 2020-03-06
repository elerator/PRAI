FROM registry.roqs.basf.net/base-images/ubuntu-python3-flaskrestplus:latest

ADD . .
EXPOSE 7000
RUN GIT_SSL_NO_VERIFY=1 pip3 install -r requirements.txt
CMD [ "python", "./manage.py", "runserver", "0.0.0.0:7000"]

COPY api.py api.py
