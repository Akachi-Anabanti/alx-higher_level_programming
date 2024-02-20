#!/usr/bin/python3

"""A script that lists all cities from the
database
"""
import MySQLdb


def list_cities(username, password, database):
    """Executes the database command"""

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )
    cur = db.cursor()

    query = "SELECT cities.id, \
            cities.name, states.name \
            FROM cities, states \
            WHERE cities.state_id=states.id \
            ORDER BY cities.id ASC";

    cur.execute(query)

    [print(item) for item in cur.fetchall()]


if __name__ == "__main__":
    import sys
    list_cities(sys.argv[1], sys.argv[2], sys.argv[3])
