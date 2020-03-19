#!/bin/bash
echo Docker container is in run stage now
#chmod -R 777 ./database
chmod a+rw database database/*
echo Listing root ...
ls -la
echo Listing contents of folder database
cd database
ls -la
cd ..
python3 ./app/manage.py runserver 0.0.0.0:5000
Server exited
