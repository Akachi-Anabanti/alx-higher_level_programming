#!/usr/bin/python3
"""Defines a module that creates a state
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import City, Base
from relationship_state import State


def create_city(username, password, db):
    """creates the state California
    with the city San Francisco
    args:
        username: str - database username
        password: str - database password
        db: str - database name
    """

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                username, password, db), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = State(name="California")
    session.add(state)
    session.commit()
    city = City(name='San Francisco', state_id=state.id)
    session.add(city)
    session.commit()


if __name__ == "__main__":
    import sys
    create_city(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3],
            )
