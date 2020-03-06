FROM registry.roqs.basf.net/base-images/ubuntu-python3-flaskrestplus:latest

ADD . .
EXPOSE 5000
RUN GIT_SSL_NO_VERIFY=1 pip3 install -r requirements.txt
RUN ls -la
CMD [ "python", "./manage.py", "runserver", "0.0.0.0:5000"]
