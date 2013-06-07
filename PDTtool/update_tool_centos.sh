#! /bin/bash
#./manage.py migrate
echo "Installing Needed Software"
#pip install openssl-devel
easy_install django==1.5.1
easy_install  south
easy_install django_extensions
easy_install psycopg2
easy_install python-dateutil

echo "Pulling from git repo:"

git pull origin feature/schedule_centric_design

echo "Syncing DB schema:"

python2.7 manage.py syncdb

python2.7 manage.py schemamigration --auto

python2.7 manage.py migrate meeting_management
python2.7 manage.py migrate topic_management

echo "Creating Directories"
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )/"
cd $DIR

mkdir uploaded_topics

mkdir uploaded_topics/approved uploaded_topics/deleted uploaded_topics/uploads

chmod 777 uploaded_topics uploaded_topics/approved uploaded_topics/deleted uploaded_topics/uploads