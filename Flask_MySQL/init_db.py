# init_db.py

import pymysql

username = 'mike'
password = '5454160s'
hostname = 'localhost'
db_name = 'books_db'

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{username}:{password}@{hostname}/{databasename}".format(
    username=username,
    password=password,
    hostname=hostname,
    databasename=db_name)
 
# Create database connection object
conn = pymysql.connections.Connection(
    user=username,
    password=password,
    host=hostname
)

# Create cursor object
curs = conn.cursor()
 
# Executing SQL query
sql_query = "CREATE DATABASE IF NOT EXISTS " + db_name
curs.execute(sql_query)
curs.execute("SHOW DATABASES")
 
# Displaying databases
for databases in curs:
    print(databases)
 
# Close the cursor and connection to the database
curs.close()
conn.close()

