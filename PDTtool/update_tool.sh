#! /bin/bash
#./manage.py migrate

./manage.py syncdb

./manage.py schemamigration topic_management meeting_management --auto

./manage.py migrate

echo "Pulling from git repo:"

git pull origin feature/schedule_centric_design