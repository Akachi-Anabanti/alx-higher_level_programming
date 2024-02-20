#!/usr/bin/python3

"""A script that lists all cities from the
database
"""
import MySQLdb


def list_cities(username, password, database, state):
    """Executes the database command"""

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )
    cur = db.cursor()

    query = "SELECT cities.name \
            FROM cities LEFT JOIN states \
            ON cities.state_id=states.id \
            WHERE BINARY states.name = %s \
            ORDER BY cities.id ASC;"

    cur.execute(query, (state,))

    cities = [item[0] for item in cur.fetchall()]
    print(", ".join(cities))


if __name__ == "__main__":
    import sys
    list_cities(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3],
            sys.argv[4]
            )
