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

    city_states = session.query(City, State)\
        .join(State, City.state_id == State.id)\
        .order_by(asc(City.id)).all()

    for city, state in city_states:
        print(f"{city.id}: {city.name} -> {state.name}")


if __name__ == "__main__":
    import sys
    list_states_cities(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
            )
