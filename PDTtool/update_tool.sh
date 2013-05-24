#! /bin/bash
#./manage.py migrate

./manage.py schemamigration topic_management meeting_management --auto

./manage.py migrate

git pull origin feature/schedule_centric_design