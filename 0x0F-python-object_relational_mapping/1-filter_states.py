#!/usr/bin/python3

"""A script that lists all states from the
database with name starting with N
"""
import MySQLdb


def list_states(username, password, database):
    """Executes the database command"""

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;")

    [print(item) for item in cur.fetchall()]


if __name__ == "__main__":
    import sys
    list_states(sys.argv[1], sys.argv[2], sys.argv[3])
