#!/usr/bin/python3
"""Inserts a new state
"""
import sys
from model_state import State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, asc


def create_state(username, password, db):
    """Inserts a new state to the db
    args:
        username: str - Username in the db
        password: str - mysql password
        db: str - name of DB
    """
    # create the engine
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                username,
                password, db),
            pool_pre_ping=True
            )
    # Create session
    Session = sessionmaker(bind=engine)

    # start a new session
    session = Session()

    state = State(name="Louisiana")
    session.add(state)
    session.commit()

    print(state.id)


if __name__ == "__main__":
    create_state(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3])
