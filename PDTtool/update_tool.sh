#! /bin/bash
#./manage.py migrate
echo "Installing Needed Software"
pip install openssl-devel
pip install django==1.5.1
pip install south
pip install django_extensions
pip install psycopg2
pip install python-dateutil

echo "Pulling from git repo:"

git pull origin feature/schedule_centric_design

echo "Syncing DB schema:"

./manage.py syncdb

./manage.py schemamigration meeting_management --auto

./manage.py migrate meeting_management
./manage.py migrate topic_management

#Do it a second time for relationships.
./manage.py migrate meeting_management
./manage.py migrate topic_management

echo "Creating Directories"
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )/"
cd $DIR

mkdir uploaded_topics

mkdir uploaded_topics/approved uploaded_topics/deleted uploaded_topics/uploads

chmod 777 uploaded_topics uploaded_topics/approved uploaded_topics/deleted uploaded_topics/uploads
