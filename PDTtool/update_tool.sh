#! /bin/bash
#./manage.py migrate

echo "Pulling from git repo:"

git pull origin feature/schedule_centric_design

echo "Syncing DB schema:"

./manage.py syncdb

./manage.py schemamigration meeting_management --auto
./manage.py migrate meeting_management

./manage.py schemamigration topic_management --auto
./manage.py migrate topic_management