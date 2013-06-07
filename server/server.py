#!/usr/bin/env python
import sys
import psycopg2 as psql


#Predefine a connection variable.
con = None

#List the notification name.
table = 'djnotifications_notification'

try:
  #Connect to the database.
  con = psql.connect(database='django_db3',
                     user='django_login',
                     password='Password',
                     host='localhost')
  cur = con.cursor()
  cur.execute('SELECT user')

except psql.DatabaseError, e:
  print 'Error %s' % e
  sys.exit(1)


finally:
  if con:
    con.close()