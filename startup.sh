#!/bin/bash
echo Docker container is in run stage now
echo Listing root ...
ls -la
echo Listing contents of folder database
ls database
python3 ./app/manage.py runserver 0.0.0.0:5000
echo Server exited
