#!/usr/bin/python3
"""Defines a module that lists a state
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, asc
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import City, Base
from relationship_state import State


def list_states_cities(username, password, db):
    """lists the state with the city
    args:
        username: str - database username
        password: str - database password
        db: str - database name
    """

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                username, password, db), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State)\
        .order_by(asc(State.id)).all()

    for state in states:
        print(f"{state.id}: {state.name}")
        cities = sorted(state.cities, key=lambda city: city.id)
        for city in cities:
            print(f"\t{city.id}: {city.name}")


if __name__ == "__main__":
    import sys
    list_states_cities(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
            )
