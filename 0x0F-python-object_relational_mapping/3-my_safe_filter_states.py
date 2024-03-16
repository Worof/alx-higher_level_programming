#!/usr/bin/python3
"""
A script that's safe from SQL injections, which takes an argument and displays
all values in the 'states' table of 'hbtn_0e_0_usa' where name matches the argument.

Usage: ./3-my_safe_filter_states.py <mysql username> <mysql password> <database name> <state name>
"""

import MySQLdb
from sys import argv

def safe_state_search(username, password, dbname, state_name):
    """
    Searches for states that match the given name, safe from SQL injection.
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=dbname, charset="utf8")
    cur = db.cursor()

    # Using a parameterized query to prevent SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (state_name,))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()

if __name__ == "__main__":
    if len(argv) == 5:
        safe_state_search(argv[1], argv[2], argv[3], argv[4])
