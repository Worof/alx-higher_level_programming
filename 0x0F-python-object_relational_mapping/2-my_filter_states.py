#!/usr/bin/python3
"""
A script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
Usage: ./2-my_filter_states.py <mysql username> <mysql password> <database name> <state name>
"""

import MySQLdb
from sys import argv

def list_states(username, password, dbname, state_name):
    """
    Connects to a MySQL database and lists all states where name matches the argument.
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=dbname, charset="utf8")
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

if __name__ == "__main__":
    if len(argv) == 5:
        list_states(argv[1], argv[2], argv[3], argv[4])
