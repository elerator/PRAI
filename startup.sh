#!/bin/bash
echo Docker container is in run stage now
echo Listing root ...
ls -la
echo Listing contents of persistant folder database
cd database
ls -la
cd ..

echo copy db.sqlite3
cp ./database1/db.sqlite3 ./database/db.sqlite3

python3 ./app/manage.py runserver 0.0.0.0:5000
