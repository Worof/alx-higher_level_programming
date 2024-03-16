#!/usr/bin/python3
"""
A script that lists all cities of a specific state from the database hbtn_0e_4_usa.
Usage: ./5-filter_cities.py <mysql username> <mysql password> <database name> <state name>
"""

import MySQLdb
from sys import argv

def list_cities(username, password, dbname, state_name):
    """
    Connects to a MySQL database and lists all cities of the specified state.
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=dbname, charset="utf8")
    cur = db.cursor()
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC;
    """
    cur.execute(query, (state_name,))
    rows = cur.fetchall()
    print(", ".join(city[0] for city in rows))
    cur.close()
    db.close()

if __name__ == "__main__":
    if len(argv) == 5:
        list_cities(argv[1], argv[2], argv[3], argv[4])
