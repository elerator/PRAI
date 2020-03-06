FROM registry.roqs.basf.net/base-images/ubuntu-python3-flaskrestplus:latest

ADD . .
EXPOSE 7000
RUN pip install -r requirements.txt
CMD [ "python", "./manage.py", "runserver", "0.0.0.0:7000"]

COPY api.py api.py
