import sys
import psycopg2 as psql

def connection():
  #Predefine a connection variable.
  con = None

  try:
    #Connect to the database.
    con = psql.connect(database='django_db3',
                       user='django_login',
                       password='Password',
                       host='localhost')
    cur = con.cursor()
    cur.execute('SELECT version()')
    ver = cur.fetchone()
    print ver

  except psql.DatabaseError, e:
    print 'Error %s' % e
    sys.exit(1)


  finally:
    if con:
      con.close()