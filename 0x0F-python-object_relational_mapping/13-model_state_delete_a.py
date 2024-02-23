#!/usr/bin/python3
"""deletes states
"""
import sys
from model_state import State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, asc


def delete_state_with_a(username, password, db):
    """deletes all states to  that has a
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

    states = session.query(State).filter(State.name.contains('a'))

    for state in states:
        session.delete(state)
    session.commit()


if __name__ == "__main__":
    delete_state_with_a(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3])
