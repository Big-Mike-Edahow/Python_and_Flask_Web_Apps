# init_db.py

import sqlite3

connection = sqlite3.connect('jacksons.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

curs = connection.cursor()

# Insert rows of data in to the brothers table
curs.execute("INSERT INTO brothers (name, age, address, salary) \
             VALUES ('Steve', 49, 'Nampa', 80000.00 );")

curs.execute("INSERT INTO brothers (name, age, address, salary) \
             VALUES ('Jared', 48, 'Woods Cross', 75000.00 );")

curs.execute("INSERT INTO brothers (name, age, address, salary) \
             VALUES ('Mike', 46, 'Blackfoot', 32000.00 );")

curs.execute("INSERT INTO brothers (name, age, address, salary) \
             VALUES ('Gabe', 44, 'Chicago', 95000.00 );")

connection.commit()
connection.close()

