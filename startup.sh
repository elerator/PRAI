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
    echo "$FILE exists already in mounted persistant volume. Do not copy from repository ..."
else
    echo "Copy db.sqlite3 from initial_database into Database (persistant volume)"
    cp ./initial_database/db.sqlite3 ./database/db.sqlite3
fi

#python3 ./app/manage.py shell -c "from users.models import Person; Person.objects.create_superuser('admin1', 'admin@example.com', 'adminpass')"
python3 ./app/manage.py runserver 0.0.0.0:5000
