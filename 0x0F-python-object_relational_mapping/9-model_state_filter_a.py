#!/usr/bin/python3
"""List states that has a in the name
"""
import sys
from model_state import State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, asc


def get_states_with_a(name, password, db):
    """Lists all states that has a in the name"""
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

    states = session.query(State).filter(State.name.contains('a'))
    .order_by(asc(State.id))

    for state in states:
        print(f"{state.id}: {state.name}")


if __name__ == "__main__":
    get_states_with_a(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3])
