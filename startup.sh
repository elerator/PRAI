#!/bin/bash
echo Docker container is in run stage now
#chmod -R 777 ./database
sudo chmod a+rw database1 database1/*
echo Listing root ...
ls -la
echo Listing contents of folder database
ls database
sudo python3 ./app/manage.py runserver 0.0.0.0:5000
echo Server exited
