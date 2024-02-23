#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, asc


def get_state(name, password, db):
    """get first state"""
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

    state = session.query(State).first()
    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")


if __name__ == "__main__":
    get_state(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3])
