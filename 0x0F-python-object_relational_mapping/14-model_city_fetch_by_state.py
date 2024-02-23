#!/usr/bin/python3
"""Defines a function that prints all City
Objects"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, asc
from model_state import Base, State
from model_city import City


def get_cities(username, password, db):
    """gets all cities from DB"""
    # create the engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, db), pool_pre_ping=True)
    # create new session
    Session = sessionmaker(bind=engine)

    session = Session()

    cities_n_state = session.query(City, State)\
        .join(State, City.state_id == State.id)\
        .order_by(asc(City.id)).all()

    for city, state in cities_n_state:
        print(f"{state.name}: ({city.id}) {city.name}")


if __name__ == "__main__":
    get_cities(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3])
