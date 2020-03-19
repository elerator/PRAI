#!/bin/bash
echo Docker container is in run stage now
echo Listing root ...
ls -la
echo Listing contents of persistant folder database
cd database
ls -la
cd ..

FILE=./database/db.sqlite3
if [ -f "$FILE" ]; then
    echo "$FILE exists already in mounted persistant volume do not copy from repository"
else
    echo "copy db.sqlite3 into persistant volume"
    cp ./database1/db.sqlite3 ./database/db.sqlite3
fi

python3 ./app/manage.py runserver 0.0.0.0:5000
