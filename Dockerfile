FROM registry.roqs.basf.net/base-images/ubuntu:latest

ADD . .
EXPOSE 5000
RUN pip3 install -r requirements.txt
RUN ls -la
CMD ["python3", "./manage.py", "runserver", "0.0.0.0:5000"]
