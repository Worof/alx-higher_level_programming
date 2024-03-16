#!/usr/bin/python3
"""
A script that lists all states from the database hbtn_0e_0_usa.
Usage: ./0-select_states.py <mysql username> <mysql password> <database name>
"""

import MySQLdb
from sys import argv

def list_states(username, password, dbname):
    """
    Connects to a MySQL database and lists all states in the database.
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=dbname, charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

if __name__ == "__main__":
    if len(argv) == 4:
        list_states(argv[1], argv[2], argv[3])
