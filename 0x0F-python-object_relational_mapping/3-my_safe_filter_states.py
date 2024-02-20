#!/usr/bin/python3

"""A script that lists A state from the
DATABASE
"""
import MySQLdb


def list_states(username, password, database, state):
    """Executes the database command"""

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )
    cur = db.cursor()
    query = "SELECT * FROM states \
            WHERE BINARY name=%s ORDER BY id ASC;"
    cur.execute(query, (state,))

    [print(item) for item in cur.fetchall()]


if __name__ == "__main__":
    import sys
    list_states(
            sys.argv[1], sys.argv[2],
            sys.argv[3], sys.argv[4]
            )
