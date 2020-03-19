#!/bin/bash
echo Docker container is in run stage now
#chmod -R 777 ./database
#chmod a+rw database database/*
echo Listing root ...
ls -la
echo Listing contents of folder database
cd database
ls -la
cd ..
#ln -s ./database/db.sqlite3 ./database2/db.sqlite3
echo copy db.sqlite3
#cp ./database1/db.sqlite3 ./database/db.sqlite3
cp ./database/db.sqlite3 ./database2/db.sqlite3
cd database2
ls -la
cd ..

python3 ./app/test_loading_database.py
python3 ./app/manage.py runserver 0.0.0.0:5000
