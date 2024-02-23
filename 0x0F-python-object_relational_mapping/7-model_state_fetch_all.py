#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, asc


def list_states(name, password, db):
    """Lists all states"""
    # create the engine
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                name,
                password, db),
            pool_pre_ping=True
            )
    # Create session
    Session = sessionmaker(bind=engine)

    # start a new session
    session = Session()

    states = session.query(State).order_by(asc(State.id))
    i = 1
    for state in states:
        print(f"{i}: {state.name}")
        i += 1


if __name__ == "__main__":
    list_states(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3])
