#!/usr/bin/python3
"""
A script that lists all cities from the database hbtn_0e_4_usa.
Usage: ./4-cities_by_state.py <mysql username> <mysql password> <database name>
"""

import MySQLdb
from sys import argv

def list_cities(username, password, dbname):
    """
    Connects to a MySQL database and lists all cities, along with their state names.
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=dbname, charset="utf8")
    cur = db.cursor()
    cur.execute("""
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

if __name__ == "__main__":
    if len(argv) == 4:
        list_cities(argv[1], argv[2], argv[3])
